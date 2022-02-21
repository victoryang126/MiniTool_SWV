import pandas as pd
import numpy as np
import json
import re
import math
import os

#

def GetDIDObjectFromSSDS(ExcelDir,SheetName,OutPut):

    df = pd.read_excel(ExcelDir, SheetName, dtype = str,header = 0)
    df.fillna("undefined",inplace = True)

    print(df.head(5))
    df = df[["Identifier","ParameterName","DataLength","Offset","BitLength","Scaling","CompareValue","Unit"]]

    df_Group = df.groupby("Identifier", as_index=False,sort = False)


    DID_Dict = dict(list(df_Group))
    # print(DID_Dict)
    for DID in DID_Dict:
        # 获取DataLength
        DataLength = DID_Dict[DID]['DataLength'].iloc[0]
        DID_Dict[DID].drop(["Identifier",'DataLength'],inplace = True,axis = 1)
        # DID_Dict[DID]['DataLength'] = DataLength
        # df_Parameter_Group = group.groupby("Parameter Name", as_index=True)
        # 获取Parameter Name的DataFrame
        DID_Dict[DID] = dict(list(DID_Dict[DID].groupby("ParameterName", as_index=False,sort = False)))
        # 对Parameter Name的DataFrame 进行处理
        for Parameter in DID_Dict[DID]:

            df_temp = DID_Dict[DID][Parameter]

            # df_temp['CompareValue'] = df_temp['CompareValue'].apply(lambda x:x if x== 'undefined' else x.split("=")[1])
            # print(df_temp['CompareValue'])
            df_unit = df_temp[['CompareValue', 'Unit']]
            dict_unit = dict(zip(df_unit['CompareValue'],df_unit['Unit']))
            dict_ValueMap = dict(zip(df_unit['Unit'], df_unit['CompareValue']))
            DID_Dict[DID][Parameter].drop_duplicates("ParameterName",inplace = True) # 删除重复元素 默认留下了第一个
            DID_Dict[DID][Parameter].drop(["ParameterName","CompareValue"], inplace=True, axis=1)
            DID_Dict[DID][Parameter] = dict(zip(DID_Dict[DID][Parameter].columns,DID_Dict[DID][Parameter].iloc[0]))
            if DID_Dict[DID][Parameter]['Unit'] != 'undefined':
                    DID_Dict[DID][Parameter]['Unit'] = dict_unit
                    DID_Dict[DID][Parameter]['ValueMap'] = dict_ValueMap
        DID_Dict[DID]['DataLength'] = DataLength


    # print(DID_Dict)

    with open(OutPut, 'w', encoding='UTF-8') as f:

        f.write("var GBB_DID_Dict = \n")
        json.dump(DID_Dict, f,indent=4)
        f.write(";\n")
    return DID_Dict



def GetMsgObjectFromSSDS(ExcelDir,SheetName,SheetName2,OutPut):

    df = pd.read_excel(ExcelDir, SheetName, dtype = str,header = 0)
    df.fillna("undefined",inplace = True)


    df = df[["Frame","Signal","PeriodicTime","Computation"]]
    # df["Signal"]
    df_Msg_Group = df.groupby("Frame", as_index=True)
    dict_Msg = {}
    for name,group in df_Msg_Group:
        # print(group[["Signal","Computation"]].to_dict(orient = "dict"))
        # print(dict(zip(group["Signal"],group["Computation"])))
        dict_Msg[name] = dict(zip(group["Signal"],group["Computation"]))
        dict_Msg[name]["PeriodicTime"] = group["PeriodicTime"].values[0]
    # print(df.head(5))
    # df.set_index("Frame",inplace= True)

    # dict_Msg = df.to_dict(orient = "index")
    print(dict_Msg)





    df_Map = pd.read_excel(ExcelDir, SheetName2, dtype = str,header = 0)
    df_Map.fillna("undefined",inplace = True)
    df_Map
    # print(df_Map.head(5))
    df_Map = df_Map[["Computation","CompareValue","Unit"]]
    # df_Map.iloc[0, 2] = {"a":1}
    # df_Map.iloc[0, 2] = [3,3,5]
    # print(df_Map.iloc[0,2])
    df_Parameter_Group = df_Map.groupby("Computation", as_index=True)
    dict_Paramter = {}
    for name,group in df_Parameter_Group:
        # dict_Paramter[name] = group.to_dict()
        # print(group[["CompareValue","Unit"]].to_dict())
        # print(dict(zip(group["CompareValue"],group["Unit"])))
        dict_Paramter[name] = {}
        dict_Paramter[name]["Unit"] = dict(zip(group["Unit"],group["CompareValue"]))
        dict_Paramter[name]['ValueMap'] = dict(zip(group["CompareValue"], group["Unit"]))
    print(dict_Paramter)


    for frame in dict_Msg:
        for signal in dict_Msg[frame]:
            if dict_Msg[frame][signal] in dict_Paramter:
                # print(1)
                dict_Msg[frame][signal] = dict_Paramter[dict_Msg[frame][signal]]
    print(dict_Msg)

    with open(OutPut, 'a', encoding='UTF-8') as f:

        f.write("var GBB_Msg_Dict = \n")
        json.dump(dict_Msg, f,indent=4)
        f.write(";\n")



##function: changed the HexStr to Bin Str
def HexStr2BinStr(HexStr):
    pattern = re.compile("0x| ",re.I)
    HexStr = pattern.sub("",HexStr.upper())
    # print(HexStr)
    Hex_Dict = {
        "0":"0000", "1":"0001", "2":"0010","3":"0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111",
    }
    Bin_Str = ""
    for TempStr in HexStr:
        Bin_Str += Hex_Dict[TempStr]
    return Bin_Str
##function: changed the Int_Str to HexStr
def IntStr2HexStr(Int_Str,ByteSize):
    Str_Hex = str(hex(int(Int_Str)))
    # print(Str_Hex)
    Str_Hex = Str_Hex.replace("0x","").upper()
    while len(Str_Hex) < ByteSize*2:
        Str_Hex = "0" + Str_Hex
    if len(Str_Hex) > ByteSize*2:
        raise Exception("ByteSize is less in function Str2Hex")
    # print(Str_Hex)
    return Str_Hex

def BinStr2DecStr(BinSstr):
    return str(int(BinSstr, 2))

def BinStr2HexStr(BinSstr,ByteSize):
    return IntStr2HexStr(BinStr2DecStr(BinSstr),ByteSize)


def GetDataRecordDetail(ResponseValue, DID_Dict,DID):

    # // 1.获取回复以后，先把空格和0x去掉 var
    pattern = re.compile("0x| ", re.I)
    L_DataRecord = re.sub(pattern, "",ResponseValue)[6:];

    # // 2.获取bin值
    # print(L_DataRecord)
    L_DataRecord_Bin = HexStr2BinStr(L_DataRecord)

    # // 获取对应DID的数据

    L_Return_Dict = {}

    if(DID in DID_Dict):
        DID_Object = DID_Dict[DID]
    else:
        # print("Not in ")
        raise Exception(DID + " is not in the dictionary")
        return
    for Parameter in DID_Object:


        if Parameter == "DataLength" or  Parameter == "DataRecord":
            continue
        L_Return_Dict[Parameter] = {}
        L_Offset = int(DID_Object[Parameter]["Offset"], 10)
        # print("L L_Offset %d" %L_Offset)
        L_BitLength = int(DID_Object[Parameter]["BitLength"], 10)
        # print("L BitLength %d" % L_BitLength)
        L_Scaling = DID_Object[Parameter]["Scaling"]
        L_Unit_Dict = DID_Object[Parameter]["Unit"]
        L_BinValue = L_DataRecord_Bin[L_Offset:L_Offset + L_BitLength]
        L_DecValue = int(L_BinValue, 2)
        L_HexValue = IntStr2HexStr(str(L_DecValue),math.ceil(L_BitLength/8))

        x = L_DecValue
        L_PhyValue = 'undefined';
        L_PhyValue = eval(L_Scaling)

        L_Return_Dict[Parameter]["Phy"] = L_PhyValue
        L_Return_Dict[Parameter]["Raw"] = L_HexValue
    # print(L_Return_Dict)
    return L_Return_Dict


def GetDataRecordDetail2(ResponseValue, DID_Dict,DID):

    # // 1.获取回复以后，先把空格和0x去掉 var
    pattern = re.compile("0x| ", re.I)
    L_DataRecord = re.sub(pattern, "",ResponseValue)[6:];

    # // 2.获取bin值
    # print(L_DataRecord)
    L_DataRecord_Bin = HexStr2BinStr(L_DataRecord)

    # // 获取对应DID的数据

    L_Return_Dict = {}

    if(DID in DID_Dict):
        DID_Object = DID_Dict[DID]
    else:
        # print("Not in ")
        raise Exception(DID + " is not in the dictionary")
        return
    for Parameter in DID_Object:


        if Parameter == "DataLength" or  Parameter == "DataRecord":
            continue
        L_Offset = int(DID_Object[Parameter]["Offset"], 10)
        # print("L L_Offset %d" %L_Offset)
        L_BitLength = int(DID_Object[Parameter]["BitLength"], 10)
        # print("L BitLength %d" % L_BitLength)
        L_Scaling = DID_Object[Parameter]["Scaling"]
        L_Unit_Dict = DID_Object[Parameter]["Unit"]
        L_BinValue = L_DataRecord_Bin[L_Offset:L_Offset + L_BitLength]
        # try:
        L_DecValue = int(L_BinValue, 2)
        # except Exception as err:
        #     # print(Parameter)
        #     # print(L_BinValue)
        #     # print(L_Offset)
        #     continue
        L_ByteLength = math.ceil(L_BitLength/8)
        L_HexValue = IntStr2HexStr(str(L_DecValue),L_ByteLength)
        if L_ByteLength == 1:
            L_Return_Dict[Parameter] = {}
            L_Return_Dict[Parameter]["Raw"] = L_HexValue
            x = int(L_HexValue, 16)
            try:
                L_PhyValue = 'undefined'
                L_PhyValue = eval(L_Scaling)
                L_Return_Dict[Parameter]["Phy"] = L_PhyValue
                L_Return_Dict[Parameter]["Scaling"] = L_Scaling
            except Exception as err:
                print(Parameter)
                L_Return_Dict[Parameter]["Phy"] = "undefined"
                L_Return_Dict[Parameter]["Scaling"] = L_Scaling


        else:
            for i in range(L_ByteLength):
                L_TempKey = Parameter + "_byte(" + str(i) + ")"
                L_Return_Dict[L_TempKey] = {}
                L_TempHexValue = L_HexValue[i*2:i*2 + 2]
                L_Return_Dict[L_TempKey]["Raw"] = L_TempHexValue

                x = int(L_TempHexValue, 16)
                try:
                    L_PhyValue = 'undefined'
                    L_PhyValue = eval(L_Scaling)
                    L_Return_Dict[L_TempKey]["Phy"] = L_PhyValue
                    L_Return_Dict[L_TempKey]["Scaling"] = L_Scaling
                except Exception as err:
                    print(Parameter)
                    L_Return_Dict[L_TempKey]["Phy"] = 'undefined'
                    L_Return_Dict[L_TempKey]["Scaling"] = L_Scaling
    return L_Return_Dict

def GenerateDataRecordExcel(DataRecordDict,DataRecordExcel,DID):
    df = pd.DataFrame.from_dict(DataRecordDict)
    df = df.T

    df.to_excel(DataRecordExcel, sheet_name=DID, index=True)

def GetInfoFromTxt(txt):
    DataRecordExcel = os.path.splitext(txt)[0]
    DID = DataRecordExcel[-4:]
    DataRecordExcel = DataRecordExcel + ".xlsx"
    # print(DataRecordExcel)

    with open(txt, "r", encoding='utf-8') as TmpF:
        ResponseValue = TmpF.read().strip("\n")
    # print(ResponseValue)
    return DataRecordExcel,DID,ResponseValue,

def GetDID_Dict(DID_Dict_Path):

    with open(DID_Dict_Path, 'r', encoding='UTF-8') as f:
        DID_Dict = json.load(f)
    # print(DID_Dict)
    return DID_Dict
# '''
if __name__ == '__main__':
    # DID = "204F"
    # DataRecordDict = {'Airbag warning lamp': {'Phy': 1, 'Raw': '0x01'}, 'Display Text "Pedestrian Protection System - Service Required" Requested': {'Phy': 1, 'Raw': '0x01'}, 'Display Text "SRS Service Urgent" Requested': {'Phy': 1, 'Raw': '0x01'}}
    # DataRecordExcel = "DIDTest.xlsx";
    ExcelDir = r"E:\Project_Test\Geely_Geea2_HX11\Deploy\Crash_Logic.xlsx"
    SheetName = "Sheet6"
    # SheetName1 = "DCS_Msg"
    # SheetName2 = "DCS_Msg_Map"
    OutPut = "../DataSource/DIDObject2.ts"
    # GenerateDataRecordExcel(DataRecordDict,DataRecordExcel,DID)
    DID_Dict_Path = "DataSource/DIDObject.ts"
    # txt = "C:\Python\GitHub\Minitool\DataSource\FrontLevel_1_FA13.txt";
    # DataRecordExcel = os.path.split(txt)[1].split(".")[0]  # 获取文件的名字，不包含路径

    DID_Dict = GetDIDObjectFromSSDS(ExcelDir, SheetName, OutPut)
    # DID_Dict = GetDID_Dict(DID_Dict_Path)
    # DataRecordExcel,DID, ResponseValue = GetInfoFromTxt(txt)
    # print("GetDataRecordDetail2")
    # DataRecordDict = GetDataRecordDetail2(ResponseValue, DID_Dict, DID)
    # print("GenerateDataRecordExcel")
    # GenerateDataRecordExcel(DataRecordDict, DataRecordExcel, DID)
    #

    # GetMsgObjectFromSSDS(ExcelDir, SheetName1, SheetName2, OutPut)

