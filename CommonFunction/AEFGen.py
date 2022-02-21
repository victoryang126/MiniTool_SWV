import os






def find_file():
    """
    查找路径下面的 prn文件
    :return: prnlist
    """
    path = os.path.abspath('.')
    dirs = os.listdir(path)                    # 获取指定路径下的文件
    prnlist = []
    for i in dirs:
        if os.path.splitext(i)[1] == ".prn":
            prnlist.append(os.path.join(path,i))
    return prnlist


def GetAEFFiles(AEFFile):
    """
    从AEF文件中获取参数
    :param AEFFile:
    :return: Content AEF 里面的paramter 列表，每行
             PRNName AEF的名字
    """
    with open(AEFFile, "r", encoding='UTF-8') as TmpF:
        Content = TmpF.readlines()
        # Content = TmpF.read()
    # print(Content)
    StartIndex = Content.index("BEGIN_PARAM\n")
    EndIndex = Content.index("END_PARAM\n")
    Content = Content[StartIndex+1:EndIndex]
    # print(Content)
    PRNName = os.path.split(AEFFile)[1].split(".")[0]  # 获取文件的名字，不包含路径
    return Content,PRNName

def GetBaseAEFContent(AEFPath):
    """
    获取AEF文件里面的内容
    :param AEFPath:
    :return: Content AEF 里面的内容 列表，每行
    """
    with open(AEFPath, "r") as TmpF:
        Content = TmpF.readlines()
    return Content

def CreateAEF(BaseAEFContent, AEFOutPut, AEFContent, AEFName):
    """
    在标定release的可以点爆的AEF 文件基础上 根据测试内容修改特定的参数
    :param BaseAEFContent: Crash AEF文件的路径，即标定依据我们的AEF request release的aef文件，可以通过导入波形点爆特定loop
    :param AEFOutPut: 生成AEF文件的路径
    :param AEFContent: 包含特定参数的AEF文件
    :param AEFName:   AEF文件的名字
    :return:AEFFile   生成以后的AEF文件
    """

    # print("*****"+ AEFName)
    AEFTemp = AEFContent[:]
    # print("----")
    # print(AEFTemp)
    # print("----")
    for Parameter in AEFContent:
        ParameterName = Parameter.split(";")[0]
        for i in range(len(BaseAEFContent)):
            if ParameterName in BaseAEFContent[i]:
                BaseAEFContent[i] = Parameter
                AEFTemp.remove(Parameter)
                break;
    for Parameter in AEFTemp:
        BaseAEFContent.insert(-2,Parameter)
    AEFFile = AEFOutPut + "/" + AEFName + ".aef"
    with open(AEFFile, "w") as TempFile:
        TempFile.writelines(BaseAEFContent)
    return AEFFile



def GenerateAEF(BaseAEFPath,AEFFiles,AEFOutPut):
    """
    在标定release的可以点爆的AEF 文件基础上 根据测试内容修改特定的参数

    :param BaseAEFPath: Crash AEF文件的路径，即标定依据我们的AEF request release的aef文件，可以通过导入波形点爆特定loop
    :param AEFFiles:    AEF文件列表，仅包含测试需要的参数的AEF
    :param AEFOutPut:   生成AEF文件的路径
    :return:New_AEFFiles 新的AEF文件
    """
    New_AEFFiles =[]
    # 新建output文件夹
    if not os.path.exists(AEFOutPut):
        os.mkdir(AEFOutPut)
    # 获取BaseAEF的内容
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






