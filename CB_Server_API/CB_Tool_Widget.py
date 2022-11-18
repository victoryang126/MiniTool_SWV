import sys

import os
import pandas as pd
import win32com

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSlot,Qt,QThread,pyqtSignal,QObject
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPalette
from CB_Server_API.Ui_CB_Tool import  Ui_CBTool
from CB_Server_API.TestSpec_Widget import TestSpec_Widget
from CB_Server_API.CodeBeamer_Swagger import *

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

def bind(objectName,propertyName):
    """
    数据绑定函数，例如，将Line_edit的text属性和对象属性绑定起来，任何一个变化，都能传递过去
    Args:
        objectName: ui object的对象名称
        propertyName: ui object 的对象属性

    Returns:

    """
    def getter(self):
        # print("getter")
        # try:
        #     func = self.findChild(QObject,objectName).property(propertyName)
        # except Exception as err:
        #     print(err)
        return self.findChild(QObject,objectName).property(propertyName)

    def setter(self,value):
        # print(dir(self.findChild(QObject, objectName)))
        # print("setter")
        # try:
        #     func = self.findChild(QObject, objectName).setProperty(propertyName,value)
        # except Exception as err:
        #     print(err)
        #     # a = self.findChild(QObject, objectName).setProperty(value)
        return self.findChild(QObject, objectName).setProperty(propertyName,value)

    return property(getter,setter)

class CB_Tool_Widget(QWidget):
    ptc_excel = bind("LE_PTC_Excel", "text")
    testcase_trackerid = bind("LE_TestCaseTrackerID", "text")
    testrun_trackerid = bind("LE_TestRunTrackerID", "text")
    testcase_folderid = bind("LE_TestCase_FolderID", "text")
    release = bind("LE_Release", "text")
    testrunid = bind("LE_TestRunID", "text")
    testrun_status = ""
    testrun_result = ""
    currentpath = os.getcwd()
    test_information = ""
    aau = ""
    __server = bind("LE_Server","text")
    user = bind("LE_User","text")
    pwd = bind("LE_Pwd","text")
    ptc_excels =  [] #bind("textBrowser_PTC_Excels","plainText") #plainText

    #下面是API的介绍
    server_api_link = "https://codebeamer.corp.int/cb/v3/swagger/editor.spr#/Traceability"

    def __init__(self):
        super().__init__()
        self.__ui = Ui_CBTool()
        self.__ui.setupUi(self)
        self.server = CodeBeamer(self.__server,"UserName","Password")
        # self.server = CodeBeamer(self.__server, "victor.yang", "Mate40@VY20082021")

        ##########定义相关属性########################


    def exract_value(self,excel_info):

        self.test_information =  excel_info["test_information"]
        self.testrun_trackerid =  excel_info["testrun_trackerid"]
        self.testcase_trackerid = excel_info["testcase_trackerid"]
        self.testcase_folderid =  excel_info["testcase_folderid"]
        self.release =  excel_info["release"]
        self.aau = excel_info["AAU"]
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

            if self.testrun_result == "PASSED":
                self.__ui.TestRun_Result.setPalette(GreenCOlor)
            else:
                self.__ui.TestRun_Result.setPalette(RedColor)

            if self.testrun_status == "FINISHED":
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
    # def check_testrun_trackername(self):
    #     # print(cls.TestRun_TrackerName == np.nan,cls.TestRun_TrackerName)
    #     print("test")
    #     if isinstance(self.testrun_trackerid,str):
    #         self.__ui.LE_TestRunTrackerID.setText(self.testrun_trackerid)
    #     else:
    #         CB_Tool.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()
    #     if not self.TestRun_TrackerName:
    #         raise Exception("TestRun_TrackerName can't be empty")

    ########################Test Run ################################


    def upload_testcase(self,ptc_excel):
        df_ptc, excel_info = read_table_of_content(ptc_excel)
        testcase_dict_list = self.server.get_testcase_infolder(excel_info["testcase_folderid"])
        release_dict = self.server.get_release(excel_info["testcase_trackerid"], excel_info["release"])
        df_cbcase = generate_cb_case(df_ptc, testcase_dict_list)
        self.exract_value(excel_info)
        args = {
            "df_cbcase": df_cbcase,
            "testcase_trackerid": self.testcase_trackerid,
            "testcase_folderid": self.testcase_folderid,
            "release_dict": release_dict
        }
        self.server.upload_testcases(**args)

    def upload_testrun(self,ptc_excel):
        df_ptc, excel_info = read_table_of_content(ptc_excel)
        testcase_dict_list = self.server.get_testcase_infolder(excel_info["testcase_folderid"])
        release_dict = self.server.get_release(excel_info["testcase_trackerid"], excel_info["release"])
        df_cbcase = generate_cb_case(df_ptc, testcase_dict_list)
        self.exract_value(excel_info)
        args = {
            "df_cbcase": df_cbcase, "testrun_trackerid": self.testrun_trackerid, "name": self.aau,
            "test_information": self.test_information, "release_dict": release_dict
        }
        self.testrunid = self.server.create_test_run_baseon_testcases(**args)
        self.server.update_test_run_result(df_cbcase, self.testrunid)


    def set_upload_results(self,err):
        self.__ui.textBrowser_UploadResults.append(err)

    def clear_upload_results(self):
        self.__ui.textBrowser_UploadResults.clear()

    @pyqtSlot()
    def on_checkBox_Lock_clicked(self):
        #将LE_Server的属性设置是否只读，默认是只读的
        print(self.__ui.checkBox_Lock.isChecked())
        if self.__ui.checkBox_Lock.isChecked():
            self.__ui.LE_Server.setReadOnly(True)
        else:
            self.__ui.LE_Server.setReadOnly(False)


    @pyqtSlot()
    def on_BT_Login_clicked(self):
        try:
            self.server.update_codebeamer(self.__server,self.user,self.pwd)
            self.DoneMessage("Login Done")
        except Exception as err:
            print(err)

    @pyqtSlot()
    def on_BT_PTC_Excel_clicked(self):
        self.__ui.LE_PTC_Excel.clear()
        file,filetype = QFileDialog.getOpenFileName(self,
                                          "Please the excel file(spec or result) in PTC ",
                                          self.currentpath,
                                          "Excel(*.xlsx *.xlsm)")  # 起始路径

        self.ptc_excel = file

    @pyqtSlot()
    def on_BT_Upload_TestCase_clicked(self):

        try:
            self.upload_testcase(self.ptc_excel)
            # df_ptc, excel_info = read_table_of_content(self.ptc_excel)
            # testcase_dict_list = self.server.get_testcase_infolder(excel_info["testcase_folderid"])
            # release_dict = self.server.get_release(excel_info["testcase_trackerid"], excel_info["release"])
            # df_cbcase = generate_cb_case(df_ptc, testcase_dict_list)
            # print(1)
            # self.exract_value(excel_info)
            # print(2)
            # args = {
            #     "df_cbcase":df_cbcase,
            #     "testcase_trackerid":self.testcase_trackerid,
            #     "testcase_folderid":self.testcase_folderid,
            #     "release_dict":release_dict
            # }
            # self.server.upload_testcases(**args)
            self.DoneMessage("Upload_TestCase Done")
        except Exception as err:
            self.WarningMessage(err)




    @pyqtSlot()
    def on_BT_Init_Upload_TestRun_clicked(self):
        ### 后期加函数处理

        # self.set_status_result(False)
        try:
            self.upload_testrun(self.ptc_excel)
            # df_ptc, excel_info = read_table_of_content(self.ptc_excel)
            # testcase_dict_list = self.server.get_testcase_infolder(excel_info["testcase_folderid"])
            # release_dict = self.server.get_release(excel_info["testcase_trackerid"], excel_info["release"])
            # df_cbcase = generate_cb_case(df_ptc, testcase_dict_list)
            # self.exract_value(excel_info)
            # args = {
            #     "df_cbcase":df_cbcase, "testrun_trackerid":self.testrun_trackerid, "name":self.aau, "test_information":self.test_information, "release_dict":release_dict
            # }
            # self.testrunid = self.server.create_test_run_baseon_testcases(**args)
            # self.server.update_test_run_result(df_cbcase,self.testrunid)
            self.DoneMessage("Init_Upload_TestRun Done")
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_Restart_TestRun_clicked(self):
        ### 后期加函数处理

        # self.set_status_result(False)
        try:
            df_ptc, excel_info = read_table_of_content(self.ptc_excel)
            testcase_dict_list = self.server.get_testcase_infolder(excel_info["testcase_folderid"])
            df_cbcase = generate_cb_case(df_ptc, testcase_dict_list)
            print(2)
            self.exract_value(excel_info)
            print(1)
            self.server.update_test_run_result(df_cbcase, self.testrunid)
            self.DoneMessage("Restart_TestRun Done")
        except Exception as err:
            self.WarningMessage(err)

    #
    # @pyqtSlot(str)
    # def on_LE_TestRun_TrackerName_textChanged(self):
    #     if self.__ui.LE_TestRun_TrackerName.text():
    #         CB_Tool.TestRun_TrackerName = self.__ui.LE_TestRun_TrackerName.text()
    #
    #
    # @pyqtSlot(str)
    # def on_LE_WorkingSet_textChanged(self):
    #     CB_Tool.WorkingSet = self.__ui.LE_WorkingSet.text()



    @pyqtSlot(str)
    def on_LE_TestRunID_textChanged(self):
        if self.__ui.LE_TestRunID.text():
            TestRun_Link = f"https://codebeamer.corp.int/cb/issue/{self.testrunid}"
            url = u'<a href=' + TestRun_Link + u'>' + u'<b>' + "Test Run" u'</b></a>'
            self.__ui.Label_TestRun_Url.setOpenExternalLinks(True)
            self.__ui.Label_TestRun_Url.setText(url)


    @pyqtSlot()
    def on_BT_PTC_Excels_clicked(self):
        self.__ui.textBrowser_PTC_Excels.clear()
        self.ptc_excels = []
        filenames, filetype = QFileDialog.getOpenFileNames(self,
                                                           "Please select the excels (spec or result)",
                                                           self.currentpath,
                                                            "Excel(*.xlsx *.xlsm)")
        # self.ptc_excels = filenames
        for file in filenames:
            self.__ui.textBrowser_PTC_Excels.append(file + ";")
            self.ptc_excels.append(file)
        print(self.ptc_excels)

    @pyqtSlot()
    def on_BT_Upload_TestCases_clicked(self):
        self.clear_upload_results()
        for ptc_excel in self.ptc_excels:
            try:
                self.upload_testcase(ptc_excel)
            except Exception as err:
                self.set_upload_results(f"upload testcase for {ptc_excel} failed" )
        self.DoneMessage("Upload_TestCases Done")

    @pyqtSlot()
    def on_BT_Upload_TestRuns_clicked(self):
        self.clear_upload_results()
        for ptc_excel in self.ptc_excels:
            try:
                self.upload_testrun(ptc_excel)
            except Exception as err:
                self.set_upload_results(f"upload testrun for {ptc_excel} failed" )
        self.DoneMessage("Upload_TestRuns Done")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    baseWidget = CB_Tool_Widget()
    baseWidget.show()
    sys.exit(app.exec_())
