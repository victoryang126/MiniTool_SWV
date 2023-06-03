import re

import numpy as np
import pandas as pd
from EDR.ImportModule import *
from EDR.Epprom import Epprom_Translate
from EDR.EDR_RecordElement import EDR_RecordElement
"""
this is used to generate 
"""



class EDR_DID_Config:
    def __init__(self,excel):
        self.excel = excel
        self.sheets = []
        self.df_read_element = pd.DataFrame()

    @func_monitor
    def refresh(self):
        self.sheets = pd.read_excel(excel, sheet_name=None)
        Monitor_Logger.info(self.sheets.keys())
        self.df_read_element = pd.DataFrame()
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            # df = pd.read_excel(excel, sheet_name)

            columnslist = ["ID", "NAME","SAMPLESIZE", "START", "LENGTH", "END", "SIGNAL",
                           "TYPE","NVM"]
            df.columns = strip_upper_columns(df.columns)
            validate_columns(df.columns,columnslist,sheet_name)
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            start0 = df["START"].values[0]
            # print(start0)
            if str(start0) != "0":
                raise Exception("start byte of the frist element not 0 ")
            df.fillna("", inplace=True)
            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df_duplicated = df.duplicated(subset=['ID'])
            if True in df_duplicated.values:
                Monitor_Logger.info("Duplicated Req ID")
                Monitor_Logger.info(df.loc[df_duplicated]["ID"])
                Debug_Logger.debug("Duplicated Req ID")
                Debug_Logger.debug(df.loc[df_duplicated]["ID"])
                raise Exception("Duplicated Req ID, Please check it")

            df.set_index("ID", inplace=True, drop=False)
            self.df_read_element = pd.concat([ self.df_read_element, df[["NAME", "SIGNAL", "TYPE","NVM","ID"]]])

        did_element_value = self.df_read_element["NAME"].values
        #检测NAME规则例如VehSpd_GB
        element_noks = []
        for element in did_element_value:
            if "_" not in element:
                element_noks.append(element)
        if len(element_noks) != 0:
            raise Exception(",".join(element_noks) + " <- these DID element format is not correct")

    @func_monitor
    def generate_check(self,checkfile):
        fileUtil.init_file_bypath(checkfile)
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            # df = pd.read_excel(excel, sheet_name)
            columnslist = ["ID", "NAME", "START", "LENGTH", "END", "SIGNAL"]
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            df.fillna("", inplace=True)
            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df.set_index("ID", inplace=True, drop=False)

            func_name = "function BB_Check_" + sheet_name + "_EDR(TYPE,DataRecord)\n{\n"
            with open(checkfile, 'a', encoding='UTF-8') as check: #写入函数名称
                check.writelines(func_name)
            with open(checkfile, 'a', encoding='UTF-8') as check:  #根据里面的数据写入数据
                with open(parameterfile, 'a', encoding='UTF-8') as para:
                    for i in df.index:
                        # 处理check函数部分
                        NAME = df.loc[i, "NAME"].replace("\n", " ")
                        comment = f"\t//{i} : {NAME};\n"
                        check.writelines(comment)
                        parametervalue = "\t" + "var ParameterValue = " + df.loc[i, "NAME"] + ";\n"
                        check.writelines(parametervalue)
                        START = str(df.loc[i, "START"])
                        LENGTH = str(df.loc[i, "LENGTH"])
                        action = f"\tvar Action = \"Check \" + TYPE + \" Value: {NAME} START:{START} LENGTH:{LENGTH} \";\n"
                        check.writelines(action)
                        callfunc = "\t" + '''BB_Check_ParameterValue(Action, ParameterValue, DataRecord, ''' \
                                   + START + ", " + LENGTH + ''' )''' + ";\n"
                        check.writelines(callfunc)
                        check.write("\n")
            with open(checkfile, 'a', encoding='UTF-8') as check:
                check.writelines("}")
                check.write("\n\n\n")

    @func_monitor
    def generate_trans(self,transitionfile):
        """
        用来生成transition函数
        Args:
            transitionfile: ts文件，用来保存函数
        Returns:
        """
        fileUtil.init_file_bypath(transitionfile)
        df_trans_func = self.df_read_element.copy()
        # print(df_trans_func["NAME"])
        # 根据NAME里面的DID元素的名称，去掉后面的EDR类型，然后根据这个去用透视表把可能类似的元素放在一起
        # 2023/4/3 定义用id作为did元素的变量名称，方便维护，，所以去掉这边的pivot_table的处理测录，直接从Excel从上到下取生成
        # df_trans_func["Value"] = df_trans_func["NAME"].apply(lambda x: "_".join(x.split("_")[:-1]))
        #
        # df_trans_func = df_trans_func.pivot_table(index=['Value'], sort=False,
        #                                           aggfunc=lambda x: '\n'.join(x))
        func_call = []
        with open(transitionfile, 'a', encoding='UTF-8') as trans:
            trans.write("CALL(BB_EDR_Parameter_Define.ts);\n")
            for i in df_trans_func.index:
                # print(df_trans_func.loc[i, "NAME"])
                func_name = "function BB_" + i + "_Transition()\n{\n"
                func_call.append("BB_" + i + "_Transition()")
                trans.writelines(func_name)
                comment = "\t// " + "ReqID : " + ", ".join(df_trans_func.loc[i, "ID"].split("\n")) + ";\n"
                trans.writelines(comment)
                comment = "\t// " + "DID Element NAME : " + ", ".join(df_trans_func.loc[i, "NAME"].split("\n")) + ";\n"
                trans.writelines(comment)
                comment = "\t// " + "SIGNAL : " + ", ".join(df_trans_func.loc[i, "SIGNAL"].split("\n")) + ";\n"
                trans.writelines(comment)
                templist = df_trans_func.loc[i, "NVM"].split("\n") # 获取NVM的参数，
                templist = [a.strip().replace(".", "") + "_NVM" for a in templist]
                comment = "\t// " + "NVM : " + ", ".join(templist) + ";\n"
                # comment = "\t// " + "NVM : " + ", ".join(df_trans_func.loc[i, "NVM_Parameter"].split("\n")) + ";\n"
                trans.writelines(comment)
                nvm_assign_values = [f"\t{x}= 0xXX;\n" for x in templist]
                trans.writelines(nvm_assign_values)
                assign_values = df_trans_func.loc[i, "NAME"].split("\n")
                assign_values = [f"\t{x}= 0xXX;\n" for x in assign_values] # 故意设置，如果相关Tranition函数不处理，编译不过
                trans.writelines(assign_values)
                trans.writelines("}")
                trans.write("\n\n\n")
        # 总的调用函数，调用所有的Transition 函数
        with open(transitionfile, 'a', encoding='UTF-8') as trans:
            callfunc_define = "function BB_EDR_Transition()\n{\n"
            trans.writelines(callfunc_define)
            for func_name in func_call:
                trans.writelines("\t" + func_name + ";\n")
            trans.writelines("}")
            trans.write("\n\n\n")

    @func_monitor
    def generate_params(self,parameterfile):
        fileUtil.init_file_bypath(parameterfile)
        df_trans_func = self.df_read_element.copy()
        element_names = []
        signals = []
        nvm_params = []
        for i in df_trans_func.index:
            element_names.extend(df_trans_func.loc[i, "NAME"].split("\n"))
            signals.extend(df_trans_func.loc[i, "SIGNAL"].split("\n"))
            #"NVM_Parameter后续处理
            templist = df_trans_func.loc[i, "NVM"].split("\n")
            templist = [a.strip().replace(".","") + "_NVM" for a in templist]
            # templist = [a for a in templist]
            nvm_params.extend(templist)
        element_names = list(set(element_names)) # 去重
        signals = list(set(signals))  # 去重
        nvm_params = list(set(nvm_params))  # 去重

        element_names = [a for a in element_names if a != ""]
        signals = [a for a in signals if a != ""]
        nvm_params = [a for a in nvm_params if a != ""]

        element_names = [f"var {arg} = \"undefined\";\n" for arg in element_names]
        signals = [f"var {arg} = \"undefined\";\n" for arg in signals]
        nvm_params = [f"var {arg} = \"undefined\";\n" for arg in nvm_params]
        with open(parameterfile, 'w', encoding='UTF-8') as para:
            # para.write(Func)
            para.write("//Element NAME ;\n")
            para.writelines(element_names)
            para.write("//Signals NAME;\n")
            para.writelines(signals)
            para.write("//NVM Parameters;\n")
            para.writelines(nvm_params)



    @func_monitor
    def generate_nvm_excel(self,nvm_excel,epprom:Epprom_Translate):
        df_trans_func = self.df_read_element.copy()


        df_trans_func["TYPE"] = df_trans_func["TYPE"].str.strip()
        # TODO if the type in NAN, shall throww exception
        #only get the NVM from CAN,CAND,DCS,Reserved
        df_trans_func = df_trans_func[df_trans_func["TYPE"].isin(["CAN", "CAND", "DCS", "Reserved"])]
        # df_trans_func = df_trans_func.query('TYPE=="Element"')
        args = []
        for i in df_trans_func.index:
            args.extend(df_trans_func.loc[i, "NVM"].split("\n"))
        # did_nvm_params = np.array(args)
        # args.extend(edr_record.nvm_parameters)

        # TODO 比较DID的NVM 参数必须在EDRNVM_Element 里面，否则剔除异常红色字体
        # nvm_params = np.array(edr_record.nvm_parameters)
        # mask = np.isin(did_nvm_params,nvm_params)
        # notin_nvms = [ did_nvm_params[indx] for indx,e in enumerate(nvm_params) if e == False]
        # if len(notin_nvms) != 0:
        #     Exception_Logger.critical(f"this nvm paramter not defined in EDR_Record element: {notin_nvms}")



        args = list(set(args))  # 去重
        args.sort() #排列
        args = [a for a in args if a!=""]
        df = pd.DataFrame({"NVM": args})
        df["ExpectNVM"] = "undefined"# 存储预期NVM值的参数
        df["Epprom"] = "undefined" # 存储NVM参数名称

        for indx in df.index:
            nvm_param = df.loc[indx,"NVM"]
            nvm_param = nvm_param.strip()
            df.loc[indx, "ExpectNVM"] = nvm_param.replace(".","") + "_NVM"
            #先以结尾完全匹配
            df_endswith = epprom.df_edr_block.query("PARAMETER_NAME.str.endswith(@nvm_param)")
            # pattern = f"{nvm_param}\\._\\d+\\._$"
            df_endswith_mutil = epprom.df_edr_block.query(f'PARAMETER_NAME.str.contains("{nvm_param}\\._\\d+_$")',engine = 'python')
            df_contains = epprom.df_edr_block.query("PARAMETER_NAME.str.contains(@nvm_param)")
            if df_endswith.empty != True:
                df.loc[indx,"Epprom"]=  "\n".join(df_endswith["PARAMETER_NAME"].values)
            elif df_endswith_mutil.empty != True:
                df.loc[indx, "Epprom"] = "\n".join(df_endswith_mutil["PARAMETER_NAME"].values)
                # print(df_endswith_mutil["PARAMETER_NAME"].values)
                # break;
            elif df_contains.empty != True: #说明有多个参数
                # print(df_contains["PARAMETER_NAME"].values)
                df.loc[indx, "Epprom"] = "\n".join(df_contains["PARAMETER_NAME"].values)
                # break;
            else:
                pass

        df.to_excel(nvm_excel, index=False)




    @func_monitor
    def generate_nvm_check(self,nvm_check,nvm_excel):
        sigle_pattern =  "(\w+)(\\._\\d_.)(\S+)" #单个元素的正则匹配  RstEdr_GlobalEventInfo.au32EventNbDiscarded._0_
        mutil_pattern = "(\w+)(\\._\\d_.)(\S+)\\._(\\d+)_" #多个元素的正则匹配  RstEdr_EventDataCaptureBuffer._0_.u8PibReq._13_
        df = pd.read_excel(nvm_excel,"Sheet1")
        global_nvms = []
        block_nvms = []
        with open(nvm_check, 'w', encoding='UTF-8') as nvm_file:
            # pass
            for indx in df.index: #循环遍历 元素
                # print(df.loc[indx,"Original_NVM"])
                expect_name = df.loc[indx,"ExpectNVM"]
                epproms = df.loc[indx,"Epprom"].split("\n")
                block_func_name = f"function BB_Check_{expect_name}_BlockEDR(Block)\n{'{'}\n"
                global_func_name = f"function BB_Check_{expect_name}_GlobalEDR()\n{'{'}\n"
                if len(epproms) == 1:  # 单个参数的时候处理方式
                    mt = re.match(sigle_pattern,epproms[0])
                    if mt:
                        groups = mt.groups()
                        block = """{0}"""
                        parameter_name = f"\tvar parameter_name = String.Format(\"{groups[0]}._{block}_.{groups[2]}\",Block);\n"
                        nvm_file.write(block_func_name)
                        nvm_file.write(parameter_name)
                        nvm_file.write(f"\tBB_CompareParameterByName(parameter_name,{expect_name});\n")
                        nvm_file.write("}\n\n")
                        block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block);\n")
                    else:# 如果没有匹配到单个参数模式，则表示这是一个global
                        nvm_file.write(global_func_name)
                        parameter_name = f"\tvar parameter_name = {epproms[0]};\n"
                        # nvm_file.write(parameter_name)
                        nvm_file.write(f"\tBB_CompareParameterByName('{epproms[0]}',{expect_name});\n")
                        nvm_file.write("}\n\n")
                        global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                else: # 有多个NVM参数的时候
                    params = []
                    # print(epproms)
                    #循环去匹配里面的数据
                    for epprom in epproms:
                        mt = re.match(mutil_pattern, epprom)
                        if mt == None: #如果这里没有找到，可能也是要比较多个参数，跳出循环
                            # print(epprom,mt)
                            break;
                        params.append(list(mt.groups()))

                    if len(params) == 0:
                        nvm_file.write(global_func_name)
                        for epprom in epproms:
                            parameter_name = f"\tvar parameter_name = {epprom};\n"
                            # nvm_file.write(parameter_name)
                            nvm_file.write(f"\tBB_CompareParameterByName('{epprom}',{expect_name});\n")
                        nvm_file.write("}\n\n")
                        global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                    else:
                        df_temp = pd.DataFrame(np.array(params),
                                           columns=["parent", "block", "param", "index"])
                        Debug_Logger.debug(params)
                        df_temp = df_temp.astype({'index': 'int32'}) #强hi在转换类型为int，然后去比较最大的index
                        df_pivot_tb = df_temp.pivot_table(index=["param"], aggfunc=np.max)
                        temp_dict = df_pivot_tb.to_dict(orient="index") # 通过Piovt_table 进行分组统计，找到不同类别的参数
                        # print(temp_dict)
                        # Monitor_Logger.info(temp_dict)
                        nvm_file.write(block_func_name)
                        for tempkey in temp_dict:
                            max_index = temp_dict[tempkey]["index"]
                            parent =  temp_dict[tempkey]["parent"]
                            forloop = f"\tfor(var i = 0; i <= {max_index}; i++)\n\t{'{'}\n"
                            block = """{0}"""
                            param_index = """{1}"""
                            nvm_file.write(forloop)

                            parameter_name = f"\t\tvar parameter_name = String.Format(\"{parent}._{block}_.{tempkey}._{param_index}_\",Block,i);\n"
                            nvm_file.write(parameter_name)
                            nvm_file.write(f"\t\tBB_CompareParameterByName(parameter_name,{expect_name});\n")
                            nvm_file.write("\t};\n")

                        nvm_file.write("}\n")
                        block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block);\n")

            global_define = "function BB_Check_GlobalEDR()\n{\n"
            nvm_file.writelines(global_define)
            for func_name in global_nvms:
                nvm_file.writelines("\t" + func_name)
            nvm_file.writelines("}")
            nvm_file.write("\n\n\n")

            block_define = "function BB_Check_BlockEDR(Block)\n{\n"
            nvm_file.writelines(block_define)
            for func_name in block_nvms:
                nvm_file.writelines("\t" + func_name)
            nvm_file.writelines("}")
            nvm_file.write("\n\n\n")

    def generate_did_config(self,did_config):
        fileUtil.init_file_bypath(did_config)
        scripts = []
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            df = df.iloc[1:]  # 剔
            df = df[["ID","SAMPLESIZE","START","LENGTH"]]
            data_record_length = df["LENGTH"].astype("int32").sum()
            df["SAMPLESIZE"] =  df["SAMPLESIZE"].astype("int32")
            scripts.append(f"function {sheet_name}_EDR_DID(Name)\n")
            scripts.append("{\n")
            scripts.append(f"\t this.Length = {data_record_length};\n")
            scripts.append(f"\t this.Name = Name;\n")
            scripts.append(f"\t this.Elements = \n")
            scripts.append("\t{\n")
            elements = []
            # "GB_EDR1": newDID_Element_ByByte(0, 0, 0, 0)
            # elements = [f"\t\'{i}\': new BB_Create_SnapshotRecord(\'{i}\')" for i in self.snapshot_recordnumbers]
            # scripts.append(",\n".join(elements) + "\n")
            for index in df.index:
                id = df.loc[index,"ID"]
                sampel_size = df.loc[index,"SAMPLESIZE"]
                start = df.loc[index,"START"]
                length = df.loc[index,"LENGTH"]
                elements.append(f"\t\t\"{id}\": new DID_Element_ByByte(\"{id}\",{sampel_size},{start},{length})")
            scripts.append(",\n".join(elements) + "\n")
            scripts.append("\t}\n")
            scripts.append("}\n\n")



        fileUtil.generate_script_bypath("".join(scripts),did_config)


    @func_monitor
    def generate_check_general(self,checkfile):
        """
        used to generate the general check function for the did element,
        current,only used to generate CAND,DCS/CAND
        Args:
            checkfile:
        Returns:
        """
        fileUtil.init_file_bypath(checkfile)
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            # df = pd.read_excel(excel, sheet_name)
            columnslist = ["ID", "NAME", "TYPE","START", "LENGTH", "END", "SIGNAL"]
            columnslist = ["ID", "TYPE"]
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            df["TYPE"] = df["TYPE"].str.strip()
            #TODO if the type in NAN, shall throww exception
            # print(df["TYPE"])
            # print(df["TYPE"].isin(["CANC","CAND","DCS","Reserved"]))
            df = df[df["TYPE"].isin(["CAN","CAND","DCS","Reserved"])]
            if df.empty == True:
                continue;

            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df.set_index("ID", inplace=True, drop=False)

            func_name = "function BB_Check_" + sheet_name + "_EDR(DID_Obj)\n{\n\tvar did_name = DID_Obj.Name;\n\n"
            with open(checkfile, 'a', encoding='UTF-8') as check: #写入函数名称
                check.writelines(func_name)
            with open(checkfile, 'a', encoding='UTF-8') as check:  #根据里面的数据写入数据
                with open(parameterfile, 'a', encoding='UTF-8') as para:
                    for i in df.index:
                        # 处理check函数部分
                        comment = f"\t//{i} ;\n"
                        check.writelines(comment)
                        parametervalue = f"\tvar expect_element_value =  {i} ;\n"
                        check.writelines(parametervalue)
                        element = f"\tvar element = BB_Get_DID_Element(DID_Obj,\"{i}\");\n"
                        check.writelines(element)
                        callfunc = f"\tBB_Compare_Element_Values(did_name,element,expect_element_value);\n\n"
                        check.writelines(callfunc)

            with open(checkfile, 'a', encoding='UTF-8') as check:
                check.writelines("}")
                check.write("\n\n\n")



    @func_monitor
    def generate_nvm_check2(self,nvm_check,nvm_excel):
        sigle_pattern =  "(\w+)(\\._\\d_.)(\S+)" #单个元素的正则匹配  RstEdr_GlobalEventInfo.au32EventNbDiscarded._0_
        mutil_pattern = "(\w+)(\\._\\d_.)(\S+)\\._(\\d+)_" #多个元素的正则匹配  RstEdr_EventDataCaptureBuffer._0_.u8PibReq._13_
        df = pd.read_excel(nvm_excel,"Sheet1")
        global_nvms = []
        block_nvms = []
        with open(nvm_check, 'w', encoding='UTF-8') as nvm_file:
            # pass
            for indx in df.index: #循环遍历 元素
                # print(df.loc[indx,"Original_NVM"])
                expect_name = df.loc[indx,"ExpectNVM"]
                epproms = df.loc[indx,"Epprom"].split("\n")
                block_func_name = f"function BB_Check_{expect_name}_BlockEDR(Block)\n{'{'}\n"
                global_func_name = f"function BB_Check_{expect_name}_GlobalEDR()\n{'{'}\n"
                if len(epproms) == 1:  # 单个参数的时候处理方式
                    mt = re.match(sigle_pattern,epproms[0])
                    if mt:
                        groups = mt.groups()
                        block = """{0}"""
                        parameter_name = f"\tvar parameter_name = String.Format(\"{groups[0]}._{block}_.{groups[2]}\",Block);\n"
                        nvm_file.write(block_func_name)
                        nvm_file.write(parameter_name)
                        nvm_file.write(f"\tBB_CompareParameterByName(parameter_name,{expect_name});\n")
                        nvm_file.write("}\n\n")
                        block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block);\n")
                    else:# 如果没有匹配到单个参数模式，则表示这是一个global
                        nvm_file.write(global_func_name)
                        parameter_name = f"\tvar parameter_name = {epproms[0]};\n"
                        # nvm_file.write(parameter_name)
                        nvm_file.write(f"\tBB_CompareParameterByName('{epproms[0]}',{expect_name});\n")
                        nvm_file.write("}\n\n")
                        global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                else: # 有多个NVM参数的时候
                    params = []
                    # print(epproms)
                    #循环去匹配里面的数据
                    for epprom in epproms:
                        mt = re.match(mutil_pattern, epprom)
                        if mt == None: #如果这里没有找到，可能也是要比较多个参数，跳出循环
                            # print(epprom,mt)
                            break;
                        params.append(list(mt.groups()))

                    if len(params) == 0:
                        nvm_file.write(global_func_name)
                        for epprom in epproms:
                            parameter_name = f"\tvar parameter_name = {epprom};\n"
                            # nvm_file.write(parameter_name)
                            nvm_file.write(f"\tBB_CompareParameterByName('{epprom}',{expect_name});\n")
                        nvm_file.write("}\n\n")
                        global_nvms.append(f"BB_Check_{expect_name}_GlobalEDR();\n")
                    else:
                        df_temp = pd.DataFrame(np.array(params),
                                           columns=["parent", "block", "param", "index"])
                        Debug_Logger.debug(params)
                        df_temp = df_temp.astype({'index': 'int32'}) #强hi在转换类型为int，然后去比较最大的index
                        df_pivot_tb = df_temp.pivot_table(index=["param"], aggfunc=np.max)
                        temp_dict = df_pivot_tb.to_dict(orient="index") # 通过Piovt_table 进行分组统计，找到不同类别的参数
                        # print(temp_dict)
                        # Monitor_Logger.info(temp_dict)
                        nvm_file.write(block_func_name)
                        for tempkey in temp_dict:
                            max_index = temp_dict[tempkey]["index"]
                            parent =  temp_dict[tempkey]["parent"]
                            forloop = f"\tfor(var i = 0; i <= {max_index}; i++)\n\t{'{'}\n"
                            block = """{0}"""
                            param_index = """{1}"""
                            nvm_file.write(forloop)

                            parameter_name = f"\t\tvar parameter_name = String.Format(\"{parent}._{block}_.{tempkey}._{param_index}_\",Block,i);\n"
                            nvm_file.write(parameter_name)
                            nvm_file.write(f"\t\tBB_CompareParameterByName(parameter_name,{expect_name});\n")
                            nvm_file.write("\t};\n")

                        nvm_file.write("}\n")
                        block_nvms.append(f"BB_Check_{expect_name}_BlockEDR(Block);\n")

            global_define = "function BB_Check_GlobalEDR()\n{\n"
            nvm_file.writelines(global_define)
            for func_name in global_nvms:
                nvm_file.writelines("\t" + func_name)
            nvm_file.writelines("}")
            nvm_file.write("\n\n\n")

            block_define = "function BB_Check_BlockEDR(Block)\n{\n"
            nvm_file.writelines(block_define)
            for func_name in block_nvms:
                nvm_file.writelines("\t" + func_name)
            nvm_file.writelines("}")
            nvm_file.write("\n\n\n")

if __name__ == '__main__':
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\Read_element_2023_0309.xlsx"
    signalexcel = r"C:\Users\victor.yang\Desktop\Work\EDR\Geely_HX11_Flexray_signal_record_strategy.xlsx"
    sheet_name = "GB"
    nvm_check = "BB_EDR_Common_NVM_Check_Define.ts"
    checkfile = "BB_EDR_Common_Check_Define.ts"
    parameterfile = "BB_EDR_Parameter_Define.ts"
    transitionfile = "BB_EDR_Transition_Define.ts"
    did_config = "BB_DID_Config.ts"
    nvm_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\NVM_Mapping3.xlsx"
    tsfile = [checkfile, parameterfile, transitionfile]
    # generateEDRFunction(excel, tsfile)
    edr_config = EDR_DID_Config(excel)

    edr_config.refresh()
    edr_config.generate_check_general(checkfile)
    # edr_config.generate_check(checkfile)
    edr_config.generate_params(parameterfile)
    edr_config.generate_trans(transitionfile)
    edr_config.generate_did_config(did_config)

    # 生成 NVM的数据
    # excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\Record_element_list_leon.xlsx"
    # sheet = "Elements"
    # edr_record = EDR_RecordElement(excel, sheet)
    # edr_record.refresh()
    #
    epprom_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\EEPROM_Translation_SAIC_ZP22_P30.00.xlsm"
    epprom = Epprom_Translate(epprom_excel)
    epprom.block_ids = [2,31]
    epprom.get_edr_block()
    #
    edr_config.generate_nvm_excel(nvm_excel,epprom)
    edr_config.generate_nvm_check(nvm_check,nvm_excel)
    # signalts = "BB_EDR_sigParameter_Define.ts"
    # generateSignalParameter(signalexcel, signalts)