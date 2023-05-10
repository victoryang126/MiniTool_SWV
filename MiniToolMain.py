'''
This is a set that combine all tool used in RCS SW test Teams

for each function, please refer to each folder to check the function

'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow,QListWidget,QStackedWidget,QHBoxLayout
from PyQt5.QtGui import  QIcon
import Res_rc
# from PyQt5.
from Regression import RegressionWidget
from Ascent_Generate_S37 import GenS37Widget
# from Other_Tool import OtToolWidget
from DTCDefine_SymFile import DTCDefine_SYMWidget
from Diagnostic_Parameter import CANDWidget
from VBFGenerate import VBFGenerateWidget
from GenerateScript import GenerateScriptsWidget
from CB_Server_API.CB_Tool_Widget import CB_Tool_Widget

class MiniTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MiniTool V1.17.2')
        self.setWindowIcon(QIcon('./Images/title.ico'))
        self.setGeometry(150,150,1300,680)

        # 左边listWidget
        self.list = QListWidget()
        self.list.insertItem(0,'Regression')
        self.list.insertItem(1,'GenS37')
        # cls.list.insertItem(2,'OtTool')
        self.list.insertItem(3, 'DTCDefine_SYM')
        self.list.insertItem(4, 'CAND')
        self.list.insertItem(5, 'VBFGenerate')
        # self.list.insertItem(6, 'CB_Spec_Tool')
        self.list.insertItem(7, 'GenerateScript')
        self.list.insertItem(8, 'Codebeamer_Tool')
        # 右边StackedWidget
        self.stack = QStackedWidget()
        self.stack.addWidget(RegressionWidget())
        self.stack.addWidget(GenS37Widget())
        # cls.stack.addWidget(OtToolWidget())
        self.stack.addWidget(DTCDefine_SYMWidget())
        self.stack.addWidget(CANDWidget())
        self.stack.addWidget(VBFGenerateWidget())
        # self.stack.addWidget(CB_Spec_Tool_Widget())
        self.stack.addWidget(GenerateScriptsWidget())
        self.stack.addWidget(CB_Tool_Widget())
        hbox = QHBoxLayout()
        hbox.addWidget(self.list)

        hbox.addWidget(self.stack)
        hbox.setStretchFactor(self.list,1)
        hbox.setStretchFactor(self.stack,10)
        # cls.setLayout(hbox)
        # cls.setCentralWidget(hbox)
        BaseWidget = QWidget();
        BaseWidget.setLayout(hbox)
        self.setCentralWidget(BaseWidget)


        # 信号部分
        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)

if __name__ == '__main__':

    # Update the text on the splash screen use in pyinstaller, can't run this in python scripts
    # some imge will show during loading python exe
    # try:
    #     import pyi_splash
    #     for i in range(100):
    #         pyi_splash.update_text("Loading .... {:.0%}".format(i / 100))
    #     # # Close the splash screen. It does not matter when the call
    #     # # to this function is made, the splash screen remains open until
    #     # # this function is called or the Python program is terminated.
    #     pyi_splash.close()
    # except:
    #     pass




    # import tempfile
    # # Use this code to signal the splash screen removal.
    # if "NUITKA_ONEFILE_PARENT" in os.environ:
    #     splash_filename = os.path.join(
    #         tempfile.gettempdir(),
    #         "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
    #     )
    #
    #     if os.path.exists(splash_filename):
    #         os.unlink(splash_filename)
    #
    # print("Done... splash should be gone.")

    app = QApplication(sys.argv)
    #
    # splash = QSplashScreen(QPixmap("Boot.PNG"))
    # splash.showMessage("Loading .... 0%")
    # splash.show()
    # icon = QIcon(":/icon/Images/title.PNG")
    MiniToolWindow = MiniTool()
    # MiniToolWindow.setWindowIcon(icon)
    MiniToolWindow.show()
    sys.exit(app.exec_())
