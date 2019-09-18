# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\newmonitor\showrawdata.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.rawdataShowTableWidget = QtWidgets.QTableWidget(Dialog)
        self.rawdataShowTableWidget.setGeometry(QtCore.QRect(0, 0, 481, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawdataShowTableWidget.sizePolicy().hasHeightForWidth())
        self.rawdataShowTableWidget.setSizePolicy(sizePolicy)
        self.rawdataShowTableWidget.setRowCount(12)
        self.rawdataShowTableWidget.setColumnCount(6)
        self.rawdataShowTableWidget.setObjectName("rawdataShowTableWidget")
        self.rawdataShowTableWidget.horizontalHeader().setDefaultSectionSize(69)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
