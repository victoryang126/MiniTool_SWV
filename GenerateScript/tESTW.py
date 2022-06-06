from GenerateScript.Test import Ui_Form
import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings

import pandas as pd
from CommonFunction import CommonFun


def GetExcelSheet(ExcelPath):
    if ExcelPath:
        Df_AllSheet = pd.read_excel(ExcelPath, sheet_name=None)
        SheetList = list(Df_AllSheet)
        # print(SheetList)
        return SheetList

def GetTestObject(ExcelPath,SheetName):
    df = pd.read_excel(ExcelPath, sheet_name=SheetName)
    df.fillna("undefined", inplace=True)
    df.set_index(df.columns[0], inplace=True,drop= False)
    TestObject_Dict = df.to_dict(orient="index")
    # print(TestObject_Dict)
    return TestObject_Dict

class GenerateScriptsWidget(QWidget):
    CurrentPath = os.getcwd()

    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_Form()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # *****************定义 GenS37相关属性****************************************
        self.Config = ""
        self.TestObject = ""
        self.SheetList = []
        self.CurrentSheet = ""
        self.ScriptTemplates = []
        self.ScriptPath = ""

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # self.__ui.LE_ScriptPath.clear()
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the folder  to store test scripts  ",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.lineEdit.setText(FolderName)
        # self.ScriptPath = self.__ui.LE_ScriptPath.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = GenerateScriptsWidget()
    baseWidget.show()
    sys.exit(app.exec_())