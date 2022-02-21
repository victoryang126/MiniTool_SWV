import os
import re






def find_file():
    path = os.path.abspath('.')
    dirs = os.listdir(path)                    # 获取指定路径下的文件
    prnlist = []
    for i in dirs:
        if os.path.splitext(i)[1] == ".prn":
            prnlist.append(os.path.join(path,i))
    return prnlist

# 仅仅只获取其中的Parameter
def GetAEFFiles(AEFFile):
    with open(AEFFile, "r", encoding='UTF-8') as TmpF:
        Content = TmpF.readlines()
        # Content = TmpF.read()
    # print(Content)
    StartIndex = Content.index("BEGIN_PARAM\n")
    EndIndex = Content.index("END_PARAM\n")
    Content = Content[StartIndex+1:EndIndex]
    # print(Content)
    PRNName = S37Name = os.path.split(AEFFile)[1].split(".")[0]  # 获取文件的名字，不包含路径
    return Content,PRNName

def GetBaseAEFContent(AEFPath):
    with open(AEFPath, "r") as TmpF:
        Content = TmpF.readlines()
    return Content

def CreateAEF(BaseAEFContent, AEFOutPut, AEFContent, AEFName):
    # print("*****"+ AEFName)
    AEFTemp = AEFContent[:]
    # print("----")
    # print(AEFTemp)
    # print("----")
    for Parameter in AEFContent:
        # print("(((((("+Parameter)
        ParameterName = Parameter.split(";")[0]
        for i in range(len(BaseAEFContent)):
            if ParameterName in BaseAEFContent[i]:
                BaseAEFContent[i] = Parameter
                # print(Parameter)
                # print(Parameter in AEFTemp)
                AEFTemp.remove(Parameter)
                break;
    for Parameter in AEFTemp:
        BaseAEFContent.insert(-2,Parameter)
    AEFFile = AEFOutPut + "/" + AEFName + ".aef"
    with open(AEFFile, "w") as TempFile:
        TempFile.writelines(BaseAEFContent)
    return AEFFile


# AEFContent = GetBaseAEF(AEFPath)

def GenerateAEF(BaseAEFPath,AEFFiles,AEFOutPut):
    New_AEFFiles =[]
    # 新建output文件夹
    if not os.path.exists(AEFOutPut):
        os.mkdir(AEFOutPut)
    # print(os.path.exists(AEFOutPut))
    BaseAEFContent = GetBaseAEFContent(BaseAEFPath)
    for AEF in AEFFiles:
        PRNContent, PRNName = GetAEFFiles(AEF)
        AEFTemp = BaseAEFContent[:]
        New_AEFFiles.append(CreateAEF(AEFTemp, AEFOutPut, PRNContent, PRNName))
    return New_AEFFiles
if __name__ == "__main__":
    # prnlist = find_file()
    prnlist = [r"E:\Python\LoopDeployPRNS\LOP_DEP_DecisionMask_LHD.prn"]
    AEFPath = r'E:\Python\LoopDeployPRNS\Deploy.aef'
    AEFOutPut = r"E:\Python\LoopDeployPRNS\AEFFolder"
    GenerateAEF(AEFPath,prnlist ,AEFOutPut)
    # prnpath = r"E:\Python\LoopDeployPRNS\LOP_DEP_AlgoInhibitionALISL.prn"
    # GetAEFFiles(prnpath)






