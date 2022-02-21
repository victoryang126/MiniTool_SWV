import os
import json


def GenS37(GenS37_Ascent,GenS37_OEM,GenS37_SWVersion,GenS37_Json,GenS37_Files,GenS37_Output):
    """
    依据Ascent的BatchMode 去批量生成S37文件

    :param GenS37_Ascent: Ascent的路径
    :param GenS37_OEM:    OEM的名称
    :param GenS37_SWVersion: 软件版本
    :param GenS37_Json: Json配置文件
        GenS37_Json = {
            "PlatformAlias": "",
            "ApplicationAlias": "",
            "FltMonr_PBCFg": "",
            "ElfFiles": [
                "",
                "",
                "",
                "",
                "",
            ],
            "PatchingFiles": [{
                "ElfFile": "",
                "PatchFiles": [""]
            }]
    :param GenS37_Files: PRN或者AEF的文件列表
    :param GenS37_Output: 生成以后S37文件的保存路径
    :return: S37_Files:  S37文件的list
    """

    S37_Files = []
    FileTemp = GenS37_Files[0]
    CmdDir = os.path.split(FileTemp)[0]
    CmdFilePath = CmdDir + "/GenerateS37.bat"  #在PRN路径下面建立cmd命令
    # print(CmdFilePath)
    CmdFile = open(CmdFilePath, 'w')
    CmdFile.write("cd /d " + GenS37_Ascent.rstrip("AscentBatch.exe"))
    # CmdFile.write('\n')
    for FileTemp in GenS37_Files:
        GenS37_Json["PatchingFiles"][0]["PatchFiles"] = [FileTemp]  #PatchFiles
        FileName_W_Path = os.path.splitext(FileTemp)[0] #获取包含路径的文件名
        S37Name = os.path.split(FileTemp)[1].split(".")[0]  # 获取文件的名字，不包含路径
        JsonFile = FileName_W_Path + ".json"
        f = open(JsonFile, 'w')
        json.dump(GenS37_Json,f,indent = 4)
        f.close()
        # 往bat写入command line命令
        # Command_Line = self.GenS37_Ascent + ' -OEM ' + self.GenS37_OEM + ' -FT GenerateS37 -SV ' + self.GenS37_SWVersion + ' -IN  ' + Txt_CWD + " -OUT " + self.GenS37_Output + " -PRE " + NamePara
        # file.write('\n')
        Command_Line = "AscentBatch.exe" + ' -OEM ' + GenS37_OEM + ' -FT GenerateS37FromElf -SV ' + GenS37_SWVersion + ' -IN  ' + JsonFile + " -OUT " + GenS37_Output + "/" + S37Name + ".s37"
        CmdFile.write('\n')
        # print(Command_Line)
        CmdFile.write(Command_Line)
        S37_Files.append(GenS37_Output + "/" + S37Name + ".s37")
    CmdFile.close()
    os.system(CmdFilePath)
    return S37_Files