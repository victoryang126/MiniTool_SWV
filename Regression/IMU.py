import pandas as pd
import os
# import ComFun
import numpy as np
import sys

import os
from CommonFunction import CommonFun

def CreateIMUCurves_Complex(IMUDataPath,File,Time,DataScale,Data):
    """
    :param IMUDataPath: 保存IMU波形数据的路劲
    :param File: 波形数据的txt的名字
    :param Time: 时间
    :param DataScale: 速率，data/s
    :param Data: 数据，LSB，
    :return: NONE
    """
    if  not IMUDataPath:
        raise Exception("folder to save IMU data not been selected")
    File = IMUDataPath + "\\" + File
    with open(File, 'w', encoding='UTF-8') as f:
        # print(int(Time)*int(DataScale))
        # print(Time)
        # print(Data)
        TimeList = Time.split("&")
        DataList = Data.split("&")
        for t in range(len(TimeList)):
            for i in range(int(TimeList[t])*int(DataScale)):
                f.writelines(DataList[t] if(t < len(DataList)) else DataList[0])
                f.write("\n")


def GetIMUObject(ExcelDir,ObjectType,IMU_Template,G_RegObjectFile,IMUDataPath,ScriptPath,TestProject):
    """
    根据Excel 里面的配置信息，抓取相关信息生成波形文件，然后根据模板脚本生成测试脚本
    保存波形数据，波形变量，测试脚本到相关路径下面
    :param ExcelDir: Regression文件的路径
    :param ObjectType:sheet 名字
    :param IMU_Template: IMU测试脚本模板
    :param G_RegObjectFile: 存放波形变量的ts文件
    :param IMUDataPath: 存放波形数据的文件夹路径
    :param ScriptPath: 存放生成测试脚本的路径
    :param TestProject:项目名称
    :return:
    """
    # pd.set_option('display.max_columns', None)
    df = pd.read_excel(ExcelDir,ObjectType,dtype = str)
    # print(df)
    dfHeaderRow = 9
    dfHeaderCol = 12
    # 1.********** 获取头部配置信息字典
    dfHeader = df.iloc[0:dfHeaderRow, 0:dfHeaderCol]
    # print(dfHeader)
    dfHeader = dfHeader[dfHeader["Config"].notnull()]
    dfHeader = dfHeader.set_index("Config")
    HeaderDict = dfHeader.to_dict(orient = "index")

    #2.******* 根据配置字典获取相关信息
    SensorColStart = HeaderDict["Config"]["SensorColStart"]
    SensorColEnd = HeaderDict["Config"]["SensorColEnd"]
    RowStart = HeaderDict["Config"]["RowStart"]
    RowEnd = HeaderDict["Config"]["RowEnd"]
    # print(SensorColStart,SensorColEnd)

    df.set_index("Config", inplace=True, drop=False)
    df.columns = df.loc[RowStart]
    DataScale = df.loc["DataScale", SensorColStart:SensorColEnd].to_list()
    # print(type(DataScale[1]),DataScale)
    # '''
    #3.******* 获取DataFrame
    dfConfig = df.loc[RowStart:RowEnd, ]
    dfConfig = dfConfig.fillna("undefined")

    #4.******* 获取sensor list,
    SensorList = dfConfig.loc[RowStart,SensorColStart:SensorColEnd].to_list()
    # print(SensorList)
    dfConfig = dfConfig.iloc[1:,0:] #去掉第一行，此行和Columns一致

    # 5.******* 波形名字定义以及生成波形，并将变量保存到相关ts文件中
    # 每个txt名字，CrashSeverityLevel+Sensor
    # dfConfig["CrashCurves"] = dfConfig["CrashCurves"].astype("list",inplace=True)
    for i in SensorList:
        dfConfig[i + "_Curves"] =  dfConfig["IMU"] + "_" + i + ".txt"
    #创建crash文件
    SensorCurves = [i + "_Curves" for i in SensorList]
    for i in dfConfig.index:
        CrashCurves_List = []
        for j in range(len(SensorCurves)):
            File = dfConfig[SensorCurves[j]].at[i];
            Time = dfConfig["Time"].at[i]
            Scale = DataScale[j]
            Data = dfConfig[SensorList[j]].at[i]
            # print(File,Time,Scale,Data)
            CreateIMUCurves_Complex(IMUDataPath,File,Time,Scale,Data)
            CrashCurves_List.append(dfConfig[SensorCurves[j]].at[i])
        dfConfig["IMUCurves"].at[i] = dict(zip(SensorList,CrashCurves_List))





    # 处理ExpectData的逻辑有问题,交给填写人员自己填写
    # df_SensorCurves = dfConfig[SensorList]
    # df_SensorCurves = df_SensorCurves.astype('float',copy = True)
    # Series_Factor = dfConfig["Factor"];
    # Series_Factor = Series_Factor.astype('float', copy=True)
    # Series_Sensitivity = dfConfig["Sensitivity"];
    # Series_Sensitivity = Series_Sensitivity.astype('float', copy=True)
    # # print(df_SensorCurves.dtypes)
    # # 处理ExpectData  = LSB/Sensitivity/Factor
    # dfConfig["ExpectData"] = df_SensorCurves.apply(lambda x:x.sum(),axis = 1)
    # dfConfig["ExpectData"] = dfConfig["ExpectData"]/Series_Sensitivity/Series_Factor
    # # print(dfConfig["ExpectData"])

    # ************ 生成脚本，保存变量
    dfConfig.set_index("IMU", inplace=True)
    dfCrash = dfConfig[["IMUCurves","ExpectData","Tolerance","Msg","Signal","SignalLength","Factor","Offset","Unsigned"]]
    ObjectDict = dfCrash.to_dict(orient = "index")
    ScriptTemplateContent, TestType = CommonFun.GetTempleteScript(IMU_Template)
    # 添加字典配置进ObjectFile里面
    for KeyTemp in ObjectDict:
        # TempStr = "var " + KeyTemp + " = " + str(ObjectDict[KeyTemp]) + ";"
        # ComFun.AddObject2Ts(G_RegObjectFile, TempStr)
        VarArguments = "var " + KeyTemp + " = "
        CommonFun.DumpObject2Ts(G_RegObjectFile,VarArguments,ObjectDict[KeyTemp])
        # CommonFun.CreateScript(ScriptTemplateContent,ScriptPath, TestType, ObjectType, KeyTemp,TestProject)
        ReplaceDict = {"TestProject": TestProject, "TestObjectStr": KeyTemp, "ObjectType": ObjectType}
        CommonFun.GenerateScripts_BaseTemplate(ScriptTemplateContent, ReplaceDict, ScriptPath, KeyTemp, TestType)
    # '''
if __name__ == "__main__":
    G_RegParameterFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionParameter.ts"
    G_RegObjectFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionObject.ts"
    ExcelDir = "C:\Python\GitHub\Minitool\DataSource\RegressionImprove.xlsx"
    IMU_Template = "C:\Python\GitHub\Minitool\Template\IMU_DataCheck.ts"
    IMUDataPath = "C:\Python\GitHub\Minitool\Crash_Data"
    ScriptPath = "C:\Python\GitHub\Minitool\OutPut"
    TestProject = "GAC_A55"
    GetIMUObject(ExcelDir,"IMU",IMU_Template,G_RegObjectFile,IMUDataPath,ScriptPath,TestProject)



