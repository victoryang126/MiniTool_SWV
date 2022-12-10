import sys
# sys.path.append(r'C:\Python\Regression\Module')
import os
import pandas as pd
import numpy as np
import win32com
from win32com.client import Dispatch
# import xlwings as xw

from DTCDefine_SymFile.Ui_DTCDefine_SYM import Ui_DTCDefine_SYM
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QFileDialog,QLabel
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtCore import  QSettings,QThread,QMutex
import openpyxl

class Generate_Thread(QThread):
    def __init__(self,ActionFunc):
        super().__init__();
        self.ActionFunc = ActionFunc
    def run(self) -> None:
        self.ActionFunc()
        # Generate_SYM(Project, SWVersion, PBCT_Excel, EPPROM_Trans_Excel, SYM_OutPut, SheetList)


def SaveErrorDefinitionFromFltMonr_Configurator(FltMonr_Configurator,ErrorDefinition):
    """
    使用 win32com.client.DispatchEx('Excel.Application') 将从FltMonr_Configurator 生成ErrorDefinition文件
    注意，这个文件路径必须用os.path.abspath 处理，否则会报错误
    :param FltMonr_Configurator:
    :param ErrorDefinition:
    :return: NONE
    """
    ExcelAPP = win32com.client.DispatchEx('Excel.Application')
    ExcelAPP.Visible = 0
    ExcelAPP.DisplayAlerts = 0
    wb = ExcelAPP.Workbooks.Open(os.path.abspath(FltMonr_Configurator))
    for sheetObj in wb.Worksheets:
        # print(sheetObj.Name)
        if sheetObj.Name == "ACCT Autoliv Faults":
            sheetObj.Name = "Errors"
        else:
            # pass
            wb.Worksheets(sheetObj.Name).Delete()
    wb.SaveAs(os.path.abspath(ErrorDefinition))
    wb.Close(SaveChanges=0)
    ExcelAPP.Quit()


def SaveErrorDefinitionFromFltMonr_Configurator(ExcelAPP,FltMonr_Configurator,ErrorDefinition):
    """
    使用 win32com.client.DispatchEx('Excel.Application') 将从FltMonr_Configurator 生成ErrorDefinition文件
    注意，这个文件路径必须用os.path.abspath 处理，否则会报错误
    :param ExcelAPP  win32com.client.DispatchEx('Excel.Application') 生成的
    :param FltMonr_Configurator:
    :param ErrorDefinition:
    :return: NONE
    """
    wb = ExcelAPP.Workbooks.Open(os.path.abspath(FltMonr_Configurator))
    for sheetObj in wb.Worksheets:
        # print(sheetObj.Name)
        if sheetObj.Name == "ACCT Autoliv Faults":
            sheetObj.Name = "Errors"
        else:
            # pass
            wb.Worksheets(sheetObj.Name).Delete()
    wb.SaveAs(os.path.abspath(ErrorDefinition))
    wb.Close(SaveChanges=0)
    ExcelAPP.Quit()

def Xlsx2Xlsm(path):
    """
    通过openpyxl keep_vba=True的属性，读取xlsx,然后把文件保存成xlsm格式

    :param path:Excel的路径
    :return:
    """
    wb = openpyxl.load_workbook(path, keep_vba=True)
    newpath = os.path.splitext(path)[0] + ".xlsm"
    wb.save(newpath)
    wb.close()

def Str2Hex(Int_Str,ByteSize):
    """

    :param Int_Str:int 数据的字符串
    :param ByteSize:
    :return: Hex数据中的字符串
    """
    Str_Hex = str(hex(int(Int_Str)))
    Str_Hex = Str_Hex.replace("0x","").upper()
    # Str_Hex_List = [Str_Hex]
    while len(Str_Hex) < ByteSize*2:
        Str_Hex = "0" + Str_Hex
        # Str_Hex_List.insert(0,"0")
    # Str_Hex = "".join(Str_Hex_List)
    if len(Str_Hex) > ByteSize*2:
        raise Exception("ByteSize is less in function Str2Hex")
    # print(Str_Hex)
    return Str_Hex


def Generate_ErrorDefinition(ExcelAPP,Project,SWVersion,DTC_OutPut,FltMonr_Excel):
    """
    提取FltMonr_Configurator的ACCT Autoliv Faults的信息
    保存到另外一个文件中，sheet 名字为Errors ，供Aria解析内外部错误
    :param ExcelAPP  win32com.client.DispatchEx('Excel.Application') 生成的
    :param Project: 项目名称
    :param SWVersion: 软件版本
    :param DTC_OutPut: error_definition文件的保存路径
    :param FltMonr_Excel:FltMonr_Excel的Excel
    :return:
    """
    ErrorDefintion = DTC_OutPut + "/error_definition_" + Project + "_" + SWVersion + ".xlsm"
    SaveErrorDefinitionFromFltMonr_Configurator(ExcelAPP,FltMonr_Excel,ErrorDefintion)

    # # 去读ACCT Autoliv Faults参数信息
    # # *******************************************************************
    # df_VeoneerCode = pd.read_excel(FltMonr_Excel, "ACCT Autoliv Faults", dtype='str', header=0)
    # df_VeoneerCode.to_excel(ErrorDefintion,sheet_name="Errors",index= False,)
    # Xlsx2Xlsm(ErrorDefintion)
    # os.remove(ErrorDefintion)




#########FltMonr_Excel 从o行开始就没有columns
######### ACCT Autoliv Faults sheet 从第四行才开始有数据
######### Data 从第五行才开始有数据
######### 列是通过index 抓的，一旦位置变化，函数就需要变化
def Get_Df_DTCDefine(FltMonr_Excel):
    """
    提取FltMonr_Configurator的ACCT Autoliv Faults的信息 和 Data sheet的信息
    获取外部DTC ，内部Veoneer Code 和名字的列表
    :param FltMonr_Excel: 提取FltMonr_Configurator的ACCT的Excel
    :return:DTCDefine_List "VeonnerCodeName","DTCRecord","VeoneerCode_Dec","VeoneerCode_Hex","WL","Permanent_Latched","Latched_KeyCycle"的列表
    """
    # 去读ACCT Autoliv Faults参数信息
    print("$$$$$$$$$$$$$$$$$$$$$$Get_Df_DTCDefine")
    # *******************************************************************
    df_VeoneerCode = pd.read_excel(FltMonr_Excel, "ACCT Autoliv Faults", dtype='str', header=0)
    df_VeoneerCode = df_VeoneerCode.iloc[2:,[0,3,4]]
    # print("$$$$$$$$$$$$$$$$$$$$$$ read ACCT Autoliv Faults Finished")
    # print(df_VeoneerCode.info())
    df_VeoneerCode.columns = ["VeonnerCodeName","VeoneerCode_Dec","VeoneerCode_Hex"]

    # 去读Data 参数信息
    # *******************************************************************
    df_Data = pd.read_excel(FltMonr_Excel, "DATA", dtype='str', header=0)
    # WL 在N列，ASCII N - ASCII A = 13
    df_Data = df_Data.iloc[3:, [0, 1, 13,15,16]]
    df_Data.columns = ["VeonnerCodeName", "DTCRecord", "WL","Permanent_Latched","Latched_KeyCycle"]
    df_Data["DTCRecord"] = df_Data["DTCRecord"].apply(lambda x:"" if x == "0xFFFFFF" else x) #将0xFFFFFF的部分删除掉
    df_Data["DTCRecord"] = df_Data["DTCRecord"].apply(lambda x: x.replace("0x", ""))#将"0x"去掉

    # 处理两个DataFrame
    # *******************************************************************
    # df_DTCDefine = df_VeoneerCode.join(df_Data)
    df_DTCDefine = pd.merge(df_VeoneerCode,df_Data,on = "VeonnerCodeName",how = "left")
    # print("$$$$$$$$$$$$$$$$$$$$$$Merage DATA  and ACCT Autoliv Faults")
    df_DTCDefine = df_DTCDefine[["VeonnerCodeName","DTCRecord","VeoneerCode_Dec","VeoneerCode_Hex","WL","Permanent_Latched","Latched_KeyCycle"]]
    df_DTCDefine["VeonnerCodeName"] = df_DTCDefine["VeonnerCodeName"] + "_0"
    # df_DTCDefine.set_index("VeonnerCodeName", inplace=True, drop=False)
    df_DTCDefine.set_index(np.arange(df_DTCDefine["VeonnerCodeName"].shape[0]), inplace=True)

    DTCDefine_Dict = df_DTCDefine.to_dict(orient="split")
    DTCDefine_List = DTCDefine_Dict["data"]
    print("$$$$$$$$$$$$$$$$$$$$$$Get_Df_DTCDefine Finished")
    return DTCDefine_List;

def Generate_DTCDefine(Project,SWVersion,DTC_OutPut,DTCDefine_List):
    """
    根据从FltMonr_Configurator提取的信息，生成测试脚本使用的
    AA_Geely_GEEA2_HX11_DTCDefine_P23
    AA_Geely_GEEA2_HX11_InterpreteVeoneerCode_function_P23
    :param Project: 项目名称，用于文件名字的前缀
    :param SWVersion: 软件版本 用于文件名字的前缀
    :param DTC_OutPut: 保存ts文件的路径
    :param DTCDefine_List: 从函数 Get_Df_DTCDefine 中获取出来的
                            "VeonnerCodeName","DTCRecord","VeoneerCode_Dec","VeoneerCode_Hex","WL","Permanent_Latched","Latched_KeyCycle"的列表
    :return:NONE
    """
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Generate_DTCDefine")
    DTCDefine = DTC_OutPut + "/AA_" + Project + "_DTCDefine_" + SWVersion + ".ts"
    VeoneerCode_Function = DTC_OutPut + "/AA_" + Project + "_InterpreteVeoneerCode_function_" + SWVersion + ".ts"

    # 生成DTCDefine
    # *******************************************************************
    DTCDefine_File = open(DTCDefine,'w')
    VeoneerCode_Function_File = open(VeoneerCode_Function,'w')
    DTCDefine_Start = ("""/*
      ******Please update this file base on the latest error definition file after each software release!!!******\n
            var VeoneerCodeNameDefine = DTCCode,VeoneerCode,VeoneerCodeName,WLAttributes,Permanent_Latched,Latched_KeyCycle;
      */ \n\n""")

    VeoneerCode_Function_Start = ("""/*
    ******Please copy this InterpreteVeoneerCode function to your project's common function.ts file!!!******\n*/
    
    //Translate Veoneer code into Error Name """ + "\n"
    "function InterpreteVeoneerCode(VeoneerCode:int)\n"
    "{\n" + '\t'*1 + 'var DTCname:String = "";'
    '\n' + '\t'*1 + "switch(VeoneerCode)\n" + '\t'*1  + "{\n")

    DTCDefine_File.write(DTCDefine_Start)
    VeoneerCode_Function_File.write(VeoneerCode_Function_Start)
    for temp in DTCDefine_List:
        print(temp)
        DTCDefine_TempStr = ("var " + temp[0] + "_define = " + '"' + temp[1] + ","
                            + temp[3] + "," + temp[0] + "," + temp[4] + "," + temp[5] + "," + temp[6] +  '";\n')
        VeoneerCode_Function_TempStr = ("\t"*2 + "case " + temp[2] + " :\n" + "\t"*3 +
                                       "DTCname = " + '"' + temp[0]  + '";\n' + "\t"*3 + "break;\n")
        DTCDefine_File.write(DTCDefine_TempStr)
        VeoneerCode_Function_File.write(VeoneerCode_Function_TempStr)

    VeoneerCode_Function_End = ("\t"*2 + "default:\n " + "\t"*3 + """RESULT.InterpretEqualResult('DTC Name Define : ',
                                ['1111','DTC Name is not Define for Veonner code ' + VeoneerCode])"""
                                + ";\n" + "\t"*3 + "break;\n" + "\t"*1 + "}\n\t" + "return DTCname;\n}")
    VeoneerCode_Function_File.write(VeoneerCode_Function_End)
    DTCDefine_File.close();
    VeoneerCode_Function_File.close()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Generate_DTCDefine Finished")



#########PBCT_Excel 从o行开始作为columns，第11 行才开始有数据
#########EPPROM_Trans_Excel 直接从0行作为columns
######### Columns 是通过关键字抓，所以不用担心列的变动
def Generate_SYM(Project,SWVersion,PBCT_Excel,EPPROM_Trans_Excel,SYM_OutPut,SheetList):
    """
    通过对EEPROM_Translation PBCT_Smart_P23的数据抓取，生成symbol file 文件 形成如下的文件

    address  Parameter_name,                    数据长度，未知数据保持为0
    8001C000,A2_AlgoSectionHeader.StartAddress,  4,    0
    :param Project: 项目名称，用于文件名字的前缀
    :param SWVersion: 软件版本 用于文件名字的前缀
    :param PBCT_Excel:
    :param EPPROM_Trans_Excel:
    :param SYM_OutPut:symbol file 文件 的输出路径
    :param SheetList:PBCT_Excel 抓取sheet的二元列表，由于项目不同，可能没有Ip或者多algo
                    [ [sheet名字，Paramneter前缀]]
    :return:SYM_OutPut symbol file 文件 的输出路径 + 文件名字
    """

    #获取PBCT参数信息
    print("Generate_SYM")
    # *******************************************************************
    SYM_OutPut = SYM_OutPut + "/" + Project + "_" + SWVersion + ".sym"
    print(SheetList)
    df_SYM = pd.DataFrame(columns=["PARAMETER NAME", "FLASH ADDRESS", "SIZE", "UNKNOWN"])
    for SheetName in SheetList:
        print("Read " + SheetName[0])
        df_temp = pd.read_excel(PBCT_Excel, SheetName[0],dtype='str',header=0)

        #如果有缩写表示需要在parameter 前加前缀
        if len(SheetName) > 1:
            df_temp["PARAMETER NAME"] = SheetName[1] + "_" + df_temp["PARAMETER NAME"]
        df_temp["UNKNOWN"] = pd.Series(np.zeros(df_temp["FLASH ADDRESS"].shape[0]), dtype=int)
        df_temp = df_temp[9:][["PARAMETER NAME", "FLASH ADDRESS", "SIZE", "UNKNOWN"]]
        df_SYM = pd.concat([df_temp,df_SYM])
    # print(SYM_OutPut)

    #获取NVM 参数信息
    # *******************************************************************
    #NVM 地址计算公式为："EE" +DEC2Hex(BlockID,1) + Dec2Hex(Block address offset,2)
    print("Read EPPROM_Trans_Excel")
    df_NVM = pd.read_excel(EPPROM_Trans_Excel, "EEPROM Parameters",dtype='str')
    # df_NVM.info()
    Fun_BlockId = lambda x: Str2Hex(x, 1)
    Fun_BlockOffset = lambda x:Str2Hex(x,2)
    # print(df_NVM["BLOCK ID"].apply(Fun_BlockId))
    # print(df_NVM["BLOCK ADDRESS OFFSET"].apply(Fun_BlockOffset))
    df_NVM["FLASH ADDRESS"] = "EE" + df_NVM["BLOCK ID"].apply(Fun_BlockId)+ df_NVM["BLOCK ADDRESS OFFSET"].apply(Fun_BlockOffset)
    # print(df_NVM["FLASH ADDRESS"])
    df_NVM["UNKNOWN"] = pd.Series(np.zeros(df_NVM["FLASH ADDRESS"].shape[0]),dtype='int')
    df_NVM = df_NVM[["PARAMETER NAME","FLASH ADDRESS","SIZE","UNKNOWN"]]


    # Sym file 数据生成
    # *******************************************************************
    df_SYM = pd.concat([df_SYM,df_NVM])
    df_SYM = df_SYM[["FLASH ADDRESS","PARAMETER NAME","SIZE","UNKNOWN"]]
    df_SYM.set_index(np.arange(df_SYM["FLASH ADDRESS"].shape[0]), inplace=True)
    df_SYM["UNKNOWN"] = df_SYM["UNKNOWN"].astype("str")
    # print(df_SYM["UNKNOWN"].dtype)
    # print(df_SYM)
    SYM_Dict = df_SYM.swapaxes(1,0).to_dict(orient="list")
    SYM_Str = "\n".join([",".join(i) for i in list(SYM_Dict.values())])
    with open(SYM_OutPut,'w') as f:
        f.write(SYM_Str)
    return SYM_OutPut


class DTCDefine_SYMWidget(QWidget):

    # def __new__(cls):
    #     if not hasattr(cls,'instance'):
    #         cls.instance = super(MinToolWidget, cls).__new__(cls)
    #     return cls.instance
    # *****************定义 类相关属性****************************************
    CurrentPath = os.getcwd()
    def __init__(self):
        super().__init__()  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_DTCDefine_SYM()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面

        # font = cls.font()
        # font.setPixelSize(20)
        # cls.pb = QLabel(cls)
        # cls.pb.setGeometry(400,400,400,55)
        # cls.pb.setFont(font)
        # # cls.pb.setStyleSheet('font-size:44px;')
        # cls.pb.setStyleSheet("background-color:cornflowerBlue")
        # cls.pb.setText("^-^ Generating file,Please wait for moment")
        # cls.pb.hide()
        # cls.timer = QBasicTimer();
        # cls.step = 0
        # cls.pb.hide()
        # *****************定义 OtTool相关属性****************************************
        self.Config = ""

        self.Project = ""
        self.SWVersion = ""

        self.FltMonrConfig_Excel = ""
        self.DTC_OutPut = ""
        # cls.DTCDefine_Ts = ""
        # cls.VeoneerName_Ts = ""
        # cls.ErrorDefinition_Excel = ""

        self.PBCT_SheetList = ["IP Fixed Calibration:IP","Vehicle Fixed Calibration","Algo Calibration Variant 1","Algo Calibration Variant 2:A2","Algo Calibration Variant 3:A3"]

        self.PBCT_Excel = ""
        self.EEPROM_Trans_Excel = ""
        self.SYM_OutPut = ""
        # cls.SYM_OutPut_Folder = ""




        # *****************设置OtToll LineEdit默认值****************************************
        if os.path.exists('./ini/DTCDefine_SYMWidget.ini'):
            self.Config = QSettings('./ini/DTCDefine_SYMWidget.ini', QSettings.IniFormat)
            self.LoadConfig()

    # def timerEvent(cls, e) -> None:
    #     if cls.step >=100:
    #         cls.time.stop()
    #         return
    #     cls.step +=1
    #     cls.pb.setValue(cls.step)

    # def doAction(cls,value):

    # 定义错误提示框
    def WarningMessage(self,str):
        DigTitle = "Warning Message"
        StrInfo = str
        QMessageBox.warning(self,DigTitle,StrInfo)
    def DoneMessage(self,str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)
    def LoadConfig(self):
        self.Project = self.Config.value("CONFIG/Project")
        self.SWVersion = self.Config.value("CONFIG/SWVersion")
        self.FltMonrConfig_Excel = self.Config.value("CONFIG/FltMonrConfig_Excel")
        self.DTC_OutPut = self.Config.value("CONFIG/DTC_OutPut")
        self.PBCT_Excel = self.Config.value("CONFIG/PBCT_Excel")
        self.PBCT_SheetList = self.Config.value("CONFIG/PBCT_SheetList")
        # print(cls.PBCT_SheetList)
        self.EEPROM_Trans_Excel = self.Config.value("CONFIG/EEPROM_Trans_Excel")
        self.SYM_OutPut = self.Config.value("CONFIG/SYM_OutPut")
        self.__ui.LE_Project.setText(self.Project)
        self.__ui.LE_SWVersion.setText(self.SWVersion)
        self.__ui.LE_FltMonrConfig.setText(self.FltMonrConfig_Excel)

        self.__ui.CB_SheetConfig.clear()
        self.__ui.CB_SheetConfig.addItems(self.PBCT_SheetList)

        self.__ui.LE_PBCT.setText(self.PBCT_Excel)
        self.__ui.LE_EEPROM_Trans.setText(self.EEPROM_Trans_Excel)
        self.__ui.LE_SYM_OutPut.setText(self.SYM_OutPut)


    def SaveConfig(self):
        self.Config = QSettings('./ini/DTCDefine_SYMWidget.ini', QSettings.IniFormat)
        self.Config.setIniCodec('UTF-8')  # 设置ini文件编码为 UTF-8
        self.Config.setValue("CONFIG/Project",self.Project)
        self.Config.setValue("CONFIG/SWVersion", self.SWVersion)
        self.Config.setValue("CONFIG/FltMonrConfig_Excel", self.FltMonrConfig_Excel)
        self.Config.setValue("CONFIG/DTC_OutPut", self.DTC_OutPut)
        self.Config.setValue("CONFIG/PBCT_SheetList",self.PBCT_SheetList)
        self.Config.setValue("CONFIG/PBCT_Excel", self.PBCT_Excel)
        self.Config.setValue("CONFIG/EEPROM_Trans_Excel", self.EEPROM_Trans_Excel)
        self.Config.setValue("CONFIG/SYM_OutPut", self.SYM_OutPut)

    #*******************************设置槽函数******************************
    # 1 设置LE_Project
    @pyqtSlot(str)
    def on_LE_Project_textChanged(self,str):
        self.Project = self.__ui.LE_Project.text()
        # print(cls.Project)

    #2 .设置LE_SWVersion
    @pyqtSlot(str)
    def on_LE_SWVersion_textChanged(self,str):
        self.SWVersion = self.__ui.LE_SWVersion.text()
        # print(cls.SWVersion)

    #3。 设置BT_FltMonrConfig
    @pyqtSlot()
    def on_BT_FltMonrConfig_clicked(self):

        self.__ui.LE_FltMonrConfig.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select FltMonr_Configurator_PXX.xlsm ",
                                                         self.CurrentPath,
                                                         "Excel(*.xlsx *.xlsm)")
        self.__ui.LE_FltMonrConfig.setText(FileName)
        self.FltMonrConfig_Excel = self.__ui.LE_FltMonrConfig.text()
        path = self.FltMonrConfig_Excel
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)
        # print(cls.FltMonrConfig_Excel)

    #4 。 设置BT_DTC_OutPut
    @pyqtSlot()
    def on_BT_DTC_OutPut_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the DTCdefine.ts output path",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_DTC_OutPut.setText(FolderName)
        self.DTC_OutPut = self.__ui.LE_DTC_OutPut.text()
        # print(cls.DTC_OutPut)
        path = self.DTC_OutPut
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #5。
    @pyqtSlot()
    def on_BT_Generate_DTCDefine_clicked(self):
        try:
            DTCDefine_List = Get_Df_DTCDefine(self.FltMonrConfig_Excel)
            # Generate_DTCDefine(cls.Project,cls.SWVersion,cls.DTC_OutPut,DTCDefine_List);
            args = {"Project":self.Project,"SWVersion":self.SWVersion,
                    "DTC_OutPut":self.DTC_OutPut,"DTCDefine_List":DTCDefine_List}
            Generate_DTCDefine(**args)
            self.DoneMessage("Generate dtcdefine and InterpreteVeoneerCode function successfully")
            self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))

    # 6。
    @pyqtSlot()
    def on_BT_Generate_ErrorDefinition_clicked(self):
        try:
            ExcelAPP = win32com.client.DispatchEx('Excel.Application')
            ExcelAPP.Visible = 0
            ExcelAPP.DisplayAlerts = 0
            args = {"ExcelAPP":ExcelAPP,"Project":self.Project,"SWVersion":self.SWVersion,
                    "DTC_OutPut":self.DTC_OutPut,"FltMonr_Excel":self.FltMonrConfig_Excel}
            Generate_ErrorDefinition(**args)
            self.DoneMessage("Generate ErrorDefinition successfully")
            self.SaveConfig()
        except Exception as err:
            ExcelAPP.Quit()
            self.WarningMessage(str(err))

        # cls.WarningMessage("Aria need Xlsm format, so please changed the format manually")

    # 11
    @pyqtSlot()
    def on_BT_DeleteSheet_clicked(self):
        if self.__ui.LE_SheetName.text():
            templist = []
            for count in range(self.__ui.CB_SheetConfig.count()):
                templist.append(self.__ui.CB_SheetConfig.itemText(count))
            sheetindex = templist.index(self.__ui.LE_SheetName.text())
            if self.__ui.LE_SheetName.text() in templist:
                self.__ui.CB_SheetConfig.removeItem(sheetindex)
                self.PBCT_SheetList.pop(sheetindex)

    @pyqtSlot()
    def on_BT_AddSheet_clicked(self):
        if self.__ui.LE_SheetName.text():
            templist = []
            for count in range(self.__ui.CB_SheetConfig.count()):
                templist.append(self.__ui.CB_SheetConfig.itemText(count))
            if self.__ui.LE_SheetName.text() not in templist:
                self.__ui.CB_SheetConfig.addItem(self.__ui.LE_SheetName.text())
                self.PBCT_SheetList.append(self.__ui.LE_SheetName.text())

    @pyqtSlot(str)
    def on_CB_SheetConfig_currentTextChanged(self, str):
        self.__ui.LE_SheetName.setText(self.__ui.CB_SheetConfig.currentText())

    @pyqtSlot()
    def on_BT_PBCT_clicked(self):
        self.__ui.LE_PBCT.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select PBCT_Project_PXX.xlsm ",
                                                         self.CurrentPath,
                                                         "Excel(*.xlsx *.xlsm)")
        self.__ui.LE_PBCT.setText(FileName)
        self.PBCT_Excel = self.__ui.LE_PBCT.text()
        # print(cls.PBCT_Excel)
        path = self.PBCT_Excel
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    #12
    @pyqtSlot()
    def on_BT_EEPROM_Trans_clicked(self):
        self.__ui.LE_EEPROM_Trans.clear()
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select EEPROM translation sheet_Project_PXX.xlsm ",
                                                         self.CurrentPath,
                                                         "Excel(*.xlsx *.xlsm)")
        self.__ui.LE_EEPROM_Trans.setText(FileName)
        self.EEPROM_Trans_Excel = self.__ui.LE_EEPROM_Trans.text()
        # print(cls.EEPROM_Trans_Excel)

        path = self.EEPROM_Trans_Excel
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    # 13
    @pyqtSlot()
    def on_BT_SYM_OutPut_clicked(self):
        FolderName = QFileDialog.getExistingDirectory(self,
                                                      "Please the symfiles.sym output path",
                                                      self.CurrentPath)  # 起始路径
        self.__ui.LE_SYM_OutPut.setText(FolderName)
        # cls.SYM_OutPut_Folder = cls.__ui.LE_SYM_OutPut.text()
        self.SYM_OutPut = self.__ui.LE_SYM_OutPut.text()
        # print(cls.SYM_OutPut)
        path = self.SYM_OutPut
        self.CurrentPath = os.path.abspath(path) if os.path.isdir(path) else os.path.dirname(path)

    def Generate_Sym(self):

        self.PBCT_SheetList = []
        print("on_BT_Generate_SYM_clicked")
        for count in range(self.__ui.CB_SheetConfig.count()):
            self.PBCT_SheetList.append(self.__ui.CB_SheetConfig.itemText(count))
        SheetList = [i.split(":") for i in self.PBCT_SheetList]
        try:
            args = {"Project": self.Project, "SWVersion": self.SWVersion,
                    "PBCT_Excel": self.PBCT_Excel, "EPPROM_Trans_Excel": self.EEPROM_Trans_Excel,
                    "SYM_OutPut": self.SYM_OutPut, "SheetList": SheetList}
            file = Generate_SYM(**args)
            if not os.path.exists(file):
                self.WarningMessage(file + " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate symfile successfully")
                self.SaveConfig()

        except Exception as err:
            self.WarningMessage(str(err))

        self.__ui.BT_Generate_SYM.setEnabled(True)
        self.pb.hide()
    # def Pb_Thread(cls):
    #     cls.timer.start(100, cls)

    # @pyqtSlot()
    # def on_BT_Generate_SYM_clicked(cls):
    #     cls.__ui.BT_Generate_SYM.setEnabled(False)
    #     cls.pb.show()
    #     try:
    #         cls.Thread = Generate_Thread(cls.Generate_Sym)
    #         cls.Thread.run()
    #     except Exception as err:
    #         print(err)
    # # 14
    @pyqtSlot()
    def on_BT_Generate_SYM_clicked(self):

        self.PBCT_SheetList = []
        print("on_BT_Generate_SYM_clicked")
        for count in range(self.__ui.CB_SheetConfig.count()):
            self.PBCT_SheetList.append(self.__ui.CB_SheetConfig.itemText(count))
        SheetList = [i.split(":") for i in self.PBCT_SheetList]
        try:
            args = {"Project":self.Project, "SWVersion":self.SWVersion,
                    "PBCT_Excel":self.PBCT_Excel, "EPPROM_Trans_Excel":self.EEPROM_Trans_Excel,
                    "SYM_OutPut":self.SYM_OutPut,"SheetList":SheetList}
            file = Generate_SYM(**args)
            if not os.path.exists(file):
                self.WarningMessage(file+ " not been generated, please check related setting")
            else:
                self.DoneMessage("Generate symfile successfully")
                self.SaveConfig()
        except Exception as err:
            self.WarningMessage(str(err))


    #15设置BT_SaveConfig
    @pyqtSlot()
    def on_BT_SaveConfig_clicked(self):
        self.SaveConfig()

    #16设置BT_LoadConfig
    @pyqtSlot()
    def on_BT_LoadConfig_clicked(self):
        FileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "Select an ini file ",
                                                         self.CurrentPath,
                                                         "ini(*.ini)")
        if FileName:
            self.Config= QSettings(FileName, QSettings.IniFormat)
            self.LoadConfig()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = DTCDefine_SYMWidget()
    baseWidget.show()
    sys.exit(app.exec_())
