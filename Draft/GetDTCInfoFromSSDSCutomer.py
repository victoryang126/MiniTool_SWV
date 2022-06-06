import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import numpy as np


def GenerateDTCiniFile(SSDSPath, SheetName, iniFile):
    df_DTC = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # DTC Identifier   Description 11,13

    # ColumnsList = ["Status", "Identifier", "confirmedDTCLimit", "agedDTCLimit", "DTCEventPriority", "WarningIndicator",
    #                "TestPeriod", "Maxvalue", "Stepup", "Stepdown"]
    ColumnsList = [ "Identifier", "confirmedDTCLimit", "agedDTCLimit", "DTCEventPriority", "WarningIndicator",
                   "TestPeriod", "Maxvalue", "Stepup", "Stepdown"]
    # print(ColumnsList)
    print(df_DTC.columns)
    df_DTC = df_DTC[ColumnsList]
    df_DTC = df_DTC[df_DTC["Identifier"].notnull()]
    # df_DTC = df_DTC[df_DTC["Status"] == 'Approved']

    # df_DTC.drop("Status", axis=1, inplace=True)

    df_Duplicated = df_DTC[df_DTC["Identifier"].duplicated() == True]
    print(df_Duplicated['Identifier'])
    df_DTC.drop_duplicates(subset=['Identifier'], keep='last', inplace=True)
    df_DTC.set_index("Identifier", inplace=True)
    DTC_Dict = df_DTC.to_dict(orient="index")

    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        for DTC in DTC_Dict:
            tempstr = "[" + DTC + "]\n"
            ini_f.write(tempstr)
            for DTC_Attrib in DTC_Dict[DTC]:
                tempstr = DTC_Attrib + " = \"" + str(DTC_Dict[DTC][DTC_Attrib]) + "\"\n"
                ini_f.write(tempstr)
    print(DTC_Dict)


def GenerateSnapotIni(SSDSPath, SheetName, iniFile):
    df_Snapshot = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # DTC Identifier   Description 11,13

    # ColumnsList = ["Status", "Identifier", "SnapshotDataIdentification", "Sortorder"]
    ColumnsList = ["Identifier", "SnapshotDataIdentification", "Sortorder"]

    df_Snapshot = df_Snapshot[ColumnsList]

    # df_Snapshot = df_Snapshot[df_Snapshot["Status"] == 'Approved']

    # df_Snapshot.drop("Status", axis=1, inplace=True)

    print(df_Snapshot.columns)
    df_Snapshot["SnapshotDataIdentification"] = df_Snapshot["SnapshotDataIdentification"].apply(lambda x:x.split(" ")[-1])
    print(df_Snapshot["SnapshotDataIdentification"])
    df_Group = df_Snapshot.groupby(by="Identifier", as_index=False, sort=False)

    snapShot_Dict = {}
    for name, group in df_Group:
        # print(name)
        # snapShot_Dict[]
        group.sort_values(by=['Sortorder'], inplace=True)
        # print(group)
        Data = group["SnapshotDataIdentification"].values
        # print(group["SnapshotDataIdentification"].values)
        snapShot_Dict[name] = Data

    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        for DTC in snapShot_Dict:
            tempstr = "[" + DTC + "]\n"
            ini_f.write(tempstr)

            tempstr = "SnapshotDataIdentification =" + ",".join(snapShot_Dict[DTC])  + "\n";
            ini_f.write(tempstr)

def GenerateSnapotDict(SSDSPath, SheetName, DictFile):
    df_Snapshot = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    # DTC Identifier   Description 11,13

    # ColumnsList = ["Status", "Identifier", "SnapshotDataIdentification", "Sortorder"]
    ColumnsList = ["Identifier", "SnapshotDataIdentification", "Sortorder"]

    df_Snapshot = df_Snapshot[ColumnsList]

    # df_Snapshot = df_Snapshot[df_Snapshot["Status"] == 'Approved']

    # df_Snapshot.drop("Status", axis=1, inplace=True)

    print(df_Snapshot.columns)
    df_Snapshot["SnapshotDataIdentification"] = df_Snapshot["SnapshotDataIdentification"].apply(lambda x:x.split(" ")[-1])
    print(df_Snapshot["SnapshotDataIdentification"])
    df_Group = df_Snapshot.groupby(by="Identifier", as_index=False, sort=False)

    snapShot_Dict = {}
    for name, group in df_Group:
        # print(name)
        # snapShot_Dict[]
        group.sort_values(by=['Sortorder'], inplace=True)
        # print(group)
        Data = group["SnapshotDataIdentification"].values
        # print(group["SnapshotDataIdentification"].values)
        snapShot_Dict[name] = Data

    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        for DTC in snapShot_Dict:
            tempstr = "[" + DTC + "]\n"
            ini_f.write(tempstr)

            tempstr = "SnapshotDataIdentification =" + ",".join(snapShot_Dict[DTC])  + "\n";
            ini_f.write(tempstr)

def GenerateSnapotDIDIni(SSDSPath, SheetName, iniFile):
    df_Snapshot = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)

    ColumnsList = ["Errorname", "VeoneerCode"]


def GenerateVeoneerCodeIni(SSDSPath, SheetName, iniFile):
    df_VeoneerCode = pd.read_excel(SSDSPath, SheetName, dtype='str', header=3)
    df_VeoneerCode = df_VeoneerCode.iloc[0:,[0,4,5,6]]
    df_VeoneerCode = df_VeoneerCode.fillna("")

    ColumnsList = ["Errorname", "VeoneerCode","DTC_HexValue","FailureType"]
    df_VeoneerCode.columns = ColumnsList;

    df_VeoneerCode["VeoneerCode"] = df_VeoneerCode["VeoneerCode"].apply(lambda x:(x[0:2] + "0" + x[2:]))

    df_VeoneerCode["FailureType"] = df_VeoneerCode["FailureType"].apply(lambda x: "0" + x if len(x) == 1 else x)

    df_VeoneerCode["DTCRecord"] = df_VeoneerCode["DTC_HexValue"] + df_VeoneerCode["FailureType"];
    # print(df_VeoneerCode)
    # for DTC in df_VeoneerCode["VeoneerCode"]:
    #     print(DTC)
    with open(iniFile, "w", encoding='UTF-8') as ini_f:
        for i in df_VeoneerCode.index:
            tempstr = "[" + df_VeoneerCode.iloc[i,1] + "]\n"
            ini_f.write(tempstr)

            tempstr = "Errorname =" +  df_VeoneerCode.iloc[i,0] + "\n";
            ini_f.write(tempstr)
            tempstr = "DTCCode =" + df_VeoneerCode.iloc[i, 4] + "\n";
            ini_f.write(tempstr)

if __name__ == '__main__':

    SSDSPath = "C:\Project\Geely_GEEA2_HX11\SW_Release\P31_03\BuildGenerationReport\error_definition_Geely_GEEA2_HX11_P31_03.xlsm"
    # E:\GitHub\MiniTool\DataSource\SSDS_Customer.xlsx
    iniFile = "C:\Project\Geely_GEEA2_HX11\SW_Release\P31_03\BuildGenerationReport\VeoneerCode.ini"
    # SnapshotiniFile = "..\DataSource\SnapShot.ini"
    # GenerateDTCiniFile(SSDSPath, "DTC", iniFile)

    # GenerateSnapotIni(SSDSPath, "Snapshot", SnapshotiniFile)

    # GenerateSnapotDIDIni(SSDSPath, "Snapshot DID", SnapshotiniFile)
    GenerateVeoneerCodeIni(SSDSPath, "Errors", iniFile)
