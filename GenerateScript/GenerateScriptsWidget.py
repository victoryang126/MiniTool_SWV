from GenerateScript.Ui_GenerateScripts import Ui_GenerateScripts
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
        self.__ui = Ui_GenerateScripts()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # *****************定义 GenS37相关属性****************************************
        self.Config = ""
        self.TestObject = ""
        self.SheetList = []
        self.CurrentSheet = ""
        self.ScriptTemplates = []
        self.ScriptPath = ""

        # *****************设置OtToll LineEdit默认值****************************************
        if os.path.exists('./ini/GenerateScripts.ini'):

            self.Config = QSettings('./ini/GenerateScripts.ini', QSettings.IniFormat)
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
        self.TestObject = self.Config.value("CONFIG/TestObject")
        self.SheetList = self.Config.value("CONFIG/SheetList")
        self.CurrentSheet = self.Config.value("CONFIG/CurrentSheet")
        self.ScriptTemplates = self.Config.value("CONFIG/ScriptTemplates")
        self.ScriptPath = self.Config.value("CONFIG/ScriptPath")

        self.__ui.LE_TestObject.setText(self.TestObject)
        self.__ui.CB_SheetList.clear()
        self.__ui.CB_SheetList.addItems(self.SheetList)


        if self.ScriptTemplates:
            for file in self.ScriptTemplates:
                self.__ui.textB_ScriptTemplates.append(file)
        self.__ui.LE_ScriptPath.setText(self.ScriptPath)


    def SaveConfig(self):
        self.Config = QSettings('./ini/GenerateScripts.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8
        self.Config.setValue("CONFIG/TestObject", self.TestObject)
        self.Config.setValue("CONFIG/SheetList", self.SheetList)
        self.Config.setValue("CONFIG/CurrentSheet", self.CurrentSheet)
        if self.ScriptTemplates:
            self.Config.setValue("CONFIG/ScriptTemplates", self.ScriptTemplates)
        self.Config.setValue("CONFIG/ScriptPath", self.ScriptPath)

    # 1 设置BT_TestObject
    @pyqtSlot()
    def on_BT_TestObject_clicked(self):
        # pass
        self.__ui.LE_TestObject.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Please select the excel files that contains all test object ",
                                                         self.CurrentPath,
                                                         "Excel for the test object(*.xlsm *.xlsx)")
        if FileName:
            #获取Excel
            self.__ui.LE_TestObject.setText(FileName)
            self.TestObject = self.__ui.LE_TestObject.text()
            print(self.TestObject)
            #将Excel 里面的sheet添加到CB_SheetList
            self.SheetList = GetExcelSheet(FileName)
            self.__ui.CB_SheetList.clear()
            self.__ui.CB_SheetList.addItems(self.SheetList)


        # path = cls.SSDS_Path
        # cls.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 2. CB_SheetList
    @pyqtSlot(str)
    def on_CB_SheetList_currentTextChanged(self,str):
        self.CurrentSheet = self.__ui.CB_SheetList.currentText()
        # print(cls.GenS37_FileType)

    # 3.设置BT_ScriptTemplates
    @pyqtSlot()
    def on_BT_ScriptTemplates_clicked(self):

        self.__ui.textB_ScriptTemplates.clear()
        self.ScriptTemplates = []
        FileNames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "select test scripts",
                                                           self.CurrentPath,
                                                           "*.*")
        # print(FileNames)
        for file in FileNames:
            self.__ui.textB_ScriptTemplates.append(file)
        self.ScriptTemplates += FileNames

    # 4.BT_ScriptPath
    @pyqtSlot()
    def on_BT_ScriptPath_clicked(self):
        self.__ui.LE_ScriptPath.clear()
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the folder  to store test scripts  ",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_ScriptPath.setText(FolderName)
        self.ScriptPath = self.__ui.LE_ScriptPath.text()


    # 5.
    @pyqtSlot()
    def on_BT_Generate_clicked(self):
        """
        1. 先从Excel 里面读取出测试对象，
        2. 然后每个测试对象遍历模板脚本去生成相对应对象的测试脚本
        :return:
        """
        #1.处理Excel
        try:
            args = {"ExcelPath": self.TestObject, "SheetName": self.CurrentSheet
                   }
            #获取测试对象的数据
            TestObject_Dict = GetTestObject(**args)

            #遍历模板脚本
            for ScriptTemplate in self.ScriptTemplates:
                ScriptTemplateContent, TestType = CommonFun.GetTempleteScript(ScriptTemplate)

                #遍历测试对象
                for TestObject_Str in TestObject_Dict:
                    ReplaceDict = TestObject_Dict[TestObject_Str]
                    args = {"ScriptTemplateContent":ScriptTemplateContent,
                            "ReplaceDict":ReplaceDict,
                            "ScriptOutputPath":self.ScriptPath,"TestObject_Str":TestObject_Str,"TestType":TestType}
                    #生成测试脚本
                    CommonFun.GenerateScripts_BaseTemplate(**args)

            self.DoneMessage("Generate Scripts successfully")
            self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = GenerateScriptsWidget()
    baseWidget.show()
    sys.exit(app.exec_())