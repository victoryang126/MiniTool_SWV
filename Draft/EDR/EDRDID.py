import pandas as pd

# def

def generateEDRFunction(excel,sheet_name,tsfile):
    allsheet = pd.read_excel(excel, sheet_name=None)
    checkfile, parameterfile, transitionfile = tsfile
    with open(checkfile, 'w', encoding='UTF-8') as check:
        pass
    with open(parameterfile, 'w', encoding='UTF-8') as para:
        pass
    with open(transitionfile, 'w', encoding='UTF-8') as trans:
        pass
    df_trans_func = pd.Series()
    for sheet_name in allsheet:
        print(sheet_name)
        df = pd.read_excel(excel, sheet_name)
        columnslist = ["ID","Name", "ParameterValue", "NotRecordValue", "Start", "Length", "End"]
        df = df[columnslist]
        df = df.iloc[1:] # 剔除header 第一行
        df.fillna("undefined",inplace = True)
        df.set_index("ID", inplace=True)
        # print(df.columns)
        # print(df)

        # 处理Transition 函数部分
        df_trans_func = pd.concat([df_trans_func, df["ParameterValue"]])

        func_name = "function BB_Check_" + sheet_name + "_EDR(Type,DataRecord)\n{\n"
        with open(checkfile, 'a', encoding='UTF-8') as check:
            check.writelines(func_name)
        with open(checkfile, 'a', encoding='UTF-8') as check:
            with open(parameterfile, 'a', encoding='UTF-8') as para:
                for i in df.index:
                    # print(df.loc[i, "Name"].
                    # 处理check函数部分
                    name = df.loc[i, "Name"].replace("\n", " ")
                    comment = "\t// " + i + " : " + name + ";\n"
                    check.writelines(comment)
                    action = "\t" + '''var Action = "Check " + Type + " Value: ''' + name + "\";\n"
                    check.writelines(action)
                    parametervalue = "\t" + "var ParameterValue = " + df.loc[i, "ParameterValue"] + ";\n"
                    check.writelines(parametervalue)
                    start = str(df.loc[i, "Start"])
                    length = str(df.loc[i, "Length"])
                    # print(type(length),length)

                    callfunc = "\t" + '''BB_Check_ParameterValue(Action, ParameterValue, DataRecord, ''' \
                               + start + ", " + length + ''' )''' + ";\n"
                    # callfunc = start + ", " + length
                    check.writelines(callfunc)
                    check.write("\n")

                    # 处理Parameter部分
                    parameter_name = df.loc[i, "ParameterValue"]
                    parameter_define = "var " + parameter_name + ''' = "";\n'''
                    para.writelines(parameter_define)
        with open(checkfile, 'a', encoding='UTF-8') as check:
            check.writelines("}")
            check.write("\n\n\n")
    df_trans_func.name = "ParameterValue"
    df_trans_func = df_trans_func.to_frame()
    df_trans_func["Value"] = df_trans_func["ParameterValue"].apply(lambda x:"_".join(x.split("_")[:-1]))
    # df_trans_func["Value"] = df_trans_func["Value"].str[]
    # print(type(df_trans_func))
    df_trans_func_group = df_trans_func.groupby("Value",sort=False)
    df_trans_func = df_trans_func_group.apply(lambda x: x["ParameterValue"].values)
    # df_trans_func.set_index("Value",inplace=True)
    # print(df_trans_func)
    # df_temp = df_trans_func.pivot(index="Value")
    df_trans_func = df_trans_func.to_frame()
    df_trans_func.columns = ["ParameterValue"]
    # print(df_trans_func)
    # print(df_trans_func["ParameterValue"])
    func_call = []
    with open(transitionfile, 'a', encoding='UTF-8') as trans:
        for i in df_trans_func.index:
            func_name = "function BB_" + i + "_Transition()\n{\n"
            func_call.append("BB_" + i + "_Transition()")
            trans.writelines(func_name)
            comment = "\t// " + " : " + ", ".join(df_trans_func.loc[i,"ParameterValue"]) + ";\n"
            trans.writelines(comment)
            assign_value = "\t" + df_trans_func.loc[i, "ParameterValue"] + '''= "0xFF";\n'''
            trans.writelines(assign_value)
            trans.writelines("}")
            trans.write("\n\n\n")

    with open(transitionfile, 'a', encoding='UTF-8') as trans:
        callfunc_define = "function BB_EDR_Transition()\n{\n"
        trans.writelines(callfunc_define)
        for func_name in func_call:
            trans.writelines("\t" + func_name + ";\n")
        trans.writelines("}")
        trans.write("\n\n\n")



def generateSignalParameter(signalexcel, signalts):
    allsheet = pd.read_excel(signalexcel, sheet_name=None)

    df_sig = pd.Series()
    with open(signalts, 'w', encoding='UTF-8') as sigf:
        pass
    for sheet_name in allsheet:
        print(sheet_name)
        df = pd.read_excel(signalexcel, sheet_name)
        df = df["Signal"]
        df_sig = pd.concat([df_sig, df], ignore_index=True)

    df_sig = df_sig.apply(lambda x:x.split("(")[0])
    df_sig = df_sig.drop_duplicates(keep="first")

    with open(signalts, 'a', encoding='UTF-8') as sigf:
        for i in df_sig.index:
            print(df_sig.loc[i])
            parameter_define = "var " + df_sig.loc[i] + ''' = "";\n'''
            sigf.writelines(parameter_define)




if __name__ == '__main__':
    excel = r"C:\Users\victor.yang\Desktop\Work\EDR\EDR DID.xlsx"
    signalexcel = r"C:\Users\victor.yang\Desktop\Work\EDR\Geely_HX11_Flexray_signal_record_strategy.xlsx"
    sheet_name = "GB"
    checkfile = "BB_EDR_Common_CheckFunction_Define.ts"
    parameterfile = "BB_EDR_Parameter_Define.ts"
    transitionfile = "BB_EDR_Transition_Define.ts"
    tsfile = [checkfile, parameterfile, transitionfile]
    generateEDRFunction(excel, sheet_name, tsfile)

    signalts = "BB_EDR_sigParameter_Define.ts"
    generateSignalParameter(signalexcel, signalts)