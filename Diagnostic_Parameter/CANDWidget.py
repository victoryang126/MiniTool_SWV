import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import re

# import ComFun
import json

from Diagnostic_Parameter.Ui_CAND import Ui_CAND
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog
from PyQt5.QtCore import  pyqtSlot

# from Module import *
# this function is used to fix the hex format in excel:
# eg: changed "0102" to "0x01 0x02"
# throw exception is len is not even number
def FixHexFormat(HexStr,ObjectType):
    pattern = re.compile(r"0x|\s",re.I)

    HexPattern = re.compile(r"[^0-9a-fA-F]")
    returnvalue = re.sub(pattern,"",HexStr)
    # print(returnvalue)
    if len(returnvalue)%2 != 0:  # check if the length is OK
        raise Exception("the length of " +  HexStr + "in " + ObjectType + " is not correct ")
        return
    elif re.findall(HexPattern,returnvalue): # check if there is any str is not hex value
        raise Exception( HexStr + "in " + ObjectType + " contains unexpect str(not hex value)")
        return
    else:
        returnList= ["0x" + returnvalue[i:i+2] for i,value in enumerate(returnvalue) if i%2==0]
        # print(returnList)
        returnvalue = " ".join(returnList)
        # print(returnvalue)
        return returnvalue

def Table2Dict(ExcelDir,ObjectType,output):
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str);
    df.fillna("undefined", inplace=True)
    # print(df)
    key = df.columns[0]
    df[key] = df[key].apply(FixHexFormat,ObjectType = ObjectType)
    df.set_index(key, inplace=True)
    # print(df)
    ObjectDict = df.to_dict(orient="index")
    # print(ObjectDict)
    TempStr = "var BB_" + ObjectType + "_" + key +  " = " + str(list(df.index))
    TempStr2 = "var BB_" + ObjectType + "_" + key +  "_Dict = "
    # ComFun.InilizeFile(TsName)
    # ComFun.AddObject2Ts(TsName, TempStr)
    # ComFun.AddObject2Ts(TsName, TempStr2)
    with open(output, 'a', encoding='UTF-8') as f:
        f.write(TempStr)
        f.write(";\n")
        f.write(TempStr2)
        json.dump(ObjectDict, f, indent=4)
        f.write(";\n")

def Table2List(ExcelDir,ObjectType,output):
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str);
    df.fillna("undefined", inplace=True)
    # print(df)
    key = df.columns[0]
    df[key] = df[key].apply(FixHexFormat,ObjectType = ObjectType)
    # df.set_index(key, inplace=True)
    # print(df)
    # ObjectDict = df.to_dict(orient="index")
    # print(ObjectDict)
    DTCList = list(df[key])
    TempStr = "var BB_" + ObjectType + "_" + key +  " = " + str(DTCList)

    # ComFun.InilizeFile(TsName)
    # ComFun.AddObject2Ts(TsName, TempStr)
    # ComFun.AddObject2Ts(TsName, TempStr2)
    with open(output, 'a', encoding='UTF-8') as f:
        f.write(TempStr)
        f.write(";\n")
    with open("DTCList.txt", 'w', encoding='UTF-8') as f:
        f.writelines([i+"\n" for i in DTCList])



class CANDWidget(QWidget):

    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_CAND()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面




        # *****************定义 相关属性****************************************
        self.CANDConfig = ""
        self.Output = "BB_CAND_Parameter_Object.ts"
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

    #1 设置BT_GenS37_Ascent
    @pyqtSlot()
    def on_BT_CANDConfig_clicked(self):

        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an the CAND Config file ",
                                                         self.CurrentPath,
                                                         "Excel (*.xlsx *.xlsm)")
        self.__ui.LE_CANDConfig.setText(FileName)
        self.CANDConfig = self.__ui.LE_CANDConfig.text()
        # print(cls.CANDConfig)
    def on_checkB_All_stateChanged(self):
        if self.__ui.checkB_All.isChecked():
            state = True
            self.__ui.checkB_TP.setChecked(state)
            self.__ui.checkB_SID10.setChecked(state)
            self.__ui.checkB_SID11.setChecked(state)
            self.__ui.checkB_SID14.setChecked(state)
            self.__ui.checkB_SID19.setChecked(state)
            self.__ui.checkB_SID22.setChecked(state)
            self.__ui.checkB_SID23.setChecked(state)
            self.__ui.checkB_SID27.setChecked(state)
            self.__ui.checkB_SID28.setChecked(state)
            self.__ui.checkB_SID2E.setChecked(state)
            self.__ui.checkB_SID2F.setChecked(state)
            self.__ui.checkB_SID31.setChecked(state)
            self.__ui.checkB_SID3E.setChecked(state)
            self.__ui.checkB_SID85.setChecked(state)
            self.__ui.checkB_DTC.setChecked(state)
        else:
            state = False
            self.__ui.checkB_TP.setChecked(state)
            self.__ui.checkB_SID10.setChecked(state)
            self.__ui.checkB_SID11.setChecked(state)
            self.__ui.checkB_SID14.setChecked(state)
            self.__ui.checkB_SID19.setChecked(state)
            self.__ui.checkB_SID22.setChecked(state)
            self.__ui.checkB_SID23.setChecked(state)
            self.__ui.checkB_SID27.setChecked(state)
            self.__ui.checkB_SID28.setChecked(state)
            self.__ui.checkB_SID2E.setChecked(state)
            self.__ui.checkB_SID2F.setChecked(state)
            self.__ui.checkB_SID31.setChecked(state)
            self.__ui.checkB_SID3E.setChecked(state)
            self.__ui.checkB_SID85.setChecked(state)
            self.__ui.checkB_DTC.setChecked(state)


    @pyqtSlot()
    def on_BT_Generate_clicked(self):
        f = open(self.Output, 'w', encoding='UTF-8')
        f.close()
        try:
            if self.__ui.checkB_TP.isChecked():
                args = {"ExcelDir":self.CANDConfig,"ObjectType":"TP","output":self.Output}
                Table2Dict(**args)
                # Table2Dict(ExcelDir, ObjectType, output)
            if self.__ui.checkB_SID10.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID10", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID11.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID11", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID14.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID14", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID19.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID19", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID22.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID22", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID23.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID23", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID27.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID27", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID28.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID28", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID2E.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID2E", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID2F.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID2F", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID31.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID31", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID3E.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID3E", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_SID85.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "SID85", "output": self.Output}
                Table2Dict(**args)
            if self.__ui.checkB_DTC.isChecked():
                args = {"ExcelDir": self.CANDConfig, "ObjectType": "DTC", "output": self.Output}
                Table2List(**args)

            self.DoneMessage("Generate BB_CAND_Parameter_Object successfully")
        except Exception as err:
            self.WarningMessage(str(err))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = CANDWidget()

    baseWidget.show()
    sys.exit(app.exec_())
    # ExcelDir = "C:\Python\MiniTool\DataSource\CAND.xlsm"
    # ObjectType = "SID10"
    # output = "C:\Python\MiniTool\OutPut" + "\\BB_CAND_Parameter_Object.ts"
    # Table2Dict(ExcelDir, ObjectType, output)
    # Table2List(ExcelDir, ObjectType, output)
    # FixHexFormat("010x02  90", ObjectType)