import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import win32com
from win32com.client import Dispatch
from CB_Spec_Tool import ConvertSpect2CBSpec as CB_Tool
from CB_Spec_Tool.Ui_CB_Spec_Tool import Ui_CB_Spec_Tool
from CB_Spec_Tool.UploadSpec2CodeBeamer import *
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QDialog,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings
from PyQt5.QtGui import  QIcon
from PyQt5.QtGui import  QIcon



class CB_Spec_Tool_Widget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()

    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_CB_Spec_Tool()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面


        # *****************定义 GenS37相关属性****************************************


        self.LookUp = ""
        self.Test_Spec_List = []
        self.CB_Spec_ExportPath = ""
        self.CB_Spec_Generate = ""
        self.Release = ""
        self.CB_Spec_FromCB = ""
        self.FinalCBSpec = ""
        self.CaseTrackerID = ""
        self.CB_Spec_Folder_ID = ""

        if os.path.exists('./ini/CB_Spec_Tool_Widget.ini'):
            self.Config = QSettings('./ini/CB_Spec_Tool_Widget.ini', QSettings.IniFormat)
            self.LoadConfig()
        else:
            self.__ui.LE_LookUp.setText(self.LookUp)
            if self.Test_Spec_List:
                for file in self.Test_Spec_List:
                    self.__ui.textB_Test_Spec.append(file)
            self.__ui.LE_CB_Spec.setText(self.CB_Spec_ExportPath)
            self.__ui.LE_CB_Spec_Generate.setText(self.CB_Spec_Generate)
            self.__ui.LE_CB_Spec_FromCB.setText(self.CB_Spec_FromCB)

        # *****************设置GenS37 LineEdit默认值****************************************

    def LoadConfig(self):
        self.LookUp = self.Config.value("CONFIG/LookUp")
        self.Test_Spec_List = self.Config.value("CONFIG/Test_Spec_List")
        self.CB_Spec_ExportPath = self.Config.value("CONFIG/CB_Spec_ExportPath")
        self.CB_Spec_Generate = self.Config.value("CONFIG/CB_Spec_Generate")
        self.CB_Spec_FromCB = self.Config.value("CONFIG/CB_Spec_FromCB")

        self.__ui.LE_LookUp.setText(self.LookUp)
        if self.Test_Spec_List:
            for file in self.Test_Spec_List:
                self.__ui.textB_Test_Spec.append(file)
        self.__ui.LE_CB_Spec.setText(self.CB_Spec_ExportPath)
        self.__ui.LE_CB_Spec_Generate.setText(self.CB_Spec_Generate)
        self.__ui.LE_Release.setText(self.Release)
        self.__ui.LE_CB_Spec_FromCB.setText(self.CB_Spec_FromCB)



    def SaveConfig(self):
        self.Config = QSettings('./ini/CB_Spec_Tool_Widget.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8

        self.Config.setValue("CONFIG/LookUp",self.LookUp)
        if self.Test_Spec_List:
            self.Config.setValue("CONFIG/Test_Spec_List", self.Test_Spec_List)
        self.Config.setValue("CONFIG/CB_Spec_ExportPath", self.CB_Spec_ExportPath)
        self.Config.setValue("CONFIG/CB_Spec_Generate", self.CB_Spec_Generate)
        self.Config.setValue("CONFIG/Release",self.Release)
        self.Config.setValue("CONFIG/CB_Spec_FromCB", self.CB_Spec_FromCB)

    # 定义错误提示框
    def WarningMessage(self,Err):
        DigTitle = "Warning Message"
        StrInfo = Err
        # print(str)
        QMessageBox.warning(self,DigTitle,str(Err))

    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    def CheckPathContainSpace(self, Path):
        if " " in Path:
            self.WarningMessage(Path + " have space, please remove it")

    #1 设置BT_LookUp
    @pyqtSlot()
    def on_BT_LookUp_clicked(self):
        # pass
        self.__ui.LE_LookUp.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an txt file that contains the doors ID and CB ID mapping ",
                                                         self.CurrentPath,
                                                         "SSDS(*.txt)")
        self.__ui.LE_LookUp.setText(FileName)
        self.LookUp = self.__ui.LE_LookUp.text()
        print(self.LookUp)
        # path = self.SSDS_Path
        # self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #2.设置BT_Test_Spec
    @pyqtSlot()
    def on_BT_Test_Spec_clicked(self):

        self.__ui.textB_Test_Spec.clear()
        self.Test_Spec_List = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "select test specification",
                                                           self.CurrentPath,
                                                           "excel(*.xlsx *.xlsm)")
        # print(FileNames)
        if FileNames:
            for file in FileNames:
                self.__ui.textB_Test_Spec.append(file)
            self.Test_Spec_List += FileNames
            FolderName = os.path.split(self.Test_Spec_List[0])[0]
            self.__ui.LE_CB_Spec.setText(FolderName)
            self.CB_Spec_ExportPath = FolderName
            print(self.CB_Spec_ExportPath)


    @pyqtSlot()
    def on_BT_CB_Spec_clicked(self):
        self.__ui.LE_CB_Spec.clear()
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the folder  to store CB Test Spec  ",
                                                    self.CurrentPath)  # 起始路径
        self.__ui.LE_CB_Spec.setText(FolderName)
        self.CB_Spec_ExportPath = self.__ui.LE_CB_Spec.text()

    @pyqtSlot()
    def on_BT_Replace_DoosID_clicked(self):
        try:
            ExcelAPP = win32com.client.DispatchEx('Excel.Application')
            ExcelAPP.Visible = 0
            ExcelAPP.DisplayAlerts = 0
            Df_LoopUp = CB_Tool.ReadLoopUp(self.LookUp)
            for Test_Spec in self.Test_Spec_List:
                Df_spec, LastSheet_Name, RowSize =CB_Tool.ReadSpec_LastSheet_ReplaceDoorsID(Test_Spec, Df_LoopUp)
                CB_Tool.RepaceDoorsID_SaveMacroEcel(ExcelAPP, Test_Spec, Df_spec, LastSheet_Name, RowSize)
            ExcelAPP.Quit()
            self.DoneMessage("Replace DoorsID successfully")
            self.SaveConfig()
        except Exception as err:
            print(err)
            ExcelAPP.Quit()
            self.WarningMessage(err)

          # 退出

    @pyqtSlot()
    def on_BT_Generate_Init_clicked(self):

        Excel_Files = []
        try:
            # Df_LoopUp = CB_Tool.ReadLoopUp(self.LookUp)
            for Test_Spec in self.Test_Spec_List:
                # print(Test_Spec)
                Df_spec,self.CaseTrackerID,self.CB_Spec_Folder_ID,self.Release= CB_Tool.ReadSpec_TableOfContent(Test_Spec)

                # print(os.path.basename(Test_Spec).split("."))
                SpecCB = os.path.basename(Test_Spec).split(".")[0] +"_CodeBeamer.xlsx"
                SpecCB = os.path.join(self.CB_Spec_ExportPath,SpecCB)
                # print(SpecCB)
                Excel_Files.append(SpecCB)
                CB_Tool.GenerateSpec_CB_Init(Df_spec,self.Release, SpecCB)

            self.FinalCBSpec =  os.path.join(self.CB_Spec_ExportPath,Excel_Files[0])
            self.__ui.LE_CB_Spec_Generate.setText(self.FinalCBSpec)
            self.__ui.LE_FinalCBSpec.setText(self.FinalCBSpec)
            self.CB_Spec_Generate = self.FinalCBSpec
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate Excel successfully")
                self.SaveConfig()
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_CB_Spec_Generate_clicked(self):
        # pass
        self.__ui.LE_CB_Spec_Generate.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the test report generate by this tool",
                                                         self.CurrentPath,
                                                          "excel(*.xlsx)")
        self.__ui.LE_CB_Spec_Generate.setText(FileName)
        self.CB_Spec_Generate = self.__ui.LE_CB_Spec_Generate.text()
        print(self.CB_Spec_Generate)

    #2 .设置LE_SWVersion
    @pyqtSlot(str)
    def on_LE_Release_textChanged(self,str):
        self.Release = self.__ui.LE_Release.text()


    @pyqtSlot()
    def on_BT_CB_Spec_FromCB_clicked(self):
        # pass
        self.__ui.LE_CB_Spec_FromCB.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the test report downlaod from CB",
                                                         self.CurrentPath,
                                                          "excel(*.xlsx)")
        self.__ui.LE_CB_Spec_FromCB.setText(FileName)
        self.CB_Spec_FromCB = self.__ui.LE_CB_Spec_FromCB.text()
        print(self.CB_Spec_FromCB)

    @pyqtSlot()
    def on_BT_Generate_Modify_clicked(self):
        Excel_Files = []
        try:
            df_SpecCB_FromCB, Df_ID_Case_FromCB =  CB_Tool.ReadSpecCB_FromCB2(self.CB_Spec_FromCB)
            df_SpecCB_Generate = pd.read_excel(self.CB_Spec_Generate,"Export")
            SpecCB_Modify = os.path.basename(self.CB_Spec_Generate).split(".")[0] + "_Modify.xlsx"
            SpecCB_Modify = os.path.join(os.path.split(self.CB_Spec_Generate)[0], SpecCB_Modify)

           

            CB_Tool.GenerateSpec_CB_Modify2(df_SpecCB_Generate, Df_ID_Case_FromCB,df_SpecCB_FromCB,self.Release,SpecCB_Modify)
            Excel_Files.append(SpecCB_Modify)
            self.FinalCBSpec = Excel_Files[0]
            self.__ui.LE_FinalCBSpec.setText(self.FinalCBSpec)
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate Excel successfully")
                self.SaveConfig()

        except Exception as err:
            self.WarningMessage(err)


    @pyqtSlot()
    def on_BT_FinalCBSpec_clicked(self):
        # pass
        self.__ui.LE_FinalCBSpec.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the test report generate by this tool",
                                                         self.CurrentPath,
                                                          "excel(*.xlsx)")
        self.__ui.LE_FinalCBSpec.setText(FileName)
        self.FinalCBSpec = self.__ui.LE_FinalCBSpec.text()
        print(self.FinalCBSpec)

    @pyqtSlot(str)
    def on_LE_CaseTrackerID_textChanged(self, str):
        self.CaseTrackerID  = self.__ui.LE_CaseTrackerID.text()
        # print(self.CaseTrackerID)

    @pyqtSlot(str)
    def on_LE_CB_Spec_Folder_ID_textChanged(self, str):
        self.CB_Spec_Folder_ID = self.__ui.LE_CB_Spec_Folder_ID.text()
        # print(self.CB_Spec_Folder_ID)

    @pyqtSlot()
    def on_BT_DownloadCBSpec_clicked(self):
        if not self.CaseTrackerID or not self.CB_Spec_Folder_ID:
            self.WarningMessage("CaseTrackerID or CB_Spec_Folder_ID can't be empty")
            return
        try:
            # print(self.FinalCBSpec)
            # DownLoadSpecFromCB(CaseTrackerID, CB_Spec_Folder, CaseFolderID):
            CB_Spec_DownloadFromCB = DownLoadSpecFromCB(self.CaseTrackerID, self.CB_Spec_ExportPath,self.CB_Spec_Folder_ID )
            self.DoneMessage("Download Succesfully")
            self.CB_Spec_FromCB = os.path.join(self.CB_Spec_ExportPath,CB_Spec_DownloadFromCB)
            self.__ui.LE_CB_Spec_FromCB.setText(self.CB_Spec_FromCB)

        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_Upload2CB_clicked(self):
        if not self.CaseTrackerID or not self.CB_Spec_Folder_ID :
            self.WarningMessage("CaseTrackerID or CB_Spec_Folder_ID can't be empty")
            return
        try:
            # print(self.FinalCBSpec)
            InitCaseList = CB_Tool.GetInitCaseList(self.FinalCBSpec)
            ReturnValue = UploadSpec2CB(self.CaseTrackerID, self.FinalCBSpec, self.CB_Spec_Folder_ID, InitCaseList)
            if ReturnValue:
                self.DoneMessage("upload successfully")
            else:
                self.WarningMessage("upload failed, Please check the file or CB Setting")
        except Exception as err:
            self.WarningMessage(err)


    @pyqtSlot()
    def on_BT_Upload2CB_1stTime_clicked(self):

        Excel_Files = []
        try:
            # Df_LoopUp = CB_Tool.ReadLoopUp(self.LookUp)
            for Test_Spec in self.Test_Spec_List:
                # print(Test_Spec)
                Df_spec,self.CaseTrackerID,self.CB_Spec_Folder_ID,self.Release = CB_Tool.ReadSpec_TableOfContent(Test_Spec)
                if not self.CaseTrackerID or not self.CB_Spec_Folder_ID:
                    self.WarningMessage("CaseTrackerID or CB_Spec_Folder_ID can't be empty")
                    return
                # print(os.path.basename(Test_Spec).split("."))
                SpecCB = os.path.basename(Test_Spec).split(".")[0] + "_CodeBeamer.xlsx"
                SpecCB = os.path.join(self.CB_Spec_ExportPath, SpecCB)
                # print(SpecCB)
                Excel_Files.append(SpecCB)
                CB_Tool.GenerateSpec_CB_Init(Df_spec, self.Release ,SpecCB)

            self.FinalCBSpec = os.path.join(self.CB_Spec_ExportPath, Excel_Files[0])
            self.__ui.LE_CB_Spec_Generate.setText(self.FinalCBSpec)
            self.__ui.LE_FinalCBSpec.setText(self.FinalCBSpec)
            self.CB_Spec_Generate = self.FinalCBSpec
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.__ui.BT_Upload2CB.click()
                self.SaveConfig()
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_Upload2CB_Modify_clicked(self):

        Excel_Files = []
        #先重新生成
        print("1st Generate")
        try:
            # Df_LoopUp = CB_Tool.ReadLoopUp(self.LookUp)
            for Test_Spec in self.Test_Spec_List:
                # print(Test_Spec)
                print("1" * 30)
                Df_spec,self.CaseTrackerID,self.CB_Spec_Folder_ID,self.Release = CB_Tool.ReadSpec_TableOfContent(Test_Spec)
                print("3"*30)
                if not self.CaseTrackerID or not self.CB_Spec_Folder_ID:
                    self.WarningMessage("CaseTrackerID or CB_Spec_Folder_ID can't be empty")
                    return
                # print(os.path.basename(Test_Spec).split("."))
                SpecCB = os.path.basename(Test_Spec).split(".")[0] + "_CodeBeamer.xlsx"
                SpecCB = os.path.join(self.CB_Spec_ExportPath, SpecCB)
                # print(SpecCB)
                Excel_Files.append(SpecCB)
                print("5" * 30)
                CB_Tool.GenerateSpec_CB_Init(Df_spec, self.Release,SpecCB)
            print("4" * 30)
            self.FinalCBSpec = os.path.join(self.CB_Spec_ExportPath, Excel_Files[0])
            self.__ui.LE_CB_Spec_Generate.setText(self.FinalCBSpec)
            self.__ui.LE_FinalCBSpec.setText(self.FinalCBSpec)
            self.CB_Spec_Generate = self.FinalCBSpec
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]

            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                #然后下载
                print("2nd Download")
                CB_Spec_DownloadFromCB = DownLoadSpecFromCB(self.CaseTrackerID, self.CB_Spec_ExportPath,
                                                            self.CB_Spec_Folder_ID)
                self.CB_Spec_FromCB = os.path.join(self.CB_Spec_ExportPath, CB_Spec_DownloadFromCB)
                self.__ui.LE_CB_Spec_FromCB.setText(self.CB_Spec_FromCB)
                try:
                    Excel_Files = []
                    #然后Modify
                    print("3nd Modify")
                    df_SpecCB_FromCB, Df_ID_Case_FromCB = CB_Tool.ReadSpecCB_FromCB(self.CB_Spec_FromCB)
                    df_SpecCB_Generate = pd.read_excel(self.CB_Spec_Generate, "Export")
                    SpecCB_Modify = os.path.basename(self.CB_Spec_Generate).split(".")[0] + "_Modify.xlsx"
                    SpecCB_Modify = os.path.join(os.path.split(self.CB_Spec_Generate)[0], SpecCB_Modify)
                    print(SpecCB_Modify)
                    if self.Release:
                        CB_Tool.GenerateSpec_CB_Modify(df_SpecCB_Generate, Df_ID_Case_FromCB, self.Release,
                                                       SpecCB_Modify)
                        Excel_Files.append(SpecCB_Modify)
                        self.FinalCBSpec = Excel_Files[0]

                        print(self.FinalCBSpec)
                        # self.WarningMessage("T")
                        self.__ui.LE_FinalCBSpec.setText(self.FinalCBSpec)
                        NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
                        if len(NotOK_Files):
                            self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
                        else:
                            print("4th upload")
                            self.__ui.BT_Upload2CB.click()
                            self.SaveConfig()
                    else:
                        self.WarningMessage("Release can't be empty")
                except Exception as err:
                    self.WarningMessage(err)
        except Exception as err:
            self.WarningMessage(err)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = CB_Spec_Tool_Widget()
    baseWidget.show()
    sys.exit(app.exec_())
