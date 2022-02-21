import pandas as pd
import sys
import os
from CommonFunction import CommonFun

def SplitCellValue2List(df,Feature_Str) -> pd.DataFrame:

    for col in df:
        if col.find(Feature_Str) >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df

def GetOtherFaultObject(ExcelPath):
    Df_OtherFault = pd.read_excel(ExcelPath, sheet_name="OtherFault",dtype='str')
    Df_OtherFault = Df_OtherFault.fillna("")
    """
    JS里面的函数的参数必须是字符串格式，然后将字符串格式处理成对应的数据
    """
    # 将QualifyTime处理成
    SplitCellValue2List(Df_OtherFault,"Qualify")
    SplitCellValue2List(Df_OtherFault,"Fault_Args")
    # print(Df_OtherFault["QualifyTime"])
    # print(Df_OtherFault["ActiveFault_Args"])
    Df_OtherFault.set_index("TestObjectStr", inplace=True, drop=False)
    # print(Df_OtherFault.loc["Power_Over","QualifyTime"])
    Dict_OtherFault = Df_OtherFault.to_dict(orient="index")
    return Dict_OtherFault
    # print(Dict_OtherFault["Power_Over"]["DisQualifyTime"])
    # pass

def GenerateOtherFaultScripts(Dict_OtherFault,TemplateFolder,ScriptOutputPath):
    for TestObject_Str in Dict_OtherFault:
        ReplaceDict = Dict_OtherFault[TestObject_Str]
        ScriptTemplate = TemplateFolder + "\\" + ReplaceDict["ScriptTemplate"]
        print(ScriptTemplate)
        TempleteContent,Test_Type = CommonFun.GetTempleteScript(ScriptTemplate)
        print(Test_Type)
        CommonFun.GenerateScripts_BaseTemplate(TempleteContent,ReplaceDict,ScriptOutputPath,TestObject_Str,Test_Type)

def GenerateOtherFaultScriptsViaExcel(ExcelPath,TemplateFolder,ScriptOutputPath):
    Dict_OtherFault = GetOtherFaultObject(ExcelPath)
    GenerateOtherFaultScripts(Dict_OtherFault,TemplateFolder,ScriptOutputPath)

if __name__ == "__main__":
    ExcelPath = "C:\Python\MiniTool_New\Draft\Fault\Test.xlsx"
    Dict_OtherFault = GetOtherFaultObject(ExcelPath)
    TemplateFolder = "C:\Python\MiniTool_New\Draft\Fault"
    ScriptOutputPath = "C:\Python\MiniTool_New\Draft\Fault"
    GenerateOtherFaultScripts(Dict_OtherFault,TemplateFolder,ScriptOutputPath)