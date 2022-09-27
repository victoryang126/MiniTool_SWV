import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings

from Ascent_Generate_S37 import  GenS37
from Ascent_Generate_S37.Ui_GenS37 import  Ui_GenS37
from CommonFunction import AEFGen





class GenS37Widget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_GenS37()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面


        # *****************定义 GenS37相关属性****************************************
        self.GenS37_Ascent = "C:\Program Files (x86)\Veoneer\Ascent\AscentBatch.exe"
        self.GenS37_OEM = "SC2.1A"
        self.GenS37_SWVersion = "V4.0"
        self.GenS37_FileType = "PRN"
        self.GenS37_SWPart = "VehFixedCal"
        self.GenS37_Files = []
        self.GenS37_Files_InTextB = []
        self.GenS37_Output = self.CurrentPath
        self.GenS37_Alias = ""
        self.GenS37_PBCfg = ""
        self.GenS37_Release = ""
        self.GenS37_BaseAEF = ""
        self.GenS37_BaseAEF_Check = False
        self.GenS37_AEFOutput = ""
        self.GenS37_ElfList = ["\\IPFixedCal.elf","\\VehFixedCal.elf","\\AlgoVar1FixedCal.elf","\\AlgoVar2FixedCal.elf","\\AlgoVar3FixedCal.elf"]
        self.GenS37_SWPart_List = ["VehFixedCal","IPFixedCal","AlgoVar1FixedCal","AlgoVar2FixedCal","AlgoVar3FixedCal"]
        self.GenS37_Json = {
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
        }
        self.GenS37_AliasPath = "C:\\Users\\Public\\Veoneer\\Ascent\\Projects\\" + self.GenS37_OEM + "\\Common\\" + self.GenS37_SWVersion + "\\OemInputs\\"




        # *****************设置GenS37 LineEdit默认值****************************************

        # *****************设置OtToll LineEdit默认值****************************************
        if os.path.exists('./ini/GenS37Widget.ini'):
            self.Config = QSettings('./ini/GenS37Widget.ini', QSettings.IniFormat)
            self.LoadConfig()
        else:
            self.__ui.LE_GenS37_Ascent.setText(self.GenS37_Ascent)
            self.__ui.LE_GenS37_OEM.setText(self.GenS37_OEM)
            self.__ui.LE_GenS37_SWVersion.setText(self.GenS37_SWVersion)
            self.__ui.LE_GenS37_Alias.setText(self.GenS37_AliasPath + "FixedCal_AliasMaster.xlsx")
            self.__ui.LE_GenS37_PBCfg.setText(self.GenS37_AliasPath + "FltMonr_PBCfg.h")
            self.__ui.LE_GenS37_Output.setText(self.GenS37_Output)


    # 定义错误提示框
    def WarningMessage(self,str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self,DigTitle,StrInfo)
    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    # 根据INI 文件导入配置信息
    def LoadConfig(self):
        self.GenS37_Ascent = self.Config.value("CONFIG/GenS37_Ascent")
        self.GenS37_OEM = self.Config.value("CONFIG/GenS37_OEM")
        self.GenS37_SWVersion = self.Config.value("CONFIG/GenS37_SWVersion")
        self.GenS37_Alias = self.Config.value("CONFIG/GenS37_Alias")
        self.GenS37_PBCfg = self.Config.value("CONFIG/GenS37_PBCfg")
        self.GenS37_Release = self.Config.value("CONFIG/GenS37_Release")

        self.__ui.LE_GenS37_Ascent.setText(self.GenS37_Ascent)
        self.__ui.LE_GenS37_OEM.setText(self.GenS37_OEM)
        self.__ui.LE_GenS37_SWVersion.setText(self.GenS37_SWVersion)
        self.__ui.LE_GenS37_Alias.setText(self.GenS37_Alias)
        self.__ui.LE_GenS37_PBCfg.setText(self.GenS37_PBCfg)
        self.__ui.LE_GenS37_Release.setText(self.GenS37_Release)
        self.AddElf()

    # 保存配置信息到INI文件
    def SaveConfig(self):
        self.Config = QSettings('./ini/GenS37Widget.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8
        self.Config.setValue("CONFIG/GenS37_Ascent",self.GenS37_Ascent)
        self.Config.setValue("CONFIG/GenS37_OEM", self.GenS37_OEM)
        self.Config.setValue("CONFIG/GenS37_SWVersion", self.GenS37_SWVersion)
        self.Config.setValue("CONFIG/GenS37_Alias", self.GenS37_Alias)
        self.Config.setValue("CONFIG/GenS37_PBCfg", self.GenS37_PBCfg)
        self.Config.setValue("CONFIG/GenS37_Release", self.GenS37_Release)

    # 根据elf文件夹里面的文件，添加elf类型选择的列表
    def AddElf(self):
        #处理Releaase Folder 添加elf名字到CB_GenS37_SWPart 里面去
        TempList = []
        for MainFolder,SubFolder,File_List in os.walk(self.GenS37_Release):
            for File in File_List:
                if File.endswith(".elf"):
                    TempList.append(File.split(".")[0])
        for Temp in TempList:
            if Temp not in self.GenS37_SWPart_List:
                self.GenS37_SWPart_List.append(Temp)
                self.__ui.CB_GenS37_SWPart.addItem(Temp)

    # 检擦 路径是否包含空格
    def CheckPathContainSpace(self, Path):
        if " " in Path:
            self.WarningMessage(Path + " have space, please remove it")

    # 基于baseAEF 生成新的AEF文件，默认在aef文件下路径下新建AEFFolder
    def GenerateAEF(self):
        GenS37_New_AEFFiles = []
        try:
            self.GenS37_AEFOutput = os.path.split(self.GenS37_Files_InTextB[0])[0] + "/AEFFolder"
        except Exception:
            self.WarningMessage("Please select PRN or AEF files which contains parameter you want to modify")
        try:
            args = {"BaseAEFPath":self.GenS37_BaseAEF,"AEFFiles": self.GenS37_Files_InTextB,"AEFOutPut":self.GenS37_AEFOutput}
            GenS37_New_AEFFiles = AEFGen.GenerateAEF(**args)
            # (GenerateAEF(BaseAEFPath,AEFFiles,AEFOutPut)
            # self.DoneMessage("Generate AEF files successfully")
        except Exception as err:
            self.WarningMessage(str(err))
        return GenS37_New_AEFFiles

    #1 设置BT_GenS37_Ascent
    @pyqtSlot()
    def on_BT_GenS37_Ascent_clicked(self):
        self.__ui.LE_GenS37_Ascent.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an AscentBatch.exe file ",
                                                         self.CurrentPath,
                                                         "Reg_Excel(*.exe)")
        self.__ui.LE_GenS37_Ascent.setText(FileName)
        self.GenS37_Ascent = self.__ui.LE_GenS37_Ascent.text()
        path = self.GenS37_Ascent
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #1设置LE_GenS37_OEM
    @pyqtSlot(str)
    def on_LE_GenS37_OEM_textChanged(self,str):
        self.GenS37_OEM = self.__ui.LE_GenS37_OEM.text()
        self.GenS37_AliasPath = "C:\\Users\\Public\\Veoneer\\Ascent\\Projects\\" + self.GenS37_OEM + "\\Common\\" + self.GenS37_SWVersion + "\\OemInputs\\"
        self.__ui.LE_GenS37_Alias.setText(self.GenS37_AliasPath + "FixedCal_AliasMaster.xlsx")
        self.__ui.LE_GenS37_PBCfg.setText(self.GenS37_AliasPath + "FltMonr_PBCfg.h")
       # print(self.GenS37_OEM)

    #2设置GenS37_SWVersion
    @pyqtSlot(str)
    def on_LE_GenS37_SWVersion_textChanged(self,str):
        self.GenS37_SWVersion = self.__ui.LE_GenS37_SWVersion.text()
        self.GenS37_AliasPath = "C:\\Users\\Public\\Veoneer\\Ascent\\Projects\\" + self.GenS37_OEM + "\\Common\\" + self.GenS37_SWVersion + "\\OemInputs\\"
        self.__ui.LE_GenS37_Alias.setText(self.GenS37_AliasPath + "FixedCal_AliasMaster.xlsx")
        self.__ui.LE_GenS37_PBCfg.setText(self.GenS37_AliasPath + "FltMonr_PBCfg.h")
        # print(self.GenS37_SWVersion)

    #1 .定义BT_GenS37_Alias
    @pyqtSlot()
    def on_BT_GenS37_Alias_clicked(self):
        self.__ui.LE_GenS37_Alias.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select FixedCal_AliasMaster.xlsx ",
                                                         self.CurrentPath,
                                                         "Alias_Excel(*.xlsx *.xlsm)")
        self.__ui.LE_GenS37_Alias.setText(FileName)
        # self.GenS37_Alias = self.__ui.LE_GenS37_Alias.text()
        # self.GenS37_Json["ApplicationAlias"] = self.GenS37_Alias
        self.CheckPathContainSpace(FileName)
        path = FileName
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 1 .定义GenS37_Alias
    @pyqtSlot()
    def on_BT_GenS37_PBCfg_clicked(self):

        self.__ui.LE_GenS37_PBCfg.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select FltMonr_PBCfg.h file ",
                                                         self.CurrentPath,
                                                         "Reg_Excel(*.h)")
        self.__ui.LE_GenS37_PBCfg.setText(FileName)
        self.CheckPathContainSpace(FileName)
        path = FileName
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    @pyqtSlot()
    def on_BT_GenS37_Release_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the elf files release folder",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_GenS37_Release.setText(FolderName)
        self.GenS37_Release = self.__ui.LE_GenS37_Release.text()
        self.CheckPathContainSpace(self.GenS37_Release)
        self.AddElf()
        # TempList = []
        # #处理Releaase Folder 添加elf名字到CB_GenS37_SWPart 里面去
        # for MainFolder,SubFolder,File_List in os.walk(self.GenS37_Release):
        #     for File in File_List:
        #         if File.endswith(".elf"):
        #             TempList.append(File.split(".")[0])
        # for Temp in TempList:
        #     if Temp not in self.GenS37_SWPart_List:
        #         self.GenS37_SWPart_List.append(Temp)
        #         self.__ui.CB_GenS37_SWPart.addItem(Temp)

        path = self.GenS37_Release
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)
        # self.GenS37_Json["ElfFiles"] = [self.GenS37_Release + elf for elf in self.GenS37_ElfList]
        # self.GenS37_Json["PatchingFiles"][0]["ElfFile"] = self.GenS37_Release + "\\" + self.GenS37_SWPart + ".elf"

    # 1 .定义GenS37_BaseAEF
    @pyqtSlot()
    def on_BT_GenS37_BaseAEF_clicked(self):

        self.__ui.LE_GenS37_BaseAEF.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the base AEF",
                                                         self.CurrentPath,
                                                         "AEF file(*.aef)")
        self.__ui.LE_GenS37_BaseAEF.setText(FileName)
        self.GenS37_BaseAEF = self.__ui.LE_GenS37_BaseAEF.text()

        path = self.GenS37_BaseAEF
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 设置CheckB_GenS37_BaseAEF
    def on_CheckB_GenS37_BaseAEF_stateChanged(self):
        self.GenS37_BaseAEF_Check = self.__ui.CheckB_GenS37_BaseAEF.isChecked()
        if self.GenS37_BaseAEF_Check:
            # if not os.path.exists(self.GenS37_BaseAEF):
            self.WarningMessage("Please select the base AEF files,I will generate AEF firstly, then generate S37 after you clicked the GenerateS37 button")
        # print("Check box " + str(self.GenS37_BaseAEF_Check))

    # 设置CB_GenS37_FileType
    @pyqtSlot(str)
    def on_CB_GenS37_FileType_currentTextChanged(self,str):
        self.GenS37_FileType = self.__ui.CB_GenS37_FileType.currentText()
        # print(self.GenS37_FileType)

    # 设置CB_GenS37_SWPart
    @pyqtSlot(str)
    def on_CB_GenS37_SWPart_currentTextChanged(self,str):
        self.GenS37_SWPart = self.__ui.CB_GenS37_SWPart.currentText()
        # self.GenS37_Json["PatchingFiles"][0]["ElfFile"] = self.GenS37_Release + "\\" + self.GenS37_SWPart + ".elf"
        # print(self.GenS37_SWPart)


    #3设置BT_GenS37__Files
    @pyqtSlot()
    def on_BT_GenS37_Files_clicked(self):
        self.__ui.TextB_GenS37_Files.clear()
        self.GenS37_Files = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Select a PRN of AEF files",
                                                           self.CurrentPath,
                                                           "prn or aef(*.prn *.aef)")
        # print(FileNames)
        for file in FileNames:
            self.__ui.TextB_GenS37_Files.append(file)
        # print(self.__ui.TextB_GenS37_Files.text())
        self.GenS37_Files += FileNames
        self.GenS37_Files_InTextB = self.GenS37_Files[:]
        #当时为啥加了一个变量 GenS37_Files_InTextB 和 GenS37_Files 有啥去吧

        try:
            path = self.GenS37_Files[0]
            self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)
        except Exception as err:
            self.WarningMessage("please select AEF or PRN files")

    # 4. 设置 BT_GenS37_Output
    @pyqtSlot()
    def on_BT_GenS37_Output_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder to save S37",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_GenS37_Output.setText(FolderName)
        self.GenS37_Output = self.__ui.LE_GenS37_Output.text()
        self.CheckPathContainSpace(self.GenS37_Output)

        path = self.GenS37_Output
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #5. 设置BT_GenS37_GenrateS37
    @pyqtSlot()
    def on_BT_GenS37_GenerateS37_clicked(self):
        self.GenS37_Alias = self.__ui.LE_GenS37_Alias.text()
        self.GenS37_Json["ApplicationAlias"] = self.GenS37_Alias
        self.GenS37_PBCfg = self.__ui.LE_GenS37_PBCfg.text()
        self.GenS37_Json["FltMonr_PBCFg"] = self.GenS37_PBCfg
        # self.GenS37_Json["ElfFiles"] = [self.GenS37_Release + elf for elf in self.GenS37_ElfList]
        self.GenS37_Json["ElfFiles"] = [self.GenS37_Release + "/" + self.GenS37_SWPart + ".elf"]
        self.GenS37_Json["PatchingFiles"][0]["ElfFile"] = self.GenS37_Release + "/" + self.GenS37_SWPart + ".elf"
        # 如果生成AEF文件的复选框被选中，则先生成AEF文件，并把新AEF文件赋值给self.GenS37_Files
        if self.GenS37_BaseAEF_Check:
            self.GenS37_Files = self.GenerateAEF()
        try:
            args = {"GenS37_Ascent":self.GenS37_Ascent, "GenS37_OEM":self.GenS37_OEM, "GenS37_SWVersion":self.GenS37_SWVersion,
                    "GenS37_Json":self.GenS37_Json, "GenS37_Files":self.GenS37_Files,
                   "GenS37_Output":self.GenS37_Output}
            S37_Files = GenS37.GenS37(**args)
            # (GenS37_Ascent,GenS37_OEM,GenS37_SWVersion,GenS37_Json,GenS37_Files,GenS37_Output)
            #获取没有生成S37的文件
            NotOK_S37Files = [S37_File for S37_File in S37_Files if not os.path.exists(S37_File)]
            if len(NotOK_S37Files):
                # pass
                self.WarningMessage(str(NotOK_S37Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate S37 successfully")
                self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = GenS37Widget()

    baseWidget.show()
    sys.exit(app.exec_())
