import os



def Sym2Ts(SymPath,TsName):

    with open(SymPath, 'r', encoding='UTF-8-sig') as f:
        SymList = f.readlines()

    PBCTList = [TempStr.split(",")[0:3] for TempStr in SymList]
    PBCTKeys = [TempList.pop(1) for TempList in PBCTList]
    # print(PBCTList[0])
    # print(PBCTKeys[0])
    PBCTDict = dict(zip(PBCTKeys,PBCTList))
    with open(TsName, 'w', encoding='UTF-8') as f:
        f.write("var PBCT = " + str(PBCTDict) + ";")

if __name__ == "__main__":
    Sympath = r"E:\Python\Dailywork\A.sym"
    FileName = "PBCT.ts"