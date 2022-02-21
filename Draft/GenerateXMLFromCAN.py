
import re
import pandas as pd
import os
#1. get CAN content and search the testcase

CANPath = r"C:\Project\Geely_GEEA2_HX11\CANoe_Configuration\P21_02\TestModules\E2E\E2E.can"
CANPath = r"C:\Project\Geely_GEEA2_HX11\CANoe_Configuration\P21_02\TestModules\GRI Basetech Security\GRI_Basetech_Security.can"
CANPath = r"C:\Project\Geely_GEEA2_HX11\CANoe_Configuration\P21_02\TestModules\UDS_Data_Test\UDS_Data_Test.can"
# CANPath = r"C:\Project\Geely_GEEA2_HX11\CANoe_Configuration\P21_02\TestModules\SWDL\SWDL.can"
ExcelDir = r"E:\Project_Test\E4_SRS HWTD&SWTD report_SWV.xlsx"
def get_TCID_Fromfile(CANPath):
    regex_TCID = re.compile(r'^testcase[ \t]+(TESTCASE_[0-9]{2,8})')
    filename = os.path.split(CANPath)[1].split(".")[0]  # 获取文件的名字，不包含路径
    # print(filename)
    TC_ID_List = [];
    with open(CANPath, "r", encoding='ansi') as f:
        content = f.readlines()
        for line in content:
            a = re.match(regex_TCID,line)
            if a:
                TC_ID_List.append(a.groups()[0].split("_")[1])
    # print(TC_ID_List)
    return  TC_ID_List,filename


def getCaseDescription(ExcelDir):
    df = pd.read_excel(ExcelDir, "sheet", dtype=str, header=0)
    # print(df)
    df_TC_ID= df[["TC ID","TestCaseName"]]
    dict_Description = dict(zip(df_TC_ID["TC ID"].values,df_TC_ID["TestCaseName"].values))

    return dict_Description


def GenerateXML(TC_ID_List,filename,dict_Description):
    vxtname = filename + ".vxt"
    with open(vxtname, "w", encoding='utf-8') as f:
        f.write('''<?xml version="1.0" encoding="iso-8859-1"?>\n''')
        f.write('''<testmodule title= "'''+ filename + '''" version="1.0"><description> ''' + filename + '''</description>\n''')
        for TC_ID in TC_ID_List:
            testsecripttion = dict_Description[TC_ID] if TC_ID in dict_Description  else "undefined"
            testsecripttion.replace("/"," ")
            testsecripttion.replace("'", " ")
            testsecripttion.replace("-", " ")
            testsecripttion = testsecripttion.strip()
            tempstr = '''<capltestcase name="TESTCASE_''' + TC_ID + '''" title="TESTCASE_''' + TC_ID + " " + testsecripttion + '''"/>\n'''
            f.write(tempstr)
        tempstr = '''</testmodule>'''
        f.write(tempstr)
if __name__ == '__main__':
    # get_TCID_Fromfile(CANPath)
    # getCaseDescription(ExcelDir)
    GenerateXML(*get_TCID_Fromfile(CANPath), getCaseDescription(ExcelDir))