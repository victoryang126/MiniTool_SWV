import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import xlrd
import pandas as pd
import win32com
from win32com.client import Dispatch
import ConvertSpect2CBSpec as CB_Tool
from Ui_CB_Spec_Tool import Ui_CB_Spec_Tool

from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QDialog,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings
from PyQt5.QtGui import  QIcon
from PyQt5.QtGui import  QIcon
# from Module import *
# import DID_SmartEDR


class SmartEDRWidget(QWidget):

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
        self.CB_Spec_FromCB = ""

        # *****************设置GenS37 LineEdit默认值****************************************



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
        # path = cls.SSDS_Path
        # cls.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #2.设置BT_Test_Spec
    @pyqtSlot()
    def on_BT_Test_Spec_clicked(self):

        self.__ui.textB_Test_Spec.clear()
        self.Test_Spec_List = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "select test specification",
                                                           self.CurrentPath,
                                                           "excel(*.xlsm)")
        # print(FileNames)
        for file in FileNames:
            self.__ui.textB_Test_Spec.append(file)
        self.Test_Spec_List += FileNames


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
        except Exception as err:
            print(err)
            ExcelAPP.Quit()
            self.WarningMessage(err)

          # 退出

    @pyqtSlot()
    def on_BT_Generate_Init_clicked(self):
        print(2)
        Excel_Files = []
        try:
            # Df_LoopUp = CB_Tool.ReadLoopUp(cls.LookUp)
            print(1)
            for Test_Spec in self.Test_Spec_List:
                # print(Test_Spec)
                Df_spec = CB_Tool.ReadSpec_TableOfContent(Test_Spec)
                # print(os.path.basename(Test_Spec).split("."))
                SpecCB = os.path.basename(Test_Spec).split(".")[0] +"_CodeBeamer.xlsx"
                SpecCB = os.path.join(self.CB_Spec_ExportPath,SpecCB)
                # print(SpecCB)
                Excel_Files.append(SpecCB)
                CB_Tool.GenerateSpec_CB_Init(Df_spec, SpecCB)
            print(3)
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate Excel successfully")
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
            df_SpecCB_FromCB, Df_ID_Case_FromCB =  CB_Tool.ReadSpecCB_FromCB(self.CB_Spec_FromCB)
            df_SpecCB_Generate = pd.read_excel(self.CB_Spec_Generate,"Export")
            SpecCB_Modify = os.path.basename(self.CB_Spec_Generate).split(".")[0] + "_Modify.xlsx"
            SpecCB_Modify = os.path.join(os.path.split(self.CB_Spec_Generate)[0], SpecCB_Modify)
            CB_Tool.GenerateSpec_CB_Modify(df_SpecCB_Generate, Df_ID_Case_FromCB, SpecCB_Modify)
            Excel_Files.append(SpecCB_Modify)
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate Excel successfully")
        except Exception as err:
            self.WarningMessage(err)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = SmartEDRWidget()
    baseWidget.show()
    sys.exit(app.exec_())
