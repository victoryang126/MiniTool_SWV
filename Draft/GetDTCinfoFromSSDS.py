import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import numpy as np
import json


def GenerateDTCiniFile(SSDSPath, SheetName, iniFile):
    df_DTC = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # DTC Identifier   Description 11,13
    #1.  Excel 需要提前定义好对应的列名，位于第四行
    ColumnsList = [ "Identifier", "Description","confirmedDTCLimit", "agedDTCLimit", "WL", "PED",
                   "Priority","Cycle", "UnconfirmedDTCLimit", "StepUp", "StepDown"]
    #2. 获取 对应列的dataFrame,删除 Identifier 为 空的行
    print(df_DTC.columns)
    df_DTC = df_DTC[ColumnsList]
    df_DTC = df_DTC[df_DTC["Identifier"].notnull()]

    df_DTC["confirmedDTCLimit"] = df_DTC["confirmedDTCLimit"].astype("int")
    df_DTC["agedDTCLimit"] = df_DTC["agedDTCLimit"].astype("int")
    df_DTC["Priority"] = df_DTC["Priority"].astype("int")
    # df_DTC["Cycle"] = df_DTC["Cycle"].astype("int")
    df_DTC["UnconfirmedDTCLimit"] = df_DTC["UnconfirmedDTCLimit"].astype("int")
    df_DTC["StepUp"] = df_DTC["StepUp"].astype("int")
    df_DTC["StepDown"] = df_DTC["StepDown"].astype("int")

    df_Duplicated = df_DTC[df_DTC["Identifier"].duplicated() == True]
    print(df_Duplicated['Identifier'])
    df_DTC.drop_duplicates(subset=['Identifier'], keep='last', inplace=True)
    df_DTC.set_index("Identifier", inplace=True)
    df_DTC.fillna('undefined', inplace=True)

    DTC_Dict = df_DTC.to_dict(orient="index")

    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        for DTC in DTC_Dict:
            tempstr = "[" + DTC + "]\n"
            ini_f.write(tempstr)
            for DTC_Attrib in DTC_Dict[DTC]:
                tempstr = DTC_Attrib + " = \"" + str(DTC_Dict[DTC][DTC_Attrib]) + "\"\n"
                ini_f.write(tempstr)
    print(DTC_Dict)



def FilterPED(CellValue):
    if "Pedestrian" in CellValue:
        return True
    else:
        return False

def GenerateDTCDictFromSSDS(SSDSPath, SheetName, OutPutFile):
    df_DTC = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # DTC Identifier   Description 11,13

    #1.  Excel 需要提前定义好对应的列名，位于第四行
    ColumnsList = [ "Identifier", "confirmedDTCLimit", "agedDTCLimit", "WL", "PED",
                   "Priority","Cycle", "UnconfirmedDTCLimit", "StepUp", "StepDown"]


    #2. 获取 对应列的dataFrame,删除 Identifier 为 空的行
    print(df_DTC.columns)
    df_DTC = df_DTC[ColumnsList] #
    df_DTC = df_DTC[df_DTC["Identifier"].notnull()]
    df_DTC["PED"] = df_DTC["PED"].apply(lambda x: "PED" if FilterPED(x) else "undefined")
    df_DTC["confirmedDTCLimit"] = df_DTC["confirmedDTCLimit"].astype("int")
    df_DTC["agedDTCLimit"] =    df_DTC["agedDTCLimit"].astype("int")
    df_DTC["Priority"] = df_DTC["Priority"].astype("int")
    # df_DTC["Cycle"] = df_DTC["Cycle"].astype("int")
    df_DTC["UnconfirmedDTCLimit"] = df_DTC["UnconfirmedDTCLimit"].astype("int")
    df_DTC["StepUp"] = df_DTC["StepUp"].astype("int")
    df_DTC["StepDown"] = df_DTC["StepDown"].astype("int")

    df_Duplicated = df_DTC[df_DTC["Identifier"].duplicated() == True]
    print(df_Duplicated['Identifier'])
    df_DTC.drop_duplicates(subset=['Identifier'], keep='last', inplace=True)
    df_DTC.set_index("Identifier", inplace=True)
    df_DTC.fillna('undefined',inplace= True)
    DTC_Dict = df_DTC.to_dict(orient="index")

    with open(OutPutFile, "w", encoding='UTF-8') as ini_f:
        ini_f.write("var G_DTC_Dict = \n")
        json.dump(DTC_Dict, ini_f, indent=4)
        ini_f.write(";\n")

    print(DTC_Dict)



def getSnapshotType(x):
    if x[0:2] == "20":
        if x[2:] == "00" or x[2:] == "01" :
            return "Snapshot20"
        else:
            return "Snapshot20_Addi"
    else:
        if x[2:] == "00" or x[2:] == "01" :
            return "Snapshot21"
        else:
            return "Snapshot21_Addi"


def SortOutSnapShot20(x):

    if x[0:2] == "20":
        return True
    else:
        False

def GenerateSnapshot(SSDSPath, SheetName,SheetName2,iniFile):
    df_Snapshot = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # # DTC Identifier   Description 11,13
    ColumnsList = [ "Identifier", "SnapshotDataIdentification", "Sortorder"]
    #
    df_Snapshot = df_Snapshot[ColumnsList]
    #提取SnapshotDataIdentification 的DID 类别
    df_Snapshot["SnapshotDataIdentification"] = df_Snapshot["SnapshotDataIdentification"].apply(lambda x:x.split(" ")[-1])
    # print(df_Snapshot["SnapshotDataIdentification"])
    # print(df_Snapshot)
    df_Snapshot.sort_values(by=['Sortorder'], inplace=True)
    df_Snapshot = df_Snapshot[[ "Identifier", "SnapshotDataIdentification"]]
    # print(df_Snapshot)
    # df_new = df_Snapshot.pivot_table(index=['Identifier'],values = "SnapshotDataIdentification",aggfunc=lambda x: ','.join(x))
    # df_new.reset_index()
    # print(df_new)


    df_Snapshot_DID = pd.read_excel(SSDSPath, SheetName2, dtype='str', header=3)
    # ColumnsList = ["SnapshotDataIdentification", "DID", "Size"]
    ColumnsList = ["SnapshotDataIdentification", "DID"]
    df_Snapshot_DID = df_Snapshot_DID[ColumnsList]
    df_Snapshot_DID.drop_duplicates(inplace= True,keep = "first")  #移除 SnapshotDataIdentification 和DID Size都重复的行
    # 生成依据SnapshotDataIdentification 的Pivot_Table,然后对DID进行统计
    df_Snapshot_DID = df_Snapshot_DID.pivot_table(index=['SnapshotDataIdentification'], aggfunc=lambda x: ','.join(x))

    df_Snapshot_DID.reset_index()
    print(df_Snapshot_DID)

    # 依据SnapshotDataIdentification 合并数据，得到每个DTC相关的DID
    df_Snapshot = pd.merge(df_Snapshot,df_Snapshot_DID,on = "SnapshotDataIdentification",how = "left")
    # df_Snapshot["SnapshotDataIdentification"] = df_Snapshot["SnapshotDataIdentification"].apply(lambda x:"Snapshot20" if SortOutSnapShot20(x) else "Snapshot21")
    # print(df_Snapshot)
    df_Snapshot["SnapshotDataIdentification"] = df_Snapshot["SnapshotDataIdentification"].apply(getSnapshotType)
    df_Snapshot = df_Snapshot.pivot_table(index=['Identifier'],columns=["SnapshotDataIdentification"],aggfunc=lambda x: ','.join(x))
    # print(df_Snapshot.index)
    # df_new.reset_index()
    # df_new.rename_axis("",axis="columns",inplace= True
    #删除Columns的二级index
    # df_Snapshot.set_axis(["Snapshot20","Snapshot21"],axis='columns',inplace=True) #
    # print([x[1] for x in df_Snapshot.columns.values])
    print(df_Snapshot.columns.values)
    df_Snapshot.set_axis([x[1] for x in df_Snapshot.columns.values], axis='columns', inplace=True)  #
    # print(df_Snapshot)
    df_Snapshot.fillna("undefined",inplace= True)
    Snapshot_Dict = df_Snapshot.to_dict(orient="index")
    print(Snapshot_Dict)

    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        ini_f.write("var G_SnapshotDID_Dict = \n")
        json.dump(Snapshot_Dict, ini_f,indent = 4)
        ini_f.write(";\n")


if __name__ == '__main__':
    SSDSPath = "E:\Project_Test\Geely_Geea2_HX11\SRS Supplementary Restraint System (VDS) 8889420300  G (2021-12-17) Rev06.xlsx"
    # SSDSPath = "..\DataSource\SSDS_Customer.xlsx"
    # E:\GitHub\MiniTool\DataSource\SSDS_Customer.xlsx
    iniFile = "..\DataSource\DTCList.ini"
    SnapshotiniFile = "..\Data\SnapShot.ts"
    SnapshotDID_File = "..\Data\SnapShotDID.ts"
    # GenerateDTCiniFile(SSDSPath, "DTC", iniFile)
    SheetName = "DTC"
    OutPutFile = r"C:\Project\Geely_GEEA2_HX11\ARiA_Configuration\P30_01\Scripts\AA\AA_Geely_GEEA2_HX11_DTC_SSDS.ts"
    # GenerateSnapotDIDDict(SSDSPath, "Snapshot DID", SnapshotDID_File)
    # GenerateDTCiniFile(SSDSPath,SheetName,iniFile)
    # GenerateSnapotIni(SSDSPath, "Snapshot", SnapshotiniFile)
    # GenerateSnapotDict(SSDSPath, "Snapshot", SnapshotiniFile)
    # GenerateDTCDictFromSSDS(SSDSPath, SheetName, OutPutFile)
    # GenerateSnapotDIDIni(SSDSPath, "Snapshot DID", SnapshotiniFile)
    GenerateSnapshot(SSDSPath, "Snapshot", "Snapshot DID",SnapshotDID_File)
