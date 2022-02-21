import pandas as pd
import numpy as np
import os
# import ComFun
import sys

import os
from CommonFunction import CommonFun

def DealMsgFrame(df):
    """
    仅处理非InValidSg 相关区域， InValidSg 需要单独处理，
    首先依据前面的数据填写空白区域内容
    然后依据后面数据填写空白区域内容
    最后，根据MsgName 删除重复内容
    :param df:
    :return: DataFrame
    """
    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    df.drop_duplicates(subset=["MsgName"], inplace=True)
    # print(df)
    return df



def GetMsgObject(ExcelDir, ObjectType, FaultTemplate, G_RegObjectFile,ScriptPath,TestProject):
    """
    根据Excel里面的信息，按照特定逻辑处理数据，抓取信号的相关信息保存字典保存到 文件中
    然后根据字典信息，替换脚本模板的相关内容，生成测试脚本
    :param ExcelDir:Regression 文件
    :param ObjectType: sheet的名字
    :param FaultTemplate: 测试脚本模板
    :param G_RegObjectFile: 用于保存数据ts文件
    :param ScriptPath: 用于保存测试脚本的路径
    :param TestProject:项目名称
    :return:NONE
    """
    #1. ********** 读取excel，指定sheet
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    df.set_index("Abbreviation", inplace=True)
    CommonFun.DealQualiyOrQualifyTime(df)# 将时间处理成两个元素的数组

    columns_Total = list(df.columns)
    columns_Signal = ["InValidSg","InValidSgValue","InValidSgDTC",	"InValidSgQualify",	"InValidSgDisQualify"]
    columns_Msg = [i for i in columns_Total if i not in columns_Signal]


    #2. *********将DataFrame分割成两个部分
    df_Signal = df[columns_Signal]
    df_Msg = df[columns_Msg]
    # print(df_Msg)



    #3. ***********处理df_Msg,填充NA的部分，然后删除重复元素
    df_Msg_Group = df_Msg.groupby(by = "MsgName",as_index=False)
    df_Msg = df_Msg_Group.apply(DealMsgFrame)

    if isinstance(df_Msg.index,pd.core.indexes.multi.MultiIndex):
        # print("####")
        df_Msg = df_Msg.droplevel(0)



     #返回的是一个二级index,必须把第一级移除
    # print(df_Msg)
    # print(df_Msg["LostCommDTC"])
    # print(df_Msg["InValidDlcDTC"])
    # for name,group in df_Msg_Group:
    #     print(name)
    #     group.fillna(method = 'ffill',inplace = True)
    #     group.fillna(method='bfill', inplace=True)
    #     print(group["LostCommDTC"])
    #     print(group["InValidDlcDTC"])


    #4.********** 处理df_Signal
    #             InValidSgValue 的数据为 ，分割的数据，可以测试多组信号值
    #
    df_Signal = df_Signal[df_Signal["InValidSg"].notnull()] # 获取InValidSg 不为空的数据
    df_Signal.fillna("undefined",inplace = True)
    # print(df_Signal.index)
    df_Signal["InValidSgValue"] = df_Signal["InValidSgValue"].str.split(",") # 将,分开的数据变成列表
    df_Signal_Group = df_Signal.groupby(by="Abbreviation", as_index=False) #根据每个缩写进行分组，
    # df_Signal = df_Signal_Group.apply(DealSignalFrame)
    df_Signal = pd.DataFrame(columns=["InValidSg"]) # 新建一个title为InValidSg 的DataFrame
    # print(df_Temp)
    for name, group in df_Signal_Group: # group即为frame的DataFrame,name 为Abbreviation
        dict_Signal = {}
        # 剔除index 和columns的以后数据列表，这样，下面的数据
        # "InValidSg": [
        #     一行数据会形成列表如下
        #     [
        #         "ECM2_ThrtlPosRatio",
        #         [
        #             "0x00",
        #             "0x01",
        #             "0xFF",
        #             "0x55"
        #         ],
        #         "undefined", DTC.如果没有则为undefined  "COM_F_SYS_WLFS_0_define"
        #         "undefined", Qualify时间 如果没有则为undefined  [50,100]
        #         "undefined" DisQualify时间 如果没有则为undefined [50,100]
        #     ],
        #
        # ]
        dict_Signal["InValidSg"] = group.to_dict(orient = 'split')['data']
        df_Signal.loc[name] = pd.Series(dict_Signal)

    #5.************* 合并两块DataFrame
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

    #6.********* 获取所有列，删除InvalidSgValue 列，最后生成字典
    MsgDict = df_Msg.to_dict(orient ="index")

    # # 7. ********* 将Object 对象加入到 G_RegObjectFile
    # #			 根据字典的key 值，根据脚本模板创建新脚本
    FaultScriptTemplateContent, FaultTestType = CommonFun.GetTempleteScript(FaultTemplate)
    # # 添加字典配置进ObjectFile里面
    for KeyTemp in MsgDict :
        VarArguments = "var " + KeyTemp + " = "
        CommonFun.DumpObject2Ts(G_RegObjectFile,VarArguments,MsgDict[KeyTemp])
        CommonFun.CreateScript(FaultScriptTemplateContent,ScriptPath, FaultTestType, ObjectType, KeyTemp,TestProject)

if __name__ == '__main__':
    # ExcelDir = "E:\GitHub\Minitool\DataSource\GWM_P0102_2S_RegressionImprove.xlsx"
    ExcelDir = "E:\GitHub\MiniTool\DataSource\CHT_SWV_EM3EF2EE4_Regression_EM3_Test Specification.xlsm"
    ObjectType = "Communication"
    FaultTemplate = "E:\GitHub\Minitool\Template\Communication_FaultCheck.ts"
    G_RegParameterFile = "E:\GitHub\Minitool\DataSource\Reg_RegressionParameter.ts"
    G_RegObjectFile = "E:\GitHub\Minitool\DataSource\Reg_RegressionObject.ts"
    ScriptPath = "E:\GitHub\Minitool\OutPut"
    TestProject = "GWM_P0102_2S"
    GetMsgObject(ExcelDir, ObjectType, FaultTemplate, G_RegObjectFile,ScriptPath,TestProject)



