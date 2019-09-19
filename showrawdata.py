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
        Dialog.resize(538, 742)
        self.rawdataShowTableWidget = QtWidgets.QTableWidget(Dialog)
        self.rawdataShowTableWidget.setGeometry(QtCore.QRect(0, 0, 531, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawdataShowTableWidget.sizePolicy().hasHeightForWidth())
        self.rawdataShowTableWidget.setSizePolicy(sizePolicy)
        self.rawdataShowTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rawdataShowTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rawdataShowTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.rawdataShowTableWidget.setAutoScrollMargin(0)
        self.rawdataShowTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rawdataShowTableWidget.setAlternatingRowColors(False)
        self.rawdataShowTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.rawdataShowTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.rawdataShowTableWidget.setShowGrid(True)
        self.rawdataShowTableWidget.setRowCount(33)
        self.rawdataShowTableWidget.setColumnCount(19)
        self.rawdataShowTableWidget.setObjectName("rawdataShowTableWidget")
        self.rawdataShowTableWidget.horizontalHeader().setVisible(False)
        self.rawdataShowTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.rawdataShowTableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.rawdataShowTableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.rawdataShowTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.rawdataShowTableWidget.horizontalHeader().setStretchLastSection(False)
        self.rawdataShowTableWidget.verticalHeader().setVisible(False)
        self.rawdataShowTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.rawdataShowTableWidget.verticalHeader().setDefaultSectionSize(10)
        self.rawdataShowTableWidget.verticalHeader().setMinimumSectionSize(10)
        self.rawdataShowTableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
