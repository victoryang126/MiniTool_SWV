import pandas as pd
import numpy as np
import json

DIDConfig = "E:\GitHub\MiniTool\DataSource\EDR list for_GAC_A55_1S.xlsx"
SymFile = "E:\GitHub\MiniTool\DataSource\GAC_A55_P30_01.sym"
SheetName = "EDR List for GB"
OutPut = "C:\Python\MiniTool\DataSource\DIDObject.ts"


df = pd.read_excel(DIDConfig,SheetName,dtype = str)
df.fillna("undefined",inplace = True)

df = df.iloc[1:,1:]

column_List = ["NO.","Name in GB","Start Byte","Length","Parameter name in element list","Conversion Formula from NVM(A) to GB(N)"]
df = df[column_List]
df.set_index("NO.",inplace = True)
EDR_Dict = df.to_dict(orient="index")
# print(EDR_Dict)
sym_list = []
with open(SymFile, 'r', encoding='UTF-8') as f:
    while True:
        line = f.readline()
        # print(line)
        if line:
            sym_list.append(line)
        else:
            break
#
print(sym_list[0])
print(sym_list[1])
print(sym_list[32384])


# sym_data = [line.split(",") for line in sym_data]
# print(sym_data)
# print(df.info)
# print(df.describe)
# print(df.columns)
# df_Group = df.groupby("NO.", as_index=False)


# print(DID_Dict['204F']['DataLength'])
# print(DID_Dict)

# with open(OutPut, 'w', encoding='UTF-8') as f:
#     f.write("var G_DID_Object = ")
#     json.dump(DID_Dict, f,indent=4)
#     f.write(";\n")