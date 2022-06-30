import pandas as pd


def GetFuncCall(x,Col,Func_Name,Df_Sig):
    temp = Func_Name + "(\'" + Df_Sig.loc[Col, "Frame"]  + "\',\'" + Df_Sig.loc[Col, "Signal"]  + "\',"+ x + ") "
    return temp
def GetCrashOutput(ExcelDir,ObjectType):

    df = pd.read_excel(ExcelDir,ObjectType,dtype = str)
    # print(df)

    dfheader_row = 9
    dfheader_col = 12

    # 1.********** 获取头部配置信息字典
    dfheader = df.iloc[0:dfheader_row, 0:dfheader_col]
    # print(dfheader.index)
    row_start = dfheader.loc[0,"RowStart"]
    row_end = dfheader.loc[0,"RowEnd"]

    print(row_start,row_end)
    # 获取 crashoutput flag是否在Crash 脚本里面添加数据
    crashoutput_flag = dfheader.iloc[0, 0]
    print(crashoutput_flag)

    df_sig = dfheader.iloc[1:]
    df_sig.dropna(subset = 'Support',inplace = True)
    df_sig.dropna(axis = 1,how ='all',inplace = True)
    df_sig.set_index("Support", inplace=True, drop=True)
    # print(df_sig)
    # print()

    # 2 **************** 获取数据段信息
    df.set_index("Support", inplace=True, drop=False)  # 不能丢弃该列，还保留在DataFrame中，
    df_data = df.loc[row_start:row_end]

    df_data.columns = df.loc[row_start]
    df_data = df_data.iloc[1:]

    df_data.dropna(axis=1, how='all', inplace=True)
    df_data.drop_duplicates(subset="CrashSeverityLevel",keep="first",inplace= True)
    # print(df_data)

    func_name = "BB_CheckCrashValue"

    # call 函数，形成 func_name("Frame","Signa","Value")
    for col in df_data.columns:
        if col == "CrashSeverityLevel":
            continue
        df_data[col] = df_data[col].apply(lambda x: GetFuncCall(x,col,func_name,df_sig))
    df_data["CrashOutput"] = ""
    pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 8000)
    df_func_call = df_data[df_sig.index]
    # print(df_func_call)


    df_data["CrashOutput"] = df_func_call.apply( lambda x: "\n    ".join(x.values),axis = 1)
    # print(df_data["CrashOutput"])

    df_crash = df_data[["CrashSeverityLevel","CrashOutput"]]
    # print(df_crash)
    crashoutput_dict = df_crash.to_dict(orient = "index")
    # print(crashoutput_dict)
    # {'FRONT_LEVEL0': {'CrashSeverityLevel': 'FRONT_LEVEL0',
    #                   'CrashOutput': "BB_CheckCrashValue('MessageName1','SignalName1',0)
    return crashoutput_dict
    #
    # for indx in df_data.index:
    #     df_data.loc[indx,"CrashOutput"] =


if __name__ == "__main__":
    pass

    ExcelDir = r"E:\GitHub\MiniTool_SWV\Data\RegressionImprove.xlsx"
    ObjectType = "CrashOutput"
    GetCrashOutput(ExcelDir, ObjectType)

    # GetCrashObject(ExcelDir,ObjectType,Crash_Template,G_RegObjectFile,CrashDataPath,ScriptPath,TestProject)