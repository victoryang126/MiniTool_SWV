import pandas as pd
import json
import os
from Other_Tool import ComFun


def DictGenerate(ExcelDir,Sheet,Key,Values,TsName):
    df = pd.read_excel(ExcelDir, Sheet,dtype = str)
    df.fillna("undefined", inplace=True)
    dfDict = df[Values]
    dfDict.set_index(df[Key],inplace = True)
    # print(dfDict)
    Keylist = list(dfDict.index)
    # print(Keylist)

    if len(Values) > 1:
        ObjectDict = dfDict.to_dict(orient="index")
    elif len(Values) == 1:
        ValuesList = dfDict[Values[0]]
        ObjectDict = dict(zip(Keylist,ValuesList))


    # TempStr = "var SupportDict = " + str(ObjectDict) + ";"
    TempStr = "var SupportDict = "
    TempStr2 = "var SupportList = " + str(Keylist) + ";"
    # ComFun.InilizeFile(TsName)
    # ComFun.AddObject2Ts(TsName, TempStr)
    # ComFun.AddObject2Ts(TsName, TempStr2)
    with open(TsName, 'w', encoding='UTF-8') as f:
        f.write(TempStr2)
        f.write("\n")
        f.write(TempStr)
        json.dump(ObjectDict, f, indent=4)
        f.write(";\n")
if __name__ == "__main__":
    ExcelDir = "/Users/monster/PycharmProjects/GitHub/MiniTool/DataSource/RegressionImprove.xlsx"
    Sheet = "SID22"
    Key = "DID"
    # Values = ["Age","Class","Name"]
    Values = ["Type",'Data']
    TsName = "/Users/monster/PycharmProjects/GitHub/MiniTool/DataSource/test.ts"
    DictGenerate(ExcelDir, Sheet, Key, Values, TsName)
