import pandas as pd
import numpy as np
import os
import win32com
from pandas import ExcelWriter
from openpyxl.utils import get_column_letter
import re

def IsCBID(ID):
    pattern = re.compile(r'^\d+$')
    return pattern.match(ID)

def IsCBID_SWTD(ID,df_lookup):

    if ID in df_lookup["CBID"].values:
        return True
    else:
        return False


def ReplaceCellValue(CellValue,Df_LoopUp):
    CellValue_list = CellValue.split('\n')
    returnValue_List = []
    # reg =
    for i,cell in enumerate(CellValue_list):
        if cell.strip() in Df_LoopUp.index:
            returnValue_List.append(Df_LoopUp.loc[cell.strip(), "CBID"])
        elif cell.strip() == "":
            pass
        else:
            returnValue_List.append(cell.strip())
    # print(returnValue_List)
    # print("*"*30)
    returnValue = "\n".join(returnValue_List)
    # returnValue = returnValue.replace(" ","").strip()
    return returnValue
    # return CellValue_list
#1. 读取spec的
def ReadSpec_LastSheet_ReplaceDoorsID(Spec, Df_LoopUp):
    #获取最后一个sheet的名字
    Df_AllSheet = pd.read_excel(Spec, sheet_name=None)
    LastSheet_Name = list(Df_AllSheet)[-1]
    # print(LastSheet_Name)
    Df_spec = pd.read_excel(Spec, LastSheet_Name, dtype='str',header= 6)

    ColumnsList = ["Test Case Name","_VerifiesDOORSRequirements_SYS","_VerifiesDOORSRequirements_SW" ,"_VerifiesNonDOORSRequirements"]
    Df_spec = Df_spec[ColumnsList]
    Df_spec = Df_spec.fillna("")

    Df_spec['_VerifiesDOORSRequirements_SYS'] = Df_spec['_VerifiesDOORSRequirements_SYS'].apply(ReplaceCellValue,Df_LoopUp = Df_LoopUp)
    Df_spec['_VerifiesDOORSRequirements_SW'] = Df_spec['_VerifiesDOORSRequirements_SW'].apply(ReplaceCellValue,Df_LoopUp = Df_LoopUp)
    Df_spec['_VerifiesNonDOORSRequirements'] = Df_spec['_VerifiesNonDOORSRequirements'].apply(ReplaceCellValue,Df_LoopUp = Df_LoopUp)

    # print(Df_spec)
    Df_spec.set_index("Test Case Name", inplace=True)
    #获取行数
    RowSize = len(Df_spec.index)

    # print(RowSize)
    return Df_spec,LastSheet_Name,RowSize
    #NA


# def ReadLoopUp(LoopUP):
#     ColumnsList = ["CBID", "DoorsID"]
#     Df_LoopUp = pd.read_csv(LoopUP, names = ColumnsList, header = None,sep = "\t",dtype= 'str')
#
#     Df_LoopUp.set_index("DoorsID", inplace=True)
#     # print(Df_LoopUp)
#     # print(Df_LoopUp.loc["DES_SA2FC_SW_REQ_BOOT_585","CBID"])
#
#     return Df_LoopUp


#
# # '''
# # # 可以重新建立一个独立的进程
# def RepaceDoorsID_SaveMacroEcel(Spec,Df_spec,LastSheet_Name,RowSize):
#
#     w = win32com.client.DispatchEx('Excel.Application')
#     w.Visible = 0
#     w.DisplayAlerts = 0
#     # print(os.path.abspath(Spec))
#     wb = w.Workbooks.Open(os.path.abspath(Spec))
#
#     try:
#         sht = wb.Worksheets(LastSheet_Name)
#         for i in range(8,RowSize + 8):
#             if sht.Cells(i, "B").Value in Df_spec.index:
#                 # print(sht.Cells(i, "B").Value)
#                 sht.Cells(i, "M").Value = Df_spec.loc[sht.Cells(i, "B").Value,"_VerifiesDOORSRequirements_SW"]
#     except:
#         pass
#     wb.Close(SaveChanges=1)
#     #
#     w.Quit()  # 退出

def RepaceDoorsID_SaveMacroEcel(ExcelAPP,Spec,Df_spec,LastSheet_Name,RowSize):


    wb = ExcelAPP.Workbooks.Open(os.path.abspath(Spec))

    try:
        sht = wb.Worksheets(LastSheet_Name)
        for i in range(8,RowSize + 8):
            if sht.Cells(i, "B").Value in Df_spec.index:
                # print(sht.Cells(i, "B").Value)
                sht.Cells(i, "L").Value = Df_spec.loc[sht.Cells(i, "B").Value, "_VerifiesDOORSRequirements_SYS"]
                sht.Cells(i, "M").Value = Df_spec.loc[sht.Cells(i, "B").Value, "_VerifiesDOORSRequirements_SW"]
                sht.Cells(i, "N").Value = Df_spec.loc[sht.Cells(i, "B").Value,"_VerifiesNonDOORSRequirements"]
    except:
        pass
    wb.Close(SaveChanges=1)

# ''

#1. 读取spec的
def ReadSpec_TableOfContent(Spec):
    Df_spec = pd.read_excel(Spec, "Table Of Contents", dtype='str')
    ColumnsList = ["Object Text", "_VerifiesDOORSRequirements"]
    Df_spec = Df_spec[ColumnsList]
    Df_spec = Df_spec.iloc[7:,:]
    Df_spec.dropna(subset = ["Object Text"],inplace = True)

    Df_spec["_VerifiesDOORSRequirements"] = Df_spec["_VerifiesDOORSRequirements"].str.rstrip()

    #判断 _VerifiesDOORSRequirements  split为多个元素的时候，拓展元素

    Df_ReqID = Df_spec['_VerifiesDOORSRequirements'].str.split('\n', expand=True)
    # print(Df_ReqID.head(6))

    Df_ReqID = Df_ReqID.stack()
    # print(Df_ReqID.head(6))

    # #
    Df_ReqID = Df_ReqID.reset_index(level=1,drop=True)
    # print(Df_ReqID.head(6))

    #
    Df_ReqID.name = "_VerifiesDOORSRequirements"
    Df_spec = Df_spec.drop(['_VerifiesDOORSRequirements'], axis=1).join(Df_ReqID)


    # print(Df_spec.head(6))
    #没有数据的时候填充空白
    Df_spec.fillna("", inplace=True)
    # Df_spec.set
    return Df_spec
    #NA



#1. 读取spec的
def ReadSpec_TableOfContent_SWTD(Spec):
    Df_spec = pd.read_excel(Spec, "sheet", dtype='str')
    # ColumnsList = ["TestCaseName","TC ID", "Requirement ID"]
    ColumnsList = ["TestCaseName", "Requirement ID"]
    Df_spec = Df_spec[ColumnsList]
    # Df_spec = Df_spec.iloc[7:,:]
    # Df_spec.dropna(subset = ["Object Text"],inplace = True)

    Df_spec["Requirement ID"] = Df_spec["Requirement ID"].str.rstrip("/")
    print(Df_spec)
    #判断 _VerifiesDOORSRequirements  split为多个元素的时候，拓展元素

    Df_ReqID = Df_spec['Requirement ID'].str.split('\/', expand=True)
    print(Df_ReqID.head(6))

    Df_ReqID = Df_ReqID.stack()
    # print(Df_ReqID.head(6))

    # #
    Df_ReqID = Df_ReqID.reset_index(level=1,drop=True)
    # print(Df_ReqID.head(6))

    #
    Df_ReqID.name = "Requirement ID"
    Df_spec = Df_spec.drop(['Requirement ID'], axis=1).join(Df_ReqID)


    print(Df_spec.head(30))
    #没有数据的时候填充空白
    Df_spec.fillna("", inplace=True)
    # Df_spec.set
    return Df_spec

#2.读取loop up table

# def ReadLoopUp(LoopUP):
#     Df_LoopUp = pd.read_excel(LoopUP, "Export", dtype='str')
#     ColumnsList = ["DoorsID", "CBID"]
#     Df_LoopUp.set_index("DoorsID",inplace= True)
#     # print(Df_LoopUp.loc["DES_SA2FC_SW_REQ_BOOT_585","CBID"])
#
#     return Df_LoopUp

def ReadLoopUp(LoopUP):
    ColumnsList = ["CBID", "DoorsID"]
    Df_LoopUp = pd.read_csv(LoopUP, names = ColumnsList, header = None,sep = "\t",dtype= 'str')

    if True in  Df_LoopUp.duplicated(subset=['CBID']).values:
        raise Exception("duplicated CBID ID")
    elif True in  Df_LoopUp.duplicated(subset=['DoorsID']).values:
        raise Exception("duplicated  Doors ID")
    Df_LoopUp.set_index("DoorsID", inplace=True)
    # print(Df_LoopUp)
    # print(Df_LoopUp.loc["DES_SA2FC_SW_REQ_BOOT_585","CBID"])


    return Df_LoopUp

def ReadLoopUp_SWTD(LoopUP):
    ColumnsList = ["CBID", "DoorsID"]
    Df_LoopUp = pd.read_csv(LoopUP, names=ColumnsList, header=None, sep="\t", dtype='str')

    # Df_LoopUp.dropna(axis = 0,subset=['CBID'],inplace= True)
    Df_LoopUp.dropna(inplace= True)
    if True in Df_LoopUp.duplicated(subset=['CBID']).values:
        # pass
        # Df_LoopUp.drop_duplicates("CBID")
        raise Exception("duplicated CBID ID")
    elif True in Df_LoopUp.duplicated(subset=['DoorsID']).values:
        # raise Exception("duplicated  Doors ID")
        Df_LoopUp = Df_LoopUp.drop_duplicates("DoorsID",keep='first')
        # pass
    Df_LoopUp.set_index("DoorsID", inplace=True)
    print(Df_LoopUp)
    # print(Df_LoopUp.loc["DES_SA2FC_SW_REQ_BOOT_585","CBID"])

    return Df_LoopUp
    # NA
    #NA

# # 3.生成表格
# def GenerateSpec_CB(Df_spec,Df_LoopUp,SpecCB):
#     # ColumnsList = ["ID", "Priority","Name","Description","Pre-Action","Post-Action","Test Steps.Action","Test Steps.Expected result","Test Steps.Critical","Test Parameters","Verifies","Status","Type"]
#     ColumnsList = ["ID", "Parent", "Priority", "Name", "Description", "Pre-Action", "Post-Action",
#                    "Test Steps.Action", "Test Steps.Expected result",
#                    "Test Steps.Critical", "Test Parameters", "Verifies",
#                    "Status", "Type", "_Original_TestCaseId", "_Test_Technique",
#                    "_VerifiesNonCbRequirements", "_LastReviewDate", "_ScriptPath",
#                    "_TestType", "_RegressionStrategy", "_FunctionGroup", "_Feature",
#                    "Functional Safety Relevant", "Cyber Security Relevant"]
#     df_SpecCB = pd.DataFrame(columns= ColumnsList)
#     # print(df_SpecCB)
#     # ColumnsList_Temp = ["Name","Verifies"]
#
#     Df_spec['_VerifiesDOORSRequirements'] = Df_spec['_VerifiesDOORSRequirements'].apply(lambda x:x if x not in Df_LoopUp.index else "[ISSUE:" + Df_LoopUp.loc[x,"CBID"] + "]")
#
#     Df_spec.columns = ["Name","Verifies"]
#
#     # print(Df_LoopUp.loc["undefined","CBID"])
#     df_SpecCB = df_SpecCB.append(Df_spec)
#     #
#     # print(df_SpecCB)
#     # print(Df_spec)
#     #CB格式要求，前面加三个空格
#     df_SpecCB["Name"] = "   " + df_SpecCB["Name"]
#     df_SpecCB.to_excel(SpecCB, sheet_name="Export", index=False)
#     # print(Df_LoopUp)

def to_excel_auto_column_weight(df, writer, sheet_name):
    """DataFrame保存为excel并自动设置列宽"""
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    #  计算表头的字符宽度
    column_widths = (
        df.columns.to_series().apply(lambda x: len(x.encode('utf-8'))).values
    )
    #  计算每列的最大字符宽度
    max_widths = (
        df.astype(str).applymap(lambda x: len(x.encode('utf'))).agg(max).values
    )
    # 计算整体最大宽度
    widths = np.max([column_widths, max_widths], axis=0)
    # 设置列宽
    worksheet = writer.sheets[sheet_name]
    for i, width in enumerate(widths, 1):
        # openpyxl引擎设置字符宽度时会缩水0.5左右个字符，所以干脆+2使左右都空出一个字宽。
        worksheet.column_dimensions[get_column_letter(i)].width = width + 2

# def GenerateSpec_CB_Init(Df_spec, Df_LoopUp, SpecCB):
def GenerateSpec_CB_Init(Df_spec, SpecCB):
    # ColumnsList = ["ID", "Priority","Name","Description","Pre-Action","Post-Action","Test Steps.Action","Test Steps.Expected result","Test Steps.Critical","Test Parameters","Verifies","Status","Type"]
    ColumnsList = ["ID", "Parent", "Priority", "Name", "Description", "Pre-Action", "Post-Action",
                   "Test Steps.Action", "Test Steps.Expected result",
                   "Test Steps.Critical", "Test Parameters", "Verifies",
                   "Status", "Type", "_Original_TestCaseId", "_Test_Technique",
                   "_VerifiesNonCbRequirements", "_LastReviewDate", "_ScriptPath",
                   "_TestType", "_RegressionStrategy", "_FunctionGroup", "_Feature",
                   "Functional Safety Relevant", "Cyber Security Relevant"]
    df_SpecCB = pd.DataFrame(columns= ColumnsList)
    print(df_SpecCB)

    Df_spec.columns = ["Name","Verifies"]

    df_SpecCB["Name"] = "   " + Df_spec["Name"]
    df_SpecCB["Verifies"] = Df_spec["Verifies"].apply(lambda x: "[ISSUE:" + x + "]" if IsCBID(x) else "")
    df_SpecCB["_VerifiesNonCbRequirements"] = Df_spec["Verifies"].apply(lambda x: x if not IsCBID(x) else "")
    #
    print(df_SpecCB)
    df_SpecCB.to_excel(SpecCB, sheet_name="Export", index=False)
    # with pd.ExcelWriter(SpecCB) as writer:
    #     to_excel_auto_column_weight(df_SpecCB, writer, "Export")
    return df_SpecCB

    # print(Df_LoopUp)
def GenerateSpec_CB_Init_SWTD(Df_spec, SpecCB):
    # ColumnsList = ["ID", "Priority","Name","Description","Pre-Action","Post-Action","Test Steps.Action","Test Steps.Expected result","Test Steps.Critical","Test Parameters","Verifies","Status","Type"]
    ColumnsList = ["ID", "Parent", "Priority", "Name", "Description", "Pre-Action", "Post-Action",
                   "Test Steps.Action", "Test Steps.Expected result",
                   "Test Steps.Critical", "Test Parameters", "Verifies",
                   "Status", "Type", "_Original_TestCaseId", "_Test_Technique",
                   "_VerifiesNonCbRequirements", "_LastReviewDate", "_ScriptPath",
                   "_TestType", "_RegressionStrategy", "_FunctionGroup", "_Feature",
                   "Functional Safety Relevant", "Cyber Security Relevant"]
    df_SpecCB = pd.DataFrame(columns= ColumnsList)
    print(df_SpecCB)

    Df_spec.columns = ["Name","Verifies"]

    df_SpecCB["Name"] = "   " + Df_spec["Name"]
    df_SpecCB["Verifies"] = Df_spec["Verifies"].apply(lambda x: "[ISSUE:" + x + "]" if IsCBID(x) else "")
    df_SpecCB["_VerifiesNonCbRequirements"] = Df_spec["Verifies"].apply(lambda x: x if not IsCBID(x) else "")
    #
    print(df_SpecCB)
    df_SpecCB.to_excel(SpecCB, sheet_name="Export", index=False)
    # with pd.ExcelWriter(SpecCB) as writer:
    #     to_excel_auto_column_weight(df_SpecCB, writer, "Export")
    return df_SpecCB

def GenerateSpec_CB_Init_SWTD(Df_spec, SpecCB,Df_LoopUp):
    # ColumnsList = ["ID", "Priority","Name","Description","Pre-Action","Post-Action","Test Steps.Action","Test Steps.Expected result","Test Steps.Critical","Test Parameters","Verifies","Status","Type"]
    ColumnsList = ["ID", "Parent", "Priority", "Name", "Description", "Pre-Action", "Post-Action",
                   "Test Steps.Action", "Test Steps.Expected result",
                   "Test Steps.Critical", "Test Parameters", "Verifies",
                   "Status", "Type", "_Original_TestCaseId", "_Test_Technique",
                   "_VerifiesNonCbRequirements", "_LastReviewDate", "_ScriptPath",
                   "_TestType", "_RegressionStrategy", "_FunctionGroup", "_Feature",
                   "Functional Safety Relevant", "Cyber Security Relevant"]
    df_SpecCB = pd.DataFrame(columns=ColumnsList)
    print(df_SpecCB)

    Df_spec.columns = ["Name", "Verifies"]
    Df_spec['Verifies'] = Df_spec['Verifies'].apply(ReplaceCellValue, Df_LoopUp=Df_LoopUp)

    df_SpecCB["Name"] = "   " + Df_spec["Name"]
    df_SpecCB["Verifies"] = Df_spec["Verifies"].apply(lambda x: "[ISSUE:" + x + "]" if IsCBID_SWTD(x,Df_LoopUp) else "")
    df_SpecCB["_VerifiesNonCbRequirements"] = Df_spec["Verifies"].apply(lambda x: x if not IsCBID_SWTD(x,Df_LoopUp) else "")
    #
    print(df_SpecCB)
    df_SpecCB.to_excel(SpecCB, sheet_name="Export", index=False)
    # with pd.ExcelWriter(SpecCB) as writer:
    #     to_excel_auto_column_weight(df_SpecCB, writer, "Export")
    return df_SpecCB


def ReadSpecCB_FromCB(SpecCB_FromCB):
    Df_SpecCB = pd.read_excel(SpecCB_FromCB, "Export", dtype='str')
    # print(Df_SpecCB.head(10))
    Df_SpecCB[["ID","Parent","Name"]] = Df_SpecCB[["ID","Parent","Name"]] .fillna(method = 'ffill')
    # print(Df_SpecCB.head(10))

    Df_ID_Case = Df_SpecCB[["ID", "Parent", "Name"]].drop_duplicates(subset=['ID'])
    Df_ID_Case.drop(0, inplace=True)
    Df_ID_Case["Name"] = Df_ID_Case["Name"].str.strip()
    Df_ID_Case.set_index("Name",inplace = True,drop = False)

    # print(Df_ID_Case.head(10))
    return Df_SpecCB,Df_ID_Case

def GenerateSpec_CB_Modify(df_SpecCB_Generate,Df_ID_Case_FromCB,SpecCB_Modify):
    # pass
    #
    df_SpecCB_Generate["Parent"] = Df_ID_Case_FromCB.iloc[1,1]
    df_SpecCB_Generate["ID"] = df_SpecCB_Generate["Name"].apply(lambda x:Df_ID_Case_FromCB.loc[x.strip(),"ID"] if x.strip() in Df_ID_Case_FromCB.index else "")

    # print(df_SpecCB_Generate.head(10))

    print("$" *60)
    for caseName in Df_ID_Case_FromCB.index:
        if caseName not in df_SpecCB_Generate["Name"].str.strip().values:
            print(caseName)
            Df_ID_Case_FromCB.loc[caseName,"Status"] = "Obsolete"
            Df_ID_Case_FromCB.loc[caseName,"Name"] = "    " + caseName
            df_SpecCB_Generate = df_SpecCB_Generate.append(Df_ID_Case_FromCB.loc[caseName])
            # print(Df_ID_Case_FromCB.loc[caseName])
    # print(df_SpecCB_Generate)
    df_SpecCB_Generate.to_excel(SpecCB_Modify, sheet_name="Export", index=False)

if __name__ == '__main__':
    Spec = r"E:\Project_Test\Geely_Geea2_HX11\06. SRS HWTD&SWTD.xls"
    LoopUP = "..\DataSource/P05CBID.txt"
    SpecCB_Generate = r"E:\Project_Test\Geely_Geea2_HX11\06. SRS HWTD&SWTD_CodeBeamer.xlsx"
    SpecCB_Modify = "..\DataSource/CHT_SWV_GWM_P0102_2S_IMU_Test Result_CodeBeamer.xlsx"
    SpecCB_FromCB = "..\DataSource/84177 _GWM_P05_IMU_Test case.xlsx"
    Df_LoopUp = ReadLoopUp_SWTD(LoopUP)
    #
    Df_spec = ReadSpec_TableOfContent_SWTD(Spec)

    GenerateSpec_CB_Init_SWTD(Df_spec, SpecCB_Generate,Df_LoopUp)
    #
    # df_SpecCB_Generate = GenerateSpec_CB_Init(Df_spec, Df_LoopUp, SpecCB_Generate)
    # df_SpecCB_FromCB,Df_ID_Case_FromCB = ReadSpecCB_FromCB(SpecCB_FromCB)
    # GenerateSpec_CB_Modify(df_SpecCB_Generate, Df_ID_Case_FromCB, SpecCB_Modify)