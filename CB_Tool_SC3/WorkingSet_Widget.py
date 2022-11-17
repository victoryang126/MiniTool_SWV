from CB_Tool_SC3.CodeBeamer import CodeBeamer
import sys
from CB_Tool_SC3.Ui_WorkingSet import Ui_WorkingSet
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDialog, QFileDialog
from CB_Tool_SC3.CB_Tool import CB_Tool
class WorkingSet_Widget(QWidget, CB_Tool):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_WorkingSet()
        self.__ui.setupUi(self)


    def WarningMessage(self, Err):
        DigTitle = "Warning Message"
        StrInfo = Err
        # print(str)
        QMessageBox.warning(self, DigTitle, str(Err))

    def DoneMessage(self, str):
        DigTitle = "Information Message"
        StrInfo = str
        QMessageBox.information(self, DigTitle, StrInfo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = WorkingSet_Widget()
    baseWidget.show()
    sys.exit(app.exec_())