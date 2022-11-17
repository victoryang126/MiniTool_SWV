from CB_Tool_SC3.CodeBeamer import CodeBeamer
import sys
import os
from CB_Tool_SC3.CodeBeamer import CodeBeamer
from CB_Tool_SC3.Ui_TestSpec import Ui_TestSpec
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
from CB_Tool_SC3.CB_Tool import CB_Tool
from CB_Tool_SC3 import HandleTestSpec as HSpec
from PyQt5.QtCore import pyqtSlot
import pandas as pd
class TestSpec_Widget(QWidget, CB_Tool):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_TestSpec()
        self.__ui.setupUi(self)

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

    def Generate_Init(self):

        print("Generate_Init : " + CB_Tool.PTC_Spec)
        Excel_Files = []
        try:
            # Df_LoopUp = CB_Tool.ReadLoopUp(cls.LookUp)

            # print(Test_Spec)ReadSpec_TableOfContent_SC3
            df_ptc_spec = HSpec.ReadSpec_TableOfContent_SC3(CB_Tool.PTC_Spec, CB_Tool)
            print(CB_Tool.CaseFolderID)
            # print(os.path.basename(Test_Spec).split("."))
            SpecCB = os.path.basename(CB_Tool.PTC_Spec).split(".")[0] + "_CodeBeamer.xlsx"


            SpecCB = os.path.join(CB_Tool.CB_Spec_ExportPath, SpecCB)
            # print(SpecCB)

            Excel_Files.append(SpecCB)

            HSpec.GenerateSpec_CB_Init(df_ptc_spec, SpecCB,CB_Tool)

            CB_Tool.FinalCBSpec = os.path.join(CB_Tool.CB_Spec_ExportPath, Excel_Files[0])

            self.__ui.LE_CB_Spec_Init.setText(CB_Tool.FinalCBSpec)
            self.__ui.LE_FinalCBSpec.setText(CB_Tool.FinalCBSpec)
            # cls.CB_Spec_Generate = cls.FinalCBSpec

            NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
            return NotOK_Files
        except Exception as err:
            self.WarningMessage(err)


    @pyqtSlot()
    def on_BT_Generate_Init_clicked(self):
        try:
            NotOK_Files = self.Generate_Init()
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate Excel successfully")
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_CB_Spec_FromCB_clicked(self):
        # pass
        self.__ui.LE_CB_Spec_FromCB.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select the test report downlaod from CB",
                                                         CB_Tool.CurrentPath,
                                                         "excel(*.xlsx)")
        self.__ui.LE_CB_Spec_FromCB.setText(FileName)
        CB_Tool.CB_Spec_FromCB = self.__ui.LE_CB_Spec_FromCB.text()
        print(CB_Tool.CB_Spec_FromCB)

    @pyqtSlot()
    def on_BT_Generate_Modify_clicked(self):
        Excel_Files = []
        try:
            df_SpecCB_FromCB, Df_ID_Case_FromCB = HSpec.ReadSpecCB_FromCB(CB_Tool.CB_Spec_FromCB)
            df_SpecCB_Generate = pd.read_excel(CB_Tool.CB_Spec_Generate, "Export")
            SpecCB_Modify = os.path.basename(CB_Tool.CB_Spec_Generate).split(".")[0] + "_Modify.xlsx"
            SpecCB_Modify = os.path.join(os.path.split(CB_Tool.CB_Spec_Generate)[0], SpecCB_Modify)

            HSpec.GenerateSpec_CB_Modify(df_SpecCB_Generate, Df_ID_Case_FromCB, df_SpecCB_FromCB, CB_Tool,
                                            SpecCB_Modify)
            Excel_Files.append(SpecCB_Modify)
            CB_Tool.FinalCBSpec = Excel_Files[0]
            self.__ui.LE_FinalCBSpec.setText(CB_Tool.FinalCBSpec)
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
                                                         CB_Tool.CurrentPath,
                                                         "excel(*.xlsx)")
        self.__ui.LE_FinalCBSpec.setText(FileName)
        CB_Tool.FinalCBSpec = self.__ui.LE_FinalCBSpec.text()
        print(CB_Tool.FinalCBSpec)



    @pyqtSlot()
    def on_BT_Upload2CB_clicked(self):
        # print(CB_Tool.CaseFolderID)
        # print(CB_Tool.CaseTrackerID)
        if not CB_Tool.CaseTrackerID or not CB_Tool.CaseFolderID:
            self.WarningMessage("CaseTrackerID or CB_Spec_Folder_ID can't be empty")
            return
        try:
            # print(cls.FinalCBSpec)

            InitCaseList = HSpec.GetInitCaseList(CB_Tool.FinalCBSpec)
            ReturnValue = CB_Tool.UploadSpec2CB(CB_Tool.FinalCBSpec, InitCaseList)
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
            NotOK_Files = self.Generate_Init()
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")

            self.__ui.BT_Upload2CB.click()
            self.DoneMessage("Please check email to check if upload successfully")
        except Exception as err:
            self.WarningMessage(err)

    @pyqtSlot()
    def on_BT_Upload2CB_Modify_clicked(self):

        Excel_Files = []
        # 先重新生成
        print("1st Generate")
        try:
            NotOK_Files = self.Generate_Init()
            if len(NotOK_Files):
                # pass
                self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
            # 然后下载
            print("2nd Download, if this file been downloaded, will not downloaded again")
            print(not CB_Tool.CB_Spec_FromCB)
            if not CB_Tool.CB_Spec_FromCB:

                CB_Tool.CB_Spec_FromCB = CB_Tool.DownLoadSpecFromCB(CB_Tool.CB_Spec_ExportPath)
                CB_Tool.CB_Spec_FromCB = os.path.join(CB_Tool.CB_Spec_ExportPath, CB_Tool.CB_Spec_FromCB)
                print(CB_Tool.CB_Spec_FromCB)
                self.__ui.LE_CB_Spec_FromCB.setText(CB_Tool.CB_Spec_FromCB)
            try:
                Excel_Files = []
                # 然后Modify
                print("3nd Modify")

                df_SpecCB_FromCB, Df_ID_Case_FromCB = HSpec.ReadSpecCB_FromCB(CB_Tool.CB_Spec_FromCB)
                df_SpecCB_Generate = pd.read_excel(CB_Tool.FinalCBSpec, "Export")
                SpecCB_Modify = os.path.basename(CB_Tool.FinalCBSpec).split(".")[0] + "_Modify.xlsx"
                SpecCB_Modify = os.path.join(os.path.split(CB_Tool.FinalCBSpec)[0], SpecCB_Modify)
                print(SpecCB_Modify)
                if CB_Tool.Release:
                    HSpec.GenerateSpec_CB_Modify(df_SpecCB_Generate, Df_ID_Case_FromCB, df_SpecCB_FromCB,
                                                    CB_Tool,
                                                    SpecCB_Modify)
                    Excel_Files.append(SpecCB_Modify)
                    CB_Tool.FinalCBSpec = Excel_Files[0]

                    print(CB_Tool.FinalCBSpec)
                    # cls.WarningMessage("T")
                    self.__ui.LE_FinalCBSpec.setText(CB_Tool.FinalCBSpec)
                    NotOK_Files = [Excel_File for Excel_File in Excel_Files if not os.path.exists(Excel_File)]
                    if len(NotOK_Files):
                        self.WarningMessage(str(NotOK_Files) + " not been generated, please check related setting")
                    else:
                        print("4th upload")
                        self.__ui.BT_Upload2CB.click()
                        self.DoneMessage("Check email to check if upload successfully")
                else:
                    self.WarningMessage("Release can't be empty")
            except Exception as err:
                self.WarningMessage(err)
        except Exception as err:
            self.WarningMessage(err)


if __name__ == '__main__':
    # CodeBeamer_Obj = CodeBeamer()
    app = QApplication(sys.argv)
    baseWidget = TestSpec_Widget()
    baseWidget.show()
    sys.exit(app.exec_())