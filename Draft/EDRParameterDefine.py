import os
import re
keywordpath = r'C:\Project\GWM_P0102_2S\ARIA_Configuration\P11\keyword.txt'
sympath  = r"C:\Project\GWM_P0102_2S\ARIA_Configuration\P11\SymbolFile.sym"
ParameterFile = r"C:\Project\GWM_P0102_2S\ARIA_Configuration\P11\test.ts"

def AddParameter2Ts(ParameterFile, Strline):
	with open(ParameterFile, 'a', encoding='UTF-8') as f:
		f.writelines(Strline)
		f.write("\n")


def GetTempleteScript(ScriptTemplate):
    with open(ScriptTemplate, "r",encoding='UTF-8') as TmpF:
        Templete = TmpF.readlines()
    return Templete


def CheckArray(KeyStr):
    Reg = re.compile(r'\w+(?=\[)')
    Reg2 = re.compile(r'\d+(?=\])')
    data = re.findall(Reg,KeyStr)
    num = re.findall(Reg2,KeyStr)
    if(len(data) == 0):
        return False,KeyStr,0
    else:
        return True,data[0],int(num[0])

keyword = GetTempleteScript(keywordpath)
keyword = [line.strip() for line in keyword]
# print(keyword)

sym = GetTempleteScript(sympath)
sym = [line.split(",") for line in sym]
for line in  sym:
    line.pop() #删除数组最后一个位 0，sym file文件固定格式多余的数据
# print(sym)



for TmpKey in keyword:
    ArrayCheck,TmpKey,ArrLength = CheckArray(TmpKey)
    TmpStr = "var " + TmpKey + " = new Array();"
    AddParameter2Ts(ParameterFile, TmpStr)
    # if ArrayCheck
    i = 1
    for TmpPa in sym:
        if TmpKey in TmpPa[1]: # 改字段再参数名字里面
            TmpStr = TmpKey + "[" + str(i) + "] = "  + str(TmpPa) + ";"
            AddParameter2Ts(ParameterFile, TmpStr)
            i += 1
