import pandas as pd
import os
import sys


import os
from CommonFunction import CommonFun
from Regression import CrashOutput

# import ComFun

# #依据文件名字，时间，scale 和data往curves写数据
# def CreateCrashCurves(File,Time,DataScale,Data):
#     File = "./CrashData/" + File
#     with open(File, 'w', encoding='UTF-8') as f:
#         # print(int(Time)*int(DataScale))
#         for i in range(int(Time)*int(DataScale)):
#             f.writelines(str(Data))
#             f.write("\n")

#依据文件名字，时间，scale 和data往curves写数据
def CreateCrashCurves_Complex(CrashDataPath,File,Time,DataScale,Data):
    print("CreateCrashCurves_Complex")
    if  not CrashDataPath:
        raise Exception("folder to save Crash data not been selected")
    # print(type(File))
    File = CrashDataPath + "/" + File
    with open(File, 'w', encoding='UTF-8') as f:
        # print(int(Time)*int(DataScale))
        # print(Time)
        # print(Data,type(Data))
        # print(TimeList)

        TimeList = Time.split("&")
        DataList = Data.split("&")
        # print(DataList)
        # except Exception:
        #     print("Test")
        for t in range(len(TimeList)):
            for i in range(int(TimeList[t])*int(DataScale)):
                # print(DataList[t])
                f.writelines(DataList[t] if(t < len(DataList)) else DataList[0])
                f.write("\n")

def JoinSeries(df)->pd.Series:
    """
    处理sensor titile 下面的数据，根据group 的结果，将sensor list 和Time 的数据用 "&"拼接在一起
    如下：
        SMIXX        SMIXX
        100    ->    100&200
        200
    Parameters:
        df -         DataFrame
    Returns:
        pd.Series - 将多行数据， 处理成 100&200&这种
    Raises:
        NONE
    """
    dict_temp = {}
    for col in df:
        sdata = df[col]
        if col == "CrashName" or col == "CrashCurves" or col == "DeployLoops" or col == "DTC" or col == "CrashSeverityLevel":
            dict_temp[col] = sdata.values[0]
        else:
            dict_temp[col] =  "&".join([str(i) for i in sdata.values])
    return pd.Series(dict_temp)

def JoinSeries(df,SensorList)->pd.Series:
    """
    处理sensor titile 下面的数据，根据group 的结果，将sensor list 和Time 的数据用 "&"拼接在一起
    如下：
        SMIXX        SMIXX
        100    ->    100&200
        200
    Parameters:
        df -         DataFrame
        SensorList -  sensor类型列表
    Returns:
        pd.Series - 将多行数据， 处理成 100&200&这种
    Raises:
        NONE
    """
    dict_temp = {}
    for col in df:
        sdata = df[col]
        #如果title 不在sensor list 或 不等于"Time" 则保留第一行数据
        if col not in SensorList and col != "Time":
            # print("Value: " + sdata.values[0])
            dict_temp[col] = sdata.values[0]
        else:
            dict_temp[col] =  "&".join([str(i) for i in sdata.values])
    return pd.Series(dict_temp)


def GetCrashObject(ExcelDir,ObjectType,Crash_Template,G_RegObjectFile,CrashDataPath,ScriptPath,TestProject)->"Nothing to return":

    """
    从Crash sheet中 获取各个点爆等级的波形数据，预期点爆的loops,预期出现的DTC
    Parameters:
        ExcelDir -         DataFrame
        ObjectType -       sheet的名字
        Crash_Template - 点爆case的模板
        CrashDataPath - 点爆波形的存放路径
        G_RegObjectFile - 存字典参数的ts 文件路径
        ScriptPath - 存放生成脚本的文件夹路径
        TestProject: - 项目名称
    Returns:
        NONE
    Raises:
        NONE
    """

    # pd.set_option('display.max_columns', None)
    df = pd.read_excel(ExcelDir,ObjectType,dtype = str)
    print("Crash Read Excel successfully")
    # df.set_index("Config", inplace=True)
    dfHeaderRow = 9
    dfHeaderCol = 12

    # 1.********** 获取头部配置信息字典
    dfHeader = df.iloc[0:dfHeaderRow, 0:dfHeaderCol]
    dfHeader = dfHeader[dfHeader["Config"].notnull()]
    dfHeader.set_index("Config", inplace=True)
    HeaderDict = dfHeader.to_dict(orient = "index")
    # print(HeaderDict)
    SensorColStart = HeaderDict["Config"]["SensorColStart"]
    SensorColEnd = HeaderDict["Config"]["SensorColEnd"]
    LoopColStart = HeaderDict["Config"]["LoopColStart"]
    LoopColEnd = HeaderDict["Config"]["LoopColEnd"]
    DTCColStart = HeaderDict["Config"]["DTCColStart"]
    DTCColEnd = HeaderDict["Config"]["DTCColEnd"]
    RowStart = HeaderDict["Config"]["RowStart"]
    RowEnd = HeaderDict["Config"]["RowEnd"]
    # print(SensorColStart,SensorColEnd)
    df.set_index("Config", inplace=True,drop = False) #不能丢弃该列，还保留在DataFrame中，
    print("Get Header data ")
    # 2.**********获取data/ms的数据
    df.columns = df.loc[RowStart]; # 将dataFrame的title设置为 CrashSeverityLevel 所在的行
    DataScale = df.loc["DataScale", SensorColStart:SensorColEnd].to_list()
    # 截取从CrashSeverityLevel 后面的数据 但是这个数据会包含CrashSeverityLevel 所在的行
    # 必须包含，下面获取sensor list ,LoopList DTCList 会用到
    dfConfig = df.loc[RowStart:RowEnd,]
    print("Get data/ms ")
    # 3.**********获取sensor list,Loop List,DTC list
    SensorList = dfConfig.loc[RowStart, SensorColStart:SensorColEnd].to_list()
    LoopList = dfConfig.loc[RowStart, LoopColStart:LoopColEnd].to_list()
    DTCList = dfConfig.loc[RowStart, DTCColStart:DTCColEnd].to_list()

    # 3.**********将sensor列里面没有填充的数据自动填充为0,其他数据填充为undefined
    fillNaValues = dict(zip(SensorList,[0 for i in SensorList]))
    dfConfig = dfConfig.fillna(value = fillNaValues)
    dfConfig = dfConfig.fillna("undefined")
    dfConfig = dfConfig.iloc[1:,0:] # 删除 CrashSeverityLevel 所在的行
    # print(dfConfig.index,dfConfig.columns)

    # 4 .********** 分组，根据CrashSeverityLevel 将测试对象分组，这里主要是为了处理复杂波形的数据，
    #                通过根据CrashSeverityLevel 相同的名字 将不同行的数据 拼接起来组成复杂波形
    dfConfig_Group = dfConfig.groupby(by="CrashSeverityLevel", as_index=False,sort = False)
    dfConfig = dfConfig_Group.apply(JoinSeries,SensorList = SensorList)
    print("sort ")
    # 5 .********** 获取support的Loops
    print(LoopList)
    dfLoops = dfConfig[LoopList]
    # print(dfLoops)
    for i in dfConfig.index:
        dfConfig['DeployLoops'].at[i] = [dfLoops[j].at[i] for j in LoopList if dfLoops[j].at[i] != "undefined"]
        if not dfConfig['DeployLoops'].at[i]:
            dfConfig['DeployLoops'].at[i] = ["NONE"]
    print("获取support的Loops")
    # 6 .********** 获取Support DTC
    dfDTC = dfConfig[DTCList]
    for i in dfConfig.index:
        dfConfig["DTC"].at[i] = ",".join([dfDTC[j].at[i]  for j in DTCList if dfDTC[j].at[i] != "undefined"])
        if not dfConfig["DTC"].at[i]:
            dfConfig["DTC"].at[i] = "NONE"
    print("获取Support DTC")
    # 7 .********** 创建Crash curves,并生成CrashCurves变量
    # 每个txt名字，CrashSeverityLevel+Sensor
    for i in SensorList:
        dfConfig[i + "_Curves"] =  dfConfig["CrashSeverityLevel"] + "_" + i + ".txt"
    #创建crash文件
    print("创建crash文件")
    SensorCurves = [i + "_Curves" for i in SensorList]
    for i in dfConfig.index:
        CrashCurves_List = []
        for j in range(len(SensorCurves)):
            File = dfConfig[SensorCurves[j]].at[i]
            Time = dfConfig["Time"].at[i]
            Scale = DataScale[j]
            Data = dfConfig[SensorList[j]].at[i]
            # print(File,Time,Scale,Data)
            # CreateCrashCurves(File,Time,Scale,Data)
            CreateCrashCurves_Complex(CrashDataPath,File, Time, Scale, Data)
            CrashCurves_List.append(dfConfig[SensorCurves[j]].at[i])
        #给CrashCurves 赋值
        dfConfig["CrashCurves"].at[i] = dict(zip(SensorList,CrashCurves_List))

    # 8 .********** 根据DataFrame 生成字典，导入每个点爆的等级的字典数据，然后生成测试脚本
    dfConfig.set_index("CrashSeverityLevel",inplace = True)
    dfCrash = dfConfig[["DeployLoops","CrashCurves","DTC"]]


    ObjectDict= dfCrash.to_dict(orient = "index")

    print(ObjectDict)

    crashoutput_dict = CrashOutput.GetCrashOutput(ExcelDir, "CrashOutput")

    ScriptTemplateContent, TestType = CommonFun.GetTempleteScript(Crash_Template)
    # 添加字典配置进ObjectFile里面 生成测试脚本
    for KeyTemp in ObjectDict:
        TempStr = "var " + KeyTemp + " = " + str(ObjectDict[KeyTemp]) + ";"
        # print(KeyTemp)
        CommonFun.AddParameter2Ts(G_RegObjectFile, TempStr)
        ReplaceDict = {"TestProject": TestProject, "TestObjectStr": KeyTemp, "ObjectType": ObjectType}
        ReplaceDict["CrashOutput"] = crashoutput_dict[KeyTemp]["CrashOutput"]
        CommonFun.GenerateScripts_BaseTemplate(ScriptTemplateContent, ReplaceDict, ScriptPath,KeyTemp,TestType)
    print("generate scripts")

def GetCrashCurvesObject(ExcelDir,ObjectType,G_CrashCurves,CrashDataPath):

    """
    从CreateCurves sheet中 获取各个点爆等级的波形数据，
    Parameters:
        ExcelDir -         DataFrame
        ObjectType -       sheet的名字
        G_CrashCurves - 存字典参数的ts 文件路径
        CrashDataPath - 点爆波形的存放路径
    Returns:
        NONE
    Raises:
        NONE
    """

    # pd.set_option('display.max_columns', None)

    df = pd.read_excel(ExcelDir,ObjectType,dtype = str)
    # print(df)
    ColumnsLength = len(df.columns)
    SensorColStart = 5 - 1
    RowStart = 3 - 2

    # 1 .********** 获取DataScale和Sensor list
    #               由于没有配置信息，所以会从最大的列获取sensor list
    DataScale = df.iloc[RowStart - 1, SensorColStart:ColumnsLength].to_list()
    SensorList = df.iloc[RowStart, SensorColStart:ColumnsLength].to_list()

    # 2 .********** 定义 波形文件的title,截取相关数据
    SensorCurves = [Sensor + "_Curves" for Sensor in SensorList]
    # print(SensorCurves)
    dfCurves = df.iloc[RowStart:,0:ColumnsLength]
    dfCurves.columns = dfCurves.iloc[0,0:]

    #3.**********  将sensor 列里面的没有填充的数据自动填充为0
    fillNaValues = dict(zip(SensorList, [0 for i in SensorList]))
    dfCurves = dfCurves.fillna(value=fillNaValues)
    dfCurves =  dfCurves.iloc[1:,0:]
    dfCurves.fillna("undefined",inplace= True)

    # 4 .********** 分组，根据CrashSeverityLevel 将测试对象分组，这里主要是为了处理复杂波形的数据，
    #                通过根据CrashSeverityLevel 相同的名字 将不同行的数据 拼接起来组成复杂波形
    dfCurves_Group = dfCurves.groupby(by = "CrashName",as_index=False)
    dfCurves = dfCurves_Group.apply(JoinSeries,SensorList = SensorList)

    # 5 .********** 创建Crash curves,并生成CrashCurves变量
    # 每个txt名字，CrashSeverityLevel+Sensor
    for SensorTemp in SensorList:
        dfCurves[SensorTemp + "_Curves"] = dfCurves["CrashName"] + "_" + SensorTemp + ".txt"
    for IndexTemp in dfCurves.index:
        CrashCurves_List = []
        for j in range(len(SensorCurves)):
            File = dfCurves[SensorCurves[j]].at[IndexTemp]
            Time = dfCurves["Time"].at[IndexTemp]
            Scale = DataScale[j]
            Data = dfCurves[SensorList[j]].at[IndexTemp]
            # print(File,Time,Scale,Data)
            CreateCrashCurves_Complex(CrashDataPath,File, Time, Scale, Data)
            CrashCurves_List.append(dfCurves[SensorCurves[j]].at[IndexTemp])
        dfCurves["CrashCurves"].at[IndexTemp] = dict(zip(SensorList, CrashCurves_List)) #字典形式存数据

    # 6 .**********  生成波形变量，并导入到ts文件里面
    dfCurves.set_index("CrashName", inplace=True)
    dfCurves = dfCurves["CrashCurves"]
    ObjectDict = dfCurves.to_dict()
    for KeyTemp in ObjectDict:
        TempStr = "var " + KeyTemp + " = " + str(ObjectDict[KeyTemp]) + ";"
        CommonFun.AddParameter2Ts(G_CrashCurves, TempStr)
        # VarArguments = "var " + KeyTemp + " = "
        # ComFun.DumpObject2Ts(G_CrashCurves,VarArguments,ObjectDict[KeyTemp])

if __name__ == "__main__":
    pass

    ExcelDir = r"C:/Users/victor.yang/Desktop/MiniTool/RegressionImprove_HX11_SWRS.xlsx"
    ObjectType = "Crash"
    Crash_Template = r"..\Template\Crash_Check.ts"
    G_RegObjectFile = r"..\DataSource\Reg_RegressionObject.ts"
    ScriptPath = "..\OutPut"
    G_CrashCurves = "..\DataSource\Curves.ts"
    CrashDataPath = "..\Crash_Data"
    TestProject = "GAC_A55"
    GetCrashObject(ExcelDir,ObjectType,Crash_Template,G_RegObjectFile,CrashDataPath,ScriptPath,TestProject)