import pandas as pd
from EDR.ImportModule import *
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# def
Func = """
function BB_Check_ParameterValue(Action,ParameterValue,DataRecord,Start,Length)
{
	var parameterValue_List2Str = BB_InsertValue2List(ParameterValue,Length)
	var expectStart = 0
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(TempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromStirng(DataRecord,Start +3,tempLength),BB_GetValueFromStirng(parameterValue_List2Str,expectStart,tempLength));
        Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}

function BB_Check_ParameterList(Action,ParameterValue_List,DataRecord,Start,Length)
{
	// RESULT.InsertComment(ParameterValue_List)

	var expectStart = 0
	var parameterValue_List2Str = ParameterValue_List.toString().replace(/,/gi," ");
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(tempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromStirng(DataRecord,Start +3,tempLength),BB_GetValueFromStirng(parameterValue_List2Str,expectStart,tempLength));
        // RESULT.InsertComment(tempLength)
		Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}



function BB_InsertValue2List(ParameterValue,ArrLength)
{	
	var tempList = new Array()
	for(var i = 0; i < ArrLength; i++)
	{
		tempList[i] = ParameterValue
	}
	return tempList.toString().replace(/,/gi," ");
}




function BB_ReturnCompareResultIgnoreH(ActualData,ExpectData)
{

	//create a Reg that ignore the data represent by "H"
	var L_Temp = "^" +  ExpectData.replace(/H/gi,"\\S") + "$";
	// var L_Temp = ExpectData.replace(/H/gi,"\\S");
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

function BB_GetValueFromStirng(DiagValue,LowIndex,ArrLength)
{
    // RESULT.InsertComment(5)
	var tempList = new Array()
	var diagValueList = DiagValue.split(" ")
	var j = 0;
	for(var i = LowIndex; i < LowIndex + ArrLength; i++)
	{
		tempList[j] = diagValueList[i]
		j++;
	}
    // RESULT.InsertComment(tempList)
	return tempList.toString().replace(/,/gi," ");
}
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

    def get_edr_block(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(self.excel,self.sheet)
        df = df[["PARAMETER NAME","BLOCK SIGNATURE","BLOCK ID"]]
        # df = df.loc[df["BLOCK ID"] in self.block_ids]
        # print(df.head(5))
        # print(df["BLOCK ID"].isin(self.block_ids))
        self.df_edr_block = df.loc[df["BLOCK ID"].isin(self.block_ids)]
        self.df_edr_block.columns = ["PARAMETER_NAME","BLOCK_SIGNATURE","BLOCK_ID"]
        self.edr_block_params = list(self.df_edr_block["PARAMETER_NAME"].values)
        # #
        # df["ParamterData"] = df["PARAMETER NAME"].str.split(".")
        # # print( df["ParamterData"])
        # df["Data_Type"] = df["ParamterData"].str[2]
        # print(list(set(df["Data_Type"].values)))
        # print(df.head(5))
        # params = list(df["PARAMETER NAME"].values)
        # a = "aEngN"
        # b = [x for x in params if a in x]
        # print(b)
        # data = df["ParamterData"]
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
                           "NVM_Parameter","Original_NVM"]
            df = df[columnslist]
            df = df.iloc[1:]  # 剔除header 第一行
            df.fillna("", inplace=True)
            # 这里必须检查是否有同一个ID，如果有，要处理报错
            df.set_index("ID", inplace=True, drop=False)
            self.df_read_element = pd.concat([ self.df_read_element, df[["Name", "Signal", "NVM_Parameter","Original_NVM","ID"]]])

    @func_monitor
    def generate_check(self,checkfile):
        for sheet_name in self.sheets:
            Monitor_Logger.info(sheet_name)
            df = self.sheets[sheet_name]
            # df = pd.read_excel(excel, sheet_name)
            columnslist = ["ID", "Name", "Start", "Length", "End", "Signal", "NVM_Parameter"]
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
                comment = "\t// " + "NVM : " + ", ".join(df_trans_func.loc[i, "NVM_Parameter"].split("\n")) + ";\n"
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
        args = []
        for i in df_trans_func.index:
            args.extend(df_trans_func.loc[i, "Name"].split("\n"))
            args.extend(df_trans_func.loc[i, "Signal"].split("\n"))
            #"NVM_Parameter后续处理
            args.extend(df_trans_func.loc[i, "NVM_Parameter"].split("\n"))
        args = list(set(args)) # 去重
        args = [f"var {arg} = \"undefined\";\n" for arg in args]
        with open(parameterfile, 'w', encoding='UTF-8') as para:
            para.write(Func)
            para.writelines(args)

    # @func_monitor
    # def generate_nvm_excel(self,nvm_excel):
    #     df_trans_func = self.df_read_element.copy()
    #     args = []
    #     for i in df_trans_func.index:
    #         args.extend(df_trans_func.loc[i, "NVM_Parameter"].split("\n"))
    #     args = list(set(args))  # 去重
    #     args = [a.strip() for a in args]
    #     df = pd.DataFrame({"NVM_Parameter" :args})
    #     df.to_excel(nvm_excel,index = False)

    @func_monitor
    def generate_nvm_excel(self,nvm_excel,epprom:Epprom_Translate):
        df_trans_func = self.df_read_element.copy()
        args = []
        for i in df_trans_func.index:
            args.extend(df_trans_func.loc[i, "Original_NVM"].split("\n"))
        args = list(set(args))  # 去重
        args.sort() #排列
        args = [a for a in args if a!=""]
        df = pd.DataFrame({"Original_NVM": args})
        df["Epprom"] = "undefined"
        print(df.head(5))
        for indx in df.index:
            nvm_param = df.loc[indx,"Original_NVM"]
            nvm_param = nvm_param.strip()
            #先以结尾完全匹配
            df_endswith = epprom.df_edr_block.query("PARAMETER_NAME.str.endswith(@nvm_param)")
            # pattern = f"{nvm_param}\\._\\d+\\._$"
            df_endswith_mutil = epprom.df_edr_block.query(f'PARAMETER_NAME.str.contains("{nvm_param}\\._\\d_$")',engine = 'python')
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






if __name__ == '__main__':
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\Read_element_2023_0309.xlsx"
    signalexcel = r"C:\Users\victor.yang\Desktop\Work\EDR\Geely_HX11_Flexray_signal_record_strategy.xlsx"
    sheet_name = "GB"
    checkfile = "BB_EDR_Common_Check_Define.ts"
    parameterfile = "BB_EDR_Parameter_Define.ts"
    transitionfile = "BB_EDR_Transition_Define.ts"
    nvm_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\NVM_Mapping.xlsx"
    tsfile = [checkfile, parameterfile, transitionfile]
    # generateEDRFunction(excel, tsfile)
    edr_config = EDR_Config(excel)
    edr_config.refresh()
    # edr_config.generate_check(checkfile)
    # edr_config.generate_params(parameterfile)
    # edr_config.generate_trans(transitionfile)
    # edr_config.generate_nvm_excel(nvm_excel)

    epprom_excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\EEPROM_Translation_SAIC_ZP22_P20.00.xlsm"
    epprom = Epprom_Translate(epprom_excel)
    epprom.block_ids = [2,31]
    epprom.get_edr_block()

    edr_config.generate_nvm_excel(nvm_excel,epprom)
    # signalts = "BB_EDR_sigParameter_Define.ts"
    # generateSignalParameter(signalexcel, signalts)