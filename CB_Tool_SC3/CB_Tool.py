import os
from CB_Tool_SC3.CodeBeamer import CodeBeamer
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
# 定义为类属性，相关工具直接继承改对象即可
class CB_Tool(CodeBeamer):
    CurrentPath = os.getcwd()

    # CodeBeamer_Obj = CodeBeamer()
    # PTC_Spec = r"C:/Users/victor.yang/Desktop/Work/CB/SpecTemplate/CHT_SWV_Project_FunctionName_Test Specification_Template_SC3.xlsm"
    PTC_Spec = ""
    # CB_Spec_ExportPath = r'C:/Users/victor.yang/Desktop/Work/CB/SpecTemplate'
    CB_Spec_ExportPath = ""

    PTC_Result = ""
    CB_Spec_FromCB = ""
    FinalCBSpec = ""

    TestRun_Link = ""
    TestRun_Report = ""
    TestRun_Status = ""
    TestRun_Result = ""
    TestRun_Link = ""


    PTC_Result_List = []

    # def __init__(cls):
    #     super().__init__()
    #
    # @classmethod
    # def WarningMessage(cls, Err):
    #     DigTitle = "Warning Message"
    #     StrInfo = Err
    #     # print(str)
    #     QMessageBox.warning( DigTitle, str(Err))
    #
    # @classmethod
    # def DoneMessage(cls, str):
    #
    #     DigTitle = "Information Message"
    #     StrInfo = str
    #     print("%%%%%%%%%%")
    #     QMessageBox.information(DigTitle, StrInfo)

    # def __init__(cls):
    #     pass
        # cls.CodeBeamer_Obj = CodeBeamer()
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
if __name__ == '__main__':
    CB = CB_Tool()
    CB.DoneMessage("TTTT")
