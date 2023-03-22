import re

import pandas as pd
from EDR.ImportModule import *
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# def
Func = """

function BB_Check_ParameterValue(Action,ParameterValue,DataRecord,Start,Length)
{
	var parameterValue_List = BB_InsertValue2List(ParameterValue,Length)
	var expectStart = 0
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(TempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromArray(DataRecord,Start,tempLength),BB_GetValueFromArray(parameterValue_List,expectStart,tempLength));
        Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}

function BB_Check_ParameterList(Action,ParameterValue_List,DataRecord,Start,Length)
{
	var expectStart = 0
	var parameterValue_List = ParameterValue_List.toString().replace(/,/gi," ");
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(tempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromArray(DataRecord,Start ,tempLength),BB_GetValueFromArray(parameterValue_List,expectStart,tempLength));
        // RESULT.InsertComment(tempLength)
		Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}


/**
 * change ABCD to 0xAB 0xCD
 * @param HexString ABCD，
 * @returns 
 */
function HexStringToByteFormatString(HexString)
{
	HexString = HexString.replace(/(0x|\s)/gi,"")
	var hex_array = new Array();
	if(HexString.length % 2 != 0)
	{
		RESULT.InterpretEqualResult("HexString length is not OK", ["0000",true],false );
		return [0]
	}
	var start_pos = 0;
	while(start_pos < HexString.length)
	{
		hex_array.push("0x" + HexString.slice(start_pos,start_pos + 2));
		start_pos +=2;
	}
	return hex_array.toString().replace(/,/gi," ");

}

/**
 * 
 * @param ParameterValue 
 * @param ArrLength 
 * @returns 
 */
function BB_InsertValue2List(ParameterValue,ArrLength)
{	
	ParameterValue = HexStringToByteFormatString(ParameterValue)
	var tempList = new Array()
	for(var i = 0; i < ArrLength; i++)
	{
		tempList[i] = ParameterValue
	}

	var ret = tempList.toString().replace(/,/gi," ");
	return ret.split(" ")
}





function BB_ReturnCompareResultIgnoreH(ActualData,ExpectData)
{
	ActualData = ActualData.replace(/(0x|\s)/gi,"")
	ExpectData = ExpectData.replace(/(0x|\s)/gi,"")
	//create a Reg that ignore the data represent by "H"
	var L_Temp = "^" +  ExpectData.replace(/H/gi,"\\S") + "$";
	// var L_Temp = ExpectData.replace(/H/gi,"\S");
	var L_Reg = new RegExp(L_Temp,'gi')
	var L_Match = ActualData.match(L_Reg); //if get the match, it shall return an array which contains the matched data
	if(L_Match == null)//Fail.Can't get the match data
	{
		return false;
	}
	else //Pass
	{
		return true;
	}
}

function BB_CompareIgnoreH(Action,ActualResp,ExpectResp)
{

	if(BB_ReturnCompareResultIgnoreH(ActualResp,ExpectResp))
	{
		RESULT.LogCustomAction(Action, ActualResp, ExpectResp, TestStatus.Passed);
	}
	else
	{
		RESULT.LogCustomAction(Action, ActualResp + "->Length->" + ActualResp.length, ExpectResp+ "->Length->" + ExpectResp.length, TestStatus.Failed);
	}


}

function BB_GetValueFromArray(DataRecord_Array,LowIndex,ArrLength)
{
	var tempList = new Array()

	for(var i = LowIndex; i < LowIndex + ArrLength; i++)
	{
		tempList.push(DataRecord_Array[i])

	}
	return tempList.toString().replace(/,/gi," ");
}

// function BB_GetValueFromStirng(DiagValue,LowIndex,ArrLength)
// {
//     // RESULT.InsertComment(5)
// 	var tempList = new Array()
// 	var diagValueList = DiagValue.split(" ")
// 	var j = 0;
// 	for(var i = LowIndex; i < LowIndex + ArrLength; i++)
// 	{
// 		tempList[j] = diagValueList[i]
// 		j++;
// 	}
//     // RESULT.InsertComment(tempList)
// 	return tempList.toString().replace(/,/gi," ");
// }


var all_message_id_list = [
    0x2FC,
    0xC9,
    0x764,
    0x55,
    0x221,
    0x1C3,
    0x60,
    0x165,
    0x22C,
    0x3B4,
    0x47D,
    0x3B1,
    0x1B1,
    0x69,
    0x16E,
    0x354,
    0x1B2,
    0xFB,
    0x368
]

"""
class Epprom_Translate:
    def __init__(self,excel):
        self.excel = excel
        self._block_ids = []
        self.sheet = "EEPROM Parameters"
        self.edr_block_params = None
        self.df_edr_block = pd.DataFrame()

    @property
    def block_ids(self):
        return self._block_ids

    @block_ids.setter
    def block_ids(self,ids):
        self._block_ids = ids

    @block_ids.getter
    def block_ids(self):
        return self._block_ids

    @func_monitor
    def get_edr_block(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(self.excel,self.sheet)
        df = df[["PARAMETER NAME","BLOCK SIGNATURE","BLOCK ID"]]
        self.df_edr_block = df.loc[df["BLOCK ID"].isin(self.block_ids)]
        self.df_edr_block.columns = ["PARAMETER_NAME","BLOCK_SIGNATURE","BLOCK_ID"]
        self.edr_block_params = list(self.df_edr_block["PARAMETER_NAME"].values)

class EDR_Config:
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
            columnslist = ["ID", "Name", "Start", "Length", "End", "Signal",
                           "Type","NVM"]
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            df.fillna("", inplace=True)
            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df.set_index("ID", inplace=True, drop=False)
            self.df_read_element = pd.concat([ self.df_read_element, df[["Name", "Signal", "Type","NVM","ID"]]])

    @func_monitor
    def generate_check(self,checkfile):
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            # df = pd.read_excel(excel, sheet_name)
            columnslist = ["ID", "Name", "Start", "Length", "End", "Signal"]
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            df.fillna("", inplace=True)
            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df.set_index("ID", inplace=True, drop=False)

            func_name = "function BB_Check_" + sheet_name + "_EDR(Type,DataRecord)\n{\n"
            with open(checkfile, 'a', encoding='UTF-8') as check: #写入函数名称
                check.writelines(func_name)
            with open(checkfile, 'a', encoding='UTF-8') as check:  #根据里面的数据写入数据
                with open(parameterfile, 'a', encoding='UTF-8') as para:
                    for i in df.index:
                        # 处理check函数部分
                        name = df.loc[i, "Name"].replace("\n", " ")
                        comment = f"\t//{i} : {name};\n"
                        check.writelines(comment)
                        parametervalue = "\t" + "var ParameterValue = " + df.loc[i, "Name"] + ";\n"
                        check.writelines(parametervalue)
                        start = str(df.loc[i, "Start"])
                        length = str(df.loc[i, "Length"])
                        action = f"\tvar Action = \"Check \" + Type + \" Value: {name} start:{start} length:{length} \";\n"
                        check.writelines(action)
                        callfunc = "\t" + '''BB_Check_ParameterValue(Action, ParameterValue, DataRecord, ''' \
                                   + start + ", " + length + ''' )''' + ";\n"
                        check.writelines(callfunc)
                        check.write("\n")
            with open(checkfile, 'a', encoding='UTF-8') as check:
                check.writelines("}")
                check.write("\n\n\n")

    @func_monitor
    def generate_trans(self,transitionfile):
        df_trans_func = self.df_read_element.copy()
        df_trans_func["Value"] = df_trans_func["Name"].apply(lambda x: "_".join(x.split("_")[:-1]))

        df_trans_func = df_trans_func.pivot_table(index=['Value'], sort=False,
                                                  aggfunc=lambda x: '\n'.join(x))
        func_call = []
        with open(transitionfile, 'a', encoding='UTF-8') as trans:
            trans.write("CALL(BB_EDR_Parameter_Define.ts);\n")
            for i in df_trans_func.index:
                func_name = "function BB_" + i + "_Transition()\n{\n"
                func_call.append("BB_" + i + "_Transition()")
                trans.writelines(func_name)
                comment = "\t// " + "ReqID : " + ", ".join(df_trans_func.loc[i, "ID"].split("\n")) + ";\n"
                trans.writelines(comment)
                comment = "\t// " + "DID Element Name : " + ", ".join(df_trans_func.loc[i, "Name"].split("\n")) + ";\n"
                trans.writelines(comment)
                comment = "\t// " + "Signal : " + ", ".join(df_trans_func.loc[i, "Signal"].split("\n")) + ";\n"
                trans.writelines(comment)
                templist = df_trans_func.loc[i, "NVM"].split("\n") # 获取NVM的参数，
                templist = [a.strip().replace(".", "") + "_NVM" for a in templist]
                comment = "\t// " + "NVM : " + ", ".join(templist) + ";\n"
                # comment = "\t// " + "NVM : " + ", ".join(df_trans_func.loc[i, "NVM_Parameter"].split("\n")) + ";\n"
                trans.writelines(comment)
                assign_values = df_trans_func.loc[i, "Name"].split("\n")
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
        df_trans_func = self.df_read_element.copy()
        element_names = []
        signals = []
        nvm_params = []
        for i in df_trans_func.index:
            element_names.extend(df_trans_func.loc[i, "Name"].split("\n"))
            signals.extend(df_trans_func.loc[i, "Signal"].split("\n"))
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
            para.write("//Element Name ;\n")
            para.writelines(element_names)
            para.write("//Signals Name;\n")
            para.writelines(signals)
            para.write("//NVM Parameters;\n")
            para.writelines(nvm_params)



    @func_monitor
    def generate_nvm_excel(self,nvm_excel,epprom:Epprom_Translate):
        df_trans_func = self.df_read_element.copy()
        args = []
        for i in df_trans_func.index:
            args.extend(df_trans_func.loc[i, "NVM"].split("\n"))
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
    # def generate(self):
    #     allsheet = pd.read_excel(excel, sheet_name=None)
    #     checkfile, parameterfile, transitionfile = tsfile
    #     with open(self.checkfile, 'w', encoding='UTF-8') as check:
    #         check.write("CALL(BB_EDR_Transition_Define.ts);\n")
    #     with open(self.parameterfile, 'w', encoding='UTF-8') as para:
    #         pass
    #     with open(self.transitionfile, 'w', encoding='UTF-8') as trans:
    #         pass
    #     df_trans_func = pd.DataFrame()
    #
    #
    #
    #     for sheet_name in allsheet:
    #         # print(sheet_name)
    #         df = pd.read_excel(excel, sheet_name)
    #         columnslist = ["ID", "Name", "Start", "Length", "End","Signal","NVM_Parameter"]
    #         df = df[columnslist]
    #         df = df.iloc[1:]  # 剔除header 第一行
    #         df.fillna("", inplace=True)
    #         #这里必须检查是否有同一个ID，如果有，要处理报错
    #         df.set_index("ID", inplace=True,drop=False)
    #         #
    #         # print(df.columns)
    #         # print(df)
    #
    #         # 处理Transition 函数部分
    #         df_trans_func = pd.concat([df_trans_func, df[["Name","Signal","NVM_Parameter","ID"]]])
    #         func_name = "function BB_Check_" + sheet_name + "_EDR(Type,DataRecord)\n{\n"
    #         with open(self.checkfile, 'a', encoding='UTF-8') as check:
    #             check.writelines(func_name)
    #         with open(self.checkfile, 'a', encoding='UTF-8') as check:
    #             with open(parameterfile, 'a', encoding='UTF-8') as para:
    #                 for i in df.index:
    #                     # print(df.loc[i, "Name"].
    #                     # 处理check函数部分
    #                     name = df.loc[i, "Name"].replace("\n", " ")
    #                     comment = "\t// " + i + " : " + name + ";\n"
    #                     check.writelines(comment)
    #
    #                     parametervalue = "\t" + "var ParameterValue = " + df.loc[i, "Name"] + ";\n"
    #                     check.writelines(parametervalue)
    #                     start = str(df.loc[i, "Start"])
    #                     length = str(df.loc[i, "Length"])
    #                     # action = "\t" + '''var Action = "Check " + Type + " Value: ''' + name + "\";\n"
    #                     action = f"\tvar Action = \"Check \" + Type + \" Value: {name} start:{start} length:{length} \";\n"
    #                     check.writelines(action)
    #                     callfunc = "\t" + '''BB_Check_ParameterValue(Action, ParameterValue, DataRecord, ''' \
    #                                + start + ", " + length + ''' )''' + ";\n"
    #                     # callfunc = start + ", " + length
    #                     check.writelines(callfunc)
    #                     check.write("\n")
    #
    #
    #         with open(self.checkfile, 'a', encoding='UTF-8') as check:
    #             check.writelines("}")
    #             check.write("\n\n\n")
    #
    #     #获取Name 里面去掉_EDRType的
    #     df_trans_func["Value"] = df_trans_func["Name"].apply(lambda x: "_".join(x.split("_")[:-1]))
    #
    #     df_trans_func = df_trans_func.pivot_table(index=['Value'],sort=False,
    #                                                   aggfunc=lambda x: '\n'.join(x))
    #     func_call = []
    #     args = []
    #     with open(transitionfile, 'a', encoding='UTF-8') as trans:
    #         for i in df_trans_func.index:
    #             func_name = "function BB_" + i + "_Transition()\n{\n"
    #             func_call.append("BB_" + i + "_Transition()")
    #
    #             args.extend(df_trans_func.loc[i, "Name"].split("\n"))
    #             args.extend(df_trans_func.loc[i, "Signal"].split("\n"))
    #             args.extend(df_trans_func.loc[i, "NVM_Parameter"].split("\n"))
    #             trans.writelines(func_name)
    #             comment = "\t// " + "ReqID : " + ", ".join(df_trans_func.loc[i, "ID"].split("\n")) + ";\n"
    #             trans.writelines(comment)
    #             comment = "\t// " + "DID : " + ", ".join(df_trans_func.loc[i, "Name"].split("\n")) + ";\n"
    #             trans.writelines(comment)
    #             comment = "\t// " + "Signal : " + ", ".join(df_trans_func.loc[i, "Signal"].split("\n")) + ";\n"
    #             trans.writelines(comment)
    #             comment = "\t// " + "NVM : " + ", ".join(df_trans_func.loc[i, "NVM_Parameter"].split("\n")) + ";\n"
    #             trans.writelines(comment)
    #             assign_values = df_trans_func.loc[i, "Name"].split("\n")
    #             assign_values = [f"\t{x}= 0xFF;\n" for x in assign_values]
    #
    #             trans.writelines(assign_values)
    #             trans.writelines("}")
    #             trans.write("\n\n\n")
    #         # print(args)
    #     args = list(set(args))
    #     args = [f"var {arg} = \"undefined\";\n" for arg in args]
    #     with open(self.parameterfile, 'w', encoding='UTF-8') as para:
    #         para.write(Func)
    #         para.writelines(args)
    #
    #     with open(transitionfile, 'a', encoding='UTF-8') as trans:
    #         trans.write("CALL(BB_EDR_Parameter_Define.ts);\n")
    #         callfunc_define = "function BB_EDR_Transition()\n{\n"
    #         trans.writelines(callfunc_define)
    #         for func_name in func_call:
    #             trans.writelines("\t" + func_name + ";\n")
    #         trans.writelines("}")
    #         trans.write("\n\n\n")



    @func_monitor
    def generate_nvm_check(self,nvm_check,nvm_excel):
        sigle_pattern =  "(\w+)(\\._\\d_.)(\S+)"
        mutil_pattern = "(\w+)(\\._\\d_.)(\S+)\\._(\\d+)_"
        df = pd.read_excel(nvm_excel,"Sheet1")
        global_nvms = []
        block_nvms = []
        with open(nvm_check, 'w', encoding='UTF-8') as nvm_file:
            # pass
            for indx in df.index:
                # print(df.loc[indx,"Original_NVM"])
                expect_name = df.loc[indx,"ExpectNVM"]
                epproms = df.loc[indx,"Epprom"].split("\n")
                block_func_name = f"function BB_Check_{expect_name}_BlockEDR(Block)\n{'{'}\n"
                global_func_name = f"function BB_Check_{expect_name}_GlobalEDR()\n{'{'}\n"
                if len(epproms) == 1:
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
                    #循环去匹配里面的数据
                    for epprom in epproms:
                        mt = re.match(mutil_pattern, epprom)
                        params.append(list(mt.groups()))

                    df_temp = pd.DataFrame(np.array(params),
                                       columns=["parent", "block", "param", "index"])
                    Debug_Logger.debug(params)
                    df_temp = df_temp.astype({'index': 'int32'}) #强hi在转换类型为int，然后去比较最大的index
                    df_pivot_tb = df_temp.pivot_table(index=["param"], aggfunc=np.max)
                    temp_dict = df_pivot_tb.to_dict(orient="index") # 通过Piovt_table 进行分组统计，找到不同类别的参数
                    # print(temp_dict)
                    Monitor_Logger.info(temp_dict)
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
    nvm_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\NVM_Mapping.xlsx"
    tsfile = [checkfile, parameterfile, transitionfile]
    # generateEDRFunction(excel, tsfile)
    edr_config = EDR_Config(excel)

    # edr_config.refresh()
    # edr_config.generate_check(checkfile)
    # edr_config.generate_params(parameterfile)
    # edr_config.generate_trans(transitionfile)
    # # edr_config.generate_nvm_excel(nvm_excel)
    # #
    # epprom_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\EEPROM_Translation_SAIC_ZP22_P20.00.xlsm"
    # epprom = Epprom_Translate(epprom_excel)
    # epprom.block_ids = [2,31]
    # epprom.get_edr_block()
    # #
    # edr_config.generate_nvm_excel(nvm_excel,epprom)

    edr_config.generate_nvm_check(nvm_check,nvm_excel)
    # signalts = "BB_EDR_sigParameter_Define.ts"
    # generateSignalParameter(signalexcel, signalts)