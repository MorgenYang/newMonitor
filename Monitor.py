from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import adb
from threading import Thread
import time
import os
import re
from PyQt5.QtGui import QIcon, QIntValidator, QRegExpValidator
import pyperclip
import math
from PyQt5.QtCore import QRegExp


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.uiThreadInitHistory = Thread(target=self.ui.initHistoryFunc)
        self.uiThreadInitHistory.start()
        self.uiThreadInitSettingsUi = Thread(target=self.ui.initSettingsUi())
        self.uiThreadInitSettingsUi.start()
        self.uiThreadSetRegExp = Thread(target=self.ui.setRegExp())
        self.uiThreadSetRegExp.start()
        self.uiThreadLoadLatestTouchInfoConfig = Thread(target=self.ui.loadLatestTouchInfoConfig())
        self.uiThreadLoadLatestTouchInfoConfig.start()
        self.uiThreadInitSelectProjectItems = Thread(target=self.ui.initSelectProjectItems(True))
        self.uiThreadInitSelectProjectItems.start()
        self.uiThreadBindEventFunc = Thread(target=self.ui.bindEventFunc())
        self.uiThreadBindEventFunc.start()
        self.statusBar().addWidget(QLabel("Ready"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        i = QIcon("./img/himax_logo.ico")
        MainWindow.setWindowIcon(i)
        MainWindow.resize(877, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(680, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.TabMainWindow = QtWidgets.QTabWidget(self.centralwidget)
        self.TabMainWindow.setGeometry(QtCore.QRect(1, 1, 861, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.TabMainWindow.sizePolicy().hasHeightForWidth())
        self.TabMainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TabMainWindow.setFont(font)
        self.TabMainWindow.setObjectName("TabMainWindow")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.touchInfoGroupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.touchInfoGroupBox.setGeometry(QtCore.QRect(0, 0, 671, 81))
        self.touchInfoGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.touchInfoGroupBox.setObjectName("touchInfoGroupBox")
        self.touchInfoRXLineEdit = QtWidgets.QLineEdit(self.touchInfoGroupBox)
        self.touchInfoRXLineEdit.setGeometry(QtCore.QRect(30, 20, 50, 20))
        self.touchInfoRXLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoRXLineEdit.setMaxLength(2)
        self.touchInfoRXLineEdit.setObjectName("touchInfoRXLineEdit")
        self.touchInfoTXLineEdit = QtWidgets.QLineEdit(self.touchInfoGroupBox)
        self.touchInfoTXLineEdit.setGeometry(QtCore.QRect(30, 45, 50, 20))
        self.touchInfoTXLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoTXLineEdit.setMaxLength(2)
        self.touchInfoTXLineEdit.setObjectName("touchInfoTXLineEdit")
        self.touchInfoRXLabel = QtWidgets.QLabel(self.touchInfoGroupBox)
        self.touchInfoRXLabel.setGeometry(QtCore.QRect(10, 20, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touchInfoRXLabel.setFont(font)
        self.touchInfoRXLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoRXLabel.setObjectName("touchInfoRXLabel")
        self.touchInfoTXLabel = QtWidgets.QLabel(self.touchInfoGroupBox)
        self.touchInfoTXLabel.setGeometry(QtCore.QRect(10, 45, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touchInfoTXLabel.setFont(font)
        self.touchInfoTXLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoTXLabel.setObjectName("touchInfoTXLabel")
        self.touchInfoRexYLabel = QtWidgets.QLabel(self.touchInfoGroupBox)
        self.touchInfoRexYLabel.setGeometry(QtCore.QRect(100, 45, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touchInfoRexYLabel.setFont(font)
        self.touchInfoRexYLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoRexYLabel.setObjectName("touchInfoRexYLabel")
        self.touchInfoRexXLabel = QtWidgets.QLabel(self.touchInfoGroupBox)
        self.touchInfoRexXLabel.setGeometry(QtCore.QRect(100, 20, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touchInfoRexXLabel.setFont(font)
        self.touchInfoRexXLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoRexXLabel.setObjectName("touchInfoRexXLabel")
        self.touchInfoResXLineEdit = QtWidgets.QLineEdit(self.touchInfoGroupBox)
        self.touchInfoResXLineEdit.setGeometry(QtCore.QRect(150, 20, 60, 20))
        self.touchInfoResXLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoResXLineEdit.setMaxLength(4)
        self.touchInfoResXLineEdit.setObjectName("touchInfoResXLineEdit")
        self.touchInfoResYLineEdit = QtWidgets.QLineEdit(self.touchInfoGroupBox)
        self.touchInfoResYLineEdit.setGeometry(QtCore.QRect(150, 45, 60, 20))
        self.touchInfoResYLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.touchInfoResYLineEdit.setMaxLength(4)
        self.touchInfoResYLineEdit.setObjectName("touchInfoResYLineEdit")
        self.settingsGroupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.settingsGroupBox.setGeometry(QtCore.QRect(0, 80, 671, 381))
        self.settingsGroupBox.setBaseSize(QtCore.QSize(0, 0))
        self.settingsGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.pathV1RadioButton = QtWidgets.QRadioButton(self.settingsGroupBox)
        self.pathV1RadioButton.setGeometry(QtCore.QRect(130, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathV1RadioButton.setFont(font)
        self.pathV1RadioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pathV1RadioButton.setMouseTracking(True)
        self.pathV1RadioButton.setTabletTracking(False)
        self.pathV1RadioButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pathV1RadioButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathV1RadioButton.setObjectName("pathV1RadioButton")
        self.pathV2RadioButton = QtWidgets.QRadioButton(self.settingsGroupBox)
        self.pathV2RadioButton.setGeometry(QtCore.QRect(170, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathV2RadioButton.setFont(font)
        self.pathV2RadioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pathV2RadioButton.setMouseTracking(True)
        self.pathV2RadioButton.setTabletTracking(False)
        self.pathV2RadioButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pathV2RadioButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathV2RadioButton.setObjectName("pathV2RadioButton")
        self.pathDriVerLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathDriVerLabel.setGeometry(QtCore.QRect(10, 20, 120, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pathDriVerLabel.setFont(font)
        self.pathDriVerLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDriVerLabel.setObjectName("pathDriVerLabel")
        self.pathDiagLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathDiagLabel.setGeometry(QtCore.QRect(0, 50, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathDiagLabel.setFont(font)
        self.pathDiagLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDiagLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathDiagLabel.setObjectName("pathDiagLabel")
        self.pathRegLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathRegLabel.setGeometry(QtCore.QRect(0, 73, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathRegLabel.setFont(font)
        self.pathRegLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathRegLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathRegLabel.setObjectName("pathRegLabel")
        self.pathResetLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathResetLabel.setGeometry(QtCore.QRect(0, 96, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathResetLabel.setFont(font)
        self.pathResetLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathResetLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathResetLabel.setObjectName("pathResetLabel")
        self.pathIntenLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathIntenLabel.setGeometry(QtCore.QRect(0, 119, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathIntenLabel.setFont(font)
        self.pathIntenLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathIntenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathIntenLabel.setObjectName("pathIntenLabel")
        self.pathDiagarrLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathDiagarrLabel.setGeometry(QtCore.QRect(0, 142, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathDiagarrLabel.setFont(font)
        self.pathDiagarrLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDiagarrLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathDiagarrLabel.setObjectName("pathDiagarrLabel")
        self.pathSenseonoffLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathSenseonoffLabel.setGeometry(QtCore.QRect(0, 165, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathSenseonoffLabel.setFont(font)
        self.pathSenseonoffLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathSenseonoffLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathSenseonoffLabel.setObjectName("pathSenseonoffLabel")
        self.pathStackLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathStackLabel.setGeometry(QtCore.QRect(0, 199, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathStackLabel.setFont(font)
        self.pathStackLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathStackLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathStackLabel.setObjectName("pathStackLabel")
        self.pathDebugLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathDebugLabel.setGeometry(QtCore.QRect(0, 231, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathDebugLabel.setFont(font)
        self.pathDebugLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDebugLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathDebugLabel.setObjectName("pathDebugLabel")
        self.pathSelftestLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathSelftestLabel.setGeometry(QtCore.QRect(0, 254, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathSelftestLabel.setFont(font)
        self.pathSelftestLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathSelftestLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathSelftestLabel.setObjectName("pathSelftestLabel")
        self.pathFlashdumpLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathFlashdumpLabel.setGeometry(QtCore.QRect(0, 277, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathFlashdumpLabel.setFont(font)
        self.pathFlashdumpLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathFlashdumpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathFlashdumpLabel.setObjectName("pathFlashdumpLabel")
        self.pathHXFolderLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathHXFolderLabel.setGeometry(QtCore.QRect(0, 307, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathHXFolderLabel.setFont(font)
        self.pathHXFolderLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathHXFolderLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathHXFolderLabel.setObjectName("pathHXFolderLabel")
        self.pathFWLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathFWLabel.setGeometry(QtCore.QRect(0, 330, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathFWLabel.setFont(font)
        self.pathFWLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathFWLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathFWLabel.setObjectName("pathFWLabel")
        self.pathDiagLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathDiagLineEdit.setGeometry(QtCore.QRect(90, 50, 400, 20))
        self.pathDiagLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDiagLineEdit.setObjectName("pathDiagLineEdit")
        self.pathRegLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathRegLineEdit.setGeometry(QtCore.QRect(90, 73, 400, 20))
        self.pathRegLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathRegLineEdit.setObjectName("pathRegLineEdit")
        self.pathResetLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathResetLineEdit.setGeometry(QtCore.QRect(90, 96, 400, 20))
        self.pathResetLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathResetLineEdit.setObjectName("pathResetLineEdit")
        self.pathIntenLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathIntenLineEdit.setGeometry(QtCore.QRect(90, 119, 400, 20))
        self.pathIntenLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathIntenLineEdit.setObjectName("pathIntenLineEdit")
        self.pathDiagarrLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathDiagarrLineEdit.setGeometry(QtCore.QRect(90, 142, 400, 20))
        self.pathDiagarrLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDiagarrLineEdit.setObjectName("pathDiagarrLineEdit")
        self.pathSenseonoffLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathSenseonoffLineEdit.setGeometry(QtCore.QRect(90, 165, 400, 20))
        self.pathSenseonoffLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathSenseonoffLineEdit.setObjectName("pathSenseonoffLineEdit")
        self.pathStackLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathStackLineEdit.setGeometry(QtCore.QRect(90, 199, 400, 20))
        self.pathStackLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathStackLineEdit.setObjectName("pathStackLineEdit")
        self.pathDebugLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathDebugLineEdit.setGeometry(QtCore.QRect(90, 231, 400, 20))
        self.pathDebugLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathDebugLineEdit.setObjectName("pathDebugLineEdit")
        self.pathSelftestLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathSelftestLineEdit.setGeometry(QtCore.QRect(90, 254, 400, 20))
        self.pathSelftestLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathSelftestLineEdit.setObjectName("pathSelftestLineEdit")
        self.pathFlashdumpLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathFlashdumpLineEdit.setGeometry(QtCore.QRect(90, 277, 400, 20))
        self.pathFlashdumpLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathFlashdumpLineEdit.setObjectName("pathFlashdumpLineEdit")
        self.pathHXFolderLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathHXFolderLineEdit.setGeometry(QtCore.QRect(90, 307, 400, 20))
        self.pathHXFolderLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathHXFolderLineEdit.setObjectName("pathHXFolderLineEdit")
        self.pathFWLineEdit = QtWidgets.QLineEdit(self.settingsGroupBox)
        self.pathFWLineEdit.setGeometry(QtCore.QRect(90, 330, 400, 20))
        self.pathFWLineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathFWLineEdit.setObjectName("pathFWLineEdit")
        self.pathConmmentLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pathConmmentLabel.setGeometry(QtCore.QRect(210, 20, 310, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pathConmmentLabel.setFont(font)
        self.pathConmmentLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.pathConmmentLabel.setObjectName("pathConmmentLabel")
        self.settingsProComboBox = QtWidgets.QComboBox(self.settingsGroupBox)
        self.settingsProComboBox.setGeometry(QtCore.QRect(500, 70, 160, 25))
        self.settingsProComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsProComboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.settingsProComboBox.setObjectName("settingsProComboBox")
        self.conmment_2 = QtWidgets.QLabel(self.settingsGroupBox)
        self.conmment_2.setGeometry(QtCore.QRect(500, 50, 151, 16))
        self.conmment_2.setObjectName("conmment_2")
        self.conmment = QtWidgets.QLabel(self.settingsGroupBox)
        self.conmment.setGeometry(QtCore.QRect(500, 110, 171, 31))
        self.conmment.setAutoFillBackground(False)
        self.conmment.setObjectName("conmment")
        self.pathSavePushButton = QtWidgets.QPushButton(self.settingsGroupBox)
        self.pathSavePushButton.setGeometry(QtCore.QRect(500, 142, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pathSavePushButton.setFont(font)
        self.pathSavePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pathSavePushButton.setWhatsThis("")
        self.pathSavePushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pathSavePushButton.setObjectName("pathSavePushButton")
        self.TabMainWindow.addTab(self.tabSettings, "")
        self.tabOptions = QtWidgets.QWidget()
        self.tabOptions.setObjectName("tabOptions")
        self.wifiGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.wifiGroupBox.setGeometry(QtCore.QRect(0, 0, 670, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiGroupBox.setFont(font)
        self.wifiGroupBox.setToolTipDuration(-1)
        self.wifiGroupBox.setAutoFillBackground(False)
        self.wifiGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.wifiGroupBox.setObjectName("wifiGroupBox")
        self.wifiConnect = QtWidgets.QPushButton(self.wifiGroupBox)
        self.wifiConnect.setGeometry(QtCore.QRect(10, 15, 90, 30))
        self.wifiConnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiConnect.setFont(font)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiConnect.setFlat(False)
        self.wifiConnect.setObjectName("wifiConnect")
        self.wifiDisconnect = QtWidgets.QPushButton(self.wifiGroupBox)
        self.wifiDisconnect.setGeometry(QtCore.QRect(105, 15, 90, 30))
        self.wifiDisconnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiDisconnect.setFont(font)
        self.wifiDisconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiDisconnect.setCheckable(False)
        self.wifiDisconnect.setObjectName("wifiDisconnect")
        self.wifiReconnect = QtWidgets.QPushButton(self.wifiGroupBox)
        self.wifiReconnect.setGeometry(QtCore.QRect(200, 15, 90, 30))
        self.wifiReconnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiReconnect.setFont(font)
        self.wifiReconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiReconnect.setCheckable(False)
        self.wifiReconnect.setObjectName("wifiReconnect")
        self.wifiStatus = QtWidgets.QLabel(self.wifiGroupBox)
        self.wifiStatus.setGeometry(QtCore.QRect(290, 15, 110, 30))
        self.wifiStatus.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wifiStatus.setFont(font)
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.wifiStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiStatus.setWordWrap(False)
        self.wifiStatus.setObjectName("wifiStatus")
        self.root = QtWidgets.QPushButton(self.wifiGroupBox)
        self.root.setGeometry(QtCore.QRect(485, 15, 90, 30))
        self.root.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.root.setFont(font)
        self.root.setObjectName("root")
        self.adbStatus = QtWidgets.QLabel(self.wifiGroupBox)
        self.adbStatus.setGeometry(QtCore.QRect(575, 15, 100, 30))
        self.adbStatus.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.adbStatus.setFont(font)
        self.adbStatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.adbStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.adbStatus.setWordWrap(False)
        self.adbStatus.setObjectName("adbStatus")
        self.adbGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.adbGroupBox.setGeometry(QtCore.QRect(0, 50, 670, 86))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.adbGroupBox.setFont(font)
        self.adbGroupBox.setToolTipDuration(-1)
        self.adbGroupBox.setAutoFillBackground(False)
        self.adbGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.adbGroupBox.setObjectName("adbGroupBox")
        self.homekey = QtWidgets.QPushButton(self.adbGroupBox)
        self.homekey.setGeometry(QtCore.QRect(10, 50, 90, 30))
        self.homekey.setMinimumSize(QtCore.QSize(0, 0))
        self.homekey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homekey.setFont(font)
        self.homekey.setStyleSheet("color: rgb(0, 0, 0);")
        self.homekey.setObjectName("homekey")
        self.reboot = QtWidgets.QPushButton(self.adbGroupBox)
        self.reboot.setGeometry(QtCore.QRect(390, 15, 90, 30))
        self.reboot.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reboot.setFont(font)
        self.reboot.setStyleSheet("color: rgb(0, 0, 0);")
        self.reboot.setObjectName("reboot")
        self.volDown = QtWidgets.QPushButton(self.adbGroupBox)
        self.volDown.setGeometry(QtCore.QRect(295, 50, 90, 30))
        self.volDown.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volDown.setFont(font)
        self.volDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.volDown.setObjectName("volDown")
        self.backkey = QtWidgets.QPushButton(self.adbGroupBox)
        self.backkey.setGeometry(QtCore.QRect(105, 50, 90, 30))
        self.backkey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backkey.setFont(font)
        self.backkey.setStyleSheet("color: rgb(0, 0, 0);")
        self.backkey.setObjectName("backkey")
        self.volUp = QtWidgets.QPushButton(self.adbGroupBox)
        self.volUp.setGeometry(QtCore.QRect(200, 50, 90, 30))
        self.volUp.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volUp.setFont(font)
        self.volUp.setStyleSheet("color: rgb(0, 0, 0);")
        self.volUp.setObjectName("volUp")
        self.powerKey = QtWidgets.QPushButton(self.adbGroupBox)
        self.powerKey.setGeometry(QtCore.QRect(105, 15, 90, 30))
        self.powerKey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.powerKey.setFont(font)
        self.powerKey.setStyleSheet("color: rgb(0, 0, 0);")
        self.powerKey.setObjectName("powerKey")
        self.screenShot = QtWidgets.QPushButton(self.adbGroupBox)
        self.screenShot.setGeometry(QtCore.QRect(295, 15, 90, 30))
        self.screenShot.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.screenShot.setFont(font)
        self.screenShot.setStyleSheet("color: rgb(0, 0, 0);")
        self.screenShot.setObjectName("screenShot")
        self.openClosePoint = QtWidgets.QPushButton(self.adbGroupBox)
        self.openClosePoint.setGeometry(QtCore.QRect(200, 15, 90, 30))
        self.openClosePoint.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openClosePoint.setFont(font)
        self.openClosePoint.setStyleSheet("color: rgb(0, 0, 0);")
        self.openClosePoint.setObjectName("openClosePoint")
        self.opencmd = QtWidgets.QPushButton(self.adbGroupBox)
        self.opencmd.setGeometry(QtCore.QRect(390, 50, 90, 30))
        self.opencmd.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opencmd.setFont(font)
        self.opencmd.setStyleSheet("color: rgb(0, 0, 0);")
        self.opencmd.setObjectName("opencmd")
        self.hideShowVirtual = QtWidgets.QPushButton(self.adbGroupBox)
        self.hideShowVirtual.setGeometry(QtCore.QRect(10, 15, 90, 30))
        self.hideShowVirtual.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hideShowVirtual.setFont(font)
        self.hideShowVirtual.setStyleSheet("color: rgb(0, 0, 0);")
        self.hideShowVirtual.setObjectName("hideShowVirtual")
        self.shutDown = QtWidgets.QPushButton(self.adbGroupBox)
        self.shutDown.setGeometry(QtCore.QRect(485, 15, 90, 30))
        self.shutDown.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shutDown.setFont(font)
        self.shutDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.shutDown.setObjectName("shutDown")
        self.touchGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.touchGroupBox.setGeometry(QtCore.QRect(0, 135, 670, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touchGroupBox.setFont(font)
        self.touchGroupBox.setAutoFillBackground(False)
        self.touchGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.touchGroupBox.setObjectName("touchGroupBox")
        self.inten0 = QtWidgets.QPushButton(self.touchGroupBox)
        self.inten0.setGeometry(QtCore.QRect(485, 15, 90, 30))
        self.inten0.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inten0.setFont(font)
        self.inten0.setStyleSheet("color: rgb(0, 0, 0);")
        self.inten0.setObjectName("inten0")
        self.senseon = QtWidgets.QPushButton(self.touchGroupBox)
        self.senseon.setGeometry(QtCore.QRect(200, 15, 90, 30))
        self.senseon.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.senseon.setFont(font)
        self.senseon.setStyleSheet("color: rgb(0, 0, 0);")
        self.senseon.setObjectName("senseon")
        self.fwVersion = QtWidgets.QPushButton(self.touchGroupBox)
        self.fwVersion.setGeometry(QtCore.QRect(10, 15, 90, 30))
        self.fwVersion.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fwVersion.setFont(font)
        self.fwVersion.setStyleSheet("color: rgb(0, 0, 0);")
        self.fwVersion.setObjectName("fwVersion")
        self.selftest = QtWidgets.QPushButton(self.touchGroupBox)
        self.selftest.setGeometry(QtCore.QRect(295, 15, 90, 30))
        self.selftest.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selftest.setFont(font)
        self.selftest.setStyleSheet("color: rgb(0, 0, 0);")
        self.selftest.setObjectName("selftest")
        self.diagArr = QtWidgets.QPushButton(self.touchGroupBox)
        self.diagArr.setGeometry(QtCore.QRect(10, 50, 90, 30))
        self.diagArr.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diagArr.setFont(font)
        self.diagArr.setStyleSheet("color: rgb(0, 0, 0);")
        self.diagArr.setObjectName("diagArr")
        self.flashDump = QtWidgets.QPushButton(self.touchGroupBox)
        self.flashDump.setGeometry(QtCore.QRect(390, 15, 90, 30))
        self.flashDump.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flashDump.setFont(font)
        self.flashDump.setStyleSheet("color: rgb(0, 0, 0);")
        self.flashDump.setObjectName("flashDump")
        self.updateFWText = QtWidgets.QTextEdit(self.touchGroupBox)
        self.updateFWText.setGeometry(QtCore.QRect(290, 50, 80, 30))
        self.updateFWText.setMaximumSize(QtCore.QSize(100, 30))
        self.updateFWText.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFWText.setObjectName("updateFWText")
        self.reset = QtWidgets.QPushButton(self.touchGroupBox)
        self.reset.setGeometry(QtCore.QRect(105, 15, 90, 30))
        self.reset.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setStyleSheet("color: rgb(0, 0, 0);")
        self.reset.setObjectName("reset")
        self.updateFW = QtWidgets.QPushButton(self.touchGroupBox)
        self.updateFW.setGeometry(QtCore.QRect(200, 50, 90, 30))
        self.updateFW.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updateFW.setFont(font)
        self.updateFW.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFW.setObjectName("updateFW")
        self.diagArrText = QtWidgets.QLineEdit(self.touchGroupBox)
        self.diagArrText.setGeometry(QtCore.QRect(100, 50, 80, 30))
        self.diagArrText.setObjectName("diagArrText")
        self.debugType = QtWidgets.QPushButton(self.touchGroupBox)
        self.debugType.setGeometry(QtCore.QRect(390, 50, 90, 30))
        self.debugType.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debugType.setFont(font)
        self.debugType.setStyleSheet("color: rgb(0, 0, 0);")
        self.debugType.setObjectName("debugType")
        self.debugComboBox = QtWidgets.QComboBox(self.touchGroupBox)
        self.debugComboBox.setGeometry(QtCore.QRect(480, 51, 90, 28))
        self.debugComboBox.setCurrentText("")
        self.debugComboBox.setObjectName("debugComboBox")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.debugComboBox.addItem("")
        self.displayGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.displayGroupBox.setGeometry(QtCore.QRect(0, 220, 670, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.displayGroupBox.setFont(font)
        self.displayGroupBox.setAutoFillBackground(False)
        self.displayGroupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.displayGroupBox.setObjectName("displayGroupBox")
        self.openBlight = QtWidgets.QPushButton(self.displayGroupBox)
        self.openBlight.setGeometry(QtCore.QRect(200, 15, 90, 30))
        self.openBlight.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openBlight.setFont(font)
        self.openBlight.setStyleSheet("color: rgb(0, 0, 0);")
        self.openBlight.setObjectName("openBlight")
        self.d1129 = QtWidgets.QPushButton(self.displayGroupBox)
        self.d1129.setGeometry(QtCore.QRect(10, 15, 90, 30))
        self.d1129.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1129.setFont(font)
        self.d1129.setStyleSheet("color: rgb(0, 0, 0);")
        self.d1129.setObjectName("d1129")
        self.d2810 = QtWidgets.QPushButton(self.displayGroupBox)
        self.d2810.setGeometry(QtCore.QRect(105, 15, 90, 30))
        self.d2810.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d2810.setFont(font)
        self.d2810.setStyleSheet("color: rgb(0, 0, 0);")
        self.d2810.setObjectName("d2810")
        self.rawdataShowText = QtWidgets.QTextBrowser(self.tabOptions)
        self.rawdataShowText.setGeometry(QtCore.QRect(10, 268, 660, 185))
        self.rawdataShowText.setMaximumSize(QtCore.QSize(700, 205))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.TabMainWindow.addTab(self.tabOptions, "")
        self.tabRawdata = QtWidgets.QWidget()
        self.tabRawdata.setObjectName("tabRawdata")
        self.MainRawdataShowtableWidget = QtWidgets.QTableWidget(self.tabRawdata)
        self.MainRawdataShowtableWidget.setGeometry(QtCore.QRect(42, 0, 630, 450))
        self.MainRawdataShowtableWidget.setMinimumSize(QtCore.QSize(630, 0))
        self.MainRawdataShowtableWidget.setMaximumSize(QtCore.QSize(640, 482))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.MainRawdataShowtableWidget.setFont(font)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.setColumnCount(0)
        self.MainRawdataShowtableWidget.setRowCount(0)
        self.MainRawdataShowtableWidget.verticalHeader().setVisible(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabRawdata)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 46, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rawdataRead = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rawdataRead.setMinimumSize(QtCore.QSize(0, 40))
        self.rawdataRead.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rawdataRead.setFont(font)
        self.rawdataRead.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rawdataRead.setStyleSheet("")
        self.rawdataRead.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/start_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rawdataRead.setIcon(icon)
        self.rawdataRead.setIconSize(QtCore.QSize(39, 39))
        self.rawdataRead.setObjectName("rawdataRead")
        self.verticalLayout.addWidget(self.rawdataRead)
        self.radioDC = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioDC.setMaximumSize(QtCore.QSize(50, 30))
        self.radioDC.setObjectName("radioDC")
        self.verticalLayout.addWidget(self.radioDC)
        self.radioIIR = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioIIR.setMaximumSize(QtCore.QSize(50, 30))
        self.radioIIR.setObjectName("radioIIR")
        self.verticalLayout.addWidget(self.radioIIR)
        self.radioTmp = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioTmp.setMaximumSize(QtCore.QSize(15, 30))
        self.radioTmp.setText("")
        self.radioTmp.setObjectName("radioTmp")
        self.verticalLayout.addWidget(self.radioTmp)
        self.textEditDiag = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEditDiag.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEditDiag.setFont(font)
        self.textEditDiag.setObjectName("textEditDiag")
        self.verticalLayout.addWidget(self.textEditDiag)
        self.log = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.log.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.recalled = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.recalled.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recalled.sizePolicy().hasHeightForWidth())
        self.recalled.setSizePolicy(sizePolicy)
        self.recalled.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recalled.setFont(font)
        self.recalled.setObjectName("recalled")
        self.verticalLayout.addWidget(self.recalled)
        self.timeLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.timeLineEdit.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.timeLineEdit.setFont(font)
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.verticalLayout.addWidget(self.timeLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.TabMainWindow.addTab(self.tabRawdata, "")
        self.tabRWRegister = QtWidgets.QWidget()
        self.tabRWRegister.setObjectName("tabRWRegister")
        self.pushButtonRead = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRead.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.pushButtonRead.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButtonRead.setFont(font)
        self.pushButtonRead.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButtonRead.setObjectName("pushButtonRead")
        self.textEditReadRegAddr = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditReadRegAddr.setGeometry(QtCore.QRect(0, 27, 100, 101))
        self.textEditReadRegAddr.setMaximumSize(QtCore.QSize(150, 170))
        self.textEditReadRegAddr.setObjectName("textEditReadRegAddr")
        self.textEditWriteVal3 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteVal3.setGeometry(QtCore.QRect(350, 90, 120, 25))
        self.textEditWriteVal3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal3.setObjectName("textEditWriteVal3")
        self.textEditWriteVal4 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteVal4.setGeometry(QtCore.QRect(350, 120, 120, 25))
        self.textEditWriteVal4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal4.setObjectName("textEditWriteVal4")
        self.textEditWriteVal2 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteVal2.setGeometry(QtCore.QRect(350, 60, 120, 25))
        self.textEditWriteVal2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal2.setObjectName("textEditWriteVal2")
        self.textEditWriteAddr1 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteAddr1.setGeometry(QtCore.QRect(220, 30, 120, 25))
        self.textEditWriteAddr1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr1.setObjectName("textEditWriteAddr1")
        self.textEditWriteAddr2 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteAddr2.setGeometry(QtCore.QRect(220, 60, 120, 25))
        self.textEditWriteAddr2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr2.setObjectName("textEditWriteAddr2")
        self.textEditWriteAddr0 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteAddr0.setGeometry(QtCore.QRect(220, 0, 120, 25))
        self.textEditWriteAddr0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr0.setObjectName("textEditWriteAddr0")
        self.textEditWriteVal1 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteVal1.setGeometry(QtCore.QRect(350, 30, 120, 25))
        self.textEditWriteVal1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal1.setObjectName("textEditWriteVal1")
        self.pushButtonRegWrite0 = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRegWrite0.setGeometry(QtCore.QRect(110, 0, 100, 25))
        self.pushButtonRegWrite0.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite0.setObjectName("pushButtonRegWrite0")
        self.pushButtonRegWrite1 = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRegWrite1.setGeometry(QtCore.QRect(110, 30, 100, 25))
        self.pushButtonRegWrite1.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite1.setObjectName("pushButtonRegWrite1")
        self.textEditWriteVal0 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteVal0.setGeometry(QtCore.QRect(350, 0, 120, 25))
        self.textEditWriteVal0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal0.setObjectName("textEditWriteVal0")
        self.textEditWriteAddr3 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteAddr3.setGeometry(QtCore.QRect(220, 90, 120, 25))
        self.textEditWriteAddr3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr3.setObjectName("textEditWriteAddr3")
        self.pushButtonRegWrite2 = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRegWrite2.setGeometry(QtCore.QRect(110, 60, 100, 25))
        self.pushButtonRegWrite2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite2.setObjectName("pushButtonRegWrite2")
        self.textEditWriteAddr4 = QtWidgets.QTextEdit(self.tabRWRegister)
        self.textEditWriteAddr4.setGeometry(QtCore.QRect(220, 120, 120, 25))
        self.textEditWriteAddr4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr4.setObjectName("textEditWriteAddr4")
        self.pushButtonRegWrite4 = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRegWrite4.setGeometry(QtCore.QRect(110, 120, 100, 25))
        self.pushButtonRegWrite4.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite4.setObjectName("pushButtonRegWrite4")
        self.pushButtonRegWrite3 = QtWidgets.QPushButton(self.tabRWRegister)
        self.pushButtonRegWrite3.setGeometry(QtCore.QRect(110, 90, 100, 25))
        self.pushButtonRegWrite3.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite3.setObjectName("pushButtonRegWrite3")
        self.tpReglengthLabel = QtWidgets.QLabel(self.tabRWRegister)
        self.tpReglengthLabel.setGeometry(QtCore.QRect(5, 128, 50, 20))
        self.tpReglengthLabel.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tpReglengthLabel.setFont(font)
        self.tpReglengthLabel.setStyleSheet("color: rgb(0, 85, 255);")
        self.tpReglengthLabel.setObjectName("tpReglengthLabel")
        self.reglength = QtWidgets.QComboBox(self.tabRWRegister)
        self.reglength.setGeometry(QtCore.QRect(70, 128, 30, 20))
        self.reglength.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.reglength.setObjectName("reglength")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.reglength.addItem("")
        self.readRegValShowText = QtWidgets.QTextBrowser(self.tabRWRegister)
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 150, 670, 300))
        self.readRegValShowText.setMinimumSize(QtCore.QSize(670, 300))
        self.readRegValShowText.setMaximumSize(QtCore.QSize(670, 300))
        self.readRegValShowText.setObjectName("readRegValShowText")
        self.TabMainWindow.addTab(self.tabRWRegister, "")
        self.tabDDRegister = QtWidgets.QWidget()
        self.tabDDRegister.setObjectName("tabDDRegister")
        self.ddRegGroupBox1 = QtWidgets.QGroupBox(self.tabDDRegister)
        self.ddRegGroupBox1.setGeometry(QtCore.QRect(0, 0, 675, 129))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ddRegGroupBox1.setFont(font)
        self.ddRegGroupBox1.setStyleSheet("color: rgb(255, 0, 0);")
        self.ddRegGroupBox1.setObjectName("ddRegGroupBox1")
        self.G1DDRead = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDRead.setGeometry(QtCore.QRect(0, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDRead.setFont(font)
        self.G1DDRead.setObjectName("G1DDRead")
        self.G1AddrlineEdit = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1AddrlineEdit.setGeometry(QtCore.QRect(80, 16, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1AddrlineEdit.setFont(font)
        self.G1AddrlineEdit.setObjectName("G1AddrlineEdit")
        self.G1DDWrite = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDWrite.setGeometry(QtCore.QRect(200, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDWrite.setFont(font)
        self.G1DDWrite.setObjectName("G1DDWrite")
        # for i in range(64):
        #     setattr(self, "G1lineEdit%s" % str(i + 1), QtWidgets.QLineEdit(self.ddRegGroupBox1))
        #     m = getattr(self, "G1lineEdit%s" % str(i + 1))
        #     m = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit1 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit1.setGeometry(QtCore.QRect(0, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit1.setFont(font)
        self.G1lineEdit1.setStyleSheet("")
        self.G1lineEdit1.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit1.setObjectName("G1lineEdit1")
        self.G1lineEdit2 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit2.setGeometry(QtCore.QRect(40, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit2.setFont(font)
        self.G1lineEdit2.setStyleSheet("")
        self.G1lineEdit2.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit2.setObjectName("G1lineEdit2")
        self.G1lineEdit3 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit3.setGeometry(QtCore.QRect(80, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit3.setFont(font)
        self.G1lineEdit3.setStyleSheet("")
        self.G1lineEdit3.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit3.setObjectName("G1lineEdit3")
        self.G1lineEdit4 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit4.setGeometry(QtCore.QRect(120, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit4.setFont(font)
        self.G1lineEdit4.setStyleSheet("")
        self.G1lineEdit4.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit4.setObjectName("G1lineEdit4")
        self.G1lineEdit5 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit5.setGeometry(QtCore.QRect(160, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit5.setFont(font)
        self.G1lineEdit5.setStyleSheet("")
        self.G1lineEdit5.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit5.setObjectName("G1lineEdit5")
        self.G1lineEdit6 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit6.setGeometry(QtCore.QRect(200, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit6.setFont(font)
        self.G1lineEdit6.setStyleSheet("")
        self.G1lineEdit6.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit6.setObjectName("G1lineEdit6")
        self.G1lineEdit7 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit7.setGeometry(QtCore.QRect(240, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit7.setFont(font)
        self.G1lineEdit7.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit7.setObjectName("G1lineEdit7")
        self.G1lineEdit8 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit8.setGeometry(QtCore.QRect(280, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit8.setFont(font)
        self.G1lineEdit8.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit8.setObjectName("G1lineEdit8")
        self.G1lineEdit9 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit9.setGeometry(QtCore.QRect(340, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit9.setFont(font)
        self.G1lineEdit9.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit9.setObjectName("G1lineEdit9")
        self.G1lineEdit10 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit10.setGeometry(QtCore.QRect(380, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit10.setFont(font)
        self.G1lineEdit10.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit10.setObjectName("G1lineEdit10")
        self.G1lineEdit11 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit11.setGeometry(QtCore.QRect(420, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit11.setFont(font)
        self.G1lineEdit11.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit11.setObjectName("G1lineEdit11")
        self.G1lineEdit12 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit12.setGeometry(QtCore.QRect(460, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit12.setFont(font)
        self.G1lineEdit12.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit12.setObjectName("G1lineEdit12")
        self.G1lineEdit21 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit21.setGeometry(QtCore.QRect(160, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit21.setFont(font)
        self.G1lineEdit21.setStyleSheet("")
        self.G1lineEdit21.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit21.setObjectName("G1lineEdit21")
        self.G1lineEdit19 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit19.setGeometry(QtCore.QRect(80, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit19.setFont(font)
        self.G1lineEdit19.setStyleSheet("")
        self.G1lineEdit19.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit19.setObjectName("G1lineEdit19")
        self.G1lineEdit22 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit22.setGeometry(QtCore.QRect(200, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit22.setFont(font)
        self.G1lineEdit22.setStyleSheet("")
        self.G1lineEdit22.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit22.setObjectName("G1lineEdit22")
        self.G1lineEdit24 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit24.setGeometry(QtCore.QRect(280, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit24.setFont(font)
        self.G1lineEdit24.setStyleSheet("")
        self.G1lineEdit24.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit24.setObjectName("G1lineEdit24")
        self.G1lineEdit15 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit15.setGeometry(QtCore.QRect(580, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit15.setFont(font)
        self.G1lineEdit15.setStyleSheet("")
        self.G1lineEdit15.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit15.setObjectName("G1lineEdit15")
        self.G1lineEdit20 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit20.setGeometry(QtCore.QRect(120, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit20.setFont(font)
        self.G1lineEdit20.setStyleSheet("")
        self.G1lineEdit20.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit20.setObjectName("G1lineEdit20")
        self.G1lineEdit13 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit13.setGeometry(QtCore.QRect(500, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit13.setFont(font)
        self.G1lineEdit13.setStyleSheet("")
        self.G1lineEdit13.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit13.setObjectName("G1lineEdit13")
        self.G1lineEdit14 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit14.setGeometry(QtCore.QRect(540, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit14.setFont(font)
        self.G1lineEdit14.setStyleSheet("")
        self.G1lineEdit14.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit14.setObjectName("G1lineEdit14")
        self.G1lineEdit23 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit23.setGeometry(QtCore.QRect(240, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit23.setFont(font)
        self.G1lineEdit23.setStyleSheet("")
        self.G1lineEdit23.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit23.setObjectName("G1lineEdit23")
        self.G1lineEdit16 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit16.setGeometry(QtCore.QRect(620, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit16.setFont(font)
        self.G1lineEdit16.setStyleSheet("")
        self.G1lineEdit16.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit16.setObjectName("G1lineEdit16")
        self.G1lineEdit18 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit18.setGeometry(QtCore.QRect(40, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit18.setFont(font)
        self.G1lineEdit18.setStyleSheet("")
        self.G1lineEdit18.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit18.setObjectName("G1lineEdit18")
        self.G1lineEdit17 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit17.setGeometry(QtCore.QRect(0, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit17.setFont(font)
        self.G1lineEdit17.setStyleSheet("")
        self.G1lineEdit17.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit17.setObjectName("G1lineEdit17")
        self.G1lineEdit28 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit28.setGeometry(QtCore.QRect(460, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit28.setFont(font)
        self.G1lineEdit28.setStyleSheet("")
        self.G1lineEdit28.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit28.setObjectName("G1lineEdit28")
        self.G1lineEdit35 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit35.setGeometry(QtCore.QRect(80, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit35.setFont(font)
        self.G1lineEdit35.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit35.setObjectName("G1lineEdit35")
        self.G1lineEdit29 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit29.setGeometry(QtCore.QRect(500, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit29.setFont(font)
        self.G1lineEdit29.setStyleSheet("")
        self.G1lineEdit29.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit29.setObjectName("G1lineEdit29")
        self.G1lineEdit33 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit33.setGeometry(QtCore.QRect(0, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit33.setFont(font)
        self.G1lineEdit33.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit33.setObjectName("G1lineEdit33")
        self.G1lineEdit34 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit34.setGeometry(QtCore.QRect(40, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit34.setFont(font)
        self.G1lineEdit34.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit34.setObjectName("G1lineEdit34")
        self.G1lineEdit32 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit32.setGeometry(QtCore.QRect(620, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit32.setFont(font)
        self.G1lineEdit32.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit32.setObjectName("G1lineEdit32")
        self.G1lineEdit26 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit26.setGeometry(QtCore.QRect(380, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit26.setFont(font)
        self.G1lineEdit26.setStyleSheet("")
        self.G1lineEdit26.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit26.setObjectName("G1lineEdit26")
        self.G1lineEdit30 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit30.setGeometry(QtCore.QRect(540, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit30.setFont(font)
        self.G1lineEdit30.setStyleSheet("")
        self.G1lineEdit30.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit30.setObjectName("G1lineEdit30")
        self.G1lineEdit27 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit27.setGeometry(QtCore.QRect(420, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit27.setFont(font)
        self.G1lineEdit27.setStyleSheet("")
        self.G1lineEdit27.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit27.setObjectName("G1lineEdit27")
        self.G1lineEdit25 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit25.setGeometry(QtCore.QRect(340, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit25.setFont(font)
        self.G1lineEdit25.setStyleSheet("")
        self.G1lineEdit25.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit25.setObjectName("G1lineEdit25")
        self.G1lineEdit31 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit31.setGeometry(QtCore.QRect(580, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit31.setFont(font)
        self.G1lineEdit31.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit31.setObjectName("G1lineEdit31")
        self.G1lineEdit36 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit36.setGeometry(QtCore.QRect(120, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit36.setFont(font)
        self.G1lineEdit36.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit36.setObjectName("G1lineEdit36")
        self.G1lineEdit47 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit47.setGeometry(QtCore.QRect(580, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit47.setFont(font)
        self.G1lineEdit47.setStyleSheet("")
        self.G1lineEdit47.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit47.setObjectName("G1lineEdit47")
        self.G1lineEdit38 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit38.setGeometry(QtCore.QRect(200, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit38.setFont(font)
        self.G1lineEdit38.setStyleSheet("")
        self.G1lineEdit38.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit38.setObjectName("G1lineEdit38")
        self.G1lineEdit46 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit46.setGeometry(QtCore.QRect(540, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit46.setFont(font)
        self.G1lineEdit46.setStyleSheet("")
        self.G1lineEdit46.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit46.setObjectName("G1lineEdit46")
        self.G1lineEdit40 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit40.setGeometry(QtCore.QRect(280, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit40.setFont(font)
        self.G1lineEdit40.setStyleSheet("")
        self.G1lineEdit40.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit40.setObjectName("G1lineEdit40")
        self.G1lineEdit48 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit48.setGeometry(QtCore.QRect(620, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit48.setFont(font)
        self.G1lineEdit48.setStyleSheet("")
        self.G1lineEdit48.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit48.setObjectName("G1lineEdit48")
        self.G1lineEdit41 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit41.setGeometry(QtCore.QRect(340, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit41.setFont(font)
        self.G1lineEdit41.setStyleSheet("")
        self.G1lineEdit41.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit41.setObjectName("G1lineEdit41")
        self.G1lineEdit44 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit44.setGeometry(QtCore.QRect(460, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit44.setFont(font)
        self.G1lineEdit44.setStyleSheet("")
        self.G1lineEdit44.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit44.setObjectName("G1lineEdit44")
        self.G1lineEdit43 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit43.setGeometry(QtCore.QRect(420, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit43.setFont(font)
        self.G1lineEdit43.setStyleSheet("")
        self.G1lineEdit43.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit43.setObjectName("G1lineEdit43")
        self.G1lineEdit37 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit37.setGeometry(QtCore.QRect(160, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit37.setFont(font)
        self.G1lineEdit37.setStyleSheet("")
        self.G1lineEdit37.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit37.setObjectName("G1lineEdit37")
        self.G1lineEdit45 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit45.setGeometry(QtCore.QRect(500, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit45.setFont(font)
        self.G1lineEdit45.setStyleSheet("")
        self.G1lineEdit45.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit45.setObjectName("G1lineEdit45")
        self.G1lineEdit39 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit39.setGeometry(QtCore.QRect(240, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit39.setFont(font)
        self.G1lineEdit39.setStyleSheet("")
        self.G1lineEdit39.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit39.setObjectName("G1lineEdit39")
        self.G1lineEdit42 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit42.setGeometry(QtCore.QRect(380, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit42.setFont(font)
        self.G1lineEdit42.setStyleSheet("")
        self.G1lineEdit42.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit42.setObjectName("G1lineEdit42")
        self.G1DDClear = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDClear.setGeometry(QtCore.QRect(580, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDClear.setFont(font)
        self.G1DDClear.setObjectName("G1DDClear")
        self.G1DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDCopy.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDCopy.setFont(font)
        self.G1DDCopy.setObjectName("G1DDCopy")
        self.G1lineEdit49 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit49.setGeometry(QtCore.QRect(0, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit49.setFont(font)
        self.G1lineEdit49.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit49.setObjectName("G1lineEdit49")
        self.G1lineEdit50 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit50.setGeometry(QtCore.QRect(40, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit50.setFont(font)
        self.G1lineEdit50.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit50.setObjectName("G1lineEdit50")
        self.G1lineEdit51 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit51.setGeometry(QtCore.QRect(80, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit51.setFont(font)
        self.G1lineEdit51.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit51.setObjectName("G1lineEdit51")
        self.G1lineEdit52 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit52.setGeometry(QtCore.QRect(120, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit52.setFont(font)
        self.G1lineEdit52.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit52.setObjectName("G1lineEdit52")
        self.G1lineEdit53 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit53.setGeometry(QtCore.QRect(160, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit53.setFont(font)
        self.G1lineEdit53.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit53.setObjectName("G1lineEdit53")
        self.G1lineEdit54 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit54.setGeometry(QtCore.QRect(200, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit54.setFont(font)
        self.G1lineEdit54.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit54.setObjectName("G1lineEdit54")
        self.G1lineEdit55 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit55.setGeometry(QtCore.QRect(240, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit55.setFont(font)
        self.G1lineEdit55.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit55.setObjectName("G1lineEdit55")
        self.G1lineEdit56 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit56.setGeometry(QtCore.QRect(280, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit56.setFont(font)
        self.G1lineEdit56.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit56.setObjectName("G1lineEdit56")
        self.G1lineEdit57 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit57.setGeometry(QtCore.QRect(340, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit57.setFont(font)
        self.G1lineEdit57.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit57.setObjectName("G1lineEdit57")
        self.G1lineEdit58 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit58.setGeometry(QtCore.QRect(380, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit58.setFont(font)
        self.G1lineEdit58.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit58.setObjectName("G1lineEdit58")
        self.G1lineEdit59 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit59.setGeometry(QtCore.QRect(420, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit59.setFont(font)
        self.G1lineEdit59.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit59.setObjectName("G1lineEdit59")
        self.G1lineEdit60 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit60.setGeometry(QtCore.QRect(460, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit60.setFont(font)
        self.G1lineEdit60.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit60.setObjectName("G1lineEdit60")
        self.G1lineEdit61 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit61.setGeometry(QtCore.QRect(500, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit61.setFont(font)
        self.G1lineEdit61.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit61.setObjectName("G1lineEdit61")
        self.G1lineEdit62 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit62.setGeometry(QtCore.QRect(540, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit62.setFont(font)
        self.G1lineEdit62.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit62.setObjectName("G1lineEdit62")
        self.G1lineEdit63 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit63.setGeometry(QtCore.QRect(580, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit63.setFont(font)
        self.G1lineEdit63.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit63.setObjectName("G1lineEdit63")
        self.G1lineEdit64 = QtWidgets.QLineEdit(self.ddRegGroupBox1)
        self.G1lineEdit64.setGeometry(QtCore.QRect(620, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1lineEdit64.setFont(font)
        self.G1lineEdit64.setAlignment(QtCore.Qt.AlignCenter)
        self.G1lineEdit64.setObjectName("G1lineEdit64")
        self.ddRegGroupBox2 = QtWidgets.QGroupBox(self.tabDDRegister)
        self.ddRegGroupBox2.setGeometry(QtCore.QRect(0, 140, 675, 129))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ddRegGroupBox2.setFont(font)
        self.ddRegGroupBox2.setStyleSheet("")
        self.ddRegGroupBox2.setObjectName("ddRegGroupBox2")
        self.G2DDRead = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDRead.setGeometry(QtCore.QRect(0, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDRead.setFont(font)
        self.G2DDRead.setObjectName("G2DDRead")
        self.G2AddrlineEdit = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2AddrlineEdit.setGeometry(QtCore.QRect(80, 16, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2AddrlineEdit.setFont(font)
        self.G2AddrlineEdit.setObjectName("G2AddrlineEdit")
        self.G2DDWrite = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDWrite.setGeometry(QtCore.QRect(200, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDWrite.setFont(font)
        self.G2DDWrite.setObjectName("G2DDWrite")
        self.G2lineEdit1 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit1.setGeometry(QtCore.QRect(0, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit1.setFont(font)
        self.G2lineEdit1.setStyleSheet("")
        self.G2lineEdit1.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit1.setObjectName("G2lineEdit1")
        self.G2lineEdit2 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit2.setGeometry(QtCore.QRect(40, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit2.setFont(font)
        self.G2lineEdit2.setStyleSheet("")
        self.G2lineEdit2.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit2.setObjectName("G2lineEdit2")
        self.G2lineEdit3 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit3.setGeometry(QtCore.QRect(80, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit3.setFont(font)
        self.G2lineEdit3.setStyleSheet("")
        self.G2lineEdit3.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit3.setObjectName("G2lineEdit3")
        self.G2lineEdit4 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit4.setGeometry(QtCore.QRect(120, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit4.setFont(font)
        self.G2lineEdit4.setStyleSheet("")
        self.G2lineEdit4.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit4.setObjectName("G2lineEdit4")
        self.G2lineEdit5 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit5.setGeometry(QtCore.QRect(160, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit5.setFont(font)
        self.G2lineEdit5.setStyleSheet("")
        self.G2lineEdit5.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit5.setObjectName("G2lineEdit5")
        self.G2lineEdit6 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit6.setGeometry(QtCore.QRect(200, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit6.setFont(font)
        self.G2lineEdit6.setStyleSheet("")
        self.G2lineEdit6.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit6.setObjectName("G2lineEdit6")
        self.G2lineEdit7 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit7.setGeometry(QtCore.QRect(240, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit7.setFont(font)
        self.G2lineEdit7.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit7.setObjectName("G2lineEdit7")
        self.G2lineEdit8 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit8.setGeometry(QtCore.QRect(280, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit8.setFont(font)
        self.G2lineEdit8.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit8.setObjectName("G2lineEdit8")
        self.G2lineEdit9 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit9.setGeometry(QtCore.QRect(340, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit9.setFont(font)
        self.G2lineEdit9.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit9.setObjectName("G2lineEdit9")
        self.G2lineEdit10 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit10.setGeometry(QtCore.QRect(380, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit10.setFont(font)
        self.G2lineEdit10.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit10.setObjectName("G2lineEdit10")
        self.G2lineEdit11 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit11.setGeometry(QtCore.QRect(420, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit11.setFont(font)
        self.G2lineEdit11.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit11.setObjectName("G2lineEdit11")
        self.G2lineEdit12 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit12.setGeometry(QtCore.QRect(460, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit12.setFont(font)
        self.G2lineEdit12.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit12.setObjectName("G2lineEdit12")
        self.G2lineEdit21 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit21.setGeometry(QtCore.QRect(160, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit21.setFont(font)
        self.G2lineEdit21.setStyleSheet("")
        self.G2lineEdit21.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit21.setObjectName("G2lineEdit21")
        self.G2lineEdit19 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit19.setGeometry(QtCore.QRect(80, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit19.setFont(font)
        self.G2lineEdit19.setStyleSheet("")
        self.G2lineEdit19.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit19.setObjectName("G2lineEdit19")
        self.G2lineEdit22 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit22.setGeometry(QtCore.QRect(200, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit22.setFont(font)
        self.G2lineEdit22.setStyleSheet("")
        self.G2lineEdit22.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit22.setObjectName("G2lineEdit22")
        self.G2lineEdit24 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit24.setGeometry(QtCore.QRect(280, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit24.setFont(font)
        self.G2lineEdit24.setStyleSheet("")
        self.G2lineEdit24.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit24.setObjectName("G2lineEdit24")
        self.G2lineEdit15 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit15.setGeometry(QtCore.QRect(580, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit15.setFont(font)
        self.G2lineEdit15.setStyleSheet("")
        self.G2lineEdit15.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit15.setObjectName("G2lineEdit15")
        self.G2lineEdit20 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit20.setGeometry(QtCore.QRect(120, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit20.setFont(font)
        self.G2lineEdit20.setStyleSheet("")
        self.G2lineEdit20.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit20.setObjectName("G2lineEdit20")
        self.G2lineEdit13 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit13.setGeometry(QtCore.QRect(500, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit13.setFont(font)
        self.G2lineEdit13.setStyleSheet("")
        self.G2lineEdit13.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit13.setObjectName("G2lineEdit13")
        self.G2lineEdit14 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit14.setGeometry(QtCore.QRect(540, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit14.setFont(font)
        self.G2lineEdit14.setStyleSheet("")
        self.G2lineEdit14.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit14.setObjectName("G2lineEdit14")
        self.G2lineEdit23 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit23.setGeometry(QtCore.QRect(240, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit23.setFont(font)
        self.G2lineEdit23.setStyleSheet("")
        self.G2lineEdit23.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit23.setObjectName("G2lineEdit23")
        self.G2lineEdit16 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit16.setGeometry(QtCore.QRect(620, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit16.setFont(font)
        self.G2lineEdit16.setStyleSheet("")
        self.G2lineEdit16.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit16.setObjectName("G2lineEdit16")
        self.G2lineEdit18 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit18.setGeometry(QtCore.QRect(40, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit18.setFont(font)
        self.G2lineEdit18.setStyleSheet("")
        self.G2lineEdit18.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit18.setObjectName("G2lineEdit18")
        self.G2lineEdit17 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit17.setGeometry(QtCore.QRect(0, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit17.setFont(font)
        self.G2lineEdit17.setStyleSheet("")
        self.G2lineEdit17.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit17.setObjectName("G2lineEdit17")
        self.G2lineEdit28 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit28.setGeometry(QtCore.QRect(460, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit28.setFont(font)
        self.G2lineEdit28.setStyleSheet("")
        self.G2lineEdit28.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit28.setObjectName("G2lineEdit28")
        self.G2lineEdit35 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit35.setGeometry(QtCore.QRect(80, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit35.setFont(font)
        self.G2lineEdit35.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit35.setObjectName("G2lineEdit35")
        self.G2lineEdit29 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit29.setGeometry(QtCore.QRect(500, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit29.setFont(font)
        self.G2lineEdit29.setStyleSheet("")
        self.G2lineEdit29.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit29.setObjectName("G2lineEdit29")
        self.G2lineEdit33 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit33.setGeometry(QtCore.QRect(0, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit33.setFont(font)
        self.G2lineEdit33.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit33.setObjectName("G2lineEdit33")
        self.G2lineEdit34 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit34.setGeometry(QtCore.QRect(40, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit34.setFont(font)
        self.G2lineEdit34.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit34.setObjectName("G2lineEdit34")
        self.G2lineEdit32 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit32.setGeometry(QtCore.QRect(620, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit32.setFont(font)
        self.G2lineEdit32.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit32.setObjectName("G2lineEdit32")
        self.G2lineEdit26 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit26.setGeometry(QtCore.QRect(380, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit26.setFont(font)
        self.G2lineEdit26.setStyleSheet("")
        self.G2lineEdit26.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit26.setObjectName("G2lineEdit26")
        self.G2lineEdit30 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit30.setGeometry(QtCore.QRect(540, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit30.setFont(font)
        self.G2lineEdit30.setStyleSheet("")
        self.G2lineEdit30.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit30.setObjectName("G2lineEdit30")
        self.G2lineEdit27 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit27.setGeometry(QtCore.QRect(420, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit27.setFont(font)
        self.G2lineEdit27.setStyleSheet("")
        self.G2lineEdit27.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit27.setObjectName("G2lineEdit27")
        self.G2lineEdit25 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit25.setGeometry(QtCore.QRect(340, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit25.setFont(font)
        self.G2lineEdit25.setStyleSheet("")
        self.G2lineEdit25.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit25.setObjectName("G2lineEdit25")
        self.G2lineEdit31 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit31.setGeometry(QtCore.QRect(580, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit31.setFont(font)
        self.G2lineEdit31.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit31.setObjectName("G2lineEdit31")
        self.G2lineEdit36 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit36.setGeometry(QtCore.QRect(120, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit36.setFont(font)
        self.G2lineEdit36.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit36.setObjectName("G2lineEdit36")
        self.G2lineEdit47 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit47.setGeometry(QtCore.QRect(580, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit47.setFont(font)
        self.G2lineEdit47.setStyleSheet("")
        self.G2lineEdit47.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit47.setObjectName("G2lineEdit47")
        self.G2lineEdit38 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit38.setGeometry(QtCore.QRect(200, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit38.setFont(font)
        self.G2lineEdit38.setStyleSheet("")
        self.G2lineEdit38.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit38.setObjectName("G2lineEdit38")
        self.G2lineEdit46 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit46.setGeometry(QtCore.QRect(540, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit46.setFont(font)
        self.G2lineEdit46.setStyleSheet("")
        self.G2lineEdit46.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit46.setObjectName("G2lineEdit46")
        self.G2lineEdit40 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit40.setGeometry(QtCore.QRect(280, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit40.setFont(font)
        self.G2lineEdit40.setStyleSheet("")
        self.G2lineEdit40.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit40.setObjectName("G2lineEdit40")
        self.G2lineEdit48 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit48.setGeometry(QtCore.QRect(620, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit48.setFont(font)
        self.G2lineEdit48.setStyleSheet("")
        self.G2lineEdit48.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit48.setObjectName("G2lineEdit48")
        self.G2lineEdit41 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit41.setGeometry(QtCore.QRect(340, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit41.setFont(font)
        self.G2lineEdit41.setStyleSheet("")
        self.G2lineEdit41.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit41.setObjectName("G2lineEdit41")
        self.G2lineEdit44 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit44.setGeometry(QtCore.QRect(460, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit44.setFont(font)
        self.G2lineEdit44.setStyleSheet("")
        self.G2lineEdit44.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit44.setObjectName("G2lineEdit44")
        self.G2lineEdit43 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit43.setGeometry(QtCore.QRect(420, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit43.setFont(font)
        self.G2lineEdit43.setStyleSheet("")
        self.G2lineEdit43.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit43.setObjectName("G2lineEdit43")
        self.G2lineEdit37 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit37.setGeometry(QtCore.QRect(160, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit37.setFont(font)
        self.G2lineEdit37.setStyleSheet("")
        self.G2lineEdit37.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit37.setObjectName("G2lineEdit37")
        self.G2lineEdit45 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit45.setGeometry(QtCore.QRect(500, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit45.setFont(font)
        self.G2lineEdit45.setStyleSheet("")
        self.G2lineEdit45.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit45.setObjectName("G2lineEdit45")
        self.G2lineEdit39 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit39.setGeometry(QtCore.QRect(240, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit39.setFont(font)
        self.G2lineEdit39.setStyleSheet("")
        self.G2lineEdit39.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit39.setObjectName("G2lineEdit39")
        self.G2lineEdit42 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit42.setGeometry(QtCore.QRect(380, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit42.setFont(font)
        self.G2lineEdit42.setStyleSheet("")
        self.G2lineEdit42.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit42.setObjectName("G2lineEdit42")
        self.G2DDClear = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDClear.setGeometry(QtCore.QRect(580, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDClear.setFont(font)
        self.G2DDClear.setObjectName("G2DDClear")
        self.G2DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDCopy.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDCopy.setFont(font)
        self.G2DDCopy.setObjectName("G2DDCopy")
        self.G2lineEdit49 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit49.setGeometry(QtCore.QRect(0, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit49.setFont(font)
        self.G2lineEdit49.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit49.setObjectName("G2lineEdit49")
        self.G2lineEdit50 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit50.setGeometry(QtCore.QRect(40, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit50.setFont(font)
        self.G2lineEdit50.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit50.setObjectName("G2lineEdit50")
        self.G2lineEdit51 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit51.setGeometry(QtCore.QRect(80, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit51.setFont(font)
        self.G2lineEdit51.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit51.setObjectName("G2lineEdit51")
        self.G2lineEdit52 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit52.setGeometry(QtCore.QRect(120, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit52.setFont(font)
        self.G2lineEdit52.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit52.setObjectName("G2lineEdit52")
        self.G2lineEdit53 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit53.setGeometry(QtCore.QRect(160, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit53.setFont(font)
        self.G2lineEdit53.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit53.setObjectName("G2lineEdit53")
        self.G2lineEdit54 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit54.setGeometry(QtCore.QRect(200, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit54.setFont(font)
        self.G2lineEdit54.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit54.setObjectName("G2lineEdit54")
        self.G2lineEdit55 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit55.setGeometry(QtCore.QRect(240, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit55.setFont(font)
        self.G2lineEdit55.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit55.setObjectName("G2lineEdit55")
        self.G2lineEdit56 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit56.setGeometry(QtCore.QRect(280, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit56.setFont(font)
        self.G2lineEdit56.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit56.setObjectName("G2lineEdit56")
        self.G2lineEdit57 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit57.setGeometry(QtCore.QRect(340, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit57.setFont(font)
        self.G2lineEdit57.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit57.setObjectName("G2lineEdit57")
        self.G2lineEdit58 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit58.setGeometry(QtCore.QRect(380, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit58.setFont(font)
        self.G2lineEdit58.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit58.setObjectName("G2lineEdit58")
        self.G2lineEdit59 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit59.setGeometry(QtCore.QRect(420, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit59.setFont(font)
        self.G2lineEdit59.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit59.setObjectName("G2lineEdit59")
        self.G2lineEdit60 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit60.setGeometry(QtCore.QRect(460, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit60.setFont(font)
        self.G2lineEdit60.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit60.setObjectName("G2lineEdit60")
        self.G2lineEdit61 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit61.setGeometry(QtCore.QRect(500, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit61.setFont(font)
        self.G2lineEdit61.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit61.setObjectName("G2lineEdit61")
        self.G2lineEdit62 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit62.setGeometry(QtCore.QRect(540, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit62.setFont(font)
        self.G2lineEdit62.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit62.setObjectName("G2lineEdit62")
        self.G2lineEdit63 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit63.setGeometry(QtCore.QRect(580, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit63.setFont(font)
        self.G2lineEdit63.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit63.setObjectName("G2lineEdit63")
        self.G2lineEdit64 = QtWidgets.QLineEdit(self.ddRegGroupBox2)
        self.G2lineEdit64.setGeometry(QtCore.QRect(620, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2lineEdit64.setFont(font)
        self.G2lineEdit64.setAlignment(QtCore.Qt.AlignCenter)
        self.G2lineEdit64.setObjectName("G2lineEdit64")
        self.ddRegGroupBox3 = QtWidgets.QGroupBox(self.tabDDRegister)
        self.ddRegGroupBox3.setGeometry(QtCore.QRect(0, 290, 675, 129))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ddRegGroupBox3.setFont(font)
        self.ddRegGroupBox3.setStyleSheet("color: rgb(0, 0, 255);")
        self.ddRegGroupBox3.setObjectName("ddRegGroupBox3")
        self.G3DDRead = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDRead.setGeometry(QtCore.QRect(0, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDRead.setFont(font)
        self.G3DDRead.setObjectName("G3DDRead")
        self.G3AddrlineEdit = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3AddrlineEdit.setGeometry(QtCore.QRect(80, 16, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3AddrlineEdit.setFont(font)
        self.G3AddrlineEdit.setObjectName("G3AddrlineEdit")
        self.G3DDWrite = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDWrite.setGeometry(QtCore.QRect(200, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDWrite.setFont(font)
        self.G3DDWrite.setObjectName("G3DDWrite")
        self.G3lineEdit1 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit1.setGeometry(QtCore.QRect(0, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit1.setFont(font)
        self.G3lineEdit1.setStyleSheet("")
        self.G3lineEdit1.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit1.setObjectName("G3lineEdit1")
        self.G3lineEdit2 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit2.setGeometry(QtCore.QRect(40, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit2.setFont(font)
        self.G3lineEdit2.setStyleSheet("")
        self.G3lineEdit2.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit2.setObjectName("G3lineEdit2")
        self.G3lineEdit3 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit3.setGeometry(QtCore.QRect(80, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit3.setFont(font)
        self.G3lineEdit3.setStyleSheet("")
        self.G3lineEdit3.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit3.setObjectName("G3lineEdit3")
        self.G3lineEdit4 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit4.setGeometry(QtCore.QRect(120, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit4.setFont(font)
        self.G3lineEdit4.setStyleSheet("")
        self.G3lineEdit4.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit4.setObjectName("G3lineEdit4")
        self.G3lineEdit5 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit5.setGeometry(QtCore.QRect(160, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit5.setFont(font)
        self.G3lineEdit5.setStyleSheet("")
        self.G3lineEdit5.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit5.setObjectName("G3lineEdit5")
        self.G3lineEdit6 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit6.setGeometry(QtCore.QRect(200, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit6.setFont(font)
        self.G3lineEdit6.setStyleSheet("")
        self.G3lineEdit6.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit6.setObjectName("G3lineEdit6")
        self.G3lineEdit7 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit7.setGeometry(QtCore.QRect(240, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit7.setFont(font)
        self.G3lineEdit7.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit7.setObjectName("G3lineEdit7")
        self.G3lineEdit8 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit8.setGeometry(QtCore.QRect(280, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit8.setFont(font)
        self.G3lineEdit8.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit8.setObjectName("G3lineEdit8")
        self.G3lineEdit9 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit9.setGeometry(QtCore.QRect(340, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit9.setFont(font)
        self.G3lineEdit9.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit9.setObjectName("G3lineEdit9")
        self.G3lineEdit10 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit10.setGeometry(QtCore.QRect(380, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit10.setFont(font)
        self.G3lineEdit10.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit10.setObjectName("G3lineEdit10")
        self.G3lineEdit11 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit11.setGeometry(QtCore.QRect(420, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit11.setFont(font)
        self.G3lineEdit11.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit11.setObjectName("G3lineEdit11")
        self.G3lineEdit12 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit12.setGeometry(QtCore.QRect(460, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit12.setFont(font)
        self.G3lineEdit12.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit12.setObjectName("G3lineEdit12")
        self.G3lineEdit21 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit21.setGeometry(QtCore.QRect(160, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit21.setFont(font)
        self.G3lineEdit21.setStyleSheet("")
        self.G3lineEdit21.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit21.setObjectName("G3lineEdit21")
        self.G3lineEdit19 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit19.setGeometry(QtCore.QRect(80, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit19.setFont(font)
        self.G3lineEdit19.setStyleSheet("")
        self.G3lineEdit19.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit19.setObjectName("G3lineEdit19")
        self.G3lineEdit22 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit22.setGeometry(QtCore.QRect(200, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit22.setFont(font)
        self.G3lineEdit22.setStyleSheet("")
        self.G3lineEdit22.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit22.setObjectName("G3lineEdit22")
        self.G3lineEdit24 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit24.setGeometry(QtCore.QRect(280, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit24.setFont(font)
        self.G3lineEdit24.setStyleSheet("")
        self.G3lineEdit24.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit24.setObjectName("G3lineEdit24")
        self.G3lineEdit15 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit15.setGeometry(QtCore.QRect(580, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit15.setFont(font)
        self.G3lineEdit15.setStyleSheet("")
        self.G3lineEdit15.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit15.setObjectName("G3lineEdit15")
        self.G3lineEdit20 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit20.setGeometry(QtCore.QRect(120, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit20.setFont(font)
        self.G3lineEdit20.setStyleSheet("")
        self.G3lineEdit20.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit20.setObjectName("G3lineEdit20")
        self.G3lineEdit13 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit13.setGeometry(QtCore.QRect(500, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit13.setFont(font)
        self.G3lineEdit13.setStyleSheet("")
        self.G3lineEdit13.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit13.setObjectName("G3lineEdit13")
        self.G3lineEdit14 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit14.setGeometry(QtCore.QRect(540, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit14.setFont(font)
        self.G3lineEdit14.setStyleSheet("")
        self.G3lineEdit14.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit14.setObjectName("G3lineEdit14")
        self.G3lineEdit23 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit23.setGeometry(QtCore.QRect(240, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit23.setFont(font)
        self.G3lineEdit23.setStyleSheet("")
        self.G3lineEdit23.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit23.setObjectName("G3lineEdit23")
        self.G3lineEdit16 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit16.setGeometry(QtCore.QRect(620, 40, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit16.setFont(font)
        self.G3lineEdit16.setStyleSheet("")
        self.G3lineEdit16.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit16.setObjectName("G3lineEdit16")
        self.G3lineEdit18 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit18.setGeometry(QtCore.QRect(40, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit18.setFont(font)
        self.G3lineEdit18.setStyleSheet("")
        self.G3lineEdit18.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit18.setObjectName("G3lineEdit18")
        self.G3lineEdit17 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit17.setGeometry(QtCore.QRect(0, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit17.setFont(font)
        self.G3lineEdit17.setStyleSheet("")
        self.G3lineEdit17.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit17.setObjectName("G3lineEdit17")
        self.G3lineEdit28 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit28.setGeometry(QtCore.QRect(460, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit28.setFont(font)
        self.G3lineEdit28.setStyleSheet("")
        self.G3lineEdit28.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit28.setObjectName("G3lineEdit28")
        self.G3lineEdit35 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit35.setGeometry(QtCore.QRect(80, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit35.setFont(font)
        self.G3lineEdit35.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit35.setObjectName("G3lineEdit35")
        self.G3lineEdit29 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit29.setGeometry(QtCore.QRect(500, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit29.setFont(font)
        self.G3lineEdit29.setStyleSheet("")
        self.G3lineEdit29.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit29.setObjectName("G3lineEdit29")
        self.G3lineEdit33 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit33.setGeometry(QtCore.QRect(0, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit33.setFont(font)
        self.G3lineEdit33.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit33.setObjectName("G3lineEdit33")
        self.G3lineEdit34 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit34.setGeometry(QtCore.QRect(40, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit34.setFont(font)
        self.G3lineEdit34.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit34.setObjectName("G3lineEdit34")
        self.G3lineEdit32 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit32.setGeometry(QtCore.QRect(620, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit32.setFont(font)
        self.G3lineEdit32.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit32.setObjectName("G3lineEdit32")
        self.G3lineEdit26 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit26.setGeometry(QtCore.QRect(380, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit26.setFont(font)
        self.G3lineEdit26.setStyleSheet("")
        self.G3lineEdit26.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit26.setObjectName("G3lineEdit26")
        self.G3lineEdit30 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit30.setGeometry(QtCore.QRect(540, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit30.setFont(font)
        self.G3lineEdit30.setStyleSheet("")
        self.G3lineEdit30.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit30.setObjectName("G3lineEdit30")
        self.G3lineEdit27 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit27.setGeometry(QtCore.QRect(420, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit27.setFont(font)
        self.G3lineEdit27.setStyleSheet("")
        self.G3lineEdit27.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit27.setObjectName("G3lineEdit27")
        self.G3lineEdit25 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit25.setGeometry(QtCore.QRect(340, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit25.setFont(font)
        self.G3lineEdit25.setStyleSheet("")
        self.G3lineEdit25.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit25.setObjectName("G3lineEdit25")
        self.G3lineEdit31 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit31.setGeometry(QtCore.QRect(580, 62, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit31.setFont(font)
        self.G3lineEdit31.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit31.setObjectName("G3lineEdit31")
        self.G3lineEdit36 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit36.setGeometry(QtCore.QRect(120, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit36.setFont(font)
        self.G3lineEdit36.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit36.setObjectName("G3lineEdit36")
        self.G3lineEdit47 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit47.setGeometry(QtCore.QRect(580, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit47.setFont(font)
        self.G3lineEdit47.setStyleSheet("")
        self.G3lineEdit47.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit47.setObjectName("G3lineEdit47")
        self.G3lineEdit38 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit38.setGeometry(QtCore.QRect(200, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit38.setFont(font)
        self.G3lineEdit38.setStyleSheet("")
        self.G3lineEdit38.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit38.setObjectName("G3lineEdit38")
        self.G3lineEdit46 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit46.setGeometry(QtCore.QRect(540, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit46.setFont(font)
        self.G3lineEdit46.setStyleSheet("")
        self.G3lineEdit46.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit46.setObjectName("G3lineEdit46")
        self.G3lineEdit40 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit40.setGeometry(QtCore.QRect(280, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit40.setFont(font)
        self.G3lineEdit40.setStyleSheet("")
        self.G3lineEdit40.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit40.setObjectName("G3lineEdit40")
        self.G3lineEdit48 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit48.setGeometry(QtCore.QRect(620, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit48.setFont(font)
        self.G3lineEdit48.setStyleSheet("")
        self.G3lineEdit48.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit48.setObjectName("G3lineEdit48")
        self.G3lineEdit41 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit41.setGeometry(QtCore.QRect(340, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit41.setFont(font)
        self.G3lineEdit41.setStyleSheet("")
        self.G3lineEdit41.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit41.setObjectName("G3lineEdit41")
        self.G3lineEdit44 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit44.setGeometry(QtCore.QRect(460, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit44.setFont(font)
        self.G3lineEdit44.setStyleSheet("")
        self.G3lineEdit44.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit44.setObjectName("G3lineEdit44")
        self.G3lineEdit43 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit43.setGeometry(QtCore.QRect(420, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit43.setFont(font)
        self.G3lineEdit43.setStyleSheet("")
        self.G3lineEdit43.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit43.setObjectName("G3lineEdit43")
        self.G3lineEdit37 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit37.setGeometry(QtCore.QRect(160, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit37.setFont(font)
        self.G3lineEdit37.setStyleSheet("")
        self.G3lineEdit37.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit37.setObjectName("G3lineEdit37")
        self.G3lineEdit45 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit45.setGeometry(QtCore.QRect(500, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit45.setFont(font)
        self.G3lineEdit45.setStyleSheet("")
        self.G3lineEdit45.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit45.setObjectName("G3lineEdit45")
        self.G3lineEdit39 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit39.setGeometry(QtCore.QRect(240, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit39.setFont(font)
        self.G3lineEdit39.setStyleSheet("")
        self.G3lineEdit39.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit39.setObjectName("G3lineEdit39")
        self.G3lineEdit42 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit42.setGeometry(QtCore.QRect(380, 84, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit42.setFont(font)
        self.G3lineEdit42.setStyleSheet("")
        self.G3lineEdit42.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit42.setObjectName("G3lineEdit42")
        self.G3DDClear = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDClear.setGeometry(QtCore.QRect(580, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDClear.setFont(font)
        self.G3DDClear.setObjectName("G3DDClear")
        self.G3DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDCopy.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDCopy.setFont(font)
        self.G3DDCopy.setObjectName("G3DDCopy")
        self.G3lineEdit49 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit49.setGeometry(QtCore.QRect(0, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit49.setFont(font)
        self.G3lineEdit49.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit49.setObjectName("G3lineEdit49")
        self.G3lineEdit50 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit50.setGeometry(QtCore.QRect(40, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit50.setFont(font)
        self.G3lineEdit50.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit50.setObjectName("G3lineEdit50")
        self.G3lineEdit51 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit51.setGeometry(QtCore.QRect(80, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit51.setFont(font)
        self.G3lineEdit51.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit51.setObjectName("G3lineEdit51")
        self.G3lineEdit52 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit52.setGeometry(QtCore.QRect(120, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit52.setFont(font)
        self.G3lineEdit52.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit52.setObjectName("G3lineEdit52")
        self.G3lineEdit53 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit53.setGeometry(QtCore.QRect(160, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit53.setFont(font)
        self.G3lineEdit53.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit53.setObjectName("G3lineEdit53")
        self.G3lineEdit54 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit54.setGeometry(QtCore.QRect(200, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit54.setFont(font)
        self.G3lineEdit54.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit54.setObjectName("G3lineEdit54")
        self.G3lineEdit55 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit55.setGeometry(QtCore.QRect(240, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit55.setFont(font)
        self.G3lineEdit55.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit55.setObjectName("G3lineEdit55")
        self.G3lineEdit56 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit56.setGeometry(QtCore.QRect(280, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit56.setFont(font)
        self.G3lineEdit56.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit56.setObjectName("G3lineEdit56")
        self.G3lineEdit57 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit57.setGeometry(QtCore.QRect(340, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit57.setFont(font)
        self.G3lineEdit57.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit57.setObjectName("G3lineEdit57")
        self.G3lineEdit58 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit58.setGeometry(QtCore.QRect(380, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit58.setFont(font)
        self.G3lineEdit58.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit58.setObjectName("G3lineEdit58")
        self.G3lineEdit59 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit59.setGeometry(QtCore.QRect(420, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit59.setFont(font)
        self.G3lineEdit59.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit59.setObjectName("G3lineEdit59")
        self.G3lineEdit60 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit60.setGeometry(QtCore.QRect(460, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit60.setFont(font)
        self.G3lineEdit60.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit60.setObjectName("G3lineEdit60")
        self.G3lineEdit61 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit61.setGeometry(QtCore.QRect(500, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit61.setFont(font)
        self.G3lineEdit61.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit61.setObjectName("G3lineEdit61")
        self.G3lineEdit62 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit62.setGeometry(QtCore.QRect(540, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit62.setFont(font)
        self.G3lineEdit62.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit62.setObjectName("G3lineEdit62")
        self.G3lineEdit63 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit63.setGeometry(QtCore.QRect(580, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit63.setFont(font)
        self.G3lineEdit63.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit63.setObjectName("G3lineEdit63")
        self.G3lineEdit64 = QtWidgets.QLineEdit(self.ddRegGroupBox3)
        self.G3lineEdit64.setGeometry(QtCore.QRect(620, 106, 35, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3lineEdit64.setFont(font)
        self.G3lineEdit64.setAlignment(QtCore.Qt.AlignCenter)
        self.G3lineEdit64.setObjectName("G3lineEdit64")
        self.TabMainWindow.addTab(self.tabDDRegister, "")
        self.tabDDLog = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabDDLog.sizePolicy().hasHeightForWidth())
        self.tabDDLog.setSizePolicy(sizePolicy)
        self.tabDDLog.setObjectName("tabDDLog")
        self.DDreadRegValShowText = QtWidgets.QTextBrowser(self.tabDDLog)
        self.DDreadRegValShowText.setGeometry(QtCore.QRect(0, 1, 673, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.DDreadRegValShowText.sizePolicy().hasHeightForWidth())
        self.DDreadRegValShowText.setSizePolicy(sizePolicy)
        self.DDreadRegValShowText.setMinimumSize(QtCore.QSize(670, 300))
        self.DDreadRegValShowText.setMaximumSize(QtCore.QSize(1000, 800))
        self.DDreadRegValShowText.setObjectName("DDreadRegValShowText")
        self.TabMainWindow.addTab(self.tabDDLog, "")
        self.tabHelp = QtWidgets.QWidget()
        self.tabHelp.setObjectName("tabHelp")
        self.TabHelpSubMain = QtWidgets.QTabWidget(self.tabHelp)
        self.TabHelpSubMain.setGeometry(QtCore.QRect(0, 0, 671, 451))
        self.TabHelpSubMain.setObjectName("TabHelpSubMain")
        self.TabAbout = QtWidgets.QWidget()
        self.TabAbout.setObjectName("TabAbout")
        self.helpLabel1 = QtWidgets.QLabel(self.TabAbout)
        self.helpLabel1.setGeometry(QtCore.QRect(5, 5, 650, 30))
        self.helpLabel1.setObjectName("helpLabel1")
        self.helpLabel2 = QtWidgets.QLabel(self.TabAbout)
        self.helpLabel2.setGeometry(QtCore.QRect(5, 40, 650, 30))
        self.helpLabel2.setObjectName("helpLabel2")
        self.TabHelpSubMain.addTab(self.TabAbout, "")
        self.TabCommands = QtWidgets.QWidget()
        self.TabCommands.setObjectName("TabCommands")
        self.TabHelpSubMain.addTab(self.TabCommands, "")
        self.TabMainWindow.addTab(self.tabHelp, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabMainWindow.setCurrentIndex(0)
        self.TabHelpSubMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB Monitor 2.0.2"))
        self.touchInfoGroupBox.setTitle(_translate("MainWindow", "Touch info"))
        self.touchInfoRXLineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.touchInfoTXLineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.touchInfoRXLabel.setText(_translate("MainWindow", "RX:"))
        self.touchInfoTXLabel.setText(_translate("MainWindow", "TX:"))
        self.touchInfoRexYLabel.setText(_translate("MainWindow", "Res Y:"))
        self.touchInfoRexXLabel.setText(_translate("MainWindow", "Res X:"))
        self.touchInfoResXLineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.touchInfoResYLineEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.settingsGroupBox.setTitle(_translate("MainWindow", "Path settings"))
        self.pathV1RadioButton.setText(_translate("MainWindow", "V1"))
        self.pathV2RadioButton.setText(_translate("MainWindow", "V2"))
        self.pathDriVerLabel.setText(_translate("MainWindow", "Driver version:"))
        self.pathDiagLabel.setText(_translate("MainWindow", "Diag:"))
        self.pathRegLabel.setText(_translate("MainWindow", "Reg:"))
        self.pathResetLabel.setText(_translate("MainWindow", "Reset:"))
        self.pathIntenLabel.setText(_translate("MainWindow", "Int_en:"))
        self.pathDiagarrLabel.setText(_translate("MainWindow", "Diag_arr:"))
        self.pathSenseonoffLabel.setText(_translate("MainWindow", "SenseOnOff:"))
        self.pathStackLabel.setText(_translate("MainWindow", "stack:"))
        self.pathDebugLabel.setText(_translate("MainWindow", "Debug:"))
        self.pathSelftestLabel.setText(_translate("MainWindow", "SelfTest:"))
        self.pathFlashdumpLabel.setText(_translate("MainWindow", "Flash_dump:"))
        self.pathHXFolderLabel.setText(_translate("MainWindow", "HX folder:"))
        self.pathFWLabel.setText(_translate("MainWindow", "FW path:"))
        self.pathConmmentLabel.setText(_translate("MainWindow", "(New project you need choose v1 or v2)"))
        self.conmment_2.setText(_translate("MainWindow", "Select project:"))
        self.conmment.setText(_translate("MainWindow", "You can save this\n"
	"settings to a project"))
        self.pathSavePushButton.setText(_translate("MainWindow", "Save as a project"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabSettings), _translate("MainWindow", "Settings"))
        self.wifiGroupBox.setTitle(_translate("MainWindow", "WIFI"))
        self.wifiConnect.setText(_translate("MainWindow", "Connect"))
        self.wifiDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.wifiReconnect.setText(_translate("MainWindow", "Reconnect"))
        self.wifiStatus.setText(_translate("MainWindow", "WiFi Status"))
        self.root.setText(_translate("MainWindow", "Root"))
        self.adbStatus.setText(_translate("MainWindow", "ADB Status"))
        self.adbGroupBox.setTitle(_translate("MainWindow", "ADB"))
        self.homekey.setText(_translate("MainWindow", "Home"))
        self.reboot.setText(_translate("MainWindow", "Reboot"))
        self.volDown.setText(_translate("MainWindow", "Vol down"))
        self.backkey.setText(_translate("MainWindow", "Back"))
        self.volUp.setText(_translate("MainWindow", "Vol up"))
        self.powerKey.setText(_translate("MainWindow", "PowerKey"))
        self.screenShot.setText(_translate("MainWindow", "ScreenShot"))
        self.openClosePoint.setText(_translate("MainWindow", "OpenPoint"))
        self.opencmd.setText(_translate("MainWindow", "Open cmd"))
        self.hideShowVirtual.setText(_translate("MainWindow", "ShowVirtual"))
        self.shutDown.setText(_translate("MainWindow", "ShutDown"))
        self.touchGroupBox.setTitle(_translate("MainWindow", "Touch"))
        self.inten0.setText(_translate("MainWindow", "Int_en"))
        self.senseon.setText(_translate("MainWindow", "SenseOn"))
        self.fwVersion.setText(_translate("MainWindow", "FWVersion"))
        self.selftest.setText(_translate("MainWindow", "SelfTest"))
        self.diagArr.setText(_translate("MainWindow", "DiagArr"))
        self.flashDump.setText(_translate("MainWindow", "FlashDump"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.updateFW.setText(_translate("MainWindow", "UpdateFW"))
        self.diagArrText.setPlaceholderText(_translate("MainWindow", "Default:6"))
        self.debugType.setText(_translate("MainWindow", "Debug"))
        self.debugComboBox.setItemText(0, _translate("MainWindow", "v"))
        self.debugComboBox.setItemText(1, _translate("MainWindow", "d"))
        self.debugComboBox.setItemText(2, _translate("MainWindow", "i2c"))
        self.debugComboBox.setItemText(3, _translate("MainWindow", "int"))
        self.debugComboBox.setItemText(4, _translate("MainWindow", "crc_test"))
        self.debugComboBox.setItemText(5, _translate("MainWindow", "fw_debug"))
        self.debugComboBox.setItemText(6, _translate("MainWindow", "esd_cnt"))
        self.debugComboBox.setItemText(7, _translate("MainWindow", "dd_debug"))
        self.displayGroupBox.setTitle(_translate("MainWindow", "Display"))
        self.openBlight.setText(_translate("MainWindow", "OpenBlight"))
        self.d1129.setText(_translate("MainWindow", "1129"))
        self.d2810.setText(_translate("MainWindow", "2810"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabOptions), _translate("MainWindow", "Options"))
        self.radioDC.setText(_translate("MainWindow", "DC"))
        self.radioIIR.setText(_translate("MainWindow", "IIR"))
        self.textEditDiag.setPlaceholderText(_translate("MainWindow", "Type"))
        self.log.setText(_translate("MainWindow", "Log"))
        self.recalled.setText(_translate("MainWindow", "ReL"))
        self.timeLineEdit.setPlaceholderText(_translate("MainWindow", "Time"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabRawdata), _translate("MainWindow", "Rawdata"))
        self.pushButtonRead.setText(_translate("MainWindow", "Read"))
        self.pushButtonRegWrite0.setText(_translate("MainWindow", "Write 0"))
        self.pushButtonRegWrite1.setText(_translate("MainWindow", "Write 1"))
        self.pushButtonRegWrite2.setText(_translate("MainWindow", "Write 2"))
        self.pushButtonRegWrite4.setText(_translate("MainWindow", "Write 4"))
        self.pushButtonRegWrite3.setText(_translate("MainWindow", "Write 3"))
        self.tpReglengthLabel.setText(_translate("MainWindow", "Length"))
        self.reglength.setItemText(0, _translate("MainWindow", "1"))
        self.reglength.setItemText(1, _translate("MainWindow", "2"))
        self.reglength.setItemText(2, _translate("MainWindow", "3"))
        self.reglength.setItemText(3, _translate("MainWindow", "4"))
        self.reglength.setItemText(4, _translate("MainWindow", "5"))
        self.reglength.setItemText(5, _translate("MainWindow", "6"))
        self.reglength.setItemText(6, _translate("MainWindow", "7"))
        self.reglength.setItemText(7, _translate("MainWindow", "8"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabRWRegister), _translate("MainWindow", "TP Reg"))
        self.ddRegGroupBox1.setTitle(_translate("MainWindow", "Group 1"))
        self.G1DDRead.setText(_translate("MainWindow", "Read"))
        self.G1AddrlineEdit.setPlaceholderText(_translate("MainWindow", "Eg:B9000A"))
        self.G1DDWrite.setText(_translate("MainWindow", "Write"))
        self.G1DDClear.setText(_translate("MainWindow", "Clear"))
        self.G1DDCopy.setText(_translate("MainWindow", "Copy"))
        self.ddRegGroupBox2.setTitle(_translate("MainWindow", "Group 2"))
        self.G2DDRead.setText(_translate("MainWindow", "Read"))
        self.G2AddrlineEdit.setPlaceholderText(_translate("MainWindow", "Eg:B9000A"))
        self.G2DDWrite.setText(_translate("MainWindow", "Write"))
        self.G2DDClear.setText(_translate("MainWindow", "Clear"))
        self.G2DDCopy.setText(_translate("MainWindow", "Copy"))
        self.ddRegGroupBox3.setTitle(_translate("MainWindow", "Group 3"))
        self.G3DDRead.setText(_translate("MainWindow", "Read"))
        self.G3AddrlineEdit.setPlaceholderText(_translate("MainWindow", "Eg:B9000A"))
        self.G3DDWrite.setText(_translate("MainWindow", "Write"))
        self.G3DDClear.setText(_translate("MainWindow", "Clear"))
        self.G3DDCopy.setText(_translate("MainWindow", "Copy"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabDDRegister), _translate("MainWindow", "DD Reg"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabDDLog), _translate("MainWindow", "DD Log"))
        self.helpLabel1.setText(_translate("MainWindow", "1.This software\'s introduction of the location is in .\\doc\\introduction.ppt"))
        self.helpLabel2.setText(_translate("MainWindow", "2.The path of this software is in\n"
	" \\SVN\\Internal\\TW\\Tool_Team_Release\\Himax_driver\\2.Debug_tool\\ADBMonitor\\"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabAbout), _translate("MainWindow", "About"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabCommands), _translate("MainWindow", "Commands"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabHelp), _translate("MainWindow", "Help"))

    def bindEventFunc(self):
        # settings
        self.pathV1RadioButton.clicked.connect(self.chooseDriverVersion)
        self.pathV2RadioButton.clicked.connect(self.chooseDriverVersion)
        self.pathSavePushButton.clicked.connect(self.saveSettingsToProject)
        self.settingsProComboBox.currentIndexChanged.connect(self.selectProjectItemEvent)

        # wifi
        self.wifiConnect.clicked.connect(self.wifiConnectFunc)
        self.wifiDisconnect.clicked.connect(self.wifiDisconnectFunc)
        self.wifiReconnect.clicked.connect(self.wifiReconnectFunc)

        # adb
        self.root.clicked.connect(self.rootFunc)
        self.homekey.clicked.connect(self.homeKeyFunc)
        self.backkey.clicked.connect(self.backKeyFunc)
        self.volUp.clicked.connect(self.volUpFunc)
        self.volDown.clicked.connect(self.volDownFunc)
        self.hideShowVirtual.clicked.connect(self.hideShowVirtualFunc)
        self.powerKey.clicked.connect(self.powerKeyFunc)
        self.openClosePoint.clicked.connect(self.openClosePointFunc)
        self.screenShot.clicked.connect(self.screenShotFunc)
        self.shutDown.clicked.connect(self.shutDownFunc)
        self.reboot.clicked.connect(self.rebootFunc)
        self.opencmd.clicked.connect(self.openCMDFunc)

        # touch
        self.fwVersion.clicked.connect(self.touchFWVersionFunc)
        self.reset.clicked.connect(self.touchResetFunc)
        self.senseon.clicked.connect(self.touchSenseOnFunc)
        self.selftest.clicked.connect(self.touchSelfTestFunc)
        self.inten0.clicked.connect(self.touchIntenFunc)
        self.flashDump.clicked.connect(self.touchFlashDumpFunc)
        self.debugType.clicked.connect(self.touchDebugTypeFunc)

        # display
        self.d1129.clicked.connect(self.display1129Func)
        self.d2810.clicked.connect(self.display2810Func)
        # self.openBlight.clicked.connect()

        # options
        self.diagArr.clicked.connect(self.touchDiagArrFunc)
        self.updateFW.clicked.connect(self.touchUpdateFWFunc)

        # rawdata show
        self.rawdataRead.clicked.connect(self.rawdataReadFunc)
        self.log.clicked.connect(self.logFunc)
        self.radioDC.clicked.connect(self.chooseRawdataType)
        self.radioIIR.clicked.connect(self.chooseRawdataType)
        self.radioTmp.clicked.connect(self.chooseRawdataType)

        # register read write
        self.pushButtonRead.clicked.connect(self.readRegFunc)
        self.pushButtonRegWrite0.clicked.connect(lambda: self.writeRegFunc(0))
        self.pushButtonRegWrite1.clicked.connect(lambda: self.writeRegFunc(1))
        self.pushButtonRegWrite2.clicked.connect(lambda: self.writeRegFunc(2))
        self.pushButtonRegWrite3.clicked.connect(lambda: self.writeRegFunc(3))
        self.pushButtonRegWrite4.clicked.connect(lambda: self.writeRegFunc(4))

        # dd new read write
        self.G1DDRead.clicked.connect(lambda: self.ddReadRegisterFunc(0))
        self.G2DDRead.clicked.connect(lambda: self.ddReadRegisterFunc(1))
        self.G3DDRead.clicked.connect(lambda: self.ddReadRegisterFunc(2))
        self.G1DDWrite.clicked.connect(lambda: self.ddWriteRegisterFunc(0))
        self.G2DDWrite.clicked.connect(lambda: self.ddWriteRegisterFunc(1))
        self.G3DDWrite.clicked.connect(lambda: self.ddWriteRegisterFunc(2))
        self.G1DDCopy.clicked.connect(lambda: self.ddCopyRegisterFunc(0))
        self.G2DDCopy.clicked.connect(lambda: self.ddCopyRegisterFunc(1))
        self.G3DDCopy.clicked.connect(lambda: self.ddCopyRegisterFunc(2))
        self.G1DDClear.clicked.connect(lambda: self.ddClearRegisterFunc(0))
        self.G2DDClear.clicked.connect(lambda: self.ddClearRegisterFunc(1))
        self.G3DDClear.clicked.connect(lambda: self.ddClearRegisterFunc(2))

    """ settings """
    def selectProjectItemEvent(self):
        name = self.settingsProComboBox.currentText()
        # read project info and init touch info
        if self.readProjectInfo(name):
            self.fillTouchConfig()
            self.initEchoMethod(self.driverVersionMode)
            self.chooseDriverVersion()
            self.initRawdataUI()
            self.initSettingsUi()
            self.disableSomeFunctions(False)
        else:
            self.disableSomeFunctions(True)

    def fillTouchConfig(self):
        self.pathDebugLineEdit.setText(self.debugPath)
        self.pathSelftestLineEdit.setText(self.selfTestPath)
        self.pathFlashdumpLineEdit.setText(self.flashDumpPath)
        self.pathHXFolderLineEdit.setText(self.hxFolderPath)
        self.pathFWLineEdit.setText(self.fwPath)

        self.touchInfoRXLineEdit.setText(str(self.rxnum))
        self.touchInfoTXLineEdit.setText(str(self.txnum))

        if self.driverVersionMode == 1:
            self.pathV1RadioButton.setChecked(True)
            self.pathV2RadioButton.setChecked(False)

            self.pathDiagLineEdit.setText(self.v1DiagPath)
            self.pathRegLineEdit.setText(self.v1RegisterPath)
            self.pathIntenLineEdit.setText(self.v1IntEnPath)
            self.pathResetLineEdit.setText(self.v1ResetPath)
            self.pathSenseonoffLineEdit.setText(self.v1SenseOnOffPath)
            self.pathDiagarrLineEdit.setText(self.v1DiagArrPath)
            self.pathStackLineEdit.clear()
        else:
            self.pathV1RadioButton.setChecked(False)
            self.pathV2RadioButton.setChecked(True)

            self.pathStackLineEdit.setText(self.v2ReadStackPath)
            self.pathDiagLineEdit.clear()
            self.pathRegLineEdit.clear()
            self.pathIntenLineEdit.clear()
            self.pathResetLineEdit.clear()
            self.pathSenseonoffLineEdit.clear()
            self.pathDiagarrLineEdit.clear()

    def readProjectInfo(self, name):
        path = './project/'
        fileName = path + name

        if not os.path.exists(fileName):
            self.dialogWin("File was not exists!")
            self.initSelectProjectItems(False)
            return False

        with open(fileName, 'rb') as r:
            for line in r.readlines():
                line = str(line, encoding='UTF-8')
                lineList = line.split('=')
                lineList[1] = lineList[1][:len(lineList[1]) - 2]

                if lineList[0] == 'DRIVER_VERSION':
                    self.driverVersionMode = int(lineList[1])
                elif lineList[0] == 'RX':
                    self.rxnum = int(lineList[1])
                elif lineList[0] == 'TX':
                    self.txnum = int(lineList[1])
                elif lineList[0] == 'V1_DIAG_PATH':
                    self.v1DiagPath = lineList[1]
                elif lineList[0] == 'V1_REG_PATH':
                    self.v1RegisterPath = lineList[1]
                elif lineList[0] == 'V1_INT_EN_PATH':
                    self.v1IntEnPath = lineList[1]
                elif lineList[0] == 'V1_RESET_PATH':
                    self.v1ResetPath = lineList[1]
                elif lineList[0] == 'V1_SENSEONOFF_PATH':
                    self.v1SenseOnOffPath = lineList[1]
                elif lineList[0] == 'V1_DIAGARR_PATH':
                    self.v1DiagArrPath = lineList[1]
                elif lineList[0] == 'V2_STACK_PATH':
                    self.v2ReadStackPath = lineList[1]
                elif lineList[0] == 'SELFTEST_PATH':
                    self.selfTestPath = lineList[1]
                elif lineList[0] == 'DEBUG_PATH':
                    self.debugPath = lineList[1]
                elif lineList[0] == 'FLASH_DUMP_PATH':
                    self.flashDumpPath = lineList[1]
                elif lineList[0] == 'HX_FOLDER_PATH':
                    self.hxFolderPath = lineList[1]
                elif lineList[0] == 'FW_PATH':
                    self.fwPath = lineList[1]

        return True

    def setRegExp(self):
        # settings limit rx tx input style
        reg = QRegExp('[1-9][0-9]')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.touchInfoRXLineEdit.setValidator(pValidator)
        self.touchInfoTXLineEdit.setValidator(pValidator)

        # settings limit node path input style
        reg = QRegExp('[/a-zA-Z_]*')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.pathDiagLineEdit.setValidator(pValidator)
        self.pathRegLineEdit.setValidator(pValidator)
        self.pathResetLineEdit.setValidator(pValidator)
        self.pathIntenLineEdit.setValidator(pValidator)
        self.pathDiagarrLineEdit.setValidator(pValidator)
        self.pathSenseonoffLineEdit.setValidator(pValidator)
        self.pathStackLineEdit.setValidator(pValidator)
        self.pathDebugLineEdit.setValidator(pValidator)
        self.pathSelftestLineEdit.setValidator(pValidator)
        self.pathFlashdumpLineEdit.setValidator(pValidator)
        self.pathHXFolderLineEdit.setValidator(pValidator)
        self.pathFWLineEdit.setValidator(pValidator)

        # options diagarr
        reg = QRegExp('[0-9]')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.diagArrText.setValidator(pValidator)

        # rawdata type, time
        reg = QRegExp('[1-9][0-9]')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.textEditDiag.setValidator(pValidator)

        reg = QRegExp('[1-9][0-9]{2}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.timeLineEdit.setValidator(pValidator)

        # DD Reg addr val
        reg = QRegExp('[0-9a-fA-F]{6}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.G1AddrlineEdit.setValidator(pValidator)
        self.G2AddrlineEdit.setValidator(pValidator)
        self.G3AddrlineEdit.setValidator(pValidator)
        reg = QRegExp('[0-9a-fA-F]{2}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        for i in range(64):
            getattr(self, "G1lineEdit%d" % (i + 1)).setValidator(pValidator)
            getattr(self, "G2lineEdit%d" % (i + 1)).setValidator(pValidator)
            getattr(self, "G3lineEdit%d" % (i + 1)).setValidator(pValidator)

    def initSelectProjectItems(self, init):
        if not init:
            self.settingsProComboBox.blockSignals(True)
            self.settingsProComboBox.clear()

        _translate = QtCore.QCoreApplication.translate
        projectList = self.findProjectFilesName()

        for i in range(len(projectList)):
            self.settingsProComboBox.addItem("")

        i = len(projectList) - 1
        while i >= 0:
            self.settingsProComboBox.setItemText(len(projectList) - 1 - i, _translate("MainWindow", projectList[i]))
            i = i - 1

        if not init:
            self.settingsProComboBox.blockSignals(False)

    def loadLatestTouchInfoConfig(self):
        path = self.findProjectDocFilesPath()

        with open(path, 'rb') as r:
            for line in r.readlines():
                line = str(line, encoding='UTF-8')
                line = line[:len(line) - 2]
                lineList = line.split('=')

                if lineList[0] == 'DRIVER_VERSION':
                    self.driverVersionMode = int(lineList[1])
                elif lineList[0] == 'RX':
                    self.rxnum = int(lineList[1])
                elif lineList[0] == 'TX':
                    self.txnum = int(lineList[1])
                elif lineList[0] == 'V1_DIAG_PATH':
                    self.v1DiagPath = lineList[1]
                elif lineList[0] == 'V1_REG_PATH':
                    self.v1RegisterPath = lineList[1]
                elif lineList[0] == 'V1_INT_EN_PATH':
                    self.v1IntEnPath = lineList[1]
                elif lineList[0] == 'V1_RESET_PATH':
                    self.v1ResetPath = lineList[1]
                elif lineList[0] == 'V1_SENSEONOFF_PATH':
                    self.v1SenseOnOffPath = lineList[1]
                elif lineList[0] == 'V1_DIAGARR_PATH':
                    self.v1DiagArrPath = lineList[1]
                elif lineList[0] == 'V2_STACK_PATH':
                    self.v2ReadStackPath = lineList[1]
                elif lineList[0] == 'SELFTEST_PATH':
                    self.selfTestPath = lineList[1]
                elif lineList[0] == 'DEBUG_PATH':
                    self.debugPath = lineList[1]
                elif lineList[0] == 'FLASH_DUMP_PATH':
                    self.flashDumpPath = lineList[1]
                elif lineList[0] == 'HX_FOLDER_PATH':
                    self.hxFolderPath = lineList[1]
                elif lineList[0] == 'FW_PATH':
                    self.fwPath = lineList[1]

        self.initEchoMethod(self.driverVersionMode)
        self.fillTouchConfig()
        self.initRawdataUI()

    def initEchoMethod(self, n):
        if n == 1:
            self.echoDiag = "echo %s > " + self.v1DiagPath
            self.catDiag = "cat " + self.v1DiagPath

            self.echoWriteRegister = "echo w:x%s:x%s > " + self.v1RegisterPath
            self.echoReadRegister = "echo r:x%s > " + self.v1RegisterPath
            self.catRegister = "cat " + self.v1RegisterPath

            self.echoIntEn = "echo %s > " + self.v1IntEnPath
            self.echoReset = "echo %s > " + self.v1ResetPath

            self.echoSenseOn = "echo 1 > " + self.v1SenseOnOffPath
            self.echoSenseOff = "echo 0 > " + self.v1SenseOnOffPath
        elif n == 2:
            self.echoDiag = "echo diag,%s > " + self.debugPath
            self.catDiag = "cat " + self.v2ReadStackPath

            self.echoWriteRegister = "echo register,w:x%s:x%s > " + self.debugPath
            self.echoReadRegister = "echo register,r:x%s > " + self.debugPath
            self.catRegister = "cat " + self.debugPath

            self.echoIntEn = "echo int_en,%s > " + self.debugPath
            self.echoReset = "echo reset,%s > " + self.debugPath

            self.echoSenseOn = "echo senseonoff,1 > " + self.debugPath
            self.echoSenseOff = "echo senseonoff,0 > " + self.debugPath

        self.catSelfTest = "cat " + self.selfTestPath
        self.echoFWVersion = "echo %s > " + self.debugPath
        self.catFWVersion = "cat " + self.debugPath

        self.pullHXFileCmd = "adb pull " + self.hxFolderPath

    def disableSomeFunctions(self, disable):
        self.tabOptions.setDisabled(disable)
        self.tabRawdata.setDisabled(disable)
        self.tabRWRegister.setDisabled(disable)
        self.tabDDRegister.setDisabled(disable)
        self.tabDDLog.setDisabled(disable)

    def saveSettingsToProject(self):
        # check all input data
        rx = self.touchInfoRXLineEdit.text()
        tx = self.touchInfoTXLineEdit.text()

        debug = self.pathDebugLineEdit.text()
        selftest = self.pathSelftestLineEdit.text()
        flashdump = self.pathFlashdumpLineEdit.text()
        hxfolder = self.pathHXFolderLineEdit.text()
        fw = self.pathFWLineEdit.text()

        if rx == '' or tx == '' or debug == '' or selftest == '' or flashdump == '' or hxfolder == '' or fw == '':
            self.dialogWin("Some input was empty!")
            return

        if self.pathV1RadioButton.isChecked():
            driverVersion = 1
            diag = self.pathDiagLineEdit.text()
            register = self.pathRegLineEdit.text()
            reset = self.pathResetLineEdit.text()
            inten = self.pathIntenLineEdit.text()
            diagarr = self.pathDiagarrLineEdit.text()
            senseonoff = self.pathSenseonoffLineEdit.text()

            if diag == '' or register == '' or inten == '' or diagarr == '' or senseonoff == '':
                self.dialogWin("Some input was empty!")
                return
        else:
            driverVersion = 2
            stack = self.pathStackLineEdit.text()

            if stack == '':
                self.dialogWin("stack was empty!")
                return

        # TODO:need show sub window to let user enter project name
        name = self.dialoInputgWin()
        if name == '':
            self.dialogWin("Name was empty")
            return

        fileName = './project/' + time.strftime("%Y%m%d%H%M%S_", time.localtime()) + name

        info = 'DRIVER_VERSION=' + str(driverVersion) + '\n'\
                + 'RX=' + rx + '\n'\
                + 'TX=' + tx + '\n'\
                + 'SELFTEST_PATH=' + selftest + '\n'\
                + 'DEBUG_PATH=' + debug + '\n'\
                + 'FLASH_DUMP_PATH=' + flashdump + '\n'\
                + 'HX_FOLDER_PATH=' + hxfolder + '\n'\
                + 'FW_PATH=' + fw + '\n'

        if driverVersion == 1:
            info = info + 'V1_DIAG_PATH=' + diag + '\n'\
                    + 'V1_REG_PATH=' + register + '\n'\
                    + 'V1_INT_EN_PATH=' + inten + '\n'\
                    + 'V1_RESET_PATH=' + reset + '\n'\
                    + 'V1_SENSEONOFF_PATH=' + senseonoff + '\n'\
                    + 'V1_DIAGARR_PATH=' + diagarr + '\n'
        else:
            info = info + 'V2_STACK_PATH=' + stack + '\n'

        projectFile = open(fileName, 'w+')
        projectFile.write(info)
        projectFile.close()

        # update select list
        self.initSelectProjectItems(False)

    def findProjectFilesName(self):
        path = "./project/"
        fileNames = os.listdir(path)

        if len(fileNames) == 0:
            self.dialogWin("No find project files!")
            return

        return fileNames

    def findProjectDocFilesPath(self):
        path = "./project/"
        fileNames = self.findProjectFilesName()

        for name in fileNames:
            fullfilename = os.path.join(path, name)

        return fullfilename

    def dialogWin(self, string):
        self.dialog = QDialog()
        self.dialog.resize(300, 115)
        self.dialog.setMaximumSize(QtCore.QSize(300, 115))
        self.buttonBoxTmp = QtWidgets.QDialogButtonBox(self.dialog)
        self.buttonBoxTmp.setGeometry(QtCore.QRect(0, 80, 291, 32))
        self.buttonBoxTmp.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxTmp.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxTmp.setObjectName("buttonBoxTmp")
        self.labelTmp = QtWidgets.QLabel(self.dialog)
        self.labelTmp.setGeometry(QtCore.QRect(5, 11, 295, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelTmp.setFont(font)
        self.labelTmp.setObjectName("labelTmp")
        self.labelTmp.setText(string)
        self.labelTmp.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(self.dialog)
        self.buttonBoxTmp.accepted.connect(self.dialog.accept)
        self.buttonBoxTmp.rejected.connect(self.dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "Confirm"))
        self.dialog.exec_()

    def dialoInputgWin(self):
        self.dialog = QDialog()
        self.dialog.resize(300, 115)
        self.dialog.setMaximumSize(QtCore.QSize(300, 100))
        self.buttonBoxTmp = QtWidgets.QDialogButtonBox(self.dialog)
        self.buttonBoxTmp.setGeometry(QtCore.QRect(0, 70, 291, 32))
        self.buttonBoxTmp.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxTmp.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxTmp.setObjectName("buttonBoxTmp")
        self.inputName = QtWidgets.QLineEdit(self.dialog)
        self.inputName.setGeometry(QtCore.QRect(5, 11, 290, 40))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.inputName.setFont(font)
        # self.labelTmp.setObjectName("labelTmp")
        # self.labelTmp.setText(string)
        self.inputName.setAlignment(QtCore.Qt.AlignCenter)
        reg = QRegExp('[a-zA-Z0-9]*')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.inputName.setValidator(pValidator)

        self.retranslateUi(self.dialog)
        self.buttonBoxTmp.accepted.connect(self.dialog.accept)
        self.buttonBoxTmp.rejected.connect(self.dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "Please enter project name"))
        if self.dialog.exec_() == QDialog.Accepted:
            # check file name is right or not
            if self.inputName.text() == '':
                return ''
            else:
                return self.inputName.text()
        else:
            return ''

    def initSettingsUi(self):
        self.touchInfoRXLineEdit.setDisabled(True)
        self.touchInfoTXLineEdit.setDisabled(True)
        self.touchInfoResXLineEdit.setDisabled(True)
        self.touchInfoResYLineEdit.setDisabled(True)

        self.pathDiagLineEdit.setDisabled(True)
        self.pathRegLineEdit.setDisabled(True)
        self.pathResetLineEdit.setDisabled(True)
        self.pathIntenLineEdit.setDisabled(True)
        self.pathDiagarrLineEdit.setDisabled(True)
        self.pathSenseonoffLineEdit.setDisabled(True)

        self.pathStackLineEdit.setDisabled(True)

        self.pathDebugLineEdit.setDisabled(True)
        self.pathSelftestLineEdit.setDisabled(True)
        self.pathFlashdumpLineEdit.setDisabled(True)
        self.pathHXFolderLineEdit.setDisabled(True)
        self.pathFWLineEdit.setDisabled(True)

        self.pathSavePushButton.setDisabled(True)

    def chooseDriverVersion(self):
        if self.pathV1RadioButton.isChecked():
            flag = False
            self.driverVersionMode = 1
        else:
            flag = True
            self.driverVersionMode = 2

        self.pathDiagLineEdit.setDisabled(flag)
        self.pathRegLineEdit.setDisabled(flag)
        self.pathResetLineEdit.setDisabled(flag)
        self.pathIntenLineEdit.setDisabled(flag)
        self.pathDiagarrLineEdit.setDisabled(flag)
        self.pathSenseonoffLineEdit.setDisabled(flag)

        self.pathStackLineEdit.setDisabled(not flag)

        self.touchInfoRXLineEdit.setDisabled(False)
        self.touchInfoTXLineEdit.setDisabled(False)

        self.pathDebugLineEdit.setDisabled(False)
        self.pathSelftestLineEdit.setDisabled(False)
        self.pathFlashdumpLineEdit.setDisabled(False)
        self.pathHXFolderLineEdit.setDisabled(False)
        self.pathFWLineEdit.setDisabled(False)

        self.pathSavePushButton.setDisabled(False)

        self.setDefaultDriverNodePath()

    def setDefaultDriverNodePath(self):
        if self.pathV1RadioButton.isChecked():
            self.pathDiagLineEdit.setText("/proc/android_touch/diag")
            self.pathRegLineEdit.setText("/proc/android_touch/register")
            self.pathIntenLineEdit.setText("/proc/android_touch/int_en")
            self.pathResetLineEdit.setText("/proc/android_touch/reset")
            self.pathSenseonoffLineEdit.setText("/proc/android_touch/SenseOnOff")
            self.pathDiagarrLineEdit.setText("/proc/android_touch/diag_arr")
            self.pathStackLineEdit.clear()
        else:
            self.pathStackLineEdit.setText("/proc/android_touch/diag/stack")
            self.pathDiagLineEdit.clear()
            self.pathRegLineEdit.clear()
            self.pathIntenLineEdit.clear()
            self.pathResetLineEdit.clear()
            self.pathSenseonoffLineEdit.clear()
            self.pathDiagarrLineEdit.clear()

        self.pathDebugLineEdit.setText("/proc/android_touch/debug")
        self.pathSelftestLineEdit.setText("/proc/android_touch/self_test")
        self.pathFlashdumpLineEdit.setText("/proc/android_touch/flash_dump")
        self.pathHXFolderLineEdit.setText("/sdcard/HimaxAPK/tmp")
        self.pathFWLineEdit.setText("/vendor/firmware/Himax_firmware.bin")

    def initRawdataUI(self):
        width = 32
        height = 13
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.MainRawdataShowtableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainRawdataShowtableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        sizePolicy.setHeightForWidth(self.MainRawdataShowtableWidget.sizePolicy().hasHeightForWidth())
        self.MainRawdataShowtableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.MainRawdataShowtableWidget.setSizePolicy(sizePolicy)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.setRowCount(self.rxnum + 2)
        self.MainRawdataShowtableWidget.setColumnCount(self.txnum + 2)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.verticalHeader().setVisible(False)
        self.MainRawdataShowtableWidget.horizontalHeader().setVisible(False)
        self.MainRawdataShowtableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.MainRawdataShowtableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.MainRawdataShowtableWidget.verticalHeader().setDefaultSectionSize(10)
        self.MainRawdataShowtableWidget.verticalHeader().setMinimumSectionSize(10)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.MainRawdataShowtableWidget.setFont(font)
        for i in range(self.txnum + 2):
            if i == 0:
                self.MainRawdataShowtableWidget.setColumnWidth(i, width - 7)
            else:
                self.MainRawdataShowtableWidget.setColumnWidth(i, width)
        for i in range(self.rxnum + 2):
            self.MainRawdataShowtableWidget.setRowHeight(i, height)

    """ new dd register read write """
    def reverseBacgroundColor(self, before, now, n):
        for i in range(64):
            m = getattr(self, "G%slineEdit%d" % (str(n+1), (i + 1)))
            if n == 0:
                m.setStyleSheet("background-color: rgb(255, 255, 255)")
            elif n == 1:
                m.setStyleSheet("background-color: rgb(255, 255, 255)")
            elif n == 2:
                m.setStyleSheet("background-color: rgb(255, 255, 255)")

            if before[i] != now[i]:
                if n == 0:
                    m.setStyleSheet("background-color: rgb(0, 255, 0)")
                elif n == 1:
                    m.setStyleSheet("background-color: rgb(0, 255, 0)")
                elif n == 2:
                    m.setStyleSheet("background-color: rgb(0, 255, 0)")

    def ddReadRegisterFunc(self, n):
        ret = ''
        if n == 0:
            ret = self.G1AddrlineEdit.text()
        elif n == 1:
            ret = self.G2AddrlineEdit.text()
        elif n == 2:
            ret = self.G3AddrlineEdit.text()

        # enable all line text
        self.disableLineReg(n, 0, False)

        if ret == '':
            string = "you need set value first"
            self.dialogWin(string)
            return
        elif len(ret) != 6:
            string = "value length isn't right"
            self.dialogWin(string)
            return

        # record before address
        self.beforeAddress = ret

        # translate to 4 byte
        tmpLen = ret[4:]
        tmpLen = int(tmpLen, 16)
        tmpLen = math.ceil(tmpLen/4) * 4
        self.regLength = tmpLen
        tmpLen = hex(tmpLen)
        tmpLen = tmpLen[2:]
        if len(tmpLen) == 1:
            tmpLen = '0' + tmpLen
        ret = ret[:4] + tmpLen
        self.disableLineReg(n, self.regLength, True)
        ret = self.readDDRegister(ret)
        ret = self.parseRegData(ret)
        if self.beforeRead != '':
            self.reverseBacgroundColor(self.beforeRead, ret, n)
        self.ret = ret
        self.beforeRead = ret
        self.fillDataToRegisterLineText(ret, n)

    def disableLineReg(self, n, m, b):
        if b:
            if n == 0:
                for i in range(64 - m):
                    a = getattr(self, "G1lineEdit%d" % (i + m + 1))
                    a.setDisabled(b)
            elif n == 1:
                for i in range(64 - m):
                    a = getattr(self, "G2lineEdit%d" % (i + m + 1))
                    a.setDisabled(b)
            elif n == 2:
                for i in range(64 - m):
                    a = getattr(self, "G3lineEdit%d" % (i + m + 1))
                    a.setDisabled(b)
        else:
            if n == 0:
                for i in range(64):
                    a = getattr(self, "G1lineEdit%d" % (i + 1))
                    a.setDisabled(b)
            elif n == 1:
                for i in range(64):
                    a = getattr(self, "G2lineEdit%d" % (i + 1))
                    a.setDisabled(b)
            elif n == 2:
                for i in range(64):
                    a = getattr(self, "G3lineEdit%d" % (i + 1))
                    a.setDisabled(b)

    def ddWriteRegisterFunc(self, n):
        if len(self.ret) == 0:
            self.dialogWin("You need read first!")
            return

        ret = ''
        addr = ''
        index = []
        tmpIndex = []
        realIndex = []
        localAddr = '10007f'

        if n == 0:
            addr = self.G1AddrlineEdit.text()
            for i in range(64):
                m = getattr(self, "G1lineEdit%d" % (i + 1))
                # check val is right?
                if m.text() == '':
                    self.dialogWin("value is null!")
                    return
                elif len(m.text()) == 1:
                    m.setText('0' + m.text())
                ret += m.text() + ','
        elif n == 1:
            addr = self.G2AddrlineEdit.text()
            for i in range(64):
                m = getattr(self, "G2lineEdit%d" % (i + 1))
                # check val is right?
                if m.text() == '':
                    self.dialogWin("value is null!")
                    return
                elif len(m.text()) == 1:
                    m.setText('0' + m.text())
                ret += m.text() + ','
        elif n == 2:
            addr = self.G3AddrlineEdit.text()
            for i in range(64):
                m = getattr(self, "G3lineEdit%d" % (i + 1))
                # check val is right?
                if m.text() == '':
                    self.dialogWin("value is null!")
                    return
                elif len(m.text()) == 1:
                    m.setText('0' + m.text())
                ret += m.text() + ','

        # check addr right or wrong
        if len(addr) != 6:
            self.dialogWin("addr was not right")
            return

        # compare this address with before
        if self.beforeAddress != addr:
            self.dialogWin("addr was changed!")
            return

        # get changed index
        ret = ret.split(',')
        for i in range(64):
            if ret[i] != self.ret[i]:
                index.append(i)

        # get which 4 bytes was changed
        for i in range(len(index)):
            tmpIndex.append(int(index[i]/4))

        # check change index
        if len(tmpIndex) == 0:
            self.dialogWin("you changed nothing!")
            return
        else:
            for i in tmpIndex:
                if i not in realIndex:
                    realIndex.append(i)

        # deal final address
        for i in range(len(realIndex)):
            a = realIndex[i] * 4 + 0x80
            a = hex(a)
            finalAddr = localAddr + a[2:]
            finalVal = ret[realIndex[i]*4+3] + ret[realIndex[i]*4+2] + ret[realIndex[i]*4+1] + ret[realIndex[i]*4]

            # parse addr
            tmpAddr = (realIndex[i] + 1) * 4
            tmpAddr = hex(tmpAddr)
            if len(tmpAddr) == 3:
                tmpAddr = '0' + tmpAddr[2:]
            else:
                tmpAddr = tmpAddr[2:]

            addr = addr[:4] + tmpAddr

            cmd = self.echoWriteRegister % (finalAddr, finalVal)
            self.DDreadRegValShowText.append(cmd)
            adb.shell(cmd, "SHELL")
            cmd = self.echoWriteRegister % ('900000FC', 'CC' + addr)
            self.DDreadRegValShowText.append(cmd)
            adb.shell(cmd, "SHELL")
            cmd = self.echoReadRegister % (localAddr + '80')
            self.DDreadRegValShowText.append(cmd)
            adb.shell(cmd, "SHELL")
            cmd = self.catRegister
            self.DDreadRegValShowText.append(cmd)
            ret = adb.shell(cmd, "SHELL")
            self.DDreadRegValShowText.append(ret)

        # clear read register data
        self.ret = []

    def ddCopyRegisterFunc(self, n):
        ret = ''
        if n == 0:
            ret += self.G1AddrlineEdit.text() + ':'
            for i in range(64):
                if i % 8 == 0:
                    ret += '\n'
                m = getattr(self, "G1lineEdit%d" % (i + 1))
                ret += m.text() + ','
        elif n == 1:
            ret += self.G2AddrlineEdit.text() + ':'
            for i in range(64):
                if i % 8 == 0:
                    ret += '\n'
                m = getattr(self, "G2lineEdit%d" % (i + 1))
                ret += m.text() + ','
        elif n == 2:
            ret += self.G3AddrlineEdit.text() + ':'
            for i in range(64):
                if i % 8 == 0:
                    ret += '\n'
                m = getattr(self, "G3lineEdit%d" % (i + 1))
                ret += m.text() + ','

        ret += '\n'
        pyperclip.copy(ret)
        pyperclip.paste()

    def ddClearRegisterFunc(self, n):
        if n == 0:
            for i in range(64):
                m = getattr(self, "G1lineEdit%d" % (i + 1))
                m.clear()
        elif n == 1:
            for i in range(64):
                m = getattr(self, "G2lineEdit%d" % (i + 1))
                m.clear()
        elif n == 2:
            for i in range(64):
                m = getattr(self, "G3lineEdit%d" % (i + 1))
                m.clear()

        self.ret = []

    def fillDataToRegisterLineText(self, data, n):
        if n == 0:
            for i in range(64):
                m = getattr(self, "G1lineEdit%d" % (i + 1))
                m.setText(data[i])
        elif n == 1:
            for i in range(64):
                m = getattr(self, "G2lineEdit%d" % (i + 1))
                m.setText(data[i])
        elif n == 2:
            for i in range(64):
                m = getattr(self, "G3lineEdit%d" % (i + 1))
                m.setText(data[i])

    def readDDRegister(self, ret):
        val = "AA" + str(ret)
        cmd = self.echoWriteRegister % ("900000FC", val)
        adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)

        cmd = self.echoReadRegister % "10007F80"
        adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)

        cmd = self.catRegister
        ret = adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)
        self.DDreadRegValShowText.append(ret)
        return ret

    def parseRegData(self, data):
        data = data[22:]
        info = re.compile('0x')
        data = info.sub('', data)
        info = re.compile('\n')
        data = info.sub('', data)
        data = data.split(' ')
        return data

    """ touch register read write """
    def initHistoryFunc(self):
        self.openBlight.setDisabled(True)

        self.ret = ''
        self.beforeRead = ''
        self.historyFile = './settings/register_history'
        self.showRawdataFlag = 0
        self.showKmsgFlag = 0
        self.showGeteventFlag = 0
        self.device_ip = ""
        self.device_ip_port = ""
        self.port = ""
        self.logFlag = False

        with open(self.historyFile, 'rb') as r:
            for line in r.readlines():
                line = str(line, encoding='UTF-8')
                line = line[:len(line) - 2]
                line = line.split(':')
                if line[0] == 'R':
                    length = len(line)
                    self.textEditReadRegAddr.clear()
                    for i in range(length):
                        if i == 0:
                            continue
                        self.textEditReadRegAddr.append(line[i])
                elif line[0] == 'W0':
                    self.textEditWriteAddr0.clear()
                    self.textEditWriteAddr0.append(line[1])
                    self.textEditWriteVal0.clear()
                    self.textEditWriteVal0.append(line[2])
                elif line[0] == 'W1':
                    self.textEditWriteAddr1.clear()
                    self.textEditWriteAddr1.append(line[1])
                    self.textEditWriteVal1.clear()
                    self.textEditWriteVal1.append(line[2])
                elif line[0] == 'W2':
                    self.textEditWriteAddr2.clear()
                    self.textEditWriteAddr2.append(line[1])
                    self.textEditWriteVal2.clear()
                    self.textEditWriteVal2.append(line[2])
                elif line[0] == 'W3':
                    self.textEditWriteAddr3.clear()
                    self.textEditWriteAddr3.append(line[1])
                    self.textEditWriteVal3.clear()
                    self.textEditWriteVal3.append(line[2])
                elif line[0] == 'W4':
                    self.textEditWriteAddr4.clear()
                    self.textEditWriteAddr4.append(line[1])
                    self.textEditWriteVal4.clear()
                    self.textEditWriteVal4.append(line[2])

    def readRegFunc(self):
        readRegInfo = ""
        lines = int(self.reglength.currentText())
        addr = self.textEditReadRegAddr.toPlainText().split('\n')

        for i in range(len(addr)):
            regAddress = (addr[i])
            regInfo = self.readRegister(regAddress)
            regInfo = regInfo[:103 + 81 * (lines - 1)] + '\n'
            readRegInfo += regInfo

        self.readRegValShowText.append(readRegInfo)
        self.writeHistoryFile(addr, 9, 9)

    def readRegister(self, regAddress):
        readRegInfo = ""
        regAddressList = regAddress.split()

        # Deal with reg_address without space
        if len(regAddressList) > 0:
            if len(regAddressList[0]) == 8:
                regAddress = regAddressList[0]
            elif len(regAddressList[0]) == 10 and (regAddressList[0][0:2] == "0x" or regAddressList[0][0:2] == "0X"):
                regAddress = regAddressList[0][2:]
            else:
                regAddress = ""
        else:
            regAddress = ""

        if len(regAddress) == 8:
            cmd = self.echoReadRegister % regAddress
            adb.shell(cmd, "SHELL")
            readRegInfo = adb.shell(self.catRegister, "SHELL")

        return readRegInfo

    def writeHistoryFile(self, addr, val, n):
        if addr == '\n' or addr == '\r\n' or addr == '':
            return

        if val == 9 and n == 9:
            cmd = 'R:'
            i = 0
            length = len(addr)
            while i < length:
                if i == length - 1:
                    cmd += addr[i]
                else:
                    cmd += addr[i] + ':'
                i = i + 1
        else:
            cmd = 'W%s:' % n
            cmd = cmd + addr + ':' + val

        f = open(self.historyFile, 'a+')
        f.write(cmd + '\n')
        f.close()

    def writeRegFunc(self, n):
        if n == 0:
            addr = self.textEditWriteAddr0.toPlainText()
            val = self.textEditWriteVal0.toPlainText()
        elif n == 1:
            addr = self.textEditWriteAddr1.toPlainText()
            val = self.textEditWriteVal1.toPlainText()
        elif n == 2:
            addr = self.textEditWriteAddr2.toPlainText()
            val = self.textEditWriteVal2.toPlainText()
        elif n == 3:
            addr = self.textEditWriteAddr3.toPlainText()
            val = self.textEditWriteVal3.toPlainText()
        elif n == 4:
            addr = self.textEditWriteAddr4.toPlainText()
            val = self.textEditWriteVal4.toPlainText()

        if addr == '' or val == '':
            return
        self.writeRegister(addr, val)
        self.writeHistoryFile(addr, val, n)

    def writeRegister(self, regAddress, write_value):
        regAddressList = regAddress.split()


        # Deal with reg_address without space
        if len(regAddressList) > 0:
            if len(regAddressList[0]) == 8:
                regAddress = regAddressList[0]
            elif len(regAddressList[0]) == 10 and (
                regAddressList[0][0:2] == "0x" or regAddressList[0][0:2] == "0X"):
                regAddress = regAddressList[0][2:]
            else:
                regAddress = ""
        else:
            regAddress = ""


        # Deal with value for set as 8 digit
        while len(write_value) < 8 and len(write_value) != 0:
            write_value = "0" + write_value

        if len(regAddress) == 8 and len(write_value) != 0:
            cmd = self.echoWriteRegister % (regAddress, write_value)
            adb.shell(cmd, "SHELL")

    """ rawdata show """
    def chooseRawdataType(self):
        if self.radioDC.isChecked():
            adb.shell(self.echoDiag % '2', "SHELL")
        elif self.radioIIR.isChecked():
            adb.shell(self.echoDiag % '1', "SHELL")
        elif self.radioTmp.isChecked():
            type = self.textEditDiag.text()
            if type == '':
                return False
            adb.shell(self.echoDiag % type, "SHELL")
        else:
            return False

        return True

    def rawdataReadFunc(self):
        # choose rawdata type
        if not self.chooseRawdataType():
            self.dialogWin("Please set type")
            return

        if self.rawdataRead.objectName() == 'rawdataRead':
            self.rawdataRead.setObjectName('rawdataReadStop')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/stop_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rawdataRead.setIcon(icon)
            self.rawdataRead.setIconSize(QtCore.QSize(39, 39))

            # cat diag
            self.readRawdataThread = Thread(target=self.showRawdata)
            self.readRawdataThread.start()
        else:
            self.rawdataRead.setObjectName('rawdataRead')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/start_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rawdataRead.setIcon(icon)
            self.rawdataRead.setIconSize(QtCore.QSize(39, 39))

            self.showRawdataFlag = 0
            self.showKmsgFlag = 0
            self.showGeteventFlag = 0

            if self.logFlag:
                self.logFile.close()

            self.logFlag = False
            self.log.setDisabled(False)
            self.log.setText("Log")
            self.log.setStyleSheet("color: rgb(0, 0, 0)")

            adb.shell(self.echoDiag % '0', "SHELL")

    def showRawdata(self):
        self.showRawdataFlag = 1
        while self.showRawdataFlag:
            ret = adb.shell(self.catDiag, "SHELL")
            data = self.analysisRawdata(ret)
            self.fillRawdataToTable(data)
            self.MainRawdataShowtableWidget.reset()
            self.MainRawdataShowtableWidget.update()
            if self.logFlag:
                self.logFile.write(ret)

    def analysisRawdata(self, rawdata):
        index = rawdata.find('[00]')
        rawdata = rawdata[index:]
        rawdata = (' '.join(rawdata.split()))
        rawdata = rawdata.split(' ')
        rawdata.insert(19, '0')
        rawdata.insert((self.rxnum + 1) * (self.txnum + 2), '0')
        return rawdata

    def fillRawdataToTable(self, rawdata):
        for i in range(self.rxnum + 2):
            for j in range(self.txnum + 2):
                    a = QTableWidgetItem(rawdata[i * (self.txnum + 2) + j])
                    self.MainRawdataShowtableWidget.setItem(i, j, a)

    def logFunc(self):
        if self.showRawdataFlag == 0:
            string = "Please read first!"
            self.dialogWin(string)
            return

        self.fileName = time.strftime('.\/log\/' + "%Y%m%d_%H_%M_%S", time.localtime()) + ".txt"
        self.logFlag = True
        self.logFile = open(self.fileName, 'a+')

        # toggle
        self.log.setDisabled(True)
        self.log.setText("Ing.")
        self.log.setStyleSheet("color: rgb(255, 0, 0)")

    """ touch """
    def touchDiagArrFunc(self):
        name = self.diagArrText.text()
        if name == '':
            self.rawdataShowText.append("please set value!")
            return

        if self.driverVersionMode == 1:
            cmd = "echo %s > " % name + self.v1DiagArrPath
        elif self.driverVersionMode == 2:
            cmd = "echo diag_arr,%s > " % name + self.debugPath
        adb.shell(cmd, "SHELL")

        self.rawdataShowText.append(cmd)

    def touchSenseOnFunc(self):
        if self.senseon.text() == 'SenseOn':
            self.senseon.setText('SenseOff')
            adb.shell(self.echoSenseOff, "SHELL")
            self.rawdataShowText.append(self.echoSenseOff)
        else:
            self.senseon.setText('SenseOn')
            adb.shell(self.echoSenseOn, "SHELL")
            self.rawdataShowText.append(self.echoSenseOn)

    def touchSelfTestFunc(self):
        self.selftestThread = Thread(target=self.selftestThreadFunc)
        self.selftestThread.start()

    def selftestThreadFunc(self):
        ret = adb.shell(self.catSelfTest, "SHELL")
        self.rawdataShowText.append(ret)
        self.rawdataShowText.update()

    def touchFWVersionFunc(self):
        adb.shell(self.echoFWVersion % "v", "SHELL")
        ret = adb.shell(self.catFWVersion, "SHELL")
        # ret = str(ret, encoding='utf-8')
        self.rawdataShowText.append(ret)

    def touchResetFunc(self):
        adb.shell(self.echoReset % "1", "SHELL")
        self.rawdataShowText.append(self.echoReset % "1")

    def touchIntenFunc(self):
        if self.inten0.text() == 'Int_en':
            self.inten0.setText('Int_dis')
            adb.shell(self.echoIntEn % "0", "SHELL")
            self.rawdataShowText.append("disable irq")
        else:
            self.inten0.setText('Int_en')
            adb.shell(self.echoIntEn % "1", "SHELL")
            self.rawdataShowText.append("enable irq")

    def touchFlashDumpFunc(self):
        self.rawdataShowText.append("will be add flash dump func\n")

    def touchUpdateFWFunc(self):
        fw_path = self.updateFWText.toPlainText()
        if fw_path == "":
            self.rawdataShowText.append("please choose fw file!")
            return
        ret = adb.shell("adb push %s " % fw_path + self.fwPath)
        self.rawdataShowText.append(ret)
        ret = adb.shell("echo t Himax_firmware.bin > " + self.debugPath, "SHELL")
        self.rawdataShowText.append(ret)

    def touchDebugTypeFunc(self):
        adb.shell("echo %s > " % self.debugComboBox.currentText() + self.debugPath, 'SHELL')
        ret = adb.shell("cat " + self.debugPath, 'SHELL')
        self.rawdataShowText.append(ret)

    """ display """
    def display1129Func(self):
        if self.driverVersionMode == 1:
            cmd1 = "echo w:x30011000 > " + self.v1RegisterPath
            cmd2 = "echo w:x30029000 > " + self.v1RegisterPath
        else:
            cmd1 = "echo register,w:x30011000 > " + self.debugPath
            cmd2 = "echo register,w:x30029000 > " + self.debugPath

        adb.shell(cmd1, "SHELL")
        adb.shell("sleep 1", "SHELL")
        adb.shell(cmd2, "SHELL")
        self.rawdataShowText.append(cmd1)
        self.rawdataShowText.append(cmd2)

    def display2810Func(self):
        if self.driverVersionMode == 1:
            cmd1 = "echo w:x30028000 > " + self.v1RegisterPath
            cmd2 = "echo w:x30010000 > " + self.v1RegisterPath
        else:
            cmd1 = "echo register,w:x30028000 > " + self.debugPath
            cmd2 = "echo register,w:x30010000 > " + self.debugPath

        adb.shell(cmd1, "SHELL")
        adb.shell("sleep 1", "SHELL")
        adb.shell(cmd2, "SHELL")
        self.rawdataShowText.append(cmd1)
        self.rawdataShowText.append(cmd2)

    """ wifi func """
    def wifiConnectFunc(self):
        self.threadWifiConnect = Thread(target=self.waitConnectFunc)
        self.threadWifiConnect.start()

    def waitConnectFunc(self):
        self.rawdataShowText.append("Start connect wifi adb")
        self.port = 8888
        self.wifiConnect.setDisabled(True)
        self.wifiConnect.setStyleSheet("color: rgb(105, 105, 105)")
        self.wifiConnectFlag = 1
        deviceInfo = (adb.shell("adb devices"))
        self.rawdataShowText.append(deviceInfo)
        # deviceInfo = str(deviceInfo, encoding='utf-8')
        try:
            device_list = deviceInfo.split()
            device_list.remove("List")
            device_list.remove("of")
            device_list.remove("devices")
            device_list.remove("attached")
            device_list.remove("device")
        except:
            self.rawdataShowText.append("Please connect device first!")
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return False

        deviceName = device_list[0]
        self.rawdataShowText.append(deviceName)
        self.wifiStatus.setText("Connect...")

        # Get device ip & set port
        cmd = "adb -s %s shell ip -f inet addr show wlan0" % deviceName
        ip = adb.shell(cmd)
        # ip = str(ip, encoding='utf-8')
        ip = ip[ip.find("inet 1") + 5:ip.find("/")]
        cmd = "adb -s %s tcpip %s" % (deviceName, self.port)
        ret = adb.shell(cmd)
        self.rawdataShowText.append(ret)
        if self.wifiConnectFlag == 0:
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return

        # Connect
        self.device_ip = ip
        self.device_ip_port = str(ip) + ":" + str(self.port)
        cmd = "adb connect %s:%s" % (self.device_ip, self.port)

        response = ""
        while response.find("already") < 0 and self.wifiConnectFlag != 0:
            response = (adb.shell(cmd))
        # response = str(response, encoding='utf-8')
        if self.wifiConnectFlag == 0:
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return

        # Polling wait unplugin
        devices = (adb.shell("adb devices"))
        # devices = str(devices, encoding='utf-8')
        response = ""

        self.rawdataShowText.append("Unplugin")
        self.wifiStatus.setText("Unplugin...")

        while devices.find(deviceName) < 0 and self.wifiConnectFlag != 0:
            devices = (adb.shell("adb devices"))
        # devices = str(devices, encoding='utf-8')

        if self.wifiConnectFlag == 0:
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return

        # Connect
        cmd = "adb connect %s:%s" % (self.device_ip, self.port)
        while response.find("already") < 0 and self.wifiConnectFlag != 0:
            response = (adb.shell(cmd))
        if self.wifiConnectFlag == 0:
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return

        self.rawdataShowText.append("Wifi Connect Done")
        self.wifiStatus.setText("Connected")
        self.wifiStatus.setStyleSheet("color: rgb(0, 255, 0)")
        self.wifiConnect.setDisabled(False)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")

    def wifiReconnectFunc(self):
        cmd = "adb connect %s:%s" % (self.device_ip, self.port)
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def wifiDisconnectFunc(self):
        adb.shell("adb disconnect")
        self.wifiStatus.setText("Disconnect")
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0)")
        self.wifiConnect.setDisabled(False)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
        self.wifiConnectFlag = 0
        self.device_ip = ""
        self.device_ip_port = ""
        self.rawdataShowText.append("adb disconnect")

    """ adb """
    def rootFunc(self):
        ret = adb.shell("adb root")
        self.rawdataShowText.append(ret)
        if ret == '' or 'error' in ret:
            self.adbStatus.setText('Failed')
            self.adbStatus.setStyleSheet("color: rgb(255, 0, 0);")
            return
        else:
            self.adbStatus.setText('OK')
            self.adbStatus.setStyleSheet("color: rgb(0, 255, 0);")

        ret = adb.shell("adb remount")
        self.rawdataShowText.append(ret)
        ret = adb.shell("adb shell setenforce 0")
        self.rawdataShowText.append('setenforce 0')

    def homeKeyFunc(self):
        cmd = "adb shell input keyevent KEYCODE_HOME"
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def backKeyFunc(self):
        cmd = "adb shell input keyevent KEYCODE_BACK"
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def volUpFunc(self):
        cmd = "adb shell input keyevent KEYCODE_VOLUME_UP"
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def volDownFunc(self):
        cmd = "adb shell input keyevent KEYCODE_VOLUME_DOWN"
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def hideShowVirtualFunc(self):
        if self.hideShowVirtual.text() == 'ShowVirtual':
            self.hideShowVirtual.setText("HideVirtual")
            cmd = "adb shell settings put global policy_control immersive.full=*"
            adb.shell(cmd)
            self.rawdataShowText.append(cmd)
        else:
            self.hideShowVirtual.setText("ShowVirtual")
            cmd = "adb shell settings put global policy_control null"
            adb.shell(cmd)
            self.rawdataShowText.append(cmd)

    def powerKeyFunc(self):
        adb.shell(None, "KEYEVENT", 26)

    def openClosePointFunc(self):
        if self.openClosePoint.text() == 'OpenPoint':
            self.openClosePoint.setText("ClosePoint")
            cmd = "settings put system pointer_location 1"
            adb.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
            cmd = "settings put system show_touches 1"
            adb.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
        else:
            self.openClosePoint.setText("OpenPoint")
            cmd = "settings put system pointer_location 0"
            adb.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
            cmd = "settings put system show_touches 0"
            adb.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)

    def screenShotFunc(self):
        self.rawdataShowText.append("Screen Shot...")
        name = time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) + ".png"
        cmd = "adb wait-for-device shell screencap -p /sdcard/%s" % (name)
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)
        cmd = "adb pull /sdcard/%s" % name
        adb.shell(cmd)
        self.rawdataShowText.append(cmd)

    def shutDownFunc(self):
        adb.shell("adb shell reboot -p")
        self.rawdataShowText.append("adb shell reboot -p")

    def rebootFunc(self):
        adb.shell("adb reboot")

    def openCMDFunc(self):
        cmd = "C:\Windows\System32\cmd.exe"
        os.startfile(cmd)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
