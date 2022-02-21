import sys

import os


from Other_Tool.Ui_OtTool import Ui_OtTool
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot

# from Module import *
from Other_Tool import DictGen
from Other_Tool import AEFGen
from Other_Tool import Sym2Ts

class OtToolWidget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_OtTool()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面


        # *****************定义 OtTool相关属性****************************************
        self.DictGen_Excel = ""
        self.DictGen_Sheet = ""
        self.DictGen_Key = ""
        self.DictGen_Values = ""
        self.DictGen_Output = "Dict.ts"

        self.Sym2Ts_Sym = ""
        self.Sym2Ts_Output = "PBCT.ts"

        self.AEFGen_BaseAEF = ""
        self.AEFGen_AEFFiles = []

        self.AEFGen_OutPut = "AEFFolder"



        # *****************设置OtToll LineEdit默认值****************************************
        self.__ui.LE_DictGen_Output.setText(self.DictGen_Output)
        self.__ui.LE_Sym2Ts_Output.setText(self.Sym2Ts_Output)

    # 定义错误提示框
    def WarningMessage(self,str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self,DigTitle,StrInfo)
    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    #*******************************设置DictGen槽函数******************************
    #1 设置BT_DictGen_Excel
    @pyqtSlot()
    def on_BT_DictGen_Excel_clicked(self):

        self.__ui.LE_DictGen_Excel.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an excel file ",
                                                         self.CurrentPath,
                                                         "Reg_Excel(*.xlsx *.xlsm)")
        self.__ui.LE_DictGen_Excel.setText(FileName)
        self.DictGen_Excel = self.__ui.LE_DictGen_Excel.text()
    #2设置LE_DictGen_Sheet_
    @pyqtSlot(str)
    def on_LE_DictGen_Sheet_textChanged(self,str):
        self.DictGen_Sheet = self.__ui.LE_DictGen_Sheet.text()
    #3 设置LE_DictGen_Key
    @pyqtSlot(str)
    def on_LE_DictGen_Key_textChanged(self,str):
        self.DictGen_Key = self.__ui.LE_DictGen_Key.text()
    #4设置LE_DictGen_Values
    @pyqtSlot(str)
    def on_LE_DictGen_Values_textChanged(self,str):
        self.DictGen_Values = self.__ui.LE_DictGen_Values.text()
    #5设置LE_DictGen_Output_
    @pyqtSlot(str)
    def on_LE_DictGen_Output_textChanged(self,str):
        self.DictGen_Output = self.__ui.LE_DictGen_Output.text()

    # 6.设置BT_DictGen_GenerateDict
    @pyqtSlot()
    def on_BT_DictGen_GenerateDict_clicked(self):
        try:
            args = {"ExcelDir":self.DictGen_Excel, "Sheet":self.DictGen_Sheet, "Key":self.DictGen_Key,
                    "Values":self.DictGen_Values.split(","), "TsName":self.DictGen_Output}
            DictGen.DictGenerate(**args)
            self.DoneMessage("Generate Dict successfully")
            # DictGen(ExcelDir, Sheet, Key, Values, TsName)
        except Exception as err:
            self.WarningMessage(str(err))

    #**********************设置Sym2Ts 槽********************************************
    #1 设置BT_Sym2Ts_Sym
    @pyqtSlot()
    def on_BT_Sym2Ts_Sym_clicked(self):

        self.__ui.LE_Sym2Ts_Sym.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an Sym file ",
                                                         self.CurrentPath,
                                                         "Reg_Excel(*.sym)")
        self.__ui.LE_Sym2Ts_Sym.setText(FileName)
        self.Sym2Ts_Sym = self.__ui.LE_Sym2Ts_Sym.text()
    #1设置LE_Sym2Ts_Sym
    @pyqtSlot(str)
    def on_LE_Sym2Ts_Sym_textChanged(self,str):
        self.Sym2Ts_Sym = self.__ui.LE_Sym2Ts_Sym.text()
    #2设置LE_Sym2Ts_Output
    @pyqtSlot(str)
    def on_LE_Sym2Ts_Output_textChanged(self,str):
        self.Sym2Ts_Output = self.__ui.LE_Sym2Ts_Output.text()

    # 6.设置BT_DictGen_GenerateDict
    @pyqtSlot()
    def on_BT_Sym2Ts_GenerateSymTs_clicked(self):
        try:
            args = {"SymPath":self.Sym2Ts_Sym, "TsName":self.Sym2Ts_Output}
            Sym2Ts.Sym2Ts(**args)
            self.DoneMessage("Generate Dict successfully")
            # Sym2Ts(SymPath, TsName)
        except Exception as err:
            self.WarningMessage(str(err))


    # **********************设置AEFGenerate 槽********************************************
    #2. 设置BT_AEFGen_BaseAEF
    @pyqtSlot()
    def on_BT_AEFGen_BaseAEF_clicked(self):

        self.__ui.LE_AEFGen_BaseAEF.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the base AEF file to get the AEF content ",
                                                         self.CurrentPath,
                                                         "(*.Aef)")
        self.__ui.LE_AEFGen_BaseAEF.setText(FileName)
        # if self.__ui.LE_DBC
        self.AEFGen_BaseAEF = self.__ui.LE_AEFGen_BaseAEF.text()

    #3设置LE_AEFGen_AEFFiles
    @pyqtSlot()
    def on_BT_AEFGen_AEFFiles_clicked(self):
        self.__ui.TextB_AEFGen_AEFFiles.clear()
        self.AEFGen_AEFFiles = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Select the AEF files",
                                                           self.CurrentPath,
                                                            " (*.AEF *.PRN)")
        # print(FileNames)
        for file in FileNames:
            self.__ui.TextB_AEFGen_AEFFiles.append(file)
        self.AEFGen_AEFFiles += FileNames
        # 5. 设置BT_GenS37_GenrateS37

    @pyqtSlot()
    def on_BT_AEFGen_AEFGenerate_clicked(self):
        try:
            self.AEFGen_OutPut = os.path.split(self.AEFGen_AEFFiles[0])[0] + "\\AEFFolder"
        except Exception:
            self.WarningMessage("Please select PRN or AEF files")
        try:
            args = {"BaseAEFPath":self.AEFGen_BaseAEF,"AEFFiles": self.AEFGen_AEFFiles,"AEFOutPut":self.AEFGen_OutPut}
            AEFGen.GenerateAEF(**args)
            # (GenerateAEF(BaseAEFPath,AEFFiles,AEFOutPut)
            self.DoneMessage("Generate AEF files successfully")
        except Exception as err:
            self.WarningMessage(str(err))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = OtToolWidget()

    baseWidget.show()
    sys.exit(app.exec_())
