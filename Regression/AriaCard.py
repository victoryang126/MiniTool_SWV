import pandas as pd
import sys

import os
from CommonFunction import CommonFun

def DealQualiyOrQualifyTime(df) -> pd.DataFrame:
    """
    处理Excel中的qualify和disqualify 时间
    当前的规则是在单元格里面填写 1000, 2000 或者1000,
    然后将单元格弄从两个元素的列表
    Parameters:
        df - DataFrame 包含qualify和disqualify 的数据
    Returns:
        df - 处理了qualifytime和disqualifytime 以后的DataFrane
    Raises:
        NONE
    """
    for col in df:
        if col.find("Qualify") >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df

def GetSensorObject(ExcelDir, ObjectType, FaultTemplate, NormalTemplate, G_RegParameterFile, G_RegObjectFile,
                    ScriptPath, TestProject):
    """
    从Regression 的excel文件，获取特定sheet 内sensor的属性，然后把这个Dict输出到特定文件中形成json对象
    在获取文件文件的过程中往parameter.ts文件中写入Regression需要的参数
    并根据每个需要测试的AriaCard 对象去生成测试脚本
    Parameters:
        ExcelDir  - Reg_Excel 的路径
        ObjectType -类型名字，即Sheet名字 DCS/Loop/RSU/GPO/ENS
        FaultTemplate - 测试Fault 的模板
        NormalTemplate - 测试正常case的模板，目前仅DCS 使用这个参数
        G_RegParameterFile - 存在非字典参数的ts 文件路径
        G_RegObjectFile - 存在字典参数的ts 文件路径
        ScriptPath - 存放生成脚本的文件夹路径
        TestProject: - 项目名称
    Returns:
        NONE
    Raises:
        NONE
    """

    # 定义 对象字典
    ObjectDict = {}
    dfHeaderRow = 9
    dfHeaderCol = 12

    df = pd.read_excel(ExcelDir, ObjectType, dtype='str')
    df.set_index("Abbreviation", inplace=True, drop=False)
    df.drop(["SensorType"], inplace=True, axis=1)
    # del df["SensorType"]
    # print(df.head(5))
    # 1.********** 获取头部配置信息字典
    dfHeader = df.iloc[0:dfHeaderRow, 0:dfHeaderCol]
    # 去除空白的区域 并获取头部信息的字典
    dfHeader = dfHeader[dfHeader["Abbreviation"].notnull()]

    dfHeader = dfHeader.set_index("Abbreviation")  # 将Abbreviation 设置为index
    dfHeader = dfHeader.fillna("undefined")  # 将空白区域填充为undefined
    # 获取头部区域文件的属性，主要是读取Sensor的开始行，Status 状态获取的列，Fault状态获取的列
    HeaderDict = dfHeader.to_dict(orient="index")  # 字典：多行配置信息
    # print(HeaderDict)
    # 2.********** 根据Header字典的内容循环处理信息，每个sensor的相关属性
    # RowStart	RowEnd	NormalCol	StatusColStart	StatusColEnd	FaultColStart	FaultColEnd

    for key in HeaderDict:

        # 获取头部每行数据的信息，然后用来抓取
        HeaderKeyDict = HeaderDict[key]  # 字典 单行配置信
        # 根据头部信息抓取对应行的数据段
        RowStart = HeaderKeyDict['RowStart']
        RowEnd = HeaderKeyDict['RowEnd']
        dfDataTemp = df.loc[RowStart:RowEnd, ]
        dfDataTemp.columns = dfDataTemp.loc[HeaderKeyDict['RowStart'],]
        # print(dfDataTemp.columns)
        # print(dfDataTemp.index)
        Status = "undefined"  # 默认
        # 3.********** 获取Status支持哪些状态 后面加判定条件，如果DictTemp["StatusColStart"] 不是undefned才执行
        # 否则表示没有Status
        if HeaderKeyDict["StatusColStart"] != "undefined":
            StatusColStart = HeaderKeyDict["StatusColStart"]
            StatusColEnd = HeaderKeyDict["StatusColEnd"]
            # print(StatusStart,StatusEnd,HeaderKeyDict['RowStart'])
            # print(dfDataTemp.loc[HeaderKeyDict['RowStart']:, StatusStart:StatusEnd])
            Status = dfDataTemp.loc[HeaderKeyDict['RowStart'], StatusColStart:StatusColEnd].to_list()
        # print("Status ->%s"%Status)
        # '''
        # 4. ********** 获取支持的Fault有哪些
        FaultColStart = HeaderKeyDict["FaultColStart"]
        FaultColEnd = HeaderKeyDict["FaultColEnd"]
        # print(FaultColStart,FaultColEnd)
        FaultName = dfDataTemp.loc[RowStart, FaultColStart:FaultColEnd].to_list()
        # print(FaultName)
        FaultCycle = [500 for i in FaultName]
        Fault = dict(zip(FaultName, FaultCycle))
        # print(Fault)
        # '''
        # 5.******** 对dataframe进行数据处理，重新以 该df的0行为列索引，
        #           丢弃不配置的
        #			以“Abbreviation”为key 获取字典
        #			为每个DCS添加Status

        # print(dfDataTemp.head(5))
        dfDataTemp = dfDataTemp[dfDataTemp["Config"] == "Yes"]
        dfDataTemp.drop(["Config"], inplace=True, axis=1)
        dfDataTemp.drop([RowStart], inplace=True, axis=1)
        # dfDataTemp.drop([RowStart], inplace=True, axis=0)
        dfDataTemp.fillna("undefined", inplace=True)  # 填充空白区域 为undefined

        # print(dfDataTemp.head(5))
        CommonFun.DealQualiyOrQualifyTime(dfDataTemp)

        ObjectDictTemp = dfDataTemp.to_dict(orient="index")
        # print(dfDataTemp.columns)

        # 为每个DCS里面加“Status”的属性，Statu内容格式为list
        for key in ObjectDictTemp:
            if Status != "undefined":
                ObjectDictTemp[key]["Status"] = Status
        ##将这个段信息跟新到Sensor的Object里面
        ObjectDict.update(ObjectDictTemp)
        # print(ObjectDictTemp)
        # print(ObjectDict)
    # '''
    # 6.********** Parameter 信息加入到G_RegParameterFile 中
    CommonFun.GetParameters(ObjectType, ObjectDict, Fault, G_RegParameterFile)

    # 添加Sensor支持的Fault的最大范围
    # DictObject[ObjectType + "_Fault"] = Fault
    # 7. ********* 将Object 对象加入到 G_RegObjectFile
    #			 根据字典的key 值，根据脚本模板创建新脚本
    FaultScriptTemplateContent, FaultTestType = CommonFun.GetTempleteScript(FaultTemplate)
    NomrlaScriptTemplateContent, NormalTestType = CommonFun.GetTempleteScript(NormalTemplate)
    # 添加字典配置进ObjectFile里面
    for KeyTemp in ObjectDict:
        # TempStr = "var " + KeyTemp + " = " + str(ObjectDict[KeyTemp]) + ";"
        # ComFun.AddObject2Ts(G_RegObjectFile, TempStr)
        VarArguments = "var " + KeyTemp + " = "
        ReplaceDict = {"TestProject": TestProject, "TestObjectStr": KeyTemp, "ObjectType": ObjectType}
        CommonFun.DumpObject2Ts(G_RegObjectFile, VarArguments, ObjectDict[KeyTemp])
        # CommonFun.CreateScript(FaultScriptTemplateContent, ScriptPath, FaultTestType, ObjectType, KeyTemp, TestProject)
        CommonFun.GenerateScripts_BaseTemplate(FaultScriptTemplateContent,ReplaceDict,ScriptPath,KeyTemp,FaultTestType)
        if ObjectType == "DCS":
            # CommonFun.CreateScript(NomrlaScriptTemplateContent, ScriptPath, NormalTestType, ObjectType, KeyTemp,
            #                        TestProject)
            CommonFun.GenerateScripts_BaseTemplate(NomrlaScriptTemplateContent, ReplaceDict, ScriptPath, KeyTemp,
                                                   NormalTestType)

        # CommonFun.GenerateScripts_BaseTemplate(ScriptTemplateContent, ReplaceDict, ScriptPath, KeyTemp, TestType)

    # '''


if __name__ == '__main__':
    ExcelDir = "C:\Python\GitHub\Minitool\DataSource\RegressionImprove.xlsx"
    ObjectType = "DCS"
    FaultTemplate = "C:\Python\GitHub\Minitool\Template\DCS_FaultCheck.ts"
    NormalTemplate = "C:\Python\GitHub\Minitool\Template\DCS_NormalCheck.ts"
    G_RegParameterFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionParameter.ts"
    G_RegObjectFile = "C:\Python\GitHub\Minitool\DataSource\Reg_RegressionObject.ts"
    ScriptPath = "C:\Python\GitHub\Minitool\OutPut"
    TestProject = "GAC_A55"
    GetSensorObject(ExcelDir, ObjectType, FaultTemplate, NormalTemplate, G_RegParameterFile, G_RegObjectFile,
                    ScriptPath, TestProject)
