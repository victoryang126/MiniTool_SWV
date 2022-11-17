import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import win32com
from win32com.client import Dispatch
from CB_Tool_SC3.HandleTestRun import  *
from CB_Tool_SC3.HandleTestRun import *
from CB_Tool_SC3.Ui_CB_Tool import Ui_CBTool
from CB_Tool_SC3.Ui_WorkingSet import Ui_WorkingSet
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot,Qt,QThread,pyqtSignal,QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPalette
from CB_Tool_SC3.CodeBeamer import CodeBeamer
from CB_Tool_SC3.WorkingSet_Widget import WorkingSet_Widget
from CB_Tool_SC3.CB_Tool import CB_Tool
from CB_Tool_SC3.TestSpec_Widget import TestSpec_Widget

import numpy as np

# class BackgoundThread(QThread,CB_Tool):
#     # ui_value = ""
#     # attr_value = ""
#     update_release = pyqtSignal(str)
#     update_casefolderid = pyqtSignal(str)
#     update_casetrackerid = pyqtSignal(str)
#     def run(self):
#         while True:
#         #     # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#             if CB_Tool.Release != "" and :
#                 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", CB_Tool.Release,
#                       CB_Tool.CaseFolderID)
#                 self.update_release.emit(CB_Tool.Release)
#             if CB_Tool.CaseFolderID != "":
#
#                 self.update_casefolderid.emit(CB_Tool.CaseFolderID)
#             if CB_Tool.CaseTrackerID != "":
#                     self.update_casetrackerid.emit(CB_Tool.CaseTrackerID)

def Bind(objectName,propertyName):
    def getter(self):
        return self.findChild(QObject,objectName).property(propertyName)

    def setter(self,value):
        return self.findChild(QObject, objectName).SetProperty(propertyName,value)
    return property(getter,setter)

class CB_Tool_Widget(QWidget,CB_Tool):

    # CB_Tool = CB_Tool()
    # Release = Bind("LE_Release","text")


    def __init__(self):
        super().__init__()
        self.__ui = Ui_CBTool()
        self.__ui.setupUi(self)
        # self.SubThread = BackgoundThread()
        # self.SubThread.update_release.connect(self.__ui.LE_Release.setText)
        # self.SubThread.update_casetrackerid.connect(self.__ui.LE_CaseTrackerID.setText)
        # self.SubThread.update_casefolderid.connect(self.__ui.LE_CB_Spec_Folder_ID.setText)
        # self.SubThread.start()
        # WorkingSet = WorkingSet_Widget()
        Spec_Widget = TestSpec_Widget()
        self.__ui.CodeBeamer.addTab(Spec_Widget,"Test Spec SC3")
        # self.__ui.CodeBeamer.addTab(WorkingSet, "WorkingSet")
        # cls.__ui.CodeBeamer.setTabText()


        ##########定义相关属性########################

        #
        # cls.PTC_Spec = ""
        # cls.PTC_Result = ""
        # cls.CB_Spec_FromCB = ""
        # cls.FinalCBSpec = ""
        #
        # cls.TestRun_Link = ""
        # cls.TestRun_Report = ""
        # cls.TestRun_Status = ""
        # cls.TestRun_Result = ""
        #
        # cls.PTC_Result_List = []


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

            if CB_Tool.TestRun_Result == "PASSED":
                self.__ui.TestRun_Result.setPalette(GreenCOlor)
            else:
                self.__ui.TestRun_Result.setPalette(RedColor)

            if CB_Tool.TestRun_Status == "FINIShED":
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
    def check_testrun_trackername(self):
        # print(cls.TestRun_TrackerName == np.nan,cls.TestRun_TrackerName)
        print("test")
        # 如果是老版本的excel，没有TestRun_TrackName 这个单元格则为空，数据必须用工具界面填写的部分，否则使用工具里面的

        if isinstance(CB_Tool.TestRun_TrackerName,str):
            self.__ui.LE_TestRun_TrackerName.setText(CB_Tool.TestRun_TrackerName)
        else:
            CB_Tool.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()
        if not CB_Tool.TestRun_TrackerName:
            raise Exception("TestRun_TrackerName can't be empty")

    ########################Test Run ################################

    @pyqtSlot()
    def on_BT_PTC_Spec_clicked(self):
        self.__ui.LE_PTC_Spec.clear()
        file,filetype = QFileDialog.getOpenFileName(self,
                                          "Please the PTC Test Spec ",
                                          CB_Tool.CurrentPath,
                                          "Excel(*.xlsx *.xlsm)")  # 起始路径

        self.__ui.LE_PTC_Spec.setText(file)
        CB_Tool.PTC_Spec = file
        print(CB_Tool.PTC_Spec)
        CB_Tool.CB_Spec_ExportPath = os.path.dirname(CB_Tool.PTC_Spec)
        CB_Tool.CurrentPath = os.path.abspath(file) if os.path.isdir(file) else os.path.dirname(file)

    @pyqtSlot()
    def on_BT_PTC_Result_clicked(self):
        self.__ui.LE_PTC_Result.clear()
        file,filetype = QFileDialog.getOpenFileName(self,
                                          "Please the PTC Test Result ",
                                          CB_Tool.CurrentPath,
                                          "Excel(*.xlsx *.xlsm)")  # 起始路径

        self.__ui.LE_PTC_Result.setText(file)
        CB_Tool.PTC_Result = file
        CB_Tool.CurrentPath = os.path.abspath(file) if os.path.isdir(file) else os.path.dirname(file)

    @pyqtSlot()
    def on_BT_Init_Upload_TestRun_clicked(self):
        ### 后期加函数处理
        self.set_status_result(False)
        try:
            Df_Result  = ReadResult_TableOfContent(
                CB_Tool.PTC_Result,CB_Tool)

            # if cls.CaseTrackerID or cls.CB_Spec_Folder_ID or cls.Release:
            #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")

            # print(cls.TestRun_TrackerName)
            self.check_testrun_trackername()
            self.__ui.LE_CaseTrackerID.setText(CB_Tool.CaseTrackerID)
            self.__ui.LE_CB_Spec_Folder_ID.setText(CB_Tool.CaseFolderID)
            self.__ui.LE_Release.setText(CB_Tool.Release)


            args = {
                "Test_Run_Folder": CB_Tool.CurrentPath,
                "Df_Result": Df_Result,

            }
            CB_Tool.TestRun_Report, CB_Tool.TestRun_Status,CB_Tool.TestRun_Result = CB_Tool.CreateTestRun_UpdateResult(**args)
            self.__ui.LE_TestRun_Report.setText(CB_Tool.TestRun_Report)
            self.__ui.LE_TestRun_ID.setText(CB_Tool.TestRun_ID)
            self.__ui.TestRun_Status.setText(CB_Tool.TestRun_Status)
            self.__ui.TestRun_Result.setText(CB_Tool.TestRun_Result)
            #根据结果设置颜色
            self.set_status_result(True)
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot(str)
    def on_LE_TestRun_TrackerName_textChanged(self):
        if self.__ui.LE_TestRun_TrackerName.text():
            CB_Tool.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()


    @pyqtSlot(str)
    def on_LE_WorkingSet_textChanged(self):
        CB_Tool.WorkingSet = self.__ui.LE_WorkingSet.text()



    @pyqtSlot(str)
    def on_LE_TestRun_ID_textChanged(self):
        if self.__ui.LE_TestRun_ID.text():
            CB_Tool.TestRun_ID = self.__ui.LE_TestRun_ID.text()
            print(CB_Tool.TestRun_ID)
            CB_Tool.TestRun_Link = CB_Tool.TestRun_Url_Prefix + CB_Tool.TestRun_ID
            url = u'<a href=' + CB_Tool.TestRun_Link + u'>' + u'<b>' + "Test Run" u'</b></a>'
            self.__ui.Label_TestRun_Url.setOpenExternalLinks(True)
            self.__ui.Label_TestRun_Url.setText(url)

    #
    # @pyqtSlot()
    # def on_BT_SelectTestRunReport_clicked(cls):
    #     file,filetype = QFileDialog.getOpenFileName(cls,
    #                                       "Please the PTC Test Result ",
    #                                       cls.CurrentPath,
    #                                       "Excel(*.xlsx *.xlsm)")  # 起始路径
    #     cls.__ui.LE_TestRun_Report.setText(file)
    #     cls.TestRun_Report = file
    #     cls.CurrentPath = os.path.abspath(file) if os.path.isdir(file) else os.path.dirname(file)

    def Debug(self):
        # cls.CaseTrackerID = "10574131"
        # cls.CaseFolderID = "15704840"
        # cls.Release = "CHERY_T26&M1E_Release P10"
        # cls.TestRun_TrackerName = "TR_SHR_TestRuns"
        pass

    @pyqtSlot()
    def on_BT_Restart_TestRun_clicked(self):
        self.set_status_result(False)
        try:
            Df_Result = ReadResult_TableOfContent(
                CB_Tool.PTC_Result,CB_Tool)

            # if cls.CaseTrackerID or cls.CB_Spec_Folder_ID or cls.Release:
            #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")
            self.Debug()
            self.__ui.LE_CaseTrackerID.setText(CB_Tool.CaseTrackerID)
            self.__ui.LE_CB_Spec_Folder_ID.setText(CB_Tool.CaseFolderID)
            self.__ui.LE_Release.setText(CB_Tool.Release)
            #为了 让旧模板的人通过填写TestRun的方式，而不是在Excel里填写
            self.check_testrun_trackername()
            args = {
                "Test_Run_Folder": CB_Tool.CurrentPath,
                "Df_Result": Df_Result,
            }

            CB_Tool.TestRun_Report, CB_Tool.TestRun_Status, CB_Tool.TestRun_Result = CB_Tool.Restart_TestRun( **args)
            self.__ui.LE_TestRun_Report.setText(CB_Tool.TestRun_Report)
            self.__ui.LE_TestRun_ID.setText(CB_Tool.TestRun_ID)
            self.__ui.TestRun_Status.setText(CB_Tool.TestRun_Status)
            self.__ui.TestRun_Result.setText(CB_Tool.TestRun_Result)

            # 根据结果设置颜色
            self.set_status_result(True)
        except Exception as err:
            self.WarningMessage(err)


    @pyqtSlot()
    def on_BT_PTC_Results_clicked(self):
        CB_Tool.PTC_Result_List = []
        self.__ui.textBrowser_TestResults.clear()
        Files, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Select Test Result files",
                                                           CB_Tool.CurrentPath,
                                                           "Excel(*.xlsm *.xlsx)")
        # print(FileNames)
        for file in Files:
            self.__ui.textBrowser_TestResults.append(file)
            CB_Tool.PTC_Result_List = Files[:]
        if Files:
            CB_Tool.CurrentPath =  os.path.abspath(Files[0]) if os.path.isdir(Files[0]) else os.path.dirname(Files[0])

    @pyqtSlot()
    def on_BT_Init_Upload_TestRuns_clicked(self):
        for ptc_result in CB_Tool.PTC_Result_List:
            try:
                Df_Result = ReadResult_TableOfContent(
                    ptc_result,CB_Tool)

                # if cls.CaseTrackerID or cls.CB_Spec_Folder_ID or cls.Release:
                #     raise Exception("CaseTrackerID or CB_Spec_Folder_ID or Release can't be empty")
                self.check_testrun_trackername()
                args = {
                    "Test_Run_Folder": CB_Tool.CurrentPath,
                    "Df_Result": Df_Result,

                }
                CB_Tool.TestRun_Report, CB_Tool.TestRun_Status, CB_Tool.TestRun_Result = CB_Tool.CreateTestRun_UpdateResult(
                    **args)
                print("### Upload" + ptc_result + " to test run,TestRun_Status:" + CB_Tool.TestRun_Status + "TestRun_Result: " + CB_Tool.TestRun_Result)
                # cls.__ui.LE_TestRun_Report.setText(cls.TestRun_Report)
                # cls.__ui.LE_TestRun_ID.setText(cls.TestRun_ID)
                # cls.__ui.TestRun_Status.setText(cls.TestRun_Status)
                # cls.__ui.TestRun_Result.setText(cls.TestRun_Result)
                # 根据结果设置颜色
                # cls.set_status_result(True)
            except Exception as err:
                self.WarningMessage(err)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    baseWidget = CB_Tool_Widget()
    baseWidget.show()
    sys.exit(app.exec_())
