from string import Template
import os
import re
import json
import pandas as pd
import sys



"""
目前生成脚本的规则
    1。定义好测试对象，和测试对象的相关属性
    2。根据测试逻辑，写好依据测试对象的相关属性的函数，即函数里面信息可以通过调用测试对象的属性获取
    3。编写模版测试用例，测试用例的编写规则是对脚本中需要变更的变量用一个特殊名称"{特殊名称}" 表示
       然后根据对象的相关信息或者其他信息
       用Template(ScriptTemplateContent).safe_substitute(ReplaceDict) 生成新的脚本内容
       然后生成脚本
"""


def InilizeFile(ObjectFile)->"Nothing to return":
    """
    初始化文件，使用 'w'模式，创建新的文件
    Parameters:
      ObjectFile - 文件名字
    Returns:
        NONE
    Raises:
        NONE
    """
    f = open(ObjectFile,'w',encoding='UTF-8')
    f.close()

def CreateFolder_IfNotExist(path)->"Nothing to return":
    """
    如果某个路径下文件不存在，则创建，否则不运行
    Parameters:
      path - 路径参数
    Returns:
        NONE
    Raises:
        IOerror - an error will be raised when the path is an file but not an folder
    """
    if not os.path.exists(path):
            os.mkdir(path)
    else:
        if os.path.isfile(path): # 如果是文件，不是文件夹，则抛出异常
            raise Exception(path + " is not a folder but a flle")


def AddParameter2Ts(ParameterFile, Strline)->"Nothing to return":
    """
    固定的ts文件里面追加信息，主要是需要在Regression里面用到的parameters,
    通过 "a" 模式追加数据，如果文件不存在，会报错
    Parameters:
      ParameterFile - 文件路径 + 文件名字
      Strline - 需要添加到文件中的字符串，不需要包含 换行符
    Returns:
        NONE
    Raises:
        NONE
    """
    with open(ParameterFile, 'a', encoding='UTF-8') as f:
        f.writelines(Strline)
        f.write("\n")

def DumpObject2Ts(ObjectFile,VarArguments,ObjectDict)->"Nothing to return":
    """
    固定的ts文件里面追加信息，主要是需要在Regression里面用到的字典对象
    通过 "a" 模式追加数据，如果文件不存在，会报错
    Parameters:
      ObjectFile - 文件路径 + 文件名字
      VarArguments - 在js 里面的字典名字 eg: var G_BBSD_DCS
      ObjectDict  -  字典对象 使用json.dump
    Returns:
        NONE
    Raises:
        NONE
    """
    with open(ObjectFile, 'a', encoding='UTF-8') as f:
        f.write(VarArguments)
        json.dump(ObjectDict, f, indent=4)
        f.write(";\n")


def GetParameters(ObjectType, Object_Dict, Fault_List, RegParameterFile)-> "Nothing to return":
    """
    获取Parameter 然后将Parameter写入ts
    如下数据
        var G_xxx_Fault = []
        var G_Supportxxx = []
        var G_CrossCxxx = []
        var G_NSCrossxxx = []

    Parameters:
      ObjectType -  对象类型，DCS/Loop/RSU
      Object_Dict - 字典对象，从excel中抓取出来的字典：测试对象 ：{测试对象的相关属性：值}
      Fault_List  - 列表，表示改类型 支持的最大fault ，例如["HighRes","LowRes","Open"]
      RegParameterFile  -  RegressionParameter.ts 的路径 + 名字
    Returns:
        NONE
    Raises:
        NONE
    """
    # 将参数写入文件
    ParaObjStr = ObjectType + "_Object"

    # 1**********. 支持的Fault 数组
    #var DCS_Fault = ['CrossC', 'STB', 'GND', 'Open', 'TooHigh', 'TooLow', 'BadSensor', 'CFG']
    if(Fault_List != "None"):
        TmpStr = "var G_" + ObjectType + "_Fault = " + str(Fault_List) + ";"
        # print(TmpStr)
        AddParameter2Ts(RegParameterFile, TmpStr)

    #2**********. 该类型可配置的有哪些
    #var SupportDCS = ['BBSD', 'BBSP', 'BB2L', 'BB3L', 'BB3R']
    SupportObjectStr = list(Object_Dict.keys())
    # print(SupportObjectStr.__len__())
    TmpStr = "var G_Support" + ObjectType + " = " + str(SupportObjectStr) + ";"
    # print(TmpStr)
    AddParameter2Ts(RegParameterFile, TmpStr)

    # 3.**********该类型支持CrossConnect 错误的有哪些 var CrossCDCS = ['BBSD', 'STSDX', 'STSPX', 'PACOSA', 'PACOSB'];
    #   ***********改类型不支持CrossConnect错误的有哪些 var NSCrossCDCS = [];

    if "CrossC" in Fault_List:
        CrossCObjStr = [i for i in Object_Dict if Object_Dict[i]["CrossC"] != "undefined"]
        TmpStr = "var G_CrossC" + ObjectType + " = " + str(CrossCObjStr) + ";"
        # print(TmpStr)
        AddParameter2Ts(RegParameterFile,TmpStr)
        NSCrossCObjStr = [i for i in Object_Dict if Object_Dict[i]["CrossC"] == "undefined"]
        TmpStr = "var G_NSCrossC" + ObjectType + " = " + str(NSCrossCObjStr) + ";"
        AddParameter2Ts(RegParameterFile,TmpStr)

def GetTempleteScript(ScriptTemplate):
    """
    获取模板文件的内容，和模板文件的名字
    Parameters:
      ScriptTemplate - 模板文件（路径加名字） 目前名字的规则是xxx_yyyy.ts
                       xxxx最终会被替换成测试对象的名字，例如G_BBSD_DCS4
                       yyyy 定义为测试类型 FaultCheck/NormalCheck等
    Returns:
        TempleteContent - 模板脚本里面的所有内容
        Test_Type - 测试类型  _yyyy.ts
    Raises:
        IOerror - 当模板脚本不能被发现的时候会抛出异常
    """
    with open(ScriptTemplate, "r",encoding='UTF-8') as TmpF:
        TempleteContent = TmpF.read()

    Test_Type ="_".join( os.path.split(ScriptTemplate)[1].split(".")[0].split("_")[1:])
    return TempleteContent,Test_Type

def CreateScript(ScriptTemplateContent, ScriptPath, Test_Type, ObjectType, TestObjectStr, TestProject):
    """
    获取Parameter 然后将Parameter写入ts
    Parameters:
      ScriptTemplateContent - 模板脚本的内容，通过GetTempleteScript 获取返回
      ScriptPath -   存放生成测试脚本的路径，文件夹
      Test_Type  -  测试类型，FaultCheck. or NormalCheck
      ObjectType -   对象类型，DCS/Loop/RSU/IMU
      TestObjectStr -测试对象， G_BBSD_DCS8
      TestProject - 项目名称
    Returns:
        模板文件内容，模板文件的测试类型
    Raises:
        IOerror - an error will be raised when no folder been selected to save the scripts
    """
    #1.*********替换为测试对象名字，测试对象类型，项目名称
    ReplaceDict = {"TestProject":TestProject,"TestObjectStr":TestObjectStr,"ObjectType":ObjectType}
    TempleteTemp = Template(ScriptTemplateContent).safe_substitute(ReplaceDict)
    #2.******** 根据测试类型生成新的测试脚本
    # ScriptFile = "Scripts\\" + TestObjectStr + "_" + TestType + ".ts"
    if  not ScriptPath:
        raise Exception("folder to save Scripts not been selected")
    ScriptFile = ScriptPath + "/" + TestObjectStr + "_" + Test_Type + ".ts"
    with open(ScriptFile, "w") as ScriptTemp:
        ScriptTemp.write(TempleteTemp)

def GenerateScripts_BaseTemplate(ScriptTemplateContent,ReplaceDict,ScriptName_W_Path):
    """

    :param ScriptTemplateContent: 模板脚本的内容
    :param ReplaceDict: 需要替换模版里面到相关内容 字典格式 Key 为模版里面需要被替换到部分
                        ，Value为 对应替换到内容
    :param ScriptName_W_Path: 需要生成到脚本，以及相关路径
    :return: NA
    """
    TempleteTemp = Template(ScriptTemplateContent).safe_substitute(ReplaceDict)
    with open(ScriptName_W_Path, "w") as ScriptTemp:
        ScriptTemp.write(TempleteTemp)


def GenerateScripts_BaseTemplate(ScriptTemplateContent,ReplaceDict,ScriptOutputPath,TestObject_Str,TestType):
    """

    :param ScriptTemplateContent: 模板脚本的内容
    :param ReplaceDict:需要替换模版里面到相关内容 字典格式 Key 为模版里面需要被替换到部分
                        ，Value为 对应替换到内容
    :param ScriptOutputPath:脚本保存的路径
    :param TestObject_Str: 测试对象的名称
    :param Test_Type: 测试类型
    :return:
    """
    ScriptName_W_Path = ScriptOutputPath + "/" + TestObject_Str + "_" +TestType + ".ts"
    TempleteTemp = Template(ScriptTemplateContent).safe_substitute(ReplaceDict)
    with open(ScriptName_W_Path, "w") as ScriptTemp:
        ScriptTemp.write(TempleteTemp)

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
if __name__ == '__main__':
    pass