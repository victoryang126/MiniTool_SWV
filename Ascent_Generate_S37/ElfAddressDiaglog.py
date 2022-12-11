from Ascent_Generate_S37.Ui_ElfAddress import Ui_ElfAddress
from PyQt5.QtWidgets import *
import sys
class ElfAddressQdiaglog(QDialog,Ui_ElfAddress):
    def __init__(self):
        super(ElfAddressQdiaglog, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    baseWidget = ElfAddressQdiaglog()

    baseWidget.show()
    sys.exit(app.exec_())
