# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CB_Spec_Tool.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CB_Spec_Tool(object):
    def setupUi(self, CB_Spec_Tool):
        CB_Spec_Tool.setObjectName("CB_Spec_Tool")
        CB_Spec_Tool.resize(1121, 663)
        self.gridLayout = QtWidgets.QGridLayout(CB_Spec_Tool)
        self.gridLayout.setObjectName("gridLayout")
        self.LE_FinalCBSpec = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_FinalCBSpec.setFont(font)
        self.LE_FinalCBSpec.setReadOnly(True)
        self.LE_FinalCBSpec.setObjectName("LE_FinalCBSpec")
        self.gridLayout.addWidget(self.LE_FinalCBSpec, 11, 1, 1, 3)
        self.LE_CB_Spec_FromCB = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_CB_Spec_FromCB.setFont(font)
        self.LE_CB_Spec_FromCB.setReadOnly(True)
        self.LE_CB_Spec_FromCB.setObjectName("LE_CB_Spec_FromCB")
        self.gridLayout.addWidget(self.LE_CB_Spec_FromCB, 9, 1, 1, 3)
        self.Lable_CB_Spec = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_CB_Spec.setFont(font)
        self.Lable_CB_Spec.setObjectName("Lable_CB_Spec")
        self.gridLayout.addWidget(self.Lable_CB_Spec, 2, 0, 1, 1)
        self.BT_Upload2CB_1stTime = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Upload2CB_1stTime.setFont(font)
        self.BT_Upload2CB_1stTime.setObjectName("BT_Upload2CB_1stTime")
        self.gridLayout.addWidget(self.BT_Upload2CB_1stTime, 13, 0, 1, 1)
        self.BT_Replace_DoosID = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_Replace_DoosID.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Replace_DoosID.setFont(font)
        self.BT_Replace_DoosID.setCheckable(False)
        self.BT_Replace_DoosID.setChecked(False)
        self.BT_Replace_DoosID.setObjectName("BT_Replace_DoosID")
        self.gridLayout.addWidget(self.BT_Replace_DoosID, 3, 0, 1, 1)
        self.LE_CB_Spec_Generate = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_CB_Spec_Generate.setFont(font)
        self.LE_CB_Spec_Generate.setReadOnly(True)
        self.LE_CB_Spec_Generate.setObjectName("LE_CB_Spec_Generate")
        self.gridLayout.addWidget(self.LE_CB_Spec_Generate, 5, 1, 1, 3)
        self.BT_CB_Spec_Generate = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_CB_Spec_Generate.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_CB_Spec_Generate.setFont(font)
        self.BT_CB_Spec_Generate.setObjectName("BT_CB_Spec_Generate")
        self.gridLayout.addWidget(self.BT_CB_Spec_Generate, 5, 4, 1, 1)
        self.LE_CB_Spec = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_CB_Spec.setFont(font)
        self.LE_CB_Spec.setReadOnly(True)
        self.LE_CB_Spec.setObjectName("LE_CB_Spec")
        self.gridLayout.addWidget(self.LE_CB_Spec, 2, 1, 1, 3)
        self.BT_FinalCBSpec = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_FinalCBSpec.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_FinalCBSpec.setFont(font)
        self.BT_FinalCBSpec.setObjectName("BT_FinalCBSpec")
        self.gridLayout.addWidget(self.BT_FinalCBSpec, 11, 4, 1, 1)
        self.Lable_CB_Spec_FromCB = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_CB_Spec_FromCB.setFont(font)
        self.Lable_CB_Spec_FromCB.setObjectName("Lable_CB_Spec_FromCB")
        self.gridLayout.addWidget(self.Lable_CB_Spec_FromCB, 9, 0, 1, 1)
        self.LE_LookUp = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_LookUp.setFont(font)
        self.LE_LookUp.setObjectName("LE_LookUp")
        self.gridLayout.addWidget(self.LE_LookUp, 0, 1, 1, 3)
        self.LE_CaseTrackerID = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_CaseTrackerID.setFont(font)
        self.LE_CaseTrackerID.setReadOnly(True)
        self.LE_CaseTrackerID.setObjectName("LE_CaseTrackerID")
        self.gridLayout.addWidget(self.LE_CaseTrackerID, 8, 1, 1, 3)
        self.BT_Generate_Init = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Generate_Init.setFont(font)
        self.BT_Generate_Init.setObjectName("BT_Generate_Init")
        self.gridLayout.addWidget(self.BT_Generate_Init, 4, 0, 1, 1)
        self.Lable_CB_Spec_Folder_ID = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_CB_Spec_Folder_ID.setFont(font)
        self.Lable_CB_Spec_Folder_ID.setObjectName("Lable_CB_Spec_Folder_ID")
        self.gridLayout.addWidget(self.Lable_CB_Spec_Folder_ID, 7, 0, 1, 1)
        self.BT_LookUp = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_LookUp.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_LookUp.setFont(font)
        self.BT_LookUp.setCheckable(False)
        self.BT_LookUp.setAutoDefault(False)
        self.BT_LookUp.setObjectName("BT_LookUp")
        self.gridLayout.addWidget(self.BT_LookUp, 0, 4, 1, 1)
        self.LE_Release = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_Release.setFont(font)
        self.LE_Release.setReadOnly(True)
        self.LE_Release.setObjectName("LE_Release")
        self.gridLayout.addWidget(self.LE_Release, 6, 1, 1, 3)
        self.LE_CB_Spec_Folder_ID = QtWidgets.QLineEdit(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LE_CB_Spec_Folder_ID.setFont(font)
        self.LE_CB_Spec_Folder_ID.setReadOnly(True)
        self.LE_CB_Spec_Folder_ID.setObjectName("LE_CB_Spec_Folder_ID")
        self.gridLayout.addWidget(self.LE_CB_Spec_Folder_ID, 7, 1, 1, 3)
        self.Lable_Release = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_Release.setFont(font)
        self.Lable_Release.setObjectName("Lable_Release")
        self.gridLayout.addWidget(self.Lable_Release, 6, 0, 1, 1)
        self.Lable_LookUp = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_LookUp.setFont(font)
        self.Lable_LookUp.setObjectName("Lable_LookUp")
        self.gridLayout.addWidget(self.Lable_LookUp, 0, 0, 1, 1)
        self.BT_Generate_Modify = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Generate_Modify.setFont(font)
        self.BT_Generate_Modify.setObjectName("BT_Generate_Modify")
        self.gridLayout.addWidget(self.BT_Generate_Modify, 10, 0, 1, 1)
        self.BT_CB_Spec = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_CB_Spec.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_CB_Spec.setFont(font)
        self.BT_CB_Spec.setObjectName("BT_CB_Spec")
        self.gridLayout.addWidget(self.BT_CB_Spec, 2, 4, 1, 1)
        self.Lable_Test_Spec = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_Test_Spec.setFont(font)
        self.Lable_Test_Spec.setObjectName("Lable_Test_Spec")
        self.gridLayout.addWidget(self.Lable_Test_Spec, 1, 0, 1, 1)
        self.BT_Test_Spec = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Test_Spec.setFont(font)
        self.BT_Test_Spec.setObjectName("BT_Test_Spec")
        self.gridLayout.addWidget(self.BT_Test_Spec, 1, 4, 1, 1)
        self.Lable_CaseTrackerID = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_CaseTrackerID.setFont(font)
        self.Lable_CaseTrackerID.setObjectName("Lable_CaseTrackerID")
        self.gridLayout.addWidget(self.Lable_CaseTrackerID, 8, 0, 1, 1)
        self.Lable_CB_Spec_Generate = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_CB_Spec_Generate.setFont(font)
        self.Lable_CB_Spec_Generate.setObjectName("Lable_CB_Spec_Generate")
        self.gridLayout.addWidget(self.Lable_CB_Spec_Generate, 5, 0, 1, 1)
        self.Lable_FinalCBSpec = QtWidgets.QLabel(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Lable_FinalCBSpec.setFont(font)
        self.Lable_FinalCBSpec.setObjectName("Lable_FinalCBSpec")
        self.gridLayout.addWidget(self.Lable_FinalCBSpec, 11, 0, 1, 1)
        self.textB_Test_Spec = QtWidgets.QTextBrowser(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textB_Test_Spec.setFont(font)
        self.textB_Test_Spec.setObjectName("textB_Test_Spec")
        self.gridLayout.addWidget(self.textB_Test_Spec, 1, 1, 1, 3)
        self.BT_CB_Spec_FromCB = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_CB_Spec_FromCB.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_CB_Spec_FromCB.setFont(font)
        self.BT_CB_Spec_FromCB.setObjectName("BT_CB_Spec_FromCB")
        self.gridLayout.addWidget(self.BT_CB_Spec_FromCB, 9, 4, 1, 1)
        self.BT_Upload2CB = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Upload2CB.setFont(font)
        self.BT_Upload2CB.setObjectName("BT_Upload2CB")
        self.gridLayout.addWidget(self.BT_Upload2CB, 12, 0, 1, 1)
        self.BT_Upload2CB_Modify = QtWidgets.QPushButton(CB_Spec_Tool)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_Upload2CB_Modify.setFont(font)
        self.BT_Upload2CB_Modify.setObjectName("BT_Upload2CB_Modify")
        self.gridLayout.addWidget(self.BT_Upload2CB_Modify, 14, 0, 1, 1)
        self.BT_DownloadCBSpec = QtWidgets.QPushButton(CB_Spec_Tool)
        self.BT_DownloadCBSpec.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BT_DownloadCBSpec.setFont(font)
        self.BT_DownloadCBSpec.setObjectName("BT_DownloadCBSpec")
        self.gridLayout.addWidget(self.BT_DownloadCBSpec, 8, 4, 1, 1)

        self.retranslateUi(CB_Spec_Tool)
        QtCore.QMetaObject.connectSlotsByName(CB_Spec_Tool)

    def retranslateUi(self, CB_Spec_Tool):
        _translate = QtCore.QCoreApplication.translate
        CB_Spec_Tool.setWindowTitle(_translate("CB_Spec_Tool", "CB_Spec_Tool"))
        self.LE_FinalCBSpec.setPlaceholderText(_translate("CB_Spec_Tool", "the final spec used to upload to Codebeamer"))
        self.LE_CB_Spec_FromCB.setPlaceholderText(_translate("CB_Spec_Tool", "the Spec download from Codebeamer"))
        self.Lable_CB_Spec.setText(_translate("CB_Spec_Tool", "CB_Spec"))
        self.BT_Upload2CB_1stTime.setText(_translate("CB_Spec_Tool", "Upload_1stTime"))
        self.BT_Replace_DoosID.setText(_translate("CB_Spec_Tool", "Replace_DoorsID"))
        self.LE_CB_Spec_Generate.setPlaceholderText(_translate("CB_Spec_Tool", "The spec generante by this tool"))
        self.BT_CB_Spec_Generate.setText(_translate("CB_Spec_Tool", "Browse"))
        self.BT_FinalCBSpec.setText(_translate("CB_Spec_Tool", "Browse"))
        self.Lable_CB_Spec_FromCB.setText(_translate("CB_Spec_Tool", "CB_Spec_FromCB"))
        self.LE_CaseTrackerID.setPlaceholderText(_translate("CB_Spec_Tool", "The Case TrackerID in CodeBearmer"))
        self.BT_Generate_Init.setText(_translate("CB_Spec_Tool", "Generate_Init"))
        self.Lable_CB_Spec_Folder_ID.setText(_translate("CB_Spec_Tool", "CB_Spec_Folder_ID"))
        self.BT_LookUp.setText(_translate("CB_Spec_Tool", "Browse"))
        self.LE_Release.setPlaceholderText(_translate("CB_Spec_Tool", "the Relese version in CodeBeamer"))
        self.LE_CB_Spec_Folder_ID.setPlaceholderText(_translate("CB_Spec_Tool", "the CodeBeamerID of the Spec Folder "))
        self.Lable_Release.setText(_translate("CB_Spec_Tool", "Release"))
        self.Lable_LookUp.setText(_translate("CB_Spec_Tool", "Requirement_Lookup"))
        self.BT_Generate_Modify.setText(_translate("CB_Spec_Tool", "Generate_Modify"))
        self.BT_CB_Spec.setText(_translate("CB_Spec_Tool", "Browse"))
        self.Lable_Test_Spec.setText(_translate("CB_Spec_Tool", "Test_Spec"))
        self.BT_Test_Spec.setText(_translate("CB_Spec_Tool", "Browse"))
        self.Lable_CaseTrackerID.setText(_translate("CB_Spec_Tool", "CaseTrackerID"))
        self.Lable_CB_Spec_Generate.setText(_translate("CB_Spec_Tool", "CB_Spec_Generate"))
        self.Lable_FinalCBSpec.setText(_translate("CB_Spec_Tool", "FinalCBSpec"))
        self.BT_CB_Spec_FromCB.setText(_translate("CB_Spec_Tool", "Browse"))
        self.BT_Upload2CB.setText(_translate("CB_Spec_Tool", "Upload2CB"))
        self.BT_Upload2CB_Modify.setText(_translate("CB_Spec_Tool", "Upload_Modify"))
        self.BT_DownloadCBSpec.setText(_translate("CB_Spec_Tool", "DownloadCBSpec"))
