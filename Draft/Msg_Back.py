import pandas as pd
import numpy as np
import os
import ComFun


def DealMsgFrame(df):
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    df.drop_duplicates(subset=["MsgName"], inplace=True)
    # print(df)
    return df

# def DealSignalFrame(df,indexName):
#     dict_signal = {}
#     signal_list = [df.iloc[i].to_list() for i,indextemp in enumerate(df.index)]
#
#     print(signal_list)
#     dict_signal["InValidSg"] = signal_list
#     df_temp  = pd.Series(dict_signal)
#     df_temp.index = indexName
#     # pd_series.name = df.index[0]
#     return df_temp
def DealQualiyOrQualifyTime(df):

    for col in df:
        if col.find("Qualify") >=0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
            # print(col)
    return df

def GetMsgObject(ExcelDir, ObjectType, FaultTemplate, G_RegObjectFile,ScriptPath,TestProject):

    #1. ********** 读取excel，指定sheet
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    df.set_index("Abbreviation", inplace=True)
    DealQualiyOrQualifyTime(df)# 将时间处理成两个元素的数组
    # df.fillna("undefined",inplace = True)
    # print(df.columns)
    # print(df.index)
    # print(df.head(5))
    columns_Total = list(df.columns)
    columns_Signal = ["InValidSg","InValidSgValue","InValidSgDTC",	"InValidSgQualify",	"InValidSgDisQualify"]
    columns_Msg = [i for i in columns_Total if i not in columns_Signal]

    # print(columns_Msg)

    #2. *********将DataFrame分割成两个部分
    df_Signal = df[columns_Signal]
    # print(df_Signal)
    # print("Abbreviation" in df.columns)
    df_Msg = df[columns_Msg]
    # print(df_Msg)



    #3. ***********处理df_Msg,填充NA的部分，然后删除重复元素
    df_Msg_Group = df_Msg.groupby(by = "MsgName",as_index=False)
    df_Msg = df_Msg_Group.apply(DealMsgFrame)
    df_Msg = df_Msg.droplevel(0) #返回的是一个二级index,必须把第一级移除

    # print(df_Msg)
    # print(df_Msg["LostCommDTC"])
    # print(df_Msg["InValidDlcDTC"])
    # for name,group in df_Msg_Group:
    #     print(name)
    #     group.fillna(method = 'ffill',inplace = True)
    #     group.fillna(method='bfill', inplace=True)
    #     print(group["LostCommDTC"])
    #     print(group["InValidDlcDTC"])
    #4. 处理df_Signal
    df_Signal = df_Signal[df_Signal["InValidSg"].notnull()]
    df_Signal.fillna("undefined",inplace = True)
    # print(df_Signal.index)
    df_Signal["InValidSgValue"] = df_Signal["InValidSgValue"].str.split(",")
    df_Signal_Group = df_Signal.groupby(by="Abbreviation", as_index=False)
    # df_Signal = df_Signal_Group.apply(DealSignalFrame)
    df_Signal = pd.DataFrame(columns=["InValidSg"])
    # print(df_Temp)
    for name, group in df_Signal_Group:
        dict_Signal = {}
        dict_Signal["InValidSg"] = group.to_dict(orient = 'split')['data']
        df_Signal.loc[name] = pd.Series(dict_Signal)

    #合并两块DataFrame
    df_Msg = pd.concat([df_Msg, df_Signal], axis=1, sort=False)
    df_Msg.fillna("undefined", inplace=True)
    #
    # print(df_Msg)
    # for name, group in df_Signal_Group:
    #     dict_Signal = {}
    #     dict_Signal["InValidSg"] = {}
    #     df_group_sub = group.groupby(by="InValidSg", as_index=True)
    #     for name_sub,group_sub in df_group_sub:
    #         group_sub.drop(["InValidSg"], inplace=True,axis = 1)
    #         dict_Signal["InValidSg"][name_sub] = group_sub.to_dict(orient='split')['data']
    #     print(dict_Signal)

        # dict_Signal["InValidSg"] = group.to_dict(orient='split')['data']
        # df_Signal.loc[name] = pd.Series(dict_Signal)
        # print(pd.Series(dict_Signal))
        # pass
    # print(dict_Signal)
    # print(df_Temp.iloc[0,0])


    # '''
    #5.********* 获取所有列，删除InvalidSgValue 列，最后生成字典
    MsgDict = df_Msg.to_dict(orient ="index")
    # print(MsgDict)
    # 6.********** Parameter 信息加入到
    # ComFun.GetParameters(ObjectType, MsgDict, "None", G_RegParameterFile)
    #
    #
    # # 7. ********* 将Object 对象加入到 G_RegObjectFile
    # #			 根据字典的key 值，根据脚本模板创建新脚本
    FaultScriptTemplateContent, FaultTestType = ComFun.GetTempleteScript(FaultTemplate)
    # # 添加字典配置进ObjectFile里面
    for KeyTemp in MsgDict :
        # TempStr = "var " + KeyTemp + " = " + str(MsgDict[KeyTemp]) + ";"
        # ComFun.AddObject2Ts(G_RegObjectFile, TempStr)
        VarArguments = "var " + KeyTemp + " = "
        ComFun.DumpObject2Ts(G_RegObjectFile,VarArguments,MsgDict[KeyTemp])
        ComFun.CreateScript(FaultScriptTemplateContent,ScriptPath, FaultTestType, ObjectType, KeyTemp,TestProject)
    # '''

if __name__ == '__main__':
    ExcelDir = "C:\Python\GitHub\Minitool\DataSource\GWM_P0102_2S_RegressionImprove.xlsx"
    ObjectType = "Communication"
    FaultTemplate = "C:\Python\GitHub\Minitool\Template\Communication_FaultCheck.ts"
    G_RegParameterFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionParameter.ts"
    G_RegObjectFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionObject.ts"
    ScriptPath = "C:\Python\GitHub\Minitool\OutPut"
    TestProject = "GWM_P0102_2S"
    GetMsgObject(ExcelDir, ObjectType, FaultTemplate, G_RegObjectFile,ScriptPath,TestProject)



