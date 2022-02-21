import openpyxl
import pandas as pd
import sys
sys.path.append("../../CommonFunction")
# from CommonFunction import CommonFun
import CommonFun
def SplitCellValue2List(df,Feature_Str) -> pd.DataFrame:

    for col in df:
        if col.find(Feature_Str) >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df

def ReadExcelbyOpenpy(ExcelPath):
    excel = openpyxl.load_workbook(ExcelPath)
    sheets = excel.sheetnames
    for name in sheets:
        sheet = excel[name]
        print("*****{}*****".format(name))

        for values in sheet.values:
            if(type(values[0])) is int:
                print(values)

def ReadExcelbyPandas(ExcelPath):
    Df_AllSheet = pd.read_excel(ExcelPath, sheet_name=None)

    for sheet in Df_AllSheet:
        df_sheet = pd.read_excel(ExcelPath, sheet)
        print(df_sheet)

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
        ScriptTemplate = TemplateFolder + "/" + ReplaceDict["ScriptTemplate"]
        print(ScriptTemplate)
        TempleteContent,Test_Type = CommonFun.GetTempleteScript(ScriptTemplate)
        print(Test_Type)
        CommonFun.GenerateScripts_BaseTemplate(TempleteContent,ReplaceDict,ScriptOutputPath,TestObject_Str,Test_Type)

if __name__ == "__main__":
    ExcelPath = "Test.xlsx"
    Dict_OtherFault = GetOtherFaultObject(ExcelPath)
    TemplateFolder = "/Users/monster/PycharmProjects/GitHub/MiniTool_New/Draft/Fault"
    ScriptOutputPath = "/Users/monster/PycharmProjects/GitHub/MiniTool_New/Draft/Fault"
    GenerateOtherFaultScripts(Dict_OtherFault,TemplateFolder,ScriptOutputPath)
    # ReadExcelbyOpenpy(ExcelPath)
    # ReadExcelbyPandas(ExcelPath)
    """
     Unnamed: 0                   Unnamed: 1  ... Unnamed: 5 Unnamed: 6
    0         编号                           描述  ...        参数2        参数三
    1          1      set the DCS to HighRang  ...        NaN        NaN
    2          2            wait enough time   ...        NaN        NaN
    3          3  Check the DCS status by DID  ...        NaN        NaN
    4          3  Check the DCS status by DID  ...        NaN        NaN

    """