import os
import re
import json
#-------------------------------------------------------------------------------------------------
#初始化，创建两个文件，一个用来存放Object，一个用来存放Parameters, 用在Generate 第一步
#file: 文件名字ObjectFile
def InilizeFile(ObjectFile):
    f = open(ObjectFile,'w',encoding='UTF-8')
    f.close()
#-------------------------------------------------------------------------------------------------
#初始化，如果某个路径下文件俺家不存在，则创建，否则不运行
#file: 文件名字ObjectFile
def CreateFolder_IfNotExist(path):
    if not os.path.exists(path):
        os.mkdir(path)

#-------------------------------------------------------------------------------------------------
#定义一个function给固定的ts文件里面追加信息，主要是需要在Regression里面用到的parameters
#file: 文件名字
#strline: parameters 例如 在js里面 var Support_DCS = [];
def AddParameter2Ts(ParameterFile, Strline):
	with open(ParameterFile, 'a', encoding='UTF-8') as f:
		f.writelines(Strline)
		f.write("\n")

# 由于历史原因，这个部分后期不再使用
def AddObject2Ts(ObjectFile,Strline):
    with open(ObjectFile, 'a', encoding='UTF-8') as f:
        f.writelines(Strline)
        f.write("\n")

#-------------------------------------------------------------------------------------------------
#定义一个function给固定的ts文件里面追加信息，主要是需要在Regression里面用到的字典对象
#ObjectFile: 文件名字
#VarArguments:
# ObjectDict
def DumpObject2Ts(ObjectFile,VarArguments,ObjectDict):
    with open(ObjectFile, 'a', encoding='UTF-8') as f:
        f.write(VarArguments)
        json.dump(ObjectDict, f, indent=4)
        f.write(";\n")

#-------------------------------------------------------------------------------------------------
#定义一个function获取Parameter 然后将Parameter写入ts
#file: 文件名字
#strline: parameters 例如 在js里面 var Support_DCS = [];
def GetParameters(ObjectType, DictObject, Fault, RegressionParameterLoc):
    # 将参数写入文件
    ParaObjStr = ObjectType + "_Object"

    # 1**********. 支持的Fault 数组
    #var DCS_Fault = ['CrossC', 'STB', 'GND', 'Open', 'TooHigh', 'TooLow', 'BadSensor', 'CFG']
    if(Fault != "None"):
        TmpStr = "var G_" + ObjectType + "_Fault = " + str(Fault) + ";"
        # print(TmpStr)
        AddParameter2Ts(RegressionParameterLoc, TmpStr)

    #2**********. 该类型可配置的有哪些
    #var SupportDCS = ['BBSD', 'BBSP', 'BB2L', 'BB3L', 'BB3R']
    SupportObjectStr = list(DictObject.keys())
    # print(SupportObjectStr.__len__())
    TmpStr = "var G_Support" + ObjectType + " = " + str(SupportObjectStr) + ";"
    # print(TmpStr)
    AddParameter2Ts(RegressionParameterLoc, TmpStr)

    # 3.**********该类型支持CrossConnect 错误的有哪些 var CrossCDCS = ['BBSD', 'STSDX', 'STSPX', 'PACOSA', 'PACOSB'];
    #   ***********改类型不支持CrossConnect错误的有哪些 var NSCrossCDCS = [];

    if "CrossC" in Fault:
        CrossCObjStr = [i for i in DictObject if DictObject[i]["CrossC"] != "undefined"]
        TmpStr = "var G_CrossC" + ObjectType + " = " + str(CrossCObjStr) + ";"
        # print(TmpStr)
        AddParameter2Ts(RegressionParameterLoc,TmpStr)
        NSCrossCObjStr = [i for i in DictObject if DictObject[i]["CrossC"] == "undefined"]
        TmpStr = "var G_NSCrossC" + ObjectType + " = " + str(NSCrossCObjStr) + ";"
        AddParameter2Ts(RegressionParameterLoc,TmpStr)



#-------------------------------------------------------------------------------------------------
#定义一个function，获取模板文件的内容，和模板文件的名字
# 参数：，模板文件（路径加名字）
#返回： 模板文件内容，模板文件的测试类型
def GetTempleteScript(ScriptTemplate):
    with open(ScriptTemplate, "r",encoding='UTF-8') as TmpF:
        Templete = TmpF.read()
    ret = re.compile(r'\w+(?=\.ts)', re.I) # 抓取脚本的名字
    TestType = ret.search(ScriptTemplate).group().split("_")[1]
    return Templete,TestType

#-------------------------------------------------------------------------------------------------
#定义一个function，用于根据模板脚本创建新脚本
# 参数：，Template 模板脚本的内容，
#         TestType. 模板文件的名字格式为Sensor_FaultCheck，新脚本名字就根据测试对象名字 ObjectStr_FaultCheck.ts
#         ObjectType : sheet Name
#         TestObject : 每个测试对象
#返回： 模板文件内容，模板文件的测试类型
def CreateScript(ScriptTemplateContent, ScriptPath,TestType, ObjectType, TestObjectStr,TestProject):
    #1.*********替换__XXXX,__YYYY  __XXXX为测试对象名字，string，__YYYY为sheet name，测试对象类型
    TempleteTemp = ScriptTemplateContent.replace("__XXXX", TestObjectStr)
    TempleteTemp = TempleteTemp.replace("__YYYY",ObjectType)
    TempleteTemp = TempleteTemp.replace("__ZZZZ", TestProject)
    #2.******** 根据测试类型生成新的测试脚本
    # ScriptFile = "Scripts\\" + TestObjectStr + "_" + TestType + ".ts"
    if  not ScriptPath:
        raise Exception("folder to save Scripts not been selected")
    ScriptFile = ScriptPath + "/" + TestObjectStr + "_" + TestType + ".ts"
    with open(ScriptFile, "w") as ScriptTemp:
        ScriptTemp.write(TempleteTemp)
