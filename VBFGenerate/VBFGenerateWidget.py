import os
import sys
from VBFGenerate.Ui_VBFGenerate import Ui_VBFGenerate
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings





def VBFGenerate(VBFConvert_Path,VbfSign_Path,SourceFile_List,TargetOutput,VBB_Template,VerifyBlock_Addr):
    """
    根据客户的工具VBFConvert 和VbfSign 将s37 文件转换成VBF
    :param VBFConvert_Path:
    :param VbfSign_Path:
    :param SourceFile_List:
    :param TargetOutput:
    :param VBB_Template:
    :param VerifyBlock_Addr:
    :return:
    """
    VBF_SignFile_List = []
    with open(VBB_Template, "r", encoding='UTF-8') as VBB_f:
        VBB_List = VBB_f.readlines()
    BatFile = TargetOutput + "/"  + "VBFGenerate.bat"
    with open(BatFile, "w", encoding='UTF-8') as CmdFile:
        CmdFile.write("echo ########### Generate VBF ################\n")
    for SourceFile in SourceFile_List:
        FileName = os.path.split(SourceFile)[1].split(".")[0]
        VBFFile = TargetOutput+ "/" +   FileName + ".vbf"
        VBFLog = TargetOutput + "/" +  FileName + ".log"
        VBF_SignFile = TargetOutput + "/" +  FileName + "_Signed.vbf"
        VBF_SignFile_List.append(VBF_SignFile)
        VBB_Path = TargetOutput+ "/" +   FileName + ".VBB"
        # print(VBB_Template)

        # VBB_List = VBB_f.readlines()
        VBB_List[1] = "SourceFile=" + SourceFile + "\n"
        VBB_List[2] = "TargetFile=" + VBFFile + "\n"

        with open(VBB_Path, "w", encoding='UTF-8') as VBB_f:
             VBB_f.writelines(VBB_List)
        # print(FileName,VBFFile,VBFLog,VBF_SignFile,BatFile)
        Command_Line = VBFConvert_Path + " -BATCHFILE=\"" + VBB_Path + "-logfile=\"" +VBFLog + "\"\n" + VbfSign_Path +  " " + VBFFile + " " + VBF_SignFile + " " + VerifyBlock_Addr + "\n"
        with open(BatFile, "a", encoding='UTF-8') as CmdFile:
            CmdFile.write(Command_Line)
    os.system(BatFile)
    return VBF_SignFile_List


class VBFGenerateWidget(QWidget):
    CurrentPath = os.getcwd()

    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_VBFGenerate()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # *****************定义 GenS37相关属性****************************************
        self.VBFConvert = ""
        self.VbfSign = ""
        self.VBB_Template = ""
        self.SourceFile_List = []
        self.TargetOutput = ""
        self.VerifyBlock_Addr = ""
        self.VerifyBlock_Address_Config = [];

        # *****************设置OtToll LineEdit默认值****************************************
        if os.path.exists('./ini/VBFGenerateWidget.ini'):

            self.Config = QSettings('./ini/VBFGenerateWidget.ini', QSettings.IniFormat)
            self.LoadConfig()

    # 定义错误提示框
    def WarningMessage(self, str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self, DigTitle, StrInfo)

    def DoneMessage(self, str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    def LoadConfig(self):
        self.VBFConvert = self.Config.value("CONFIG/VBFConvert")
        self.VbfSign = self.Config.value("CONFIG/VbfSign")
        self.VBB_Template = self.Config.value("CONFIG/VBB_Template")
        self.VerifyBlock_Address_Config = self.Config.value("CONFIG/VerifyBlock_Address_Config")

        self.__ui.LE_VBFConvert.setText(self.VBFConvert)
        self.__ui.LE_VbfSign.setText(self.VbfSign)
        self.__ui.LE_VBB_Template.setText(self.VBB_Template)
        self.__ui.CB_LogicalBlock.clear()
        self.__ui.CB_LogicalBlock.addItems(self.VerifyBlock_Address_Config)


    def SaveConfig(self):
        self.Config = QSettings('./ini/VBFGenerateWidget.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8
        self.Config.setValue("CONFIG/VBFConvert",self.VBFConvert)
        self.Config.setValue("CONFIG/VbfSign", self.VbfSign)
        self.Config.setValue("CONFIG/VBB_Template", self.VBB_Template)
        self.VerifyBlock_Address_Config = []
        for count in range(self.__ui.CB_LogicalBlock.count()):
            self.VerifyBlock_Address_Config.append(self.__ui.CB_LogicalBlock.itemText(count))
        self.Config.setValue("CONFIG/VerifyBlock_Address_Config", self.VerifyBlock_Address_Config)


    # 检擦 路径是否包含空格
    def CheckPathContainSpace(self, Path):
        if " " in Path:
            self.WarningMessage(Path + " have space, please remove it")

    # 1 BT_VBFConvert
    @pyqtSlot()
    def on_BT_VBFConvert_clicked(self):
        self.__ui.LE_VBFConvert.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an VBFConvert.exe file ",
                                                         self.CurrentPath,
                                                         "VBFConvert(*.exe)")
        self.__ui.LE_VBFConvert.setText(FileName)
        self.VBFConvert = self.__ui.LE_VBFConvert.text()
        path = self.VBFConvert
        self.CheckPathContainSpace(path)
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 2 BT_VbfSign
    @pyqtSlot()
    def on_BT_VbfSign_clicked(self):
        self.__ui.LE_VbfSign.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an VbfSign.exe file ",
                                                         self.CurrentPath,
                                                         "VbfSign(*.exe)")
        self.__ui.LE_VbfSign.setText(FileName)
        self.VbfSign= self.__ui.LE_VbfSign.text()
        path = self.VbfSign
        self.CheckPathContainSpace(path)
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 3 BT_VBB_Template
    @pyqtSlot()
    def on_BT_VBB_Template_clicked(self):
        self.__ui.LE_VBB_Template.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an VBB file ",
                                                         self.CurrentPath,
                                                         "VBB(*.VBB)")
        self.__ui.LE_VBB_Template.setText(FileName)
        self.VBB_Template = self.__ui.LE_VBB_Template.text()

        path = self.VBB_Template
        self.CheckPathContainSpace(path)
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)




    # 4. LE_VerifyBlock_Addr
    @pyqtSlot(str)
    def on_LE_VerifyBlock_Addr_textChanged(self, str):
        self.VerifyBlock_Addr = self.__ui.LE_VerifyBlock_Addr.text()
        if "x" in self.VerifyBlock_Addr or "X" in self.VerifyBlock_Addr:
            self.WarningMessage("verification_block_address should be hexadecimal without 0x!!!!!")

    @pyqtSlot(str)
    def on_CB_LogicalBlock_currentTextChanged(self,str):
        AddressTemp = self.__ui.CB_LogicalBlock.currentText().split(":")
        if len(AddressTemp) == 1:
            AddressTemp = 'undefined'
        else:
            AddressTemp = AddressTemp[1].strip()

        self.__ui.LE_VerifyBlock_Addr.setText(AddressTemp)


    @pyqtSlot()
    def on_BT_Verify_Address_Config_clicked(self):
        self.__ui.LE_VerifyBlock_Addr_Config.clear()
        CurrentPath = os.getcwd()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an ini config file to modiofy the verification block address",
                                                         self.CurrentPath,
                                                         "ini(*.ini)")
        self.__ui.LE_VerifyBlock_Addr_Config.setText(FileName)
        if FileName:
            self.Config = QSettings(FileName, QSettings.IniFormat)
            self.VerifyBlock_Address_Config = self.Config.value("CONFIG/VerifyBlock_Address_Config")
            self.__ui.CB_LogicalBlock.clear()
            self.__ui.CB_LogicalBlock.addItems(self.VerifyBlock_Address_Config)



    # 5 BT_SourceFile_List
    @pyqtSlot()
    def on_BT_SourceFile_List_clicked(self):
        self.__ui.TextB_SourceFile_List.clear()
        self.SourceFile_List = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Select a s37 files",
                                                           self.CurrentPath,
                                                           "s37(*.s37)")
        # print(FileNames)
        for file in FileNames:
            self.__ui.TextB_SourceFile_List.append(file)
        self.SourceFile_List += FileNames
        try:
            path = self.SourceFile_List[0]
            self.CheckPathContainSpace(path)
            self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)
        except Exception as err:
            self.WarningMessage("please select s37 files")

    # 6. BT_TargetOutput
    @pyqtSlot()
    def on_BT_TargetOutput_clicked(self):

        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder to VBV signed files",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_TargetOutput.setText(FolderName)
        self.TargetOutput= self.__ui.LE_TargetOutput.text()
        path = self.TargetOutput
        self.CheckPathContainSpace(path)
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 7. 设置BT_VBFGenerate
    @pyqtSlot()
    def on_BT_GenerateVBF_clicked(self):
        try:
            args = {
            "VBFConvert_Path":self.VBFConvert,
                "VbfSign_Path":self.VbfSign,
                "SourceFile_List":self.SourceFile_List,
                "TargetOutput":self.TargetOutput,
                "VBB_Template":self.VBB_Template,
                "VerifyBlock_Addr":self.VerifyBlock_Addr
            }
            VBF_Signed_Files = VBFGenerate(**args)
            # (GenS37_Ascent,GenS37_OEM,GenS37_SWVersion,GenS37_Json,GenS37_Files,GenS37_Output)
            # 获取没有生成S37的文件
            NotOK_VBF_Signed_Files = [VBF_Signed_File for VBF_Signed_File in VBF_Signed_Files if not os.path.exists(VBF_Signed_File)]
            if len(NotOK_VBF_Signed_Files):
                self.WarningMessage(str(NotOK_VBF_Signed_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate VBF_Signed files successfully")
                self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = VBFGenerateWidget()
    baseWidget.show()
    sys.exit(app.exec_())