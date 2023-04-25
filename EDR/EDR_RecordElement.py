import re

import pandas as pd

from EDR.ImportModule import *
from EDR.Epprom import Epprom_Translate


def split_rows(row):
    group = row["GROUP"]
    if group != 1:
        row_list = [row.copy() for _ in range(group)]
        for i in range(group):
            row_list[i]["NVM"] += f"._{i}_"
        return pd.DataFrame(row_list)  # 为了将多类别的数据进行处理，按照特定规则，分割成多行
    else:
        return row.to_frame().T

def process_nvm_with__brackets(s):
    brackets_pattern = "(.+)(\[\d+\])"
    s = s.strip()
    mt = re.match(brackets_pattern,s)
    if mt:
        #TODO 处理异常，如果数据出错误或者不符合格式
        return mt.group(1)
    else:
        return s

def process_size(s):
    """
    在Size 列 是Group*单个点数的byte* 多少个点
    获取采样点的个数，即会采样多少个点
    Args:
        s:

    Returns:

    """
    # print(s)
    s = s.strip()
    temp = s.split("*")
    if len(temp) == 1:
        return 1
    elif len(temp) == 2:
        return int(temp[1])
    elif len(temp) == 3:
        return int(temp[2])
    else:
        pass
       #TODO 抛出异常

def process_nvm_group(s):
    """
    因为某些参数的格式，在Size 列 是Group*单个点数的byte* 多少个点
    所以需要处理一下，对于包含group的
    Args:
        s:

    Returns:

    """
    s = s.strip()
    temp = s.split("*")
    if len(temp) == 1:
        return 1
    elif len(temp) == 2:
        return 1
    elif len(temp) == 3:
        return int(temp[0])
    else:
        pass
    # TODO 抛出异常


class EDR_RecordElement:

    def __init__(self,excel,sheet):
        self.excel = excel
        self.sheet = sheet
        self.nvm_parameters = []
        self.df_nvm = pd.DataFrame()

    def refresh(self):
        df = pd.read_excel(self.excel,self.sheet,dtype="str")
        columns = ["TYPE","NVM","SIZE"]
        df.columns = strip_upper_columns(df.columns)
        validate_columns(df.columns,columns,self.sheet)
        df = df[["TYPE","NVM","SIZE"]]
        df.dropna(subset=['TYPE',"NVM","SIZE"],inplace=True)
        df = df.query("TYPE in ['Algo','Other','Deploy','Sensor']")
        # print(df)
        df["NVM"] = df["NVM"].apply(process_nvm_with__brackets)
        df["NUMBER"] = df["SIZE"].apply(process_size) # how many element will be record
        df["GROUP"] = df["SIZE"].apply(process_nvm_group)  # how many group for one element
        df =  df[["NVM","SIZE","NUMBER","GROUP"]]
        # print(df)
        self.df_nvm = pd.concat([split_rows(row) for _,row in df.iterrows()],ignore_index=True)
        # print(self.df_nvm)

    def generate_nvm_params(self,file):
        args = []
        for indx in self.df_nvm.index:
            param = self.df_nvm.loc[indx,"NVM"].replace(".", "") + "_RecordElement"
            number =  self.df_nvm.loc[indx,"NUMBER"]
            # var commandsArray: String[] = new String[2];
            if number == 1:
                arg = f"var {param} = \"undefined\";\n"
            else:
                arg = f"var {param}:String[] = new String[{number}];\n"
            args.append(arg)
        fileUtil.generate_script_bypath("".join(args),file)

    @func_monitor
    def generate_nvm_excel(self, nvm_excel, epprom: Epprom_Translate):
        df = self.df_nvm.copy()
        df["ExpectNVM"] = "undefined"  # 存储预期NVM值的参数
        df["Epprom"] = "undefined"  # 存储NVM参数名称

        for indx in df.index:
            nvm_param = df.loc[indx, "NVM"]
            nvm_param = nvm_param.strip()
            df.loc[indx, "ExpectNVM"] = nvm_param.replace(".", "") + "_RecordElement"
            # 先以结尾完全匹配
            df_endswith = epprom.df_edr_block.query("PARAMETER_NAME.str.endswith(@nvm_param)")
            # pattern = f"{nvm_param}\\._\\d+\\._$"
            df_endswith_mutil = epprom.df_edr_block.query(f'PARAMETER_NAME.str.contains("{nvm_param}\\._\\d+_$")',
                                                          engine='python')
            df_contains = epprom.df_edr_block.query("PARAMETER_NAME.str.contains(@nvm_param)")
            if df_endswith.empty != True:
                df.loc[indx, "Epprom"] = "\n".join(df_endswith["PARAMETER_NAME"].values)
            elif df_endswith_mutil.empty != True:
                df.loc[indx, "Epprom"] = "\n".join(df_endswith_mutil["PARAMETER_NAME"].values)
                # print(df_endswith_mutil["PARAMETER_NAME"].values)
                # break;
            elif df_contains.empty != True:  # 说明有多个参数
                # print(df_contains["PARAMETER_NAME"].values)
                df.loc[indx, "Epprom"] = "\n".join(df_contains["PARAMETER_NAME"].values)
                # break;
            else:
                pass

        df.to_excel(nvm_excel, index=False)

    @func_monitor
    def generate_nvm_check(self, nvm_check, nvm_excel):
        sigle_pattern = "^(\w+)(\\._\\d_.)(\S+)$"  # 单个元素的正则匹配 RstEdr_EventDataCaptureBuffer._0_.ChinaRecordDataElement.BrkSysWIStatus.Data
        mutil_pattern = "^(\w+)(\\._\\d_.)(\S+)\\._(\\d+)_$"  # 多个元素的正则匹配 RstEdr_EventDataCaptureBuffer._0_.AdditionalRecordDataElement.au16DelayFromEDR_T0._0_
        df = pd.read_excel(nvm_excel, "Sheet1")
        global_nvms = []
        block_nvms = []
        with open(nvm_check, 'w', encoding='UTF-8') as nvm_file:
            # pass
            for indx in df.index:  # 循环遍历 元素
                # print(df.loc[indx,"Original_NVM"])
                expect_name = df.loc[indx, "ExpectNVM"]
                epproms = df.loc[indx, "Epprom"].split("\n")
                block_func_name = f"function BB_Check_{expect_name}_BlockEDR(Block,Expected,ExpectedLength,CheckCount,Tolerance)\n{'{'}\n"
                global_func_name = f"function BB_Check_{expect_name}_GlobalEDR(Expected,ExpectedLength,CheckCount,Tolerance)\n{'{'}\n"
                if len(epproms) == 1:  # 单个参数的时候处理方式
                    mt = re.match(sigle_pattern, epproms[0])
                    if mt:
                        groups = mt.groups()

                        block = """{0}"""
                        parameter_name = f"\t\tvar parameter_name = String.Format(\"{groups[0]}._{block}_.{groups[2]}\",Block);\n"
                        nvm_file.write(block_func_name)
                        nvm_file.write(f"\tvar actual_nvm_data_dec = new Array();\n")
                        nvm_file.write(f"\tfor(var i = 0; i < CheckCount; i++)\n\t{'{'}\t\n")
                        nvm_file.write(parameter_name)
                        nvm_file.write(f"\t\tvar current_nvm_data_dec = BB_CompareParameterByName2(parameter_name,ExpectedLength,Expected,Tolerance);\n")
                        nvm_file.write(f"\t\tactual_nvm_data_dec.push(current_nvm_data_dec);\n")
                        nvm_file.write("\t};\n")
                        nvm_file.write(f"\treturn actual_nvm_data_dec;\n")
                        nvm_file.write("}\n\n")
                        # block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block,Expected,ExpectedLength,CheckCount,Tolerance);\n")
                    else:  # 如果没有匹配到单个参数模式，则表示这是一个global
                        nvm_file.write(global_func_name)
                        parameter_name = f"\t\tvar parameter_name = {epproms[0]};\n"
                        nvm_file.write(f"\tvar actual_nvm_data_dec = new Array();\n")
                        nvm_file.write(f"\tfor(var i = 0; i < CheckCount; i++)\n\t{'{'}\t\n")
                        nvm_file.write(parameter_name)
                        nvm_file.write(
                            f"\t\tvar current_nvm_data_dec = BB_CompareParameterByName2(parameter_name,ExpectedLength,Expected[i],Tolerance);\n")
                        nvm_file.write(f"\t\tactual_nvm_data_dec.push(current_nvm_data_dec);\n")
                        nvm_file.write("\t};\n")
                        nvm_file.write(f"\treturn actual_nvm_data_dec;\n")
                        nvm_file.write("}\n\n")


                        # # nvm_file.write(parameter_name)
                        # nvm_file.write(f"\tBB_CompareParameterByName2('{epproms[0]}',{expect_name});\n")
                        # nvm_file.write("}\n\n")
                        # global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                else:  # 有多个NVM参数的时候
                    params = []
                    # print(epproms)
                    # 循环去匹配里面的数据
                    for epprom in epproms:
                        mt = re.match(mutil_pattern, epprom)
                        if mt == None:  # 如果这里没有找到，可能也是要比较多个参数，跳出循环
                            # print(epprom,mt)
                            break;
                        params.append(list(mt.groups()))

                    if len(params) == 0: #匹配到的是golbal 里面的这种参数
                        # RstEdr_GlobalEventInfo.au32EventNbDiscarded._0_
                        global_mutil_pattern = "(\w+)(\S+)(\\._\\d_)"
                        mt = re.match(global_mutil_pattern, epproms[0])
                        if mt:
                            groups = mt.groups()
                            nvm_file.write(global_func_name)
                            param_index = """{1}"""
                            parameter_name = f"\t\ttvar parameter_name = String.Format(\"{groups[0]}{groups[1]}._{param_index}_\",i);\n"
                            nvm_file.write(f"\tvar actual_nvm_data_dec = new Array();\n")
                            nvm_file.write(f"\tfor(var i = 0; i < CheckCount; i++)\n\t{'{'}\t\n")
                            nvm_file.write(parameter_name)
                            nvm_file.write(
                                f"\t\tvar current_nvm_data_dec = BB_CompareParameterByName2(parameter_name,ExpectedLength,Expected[i],Tolerance);\n")
                            nvm_file.write(f"\t\tactual_nvm_data_dec.push(current_nvm_data_dec);\n")
                            nvm_file.write("\t};\n")
                            nvm_file.write(f"\treturn actual_nvm_data_dec;\n")
                            nvm_file.write("}\n\n")
                        else:
                            raise  Exception(f"Not handler this parameters in python {epproms}")

                        # global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                    else:
                        mt = re.match(mutil_pattern, epproms[0])
                        groups = mt.groups()
                        parent = groups[0]
                        #     forloop = f"\tfor(var i = 0; i <= {max_index}; i++)\n\t{'{'}\n"
                        block = """{0}"""
                        param_index = """{1}"""
                        tempkey = groups[2]
                        parameter_name = f"\t\tvar parameter_name = String.Format(\"{parent}._{block}_.{tempkey}._{param_index}_\",Block,i);\n"
                        nvm_file.write(block_func_name)
                        nvm_file.write(f"\tvar actual_nvm_data_dec = new Array();\n")
                        nvm_file.write(f"\tfor(var i = 0; i < CheckCount; i++)\n\t{'{'}\t\n")
                        nvm_file.write(parameter_name)
                        nvm_file.write(
                            f"\t\tvar current_nvm_data_dec = BB_CompareParameterByName2(parameter_name,ExpectedLength,Expected[i],Tolerance);\n")
                        nvm_file.write(f"\t\tactual_nvm_data_dec.push(current_nvm_data_dec);\n")
                        nvm_file.write("\t};\n")
                        nvm_file.write(f"\treturn actual_nvm_data_dec;\n")
                        nvm_file.write("}\n\n")
                        # df_temp = pd.DataFrame(np.array(params),
                        #                        columns=["parent", "block", "param", "index"])
                        # Debug_Logger.debug(params)
                        # df_temp = df_temp.astype({'index': 'int32'})  # 强hi在转换类型为int，然后去比较最大的index
                        # df_pivot_tb = df_temp.pivot_table(index=["param"], aggfunc=np.max)
                        # temp_dict = df_pivot_tb.to_dict(orient="index")  # 通过Piovt_table 进行分组统计，找到不同类别的参数
                        # # print(temp_dict)
                        # # Monitor_Logger.info(temp_dict)
                        # nvm_file.write(block_func_name)
                        # for tempkey in temp_dict:
                        #     max_index = temp_dict[tempkey]["index"]
                        #     parent = temp_dict[tempkey]["parent"]
                        #     forloop = f"\tfor(var i = 0; i <= {max_index}; i++)\n\t{'{'}\n"
                        #     block = """{0}"""
                        #     param_index = """{1}"""
                        #     nvm_file.write(forloop)
                        #
                        #     parameter_name = f"\t\tvar parameter_name = String.Format(\"{parent}._{block}_.{tempkey}._{param_index}_\",Block,i);\n"
                        #     nvm_file.write(parameter_name)
                        #     nvm_file.write(f"\t\tBB_CompareParameterByName2(parameter_name,{expect_name}[i]);\n")
                        #     nvm_file.write("\t};\n")
                        #
                        # nvm_file.write("}\n")
                        # block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block);\n")

            # global_define = "function BB_Check_GlobalEDR()\n{\n"
            # nvm_file.writelines(global_define)
            # for func_name in global_nvms:
            #     nvm_file.writelines("\t" + func_name)
            # nvm_file.writelines("}")
            # nvm_file.write("\n\n\n")
            #
            # block_define = "function BB_Check_BlockEDR(Block)\n{\n"
            # nvm_file.writelines(block_define)
            # for func_name in block_nvms:
            #     nvm_file.writelines("\t" + func_name)
            # nvm_file.writelines("}")
            # nvm_file.write("\n\n\n")

    # self.nvm_parameters = df["NVM"].to_list()
        # print(self.nvm_parameters)
        # for i in self.nvm_parameters:
        #     if isinstance(i,str) != True:
        #         print(i)


if __name__ == "__main__":

    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\Record_element_list_leon_new.xlsx"
    sheet = "Elements"
    file = "BB_EDR_Common_NVM_Check2_Define.ts"
    file2 = "BB_EDR_Common_NVM_2_Define.ts"
    nvm_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\NVM_Mapping2.xlsx"
    edr_record = EDR_RecordElement(excel, sheet)
    edr_record.refresh()

    edr_record.generate_nvm_params(file2)
    #
    # epprom_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\EEPROM_Translation_SAIC_ZP22_P20.00.xlsm"
    # epprom = Epprom_Translate(epprom_excel)
    # epprom.block_ids = [2,31]
    # epprom.get_edr_block()
    # #
    # edr_record.generate_nvm_excel(nvm_excel,epprom)

    edr_record.generate_nvm_check(file,nvm_excel)