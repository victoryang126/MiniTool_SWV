import sys
import os


from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings
from CommonFunction import CommonFun
from Regression import DBC
from Regression import AriaCard
from Regression import IMU
from Regression import OtherFault
from Regression import Crash
from Regression import CrashOutput
from Regression import Msg
from Regression.Ui_Regression import Ui_Regression



class RegressionWidget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_Regression()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        # self.stack.addWidget(self.stack1)


        #*****************定义 Regression相关属性****************************************
        self.Config = ""
        self.Project = ""
        self.Reg_Excel = ""
        self.Reg_DBC = ""
        self.Reg_TemplateFolder = self.CurrentPath + "\\Template"
        self.Reg_ScriptOutput = self.CurrentPath + "\\Scripts"
        self.Reg_CrashOutputPath = self.CurrentPath + "\\CrashData"
        self.Reg_IMUOutputPath = self.CurrentPath + "\\IMUData"
        self.Reg_RegressionObject = self.CurrentPath + "\\Reg_RegressionObject.ts"
        self.Reg_RegressionParameter = self.CurrentPath + "\\Reg_RegressionParameter.ts"

        self.Reg_Loop_FaultTemplate = self.Reg_TemplateFolder + "\\Loop_FaultCheck.ts"
        self.Reg_RSU_FaultTemplate = self.Reg_TemplateFolder + "\\RSU_FaultCheck.ts"
        self.Reg_DCS_FaultTemplate = self.Reg_TemplateFolder + "\\DCS_FaultCheck.ts"
        self.Reg_DCS_NormalTemplate = self.Reg_TemplateFolder + "\\DCS_NormalCheck.ts"
        self.Reg_Communication_Template = self.Reg_TemplateFolder + "\\Communication_FaultCheck.ts"
        self.Reg_Crash_Template = self.Reg_TemplateFolder + "\\Crash_Check.ts"
        self.Reg_IMU_Template = self.Reg_TemplateFolder + "\\IMU_DataCheck.ts"
        self.Reg_Lamps_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"
        self.Reg_ENS_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"


        # *****************设置Regression LineEdit默认值****************************************
        if os.path.exists('./ini/RegressionWidget.ini'):
            self.Config = QSettings('./ini/RegressionWidget.ini', QSettings.IniFormat)
            self.LoadConfig()
            self.Reg_Loop_FaultTemplate = self.Reg_TemplateFolder + "\\Loop_FaultCheck.ts"
            self.Reg_RSU_FaultTemplate = self.Reg_TemplateFolder + "\\RSU_FaultCheck.ts"
            self.Reg_DCS_FaultTemplate = self.Reg_TemplateFolder + "\\DCS_FaultCheck.ts"
            self.Reg_DCS_NormalTemplate = self.Reg_TemplateFolder + "\\DCS_NormalCheck.ts"
            self.Reg_Communication_Template = self.Reg_TemplateFolder + "\\Communication_FaultCheck.ts"
            self.Reg_Crash_Template = self.Reg_TemplateFolder + "\\Crash_Check.ts"
            self.Reg_IMU_Template = self.Reg_TemplateFolder + "\\IMU_DataCheck.ts"
            self.Reg_Lamps_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"
            self.Reg_ENS_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"
        else:
            self.__ui.LE_Reg_ScriptTemplate.setText(self.Reg_TemplateFolder)
            self.__ui.LE_Reg_ScirptOutput.setText(self.Reg_ScriptOutput)
            self.__ui.LE_Reg_CrashOutputPath.setText(self.Reg_CrashOutputPath)
            self.__ui.LE_Reg_IMUOutputPath.setText(self.Reg_IMUOutputPath)


    # 定义错误提示框
    def WarningMessage(self,str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self,DigTitle,StrInfo)

    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)

    # 根据INI 文件导入配置信息
    def LoadConfig(self):
        self.Project = self.Config.value("CONFIG/Project")
        self.Reg_DBC = self.Config.value("CONFIG/Reg_DBC")
        self.Reg_Excel = self.Config.value("CONFIG/Reg_Excel")
        self.Reg_TemplateFolder = self.Config.value("CONFIG/Reg_TemplateFolder")
        self.Reg_ScriptOutput = self.Config.value("CONFIG/Reg_ScriptOutput")
        self.Reg_CrashOutputPath = self.Config.value("CONFIG/Reg_CrashOutputPath")
        self.Reg_IMUOutputPath = self.Config.value("CONFIG/Reg_IMUOutputPath")

        self.__ui.LE_Reg_Project.setText(self.Project)
        self.__ui.LE_Reg_DBC.setText(self.Reg_DBC)
        self.__ui.LE_Reg_Excel.setText(self.Reg_Excel)
        self.__ui.LE_Reg_ScriptTemplate.setText(self.Reg_TemplateFolder)
        self.__ui.LE_Reg_ScirptOutput.setText(self.Reg_CrashOutputPath)
        self.__ui.LE_Reg_CrashOutputPath.setText(self.Reg_CrashOutputPath)
        self.__ui.LE_Reg_IMUOutputPath.setText(self.Reg_IMUOutputPath)

    # 保存配置信息到INI文件中
    def SaveConfig(self):
        self.Config = QSettings('./ini/RegressionWidget.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8
        self.Config.setValue("CONFIG/Project",self.Project)
        self.Config.setValue("CONFIG/Reg_DBC", self.Reg_DBC)
        self.Config.setValue("CONFIG/Reg_Excel", self.Reg_Excel)
        self.Config.setValue("CONFIG/Reg_TemplateFolder", self.Reg_TemplateFolder)
        self.Config.setValue("CONFIG/Reg_ScriptOutput", self.Reg_ScriptOutput)
        self.Config.setValue("CONFIG/Reg_CrashOutputPath", self.Reg_CrashOutputPath)
        self.Config.setValue("CONFIG/Reg_IMUOutputPath", self.Reg_IMUOutputPath)

    # *****************Rergrssion定义槽函数****************************************

    #1 .定义BT_Excel
    @pyqtSlot()
    def on_BT_Reg_Excel_clicked(self):

        self.__ui.LE_Reg_Excel.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an excel file ",
                                                         self.CurrentPath,
                                                         "Reg_Excel(*.xlsx *.xlsm)")
        self.__ui.LE_Reg_Excel.setText(FileName)
        self.Reg_Excel = self.__ui.LE_Reg_Excel.text()
        path = self.Reg_Excel
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 定义LE_Reg_Project
    @pyqtSlot(str)
    def on_LE_Reg_Project_textChanged(self,str):
        self.Project = self.__ui.LE_Reg_Project.text()
        # print(self.Project)

    #设置BT_DBC
    @pyqtSlot()
    def on_BT_Reg_DBC_clicked(self):
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an dbc file to import message",
                                                         self.CurrentPath,
                                                         "Reg_DBC(*.dbc)")
        self.__ui.LE_Reg_DBC.setText(FileName)
        self.Reg_DBC = self.__ui.LE_Reg_DBC.text()
        path = self.Reg_DBC
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #设置BT_ImportMsg
    @pyqtSlot()
    def on_BT_Reg_ImportMsg_clicked(self):
        if os.path.splitext(self.Reg_Excel)[1] == ".xlsm":
            self.WarningMessage("Can't use xlsm file to import data,This will definitely damage your files")
            return
        try:
            DBC.ImportDataIntoExcel(self.Reg_DBC, self.Reg_Excel)
            self.DoneMessage("Import Msg to Reg_Excel successfully")
        except Exception as err:
            self.WarningMessage(str(err))


    #4 设置 BT_Reg_ScriptTemplate
    @pyqtSlot()
    def on_BT_Reg_ScriptTemplate_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder where template stored",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_Reg_ScriptTemplate.setText(FolderName)
        self.Reg_TemplateFolder = self.__ui.LE_Reg_ScriptTemplate.text()
        self.Reg_Loop_FaultTemplate = self.Reg_TemplateFolder + "\\Loop_FaultCheck.ts"
        self.Reg_RSU_FaultTemplate = self.Reg_TemplateFolder + "\\RSU_FaultCheck.ts"
        self.Reg_DCS_NormalTemplate = self.Reg_TemplateFolder + "\\DCS_NormalCheck.ts"
        self.Reg_DCS_FaultTemplate = self.Reg_TemplateFolder + "\\DCS_FaultCheck.ts"
        self.Reg_Communication_Template = self.Reg_TemplateFolder + "\\Communication_FaultCheck.ts"
        self.Reg_Crash_Template = self.Reg_TemplateFolder + "\\Crash_Check.ts"
        self.Reg_IMU_Template = self.Reg_TemplateFolder + "\\IMU_DataCheck.ts"
        self.Reg_Lamps_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"
        self.Reg_ENS_FaultTemplate = self.Reg_TemplateFolder + "\\GPO_FaultCheck.ts"
        path = FolderName
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 4 设置BT_Iitialize
    @pyqtSlot()
    def on_BT_Reg_Iitialize_clicked(self):
        CommonFun.CreateFolder_IfNotExist(self.Reg_ScriptOutput)
        CommonFun.CreateFolder_IfNotExist(self.Reg_CrashOutputPath)
        CommonFun.CreateFolder_IfNotExist(self.Reg_IMUOutputPath)
        CommonFun.InilizeFile(self.Reg_RegressionObject)
        CommonFun.InilizeFile(self.Reg_RegressionParameter)

    #5. 设置 BT_ScriptOutput
    @pyqtSlot()
    def on_BT_Reg_ScriptOutput_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder to save scripts",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_Reg_ScirptOutput.setText(FolderName)
        self.Reg_ScriptOutput = self.__ui.LE_Reg_ScirptOutput.text()
        path = self.Reg_ScriptOutput
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 6. 设置 BT_CrashOutput
    @pyqtSlot()
    def on_BT_Reg_CrashOutputPath_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder to save Crashdata",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_Reg_CrashOutputPath.setText(FolderName)
        self.Reg_CrashOutputPath = self.__ui.LE_Reg_CrashOutputPath.text()
        path = self.Reg_CrashOutputPath
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 7. 设置 BT_IMUOutput
    @pyqtSlot()
    def on_BT_Reg_IMUOutputPath_clicked(self):
        # print(self.Reg_IMUOutput)
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please select a folder to save IMUdata",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_Reg_IMUOutputPath.setText(FolderName)
        self.Reg_IMUOutputPath = self.__ui.LE_Reg_IMUOutputPath.text()
        path = self.Reg_IMUOutputPath
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #8. 设置BT_Loop
    @pyqtSlot()
    def on_BT_Reg_Loop_clicked(self):
        try:
            args = {"ExcelDir":self.Reg_Excel, "ObjectType": "Loop", "FaultTemplate":self.Reg_Loop_FaultTemplate
                    , "NormalTemplate":self.Reg_Loop_FaultTemplate, "G_RegParameterFile":self.Reg_RegressionParameter,
                    "G_RegObjectFile":self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)
            self.DoneMessage("Generate Scripts of Loop successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    # 9. 设置BT_RSU
    @pyqtSlot()
    def on_BT_Reg_RSU_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "RSU", "FaultTemplate": self.Reg_RSU_FaultTemplate
                , "NormalTemplate": self.Reg_RSU_FaultTemplate, "G_RegParameterFile": self.Reg_RegressionParameter,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)
            self.DoneMessage("Generate Scripts of RSU successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    # 10. 设置BT_DCS
    @pyqtSlot()
    def on_BT_Reg_DCS_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "DCS", "FaultTemplate": self.Reg_DCS_FaultTemplate
                , "NormalTemplate": self.Reg_DCS_NormalTemplate, "G_RegParameterFile": self.Reg_RegressionParameter,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)
            self.DoneMessage("Generate Scripts of DCS successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #11 设置BT_Communication
    @pyqtSlot()
    def on_BT_Reg_Communication_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "Communication", "FaultTemplate": self.Reg_Communication_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            Msg.GetMsgObject(**args)
            self.DoneMessage("Generate Scripts of Communication successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #12 设置BT_Crash
    @pyqtSlot()
    def on_BT_Reg_Crash_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "Crash", "Crash_Template": self.Reg_Crash_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "CrashDataPath":self.Reg_CrashOutputPath, "ScriptPath":self.Reg_ScriptOutput, "TestProject":self.Project}
            Crash.GetCrashObject(**args)
            self.DoneMessage("Generate Scripts of Crash successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #13 设置BT_IMU
    @pyqtSlot()
    def on_BT_Reg_IMU_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "IMU", "IMU_Template": self.Reg_IMU_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "IMUDataPath":self.Reg_IMUOutputPath, "ScriptPath":self.Reg_ScriptOutput, "TestProject":self.Project}
            IMU.GetIMUObject(**args)
            # GetIMUObject(ExcelDir, ObjectType, IMU_Template, G_RegObjectFile, IMUDataPath, ScriptPath)
            self.DoneMessage("Generate Scripts of IMU successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #14 设置BT_Lamps
    @pyqtSlot()
    def on_BT_Reg_Lamps_clicked(self):
        try:
            args = {"ExcelDir":self.Reg_Excel, "ObjectType": "Lamps", "FaultTemplate":self.Reg_Lamps_FaultTemplate
                    , "NormalTemplate":self.Reg_Lamps_FaultTemplate, "G_RegParameterFile":self.Reg_RegressionParameter,
                    "G_RegObjectFile":self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)
            self.DoneMessage("Generate Scripts of Lamps successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #15设置BT_ENS
    @pyqtSlot()
    def on_BT_Reg_ENS_clicked(self):
        try:
            args = {"ExcelDir":self.Reg_Excel, "ObjectType": "ENS", "FaultTemplate":self.Reg_ENS_FaultTemplate
                    , "NormalTemplate":self.Reg_ENS_FaultTemplate, "G_RegParameterFile":self.Reg_RegressionParameter,
                    "G_RegObjectFile":self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)
            self.DoneMessage("Generate Scripts of ENS successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #15设置BT_ENS
    @pyqtSlot()
    def on_BT_Reg_OtherFault_clicked(self):
        try:
            args = {
                "ExcelPath":self.Reg_Excel,
                "TemplateFolder":self.Reg_TemplateFolder,
                "ScriptOutputPath":self.Reg_ScriptOutput
            }
            OtherFault.GenerateOtherFaultScriptsViaExcel(**args)
            self.DoneMessage("Generate Scripts of otherFault successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #16. 设置BT_BT_GenerateAll
    @pyqtSlot()
    def on_BT_Reg_GenerateAll_clicked(self):
        # self.__ui.BT_Reg_RSU.click()
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "Loop", "FaultTemplate": self.Reg_Loop_FaultTemplate
                , "NormalTemplate": self.Reg_Loop_FaultTemplate, "G_RegParameterFile": self.Reg_RegressionParameter,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)

            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "RSU", "FaultTemplate": self.Reg_RSU_FaultTemplate
                , "NormalTemplate": self.Reg_RSU_FaultTemplate, "G_RegParameterFile": self.Reg_RegressionParameter,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)

            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "DCS", "FaultTemplate": self.Reg_DCS_FaultTemplate
                , "NormalTemplate": self.Reg_DCS_NormalTemplate, "G_RegParameterFile": self.Reg_RegressionParameter,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)

            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "Communication", "FaultTemplate": self.Reg_Communication_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            Msg.GetMsgObject(**args)

            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "Crash", "Crash_Template": self.Reg_Crash_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "CrashDataPath": self.Reg_CrashOutputPath,
                    "ScriptPath": self.Reg_ScriptOutput,"TestProject":self.Project}
            # GetCrashObject(ExcelDir, ObjectType, Crash_Template, G_RegObjectFile, CrashDataPath, ScriptPath)
            Crash.GetCrashObject(**args)

            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "IMU", "IMU_Template": self.Reg_IMU_Template,
                    "G_RegObjectFile": self.Reg_RegressionObject, "IMUDataPath": self.Reg_IMUOutputPath, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            # GetIMUObject(ExcelDir, ObjectType, IMU_Template, G_RegObjectFile, IMUDataPath, ScriptPath):
            IMU.GetIMUObject(**args)

            args = {"ExcelDir":self.Reg_Excel, "ObjectType": "Lamps", "FaultTemplate":self.Reg_Lamps_FaultTemplate
                    , "NormalTemplate":self.Reg_Lamps_FaultTemplate, "G_RegParameterFile":self.Reg_RegressionParameter,
                    "G_RegObjectFile":self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)

            args = {"ExcelDir":self.Reg_Excel, "ObjectType": "ENS", "FaultTemplate":self.Reg_ENS_FaultTemplate
                    , "NormalTemplate":self.Reg_ENS_FaultTemplate, "G_RegParameterFile":self.Reg_RegressionParameter,
                    "G_RegObjectFile":self.Reg_RegressionObject, "ScriptPath":self.Reg_ScriptOutput,"TestProject":self.Project}
            AriaCard.GetSensorObject(**args)

            args = {
                "ExcelPath":self.Reg_Excel,
                "TemplateFolder":self.Reg_TemplateFolder,
                "ScriptOutputPath":self.Reg_ScriptOutput
            }
            OtherFault.GenerateOtherFaultScriptsViaExcel(**args)


            self.DoneMessage("Generate All Scripts successfully")
            self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))


    # @pyqtSlot()
    # def on_BT_Reg_GenerateAll_clicked(self):
    #     try:
    #         pass
    #         self.__ui.BT_Reg_Loop.click()
    #         self.DoneMessage("Generate All Scripts successfully")
    #         self.SaveConfig()
    #     except Exception as err:
    #         self.WarningMessage(str(err))

    #17设置BT_CreateCurves
    @pyqtSlot()
    def on_BT_Reg_CreateCurves_clicked(self):
        try:
            args = {"ExcelDir": self.Reg_Excel, "ObjectType": "CreateCurves", "G_CrashCurves": "CrashCurves.ts",
                     "CrashDataPath":self.Reg_CrashOutputPath}
            CommonFun.InilizeFile(args["G_CrashCurves"])
            Crash.GetCrashCurvesObject(**args)
            self.DoneMessage("Create Crash Curves successfully")
        except Exception as err:
            self.WarningMessage(str(err))

    #18设置BT_SaveConfig
    @pyqtSlot()
    def on_BT_Reg_SaveConfig_clicked(self):
        self.SaveConfig()

    #19设置BT_LoadConfig
    @pyqtSlot()
    def on_BT_Reg_LoadConfig_clicked(self):
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an ini file ",
                                                         self.CurrentPath,
                                                         "ini(*.ini)")
        if FileName:
            self.Config= QSettings(FileName, QSettings.IniFormat)
            self.LoadConfig()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = RegressionWidget()
 
    baseWidget.show()
    sys.exit(app.exec_())
