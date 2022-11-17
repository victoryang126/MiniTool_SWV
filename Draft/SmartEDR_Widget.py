import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import xlrd

from Ui_SmartEDR import Ui_SmartEDR
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QDialog,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtGui import  QIcon
# from Module import *
import DID_SmartEDR


class SmartEDRWidget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_SmartEDR()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面


        # *****************定义 GenS37相关属性****************************************


        self.SSDS_Path = ""
        self.Txt = []
        self.DID_Dict = {}
        self.DID_Dict_Path = ""

        # *****************设置GenS37 LineEdit默认值****************************************



    # 定义错误提示框
    def WarningMessage(self,str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self,DigTitle,StrInfo)
    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    def CheckPathContainSpace(self, Path):
        if " " in Path:
            self.WarningMessage(Path + " have space, please remove it")



    #1 设置BT_GenS37_Ascent
    @pyqtSlot()
    def on_BT_SSDS_clicked(self):
        # pass
        self.__ui.LE_SSDS.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an SSDS file ",
                                                         self.CurrentPath,
                                                         "SSDS(*.xlsx)")
        self.__ui.LE_SSDS.setText(FileName)
        self.SSDS_Path = self.__ui.LE_SSDS.text()
        # print(cls.SSDS_Path)
        # path = cls.SSDS_Path
        # cls.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)




    # 1 .on_BT_LoadDIDParameter_clicked
    @pyqtSlot()
    def on_BT_LoadDIDParameter_clicked(self):
        try:
            self.DID_Dict = DID_SmartEDR.GetDIDObjectFromSSDS(self.SSDS_Path,"DID","DID_Object.json")
            FileName = self.CurrentPath + "\\" + "DID_Object.json"
            self.__ui.LE_DID_Dict.setText(FileName)
            self.DoneMessage("DID object generate successfully")
        except Exception as err:
            self.WarningMessage(err)

        # 1 设置BT_GenS37_Ascent

    @pyqtSlot()
    def on_BT_DID_Dict_clicked(self):
        # pass
        self.__ui.LE_DID_Dict.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an json file ",
                                                         self.CurrentPath,
                                                         "DID_Object.json(*.json)")
        self.__ui.LE_DID_Dict.setText(FileName)
        self.DID_Dict_Path = self.__ui.LE_DID_Dict.text()

        self.DID_Dict = DID_SmartEDR.GetDID_Dict(self.DID_Dict_Path)
        # print(cls.DID_Dict_Path)
        # path = cls.DID_Dict_Path
        # cls.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    @pyqtSlot()
    def on_BT_TXT_clicked(self):

        self.__ui.textB_TXT.clear()
        self.TXT = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "select txt file where the data record stored",
                                                           self.CurrentPath,
                                                           "txt(*.txt)")
        # print(FileNames)
        for file in FileNames:
            self.__ui.textB_TXT.append(file)
        self.TXT += FileNames
        #
        # try:
        #     path = cls.TXT[0]
        #     cls.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)
        # except Exception as err:
        #     cls.WarningMessage("please txt files")
    @pyqtSlot()
    def on_BT_Generate_clicked(self):
        Excel_Files = []
        try:
            for txt in self.TXT:
                # try:
                DataRecordExcel, DID, ResponseValue = DID_SmartEDR.GetInfoFromTxt(txt)
                DataRecordDict = DID_SmartEDR.GetDataRecordDetail2(ResponseValue, self.DID_Dict, DID)
                DID_SmartEDR.GenerateDataRecordExcel(DataRecordDict, DataRecordExcel, DID)
                Excel_Files.append(DataRecordExcel)
                # except Exception as err:
                #     continue;
            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            if len(NotOK_Files):
                # pass
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
