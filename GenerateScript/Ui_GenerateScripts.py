# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GenerateScripts.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GenerateScripts(object):
    def setupUi(self, GenerateScripts):
        GenerateScripts.setObjectName("GenerateScripts")
        GenerateScripts.resize(1035, 604)
        self.gridLayout = QtWidgets.QGridLayout(GenerateScripts)
        self.gridLayout.setObjectName("gridLayout")
        self.label_ScriptTemplates = QtWidgets.QLabel(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_ScriptTemplates.setFont(font)
        self.label_ScriptTemplates.setObjectName("label_ScriptTemplates")
        self.gridLayout.addWidget(self.label_ScriptTemplates, 2, 0, 1, 1)
        self.BT_ScriptTemplates = QtWidgets.QPushButton(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BT_ScriptTemplates.setFont(font)
        self.BT_ScriptTemplates.setObjectName("BT_ScriptTemplates")
        self.gridLayout.addWidget(self.BT_ScriptTemplates, 2, 2, 2, 1)
        self.BT_TestObject = QtWidgets.QPushButton(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BT_TestObject.setFont(font)
        self.BT_TestObject.setObjectName("BT_TestObject")
        self.gridLayout.addWidget(self.BT_TestObject, 0, 2, 1, 1)
        self.label_TestObject = QtWidgets.QLabel(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_TestObject.setFont(font)
        self.label_TestObject.setObjectName("label_TestObject")
        self.gridLayout.addWidget(self.label_TestObject, 0, 0, 1, 1)
        self.label_ScriptsPath = QtWidgets.QLabel(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_ScriptsPath.setFont(font)
        self.label_ScriptsPath.setObjectName("label_ScriptsPath")
        self.gridLayout.addWidget(self.label_ScriptsPath, 4, 0, 1, 1)
        self.BT_ScriptPath = QtWidgets.QPushButton(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BT_ScriptPath.setFont(font)
        self.BT_ScriptPath.setObjectName("BT_ScriptPath")
        self.gridLayout.addWidget(self.BT_ScriptPath, 4, 2, 1, 1)
        self.textB_ScriptTemplates = QtWidgets.QTextBrowser(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textB_ScriptTemplates.setFont(font)
        self.textB_ScriptTemplates.setLineWidth(0)
        self.textB_ScriptTemplates.setObjectName("textB_ScriptTemplates")
        self.gridLayout.addWidget(self.textB_ScriptTemplates, 2, 1, 2, 1)
        self.BT_Generate = QtWidgets.QPushButton(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BT_Generate.setFont(font)
        self.BT_Generate.setObjectName("BT_Generate")
        self.gridLayout.addWidget(self.BT_Generate, 5, 0, 1, 1)
        self.LE_TestObject = QtWidgets.QLineEdit(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LE_TestObject.setFont(font)
        self.LE_TestObject.setReadOnly(True)
        self.LE_TestObject.setObjectName("LE_TestObject")
        self.gridLayout.addWidget(self.LE_TestObject, 0, 1, 1, 1)
        self.LE_ScriptPath = QtWidgets.QLineEdit(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LE_ScriptPath.setFont(font)
        self.LE_ScriptPath.setReadOnly(True)
        self.LE_ScriptPath.setObjectName("LE_ScriptPath")
        self.gridLayout.addWidget(self.LE_ScriptPath, 4, 1, 1, 1)
        self.CB_SheetList = QtWidgets.QComboBox(GenerateScripts)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CB_SheetList.setFont(font)
        self.CB_SheetList.setObjectName("CB_SheetList")
        self.gridLayout.addWidget(self.CB_SheetList, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 4)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(GenerateScripts)
        QtCore.QMetaObject.connectSlotsByName(GenerateScripts)

    def retranslateUi(self, GenerateScripts):
        _translate = QtCore.QCoreApplication.translate
        GenerateScripts.setWindowTitle(_translate("GenerateScripts", "GenerateScripts"))
        self.label_ScriptTemplates.setText(_translate("GenerateScripts", "Script Templates"))
        self.BT_ScriptTemplates.setText(_translate("GenerateScripts", "Browse"))
        self.BT_TestObject.setText(_translate("GenerateScripts", "Browse"))
        self.label_TestObject.setText(_translate("GenerateScripts", "TestObject"))
        self.label_ScriptsPath.setText(_translate("GenerateScripts", "Script Path:"))
        self.BT_ScriptPath.setText(_translate("GenerateScripts", "Browse"))
        self.textB_ScriptTemplates.setPlaceholderText(_translate("GenerateScripts", "Please select the script template"))
        self.BT_Generate.setText(_translate("GenerateScripts", "Generate"))
        self.LE_TestObject.setPlaceholderText(_translate("GenerateScripts", "Please select the excel which contains the test object data"))
        self.LE_ScriptPath.setPlaceholderText(_translate("GenerateScripts", "Please select the folder to save the scripts"))
