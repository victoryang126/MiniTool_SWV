import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import win32com
from win32com.client import Dispatch
from CB_Tool_SC3.HandleTestRun import  *
from CB_Tool_SC3.HandleTestRun import *
from CB_Tool_SC3.HandleCodebeamer import *
from CB_Tool_SC3.Ui_CB_Tool import Ui_CBTool
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPalette
import numpy as np

class CB_Tool_Widget(QWidget):

    CurrentPath = os.getcwd()
    TestRun_Link_Prefix = "https://codebeamer.corp.int/cb/issue/"

    def __init__(self):
        super().__init__()
        self.__ui = Ui_CBTool()
        self.__ui.setupUi(self)


        ##########定义相关属性########################
        self.PTC_Spec = ""
        self.PTC_Result = ""
        self.Release = ""
        self.CaseTrackerID = ""
        self.CaseFolderID = ""
        self.TestRun_TrackerName = ""

        self.CB_Spec_FromCB = ""
        self.FinalCBSpec = ""

        self.TestRun_ID = ""
        self.TestRun_Link = ""
        self.TestRun_Report = ""
        self.TestRun_Status = ""
        self.TestRun_Result = ""

        self.PTC_Result_List = []


    # 定义错误提示框
    def WarningMessage(self, Err):
        DigTitle = "Warning Message"
        StrInfo = Err
        # print(str)
        QMessageBox.warning(self, DigTitle, str(Err))

    def DoneMessage(self, str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    def set_status_result(self,flag):
        if flag:
            self.__ui.TestRun_Result.setAutoFillBackground(True)
            self.__ui.TestRun_Status.setAutoFillBackground(True)
            RedColor = QPalette()
            RedColor.setColor(QPalette.Window, Qt.red)

            GreenCOlor = QPalette()
            GreenCOlor.setColor(QPalette.Window, Qt.green)

            if self.TestRun_Result == "PASSED":
                self.__ui.TestRun_Result.setPalette(GreenCOlor)
            else:
                self.__ui.TestRun_Result.setPalette(RedColor)

            if self.TestRun_Status == "FINIShED":
                self.__ui.TestRun_Status.setPalette(GreenCOlor)
            else:
                self.__ui.TestRun_Status.setPalette(RedColor)
        else:
            self.__ui.TestRun_Result.setText("--")
            self.__ui.TestRun_Status.setText("--")
            self.__ui.TestRun_Result.setAutoFillBackground(True)
            self.__ui.TestRun_Status.setAutoFillBackground(True)
            WhiteColor = QPalette()
            WhiteColor.setColor(QPalette.Window, Qt.white)
            self.__ui.TestRun_Result.setPalette(WhiteColor)
            self.__ui.TestRun_Status.setPalette(WhiteColor)
    def check_testrun_tackename(self):
        print(self.TestRun_TrackerName == np.nan,self.TestRun_TrackerName)
        if np.isnan(self.TestRun_TrackerName):
            self.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()
        else:
            self.__ui.LE_TestRun_TrackerName.setText(self.TestRun_TrackerName)

        if not self.TestRun_TrackerName:
            raise Exception("TestRun_TrackerName can't be empty")

    ########################Test Run ################################
    @pyqtSlot()
    def on_BT_PTC_Result_clicked(self):
        self.__ui.LE_PTC_Result.clear()
        file,filetype = QFileDialog.getOpenFileName(self,
                                          "Please the PTC Test Result ",
                                          self.CurrentPath,
                                          "Excel(*.xlsx *.xlsm)")  # 起始路径

        self.__ui.LE_PTC_Result.setText(file)
        self.PTC_Result = file
        self.CurrentPath = os.path.abspath(file) if os.path.isdir(file) else os.path.dirname(file)

    @pyqtSlot()
    def on_BT_Init_Upload_TestRun_clicked(self):
        ### 后期加函数处理
        self.set_status_result(False)
        try:
            Df_Result, self.CaseTrackerID, self.CaseFolderID, self.Release, self.TestRun_TrackerName = ReadResult_TableOfContent(
                self.PTC_Result)

            # if self.CaseTrackerID or self.CB_Spec_Folder_ID or self.Release:
            #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")
            print(self.CaseTrackerID)
            print(self.CaseFolderID)
            print(self.Release)
            # print(self.TestRun_TrackerName)
            self.check_testrun_tackename()
            self.__ui.LE_CaseTrackerID.setText(self.CaseTrackerID)
            self.__ui.LE_CB_Spec_Folder_ID.setText(self.CaseFolderID)
            self.__ui.LE_Release.setText(self.Release)


            args = {
                "CaseTrackerID": self.CaseTrackerID,
                "CaseFolderID": self.CaseFolderID,
                "Test_Run_Folder": self.CurrentPath,
                "TestRun_TrackerName": self.TestRun_TrackerName,
                "Df_Result": Df_Result,
                "Release": self.Release
            }
            self.TestRun_Report, self.TestRun_ID, self.TestRun_Status,self.TestRun_Result = CreateTestRun_UpdateResult(**args)
            self.__ui.LE_TestRun_Report.setText(self.TestRun_Report)
            self.__ui.LE_TestRun_ID.setText(self.TestRun_ID)
            self.__ui.TestRun_Status.setText(self.TestRun_Status)
            self.__ui.TestRun_Result.setText(self.TestRun_Result)
            #根据结果设置颜色
            self.set_status_result(True)
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot(str)
    def on_LE_TestRun_TrackerName_textChanged(self):
        if self.__ui.LE_TestRun_TrackerName.text():
            self.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()



    @pyqtSlot(str)
    def on_LE_TestRun_ID_textChanged(self):
        if self.__ui.LE_TestRun_ID.text():

            self.TestRun_ID = self.__ui.LE_TestRun_ID.text()
            print(self.TestRun_ID)
            self.TestRun_Link = self.TestRun_Link_Prefix + self.TestRun_ID
            url = u'<a href=' + self.TestRun_Link + u'>' + u'<b>' + "Test Run" u'</b></a>'
            self.__ui.Label_TestRun_Url.setOpenExternalLinks(True)
            self.__ui.Label_TestRun_Url.setText(url)

    #
    # @pyqtSlot()
    # def on_BT_SelectTestRunReport_clicked(self):
    #     file,filetype = QFileDialog.getOpenFileName(self,
    #                                       "Please the PTC Test Result ",
    #                                       self.CurrentPath,
    #                                       "Excel(*.xlsx *.xlsm)")  # 起始路径
    #     self.__ui.LE_TestRun_Report.setText(file)
    #     self.TestRun_Report = file
    #     self.CurrentPath = os.path.abspath(file) if os.path.isdir(file) else os.path.dirname(file)

    def Debug(self):
        # self.CaseTrackerID = "10574131"
        # self.CaseFolderID = "15704840"
        # self.Release = "CHERY_T26&M1E_Release P10"
        # self.TestRun_TrackerName = "TR_SHR_TestRuns"
        pass

    @pyqtSlot()
    def on_BT_Restart_TestRun_clicked(self):
        self.set_status_result(False)
        try:
            Df_Result, self.CaseTrackerID, self.CaseFolderID, self.Release, self.TestRun_TrackerName = ReadResult_TableOfContent(
                self.PTC_Result)

            # if self.CaseTrackerID or self.CB_Spec_Folder_ID or self.Release:
            #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")
            self.Debug()
            self.__ui.LE_CaseTrackerID.setText(self.CaseTrackerID)
            self.__ui.LE_CB_Spec_Folder_ID.setText(self.CaseFolderID)
            self.__ui.LE_Release.setText(self.Release)
            #为了 让旧模板的人通过填写TestRun的方式，而不是在Excel里填写
            self.check_testrun_tackename()
            args = {
                "Test_Run_ID": self.TestRun_ID,
                "Test_Run_Folder": self.CurrentPath,
                "Df_Result": Df_Result,
            }

            self.TestRun_Report, self.TestRun_ID, self.TestRun_Status, self.TestRun_Result = Restart_TestRun( **args)
            self.__ui.LE_TestRun_Report.setText(self.TestRun_Report)
            self.__ui.LE_TestRun_ID.setText(self.TestRun_ID)
            self.__ui.TestRun_Status.setText(self.TestRun_Status)
            self.__ui.TestRun_Result.setText(self.TestRun_Result)

            # 根据结果设置颜色
            self.set_status_result(True)
        except Exception as err:
            self.WarningMessage(err)


    @pyqtSlot()
    def on_BT_PTC_Results_clicked(self):
        self.PTC_Result_List = []
        self.__ui.textBrowser_TestResults.clear()
        Files, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Select Test Result files",
                                                           self.CurrentPath,
                                                           "Excel(*.xlsm *.xlsx)")
        # print(FileNames)
        for file in Files:
            self.__ui.textBrowser_TestResults.append(file)
            self.PTC_Result_List = Files[:]
        if Files:
            self.CurrentPath =  os.path.abspath(Files[0]) if os.path.isdir(Files[0]) else os.path.dirname(Files[0])

    @pyqtSlot()
    def on_BT_Init_Upload_TestRuns_clicked(self):
        for ptc_result in self.PTC_Result_List:
            try:
                Df_Result, self.CaseTrackerID, self.CaseFolderID, self.Release, self.TestRun_TrackerName = ReadResult_TableOfContent(
                    ptc_result)

                # if self.CaseTrackerID or self.CB_Spec_Folder_ID or self.Release:
                #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")
                self.check_testrun_tackename()
                args = {
                    "CaseTrackerID": self.CaseTrackerID,
                    "CaseFolderID": self.CaseFolderID,
                    "Test_Run_Folder": self.CurrentPath,
                    "TestRun_TrackerName": self.TestRun_TrackerName,
                    "Df_Result": Df_Result,
                    "Release": self.Release
                }
                self.TestRun_Report, self.TestRun_ID, self.TestRun_Status, self.TestRun_Result = CreateTestRun_UpdateResult(
                    **args)
                print("### Upload" + ptc_result + " to test run,TestRun_Status:" + self.TestRun_Status + "TestRun_Result: " + self.TestRun_Result)
                # self.__ui.LE_TestRun_Report.setText(self.TestRun_Report)
                # self.__ui.LE_TestRun_ID.setText(self.TestRun_ID)
                # self.__ui.TestRun_Status.setText(self.TestRun_Status)
                # self.__ui.TestRun_Result.setText(self.TestRun_Result)
                # 根据结果设置颜色
                # self.set_status_result(True)
            except Exception as err:
                self.WarningMessage(err)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = CB_Tool_Widget()
    baseWidget.show()
    sys.exit(app.exec_())
