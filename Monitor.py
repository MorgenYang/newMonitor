from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
import sys
import adbtool
from threading import Thread
import time
import datetime
import os
import re
import pyperclip
import math
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # get screen resolution
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # set rawdata ui config
        self.rawdataWidth = 37
        self.rawdataHeight = 15

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.uiThreadInitHistory = Thread(target=self.ui.initHistoryFunc)
        self.uiThreadInitHistory.start()
        self.uiThreadSetRegExp = Thread(target=self.ui.setRegExp())
        self.uiThreadSetRegExp.start()
        self.uiThreadLoadLatestTouchInfoConfig = Thread(target=self.ui.loadLatestTouchInfoConfig())
        self.uiThreadLoadLatestTouchInfoConfig.start()
        self.uiThreadInitSelectProjectItems = Thread(target=self.ui.initSelectProjectItems(True))
        self.uiThreadInitSelectProjectItems.start()
        self.uiThreadBindEventFunc = Thread(target=self.ui.bindEventFunc())
        self.uiThreadBindEventFunc.start()
        self.statusBar().addWidget(QLabel("Ready"))

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()
            login.show()

        if key == QtCore.Qt.Key_T:
            self.ui.readRegValShowText.clear()

        if key == QtCore.Qt.Key_D:
            self.ui.DDreadRegValShowText.clear()

        if key == QtCore.Qt.Key_A:
            self.ui.rawdataShowText.clear()

        # calculate SNR
        # TODO: start collect no touched rawdata noise
        if key == QtCore.Qt.Key_S:
            if not self.ui.transRawdataPattern():
                return

            times = 10

            sumN = [0] * window.ui.rxnum * window.ui.txnum
            N = [0] * window.ui.rxnum * window.ui.txnum
            tmp = [0] * window.ui.transTX * window.ui.transRX
            rawdataN = [tmp] * times

            baseData = [0] * window.ui.rxnum * window.ui.txnum
            adbtool.shell(self.ui.echoDiag % '2', "SHELL")

            # TODO: collect no touched rawdata and calculate N
            for i in range(times):
                ret = adbtool.shell(self.ui.catDiag, "SHELL")
                ret = child.ui.analysisRawdata(ret)
                rawdataN[i] = child.ui.userPatternToMutual(ret)
                sumN = child.ui.sumRawdata(sumN, rawdataN[i])

            # TODO: calculate base data
            for j in range(window.ui.rxnum * window.ui.txnum):
                baseData[j] = sumN[j]/times

            print(baseData)

            # TODO: calculate each block data
            for j in range(window.ui.rxnum * window.ui.txnum):
                for i in range(times):
                    N[j] += (rawdataN[i][j] - baseData[j]) * (rawdataN[i][j] - baseData[j])
                N[j] = math.sqrt(N[j]/times)

            print(N)

            avgN = sum(N)/(window.ui.rxnum * window.ui.txnum)
            print(avgN)
            print("Calculated N")

            # TODO: collect touched rawdata and calculate S
            window.ui.dialogWin("Now start collect touched rdata")
            print("started")

            maxS = [0] * times
            tmp = [0] * window.ui.transTX * window.ui.transRX
            rawdataS = [tmp] * times

            for i in range(times):
                ret = adbtool.shell(self.ui.catDiag, "SHELL")
                ret = child.ui.analysisRawdata(ret)
                rawdataS[i] = child.ui.userPatternToMutual(ret)

            for j in range(window.ui.rxnum * window.ui.txnum):
                for i in range(times):
                    rawdataS[i][j] = rawdataS[i][j] - baseData[j]

            for i in range(times):
                maxS[i] = max(rawdataS[i])

            S = sum(maxS)/times
            print("calculated S")

            print(math.log(S/avgN, 10) * 20)

        if key == QtCore.Qt.Key_X:
            pass

        # TODO: calculate SNR
        if key == QtCore.Qt.Key_R:
            pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        i = QIcon("./img/himax_logo.ico")
        MainWindow.setWindowIcon(i)
        MainWindow.resize(590, 480)
        MainWindow.setMinimumSize(QtCore.QSize(590, 480))
        MainWindow.setMaximumSize(QtCore.QSize(590, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 461))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TabMainWindow = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.TabMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TabMainWindow.setFont(font)
        self.TabMainWindow.setObjectName("TabMainWindow")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.touchInfoGroupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.touchInfoGroupBox.setGeometry(QtCore.QRect(0, 0, 221, 81))
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
        self.settingsGroupBox.setGeometry(QtCore.QRect(0, 80, 580, 350))
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
        self.pathConmmentLabel.setGeometry(QtCore.QRect(210, 20, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pathConmmentLabel.setFont(font)
        self.pathConmmentLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.pathConmmentLabel.setObjectName("pathConmmentLabel")
        self.groupBox = QtWidgets.QGroupBox(self.tabSettings)
        self.groupBox.setGeometry(QtCore.QRect(230, 0, 351, 81))
        self.groupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox.setObjectName("groupBox")
        self.conmment = QtWidgets.QLabel(self.groupBox)
        self.conmment.setGeometry(QtCore.QRect(0, 55, 95, 15))
        self.conmment.setAutoFillBackground(False)
        self.conmment.setStyleSheet("color: rgb(0, 0, 0);")
        self.conmment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conmment.setObjectName("conmment")
        self.settingsProComboBox = QtWidgets.QComboBox(self.groupBox)
        self.settingsProComboBox.setGeometry(QtCore.QRect(100, 20, 160, 25))
        self.settingsProComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsProComboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.settingsProComboBox.setObjectName("settingsProComboBox")
        self.pathSavePushButton = QtWidgets.QPushButton(self.groupBox)
        self.pathSavePushButton.setGeometry(QtCore.QRect(100, 50, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pathSavePushButton.setFont(font)
        self.pathSavePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pathSavePushButton.setWhatsThis("")
        self.pathSavePushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
	"background-color: rgb(0, 170, 0);")
        self.pathSavePushButton.setObjectName("pathSavePushButton")
        self.conmment_2 = QtWidgets.QLabel(self.groupBox)
        self.conmment_2.setGeometry(QtCore.QRect(0, 25, 95, 15))
        self.conmment_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.conmment_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conmment_2.setObjectName("conmment_2")
        self.settingRemove = QtWidgets.QPushButton(self.groupBox)
        self.settingRemove.setGeometry(QtCore.QRect(270, 50, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.settingRemove.setFont(font)
        self.settingRemove.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)")
        self.settingRemove.setObjectName("settingRemove")
        self.settingRemoveLabel = QtWidgets.QLabel(self.groupBox)
        self.settingRemoveLabel.setGeometry(QtCore.QRect(270, 20, 75, 20))
        self.settingRemoveLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.settingRemoveLabel.setObjectName("settingRemoveLabel")
        self.TabMainWindow.addTab(self.tabSettings, "")
        self.tabOptions = QtWidgets.QWidget()
        self.tabOptions.setObjectName("tabOptions")
        self.wifiGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.wifiGroupBox.setGeometry(QtCore.QRect(0, 0, 580, 50))
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
        self.wifiStatus.setGeometry(QtCore.QRect(290, 15, 96, 30))
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
        self.root.setGeometry(QtCore.QRect(390, 15, 90, 30))
        self.root.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.root.setFont(font)
        self.root.setStyleSheet("background-color: rgb(187, 255, 255);")
        self.root.setObjectName("root")
        self.adbStatus = QtWidgets.QLabel(self.wifiGroupBox)
        self.adbStatus.setGeometry(QtCore.QRect(480, 15, 100, 30))
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
        self.adbGroupBox.setGeometry(QtCore.QRect(0, 50, 580, 86))
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
        self.screenShot.setGeometry(QtCore.QRect(390, 50, 90, 30))
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
        self.opencmd.setGeometry(QtCore.QRect(295, 15, 90, 30))
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
        self.screenRecord = QtWidgets.QPushButton(self.adbGroupBox)
        self.screenRecord.setGeometry(QtCore.QRect(485, 50, 90, 30))
        self.screenRecord.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.screenRecord.setFont(font)
        self.screenRecord.setStyleSheet("color: rgb(0, 0, 0);")
        self.screenRecord.setObjectName("screenRecord")
        self.touchGroupBox = QtWidgets.QGroupBox(self.tabOptions)
        self.touchGroupBox.setGeometry(QtCore.QRect(0, 135, 580, 81))
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
        self.displayGroupBox.setGeometry(QtCore.QRect(0, 220, 580, 50))
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
        self.showRawdataUI = QtWidgets.QPushButton(self.displayGroupBox)
        self.showRawdataUI.setGeometry(QtCore.QRect(430, 15, 150, 30))
        self.showRawdataUI.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.showRawdataUI.setFont(font)
        self.showRawdataUI.setStyleSheet("background-color: rgb(187, 255, 255);")
        self.showRawdataUI.setObjectName("showRawdataUI")
        self.rawdataShowText = QtWidgets.QTextBrowser(self.tabOptions)
        self.rawdataShowText.setGeometry(QtCore.QRect(10, 268, 570, 160))
        self.rawdataShowText.setMaximumSize(QtCore.QSize(700, 205))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.TabMainWindow.addTab(self.tabOptions, "")
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
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 150, 585, 280))
        self.readRegValShowText.setMinimumSize(QtCore.QSize(0, 0))
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
        self.G1DDClear = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDClear.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDClear.setFont(font)
        self.G1DDClear.setObjectName("G1DDClear")
        self.G1DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox1)
        self.G1DDCopy.setGeometry(QtCore.QRect(420, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G1DDCopy.setFont(font)
        self.G1DDCopy.setObjectName("G1DDCopy")
        for i in range(64):
            setattr(self, "G1lineEdit%d" % (i + 1), QtWidgets.QLineEdit(self.ddRegGroupBox1))
            m = getattr(self, "G1lineEdit%d" % (i + 1))
            if i // 8 == 1 or i // 8 == 3 or i // 8 == 5 or i // 8 == 7:
                m.setGeometry(QtCore.QRect(20 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            else:
                m.setGeometry(QtCore.QRect(0 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            font = QtGui.QFont()
            font.setPointSize(11)
            m.setFont(font)
            m.setStyleSheet("")
            m.setAlignment(QtCore.Qt.AlignCenter)
            m.setObjectName("G1lineEdit%d" % (i + 1))

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
        self.G2DDClear = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDClear.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDClear.setFont(font)
        self.G2DDClear.setObjectName("G2DDClear")
        self.G2DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox2)
        self.G2DDCopy.setGeometry(QtCore.QRect(420, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G2DDCopy.setFont(font)
        self.G2DDCopy.setObjectName("G2DDCopy")

        for i in range(64):
            setattr(self, "G2lineEdit%d" % (i + 1), QtWidgets.QLineEdit(self.ddRegGroupBox2))
            m = getattr(self, "G2lineEdit%d" % (i + 1))
            if i // 8 == 1 or i // 8 == 3 or i // 8 == 5 or i // 8 == 7:
                m.setGeometry(QtCore.QRect(20 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            else:
                m.setGeometry(QtCore.QRect(0 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            font = QtGui.QFont()
            font.setPointSize(11)
            m.setFont(font)
            m.setStyleSheet("")
            m.setAlignment(QtCore.Qt.AlignCenter)
            m.setObjectName("G2lineEdit%d" % (i + 1))

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
        self.G3DDClear = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDClear.setGeometry(QtCore.QRect(500, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDClear.setFont(font)
        self.G3DDClear.setObjectName("G3DDClear")
        self.G3DDCopy = QtWidgets.QPushButton(self.ddRegGroupBox3)
        self.G3DDCopy.setGeometry(QtCore.QRect(420, 15, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.G3DDCopy.setFont(font)
        self.G3DDCopy.setObjectName("G3DDCopy")

        for i in range(64):
            setattr(self, "G3lineEdit%d" % (i + 1), QtWidgets.QLineEdit(self.ddRegGroupBox3))
            m = getattr(self, "G3lineEdit%d" % (i + 1))
            if i // 8 == 1 or i // 8 == 3 or i // 8 == 5 or i // 8 == 7:
                m.setGeometry(QtCore.QRect(20 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            else:
                m.setGeometry(QtCore.QRect(0 + 35 * (i % 16), 40 + 22 * (i // 16), 30, 20))
            font = QtGui.QFont()
            font.setPointSize(11)
            m.setFont(font)
            m.setStyleSheet("")
            m.setAlignment(QtCore.Qt.AlignCenter)
            m.setObjectName("G3lineEdit%d" % (i + 1))

        self.TabMainWindow.addTab(self.tabDDRegister, "")
        self.tabDDLog = QtWidgets.QWidget()
        self.tabDDLog.setObjectName("tabDDLog")
        self.DDreadRegValShowText = QtWidgets.QTextBrowser(self.tabDDLog)
        self.DDreadRegValShowText.setGeometry(QtCore.QRect(0, 1, 585, 430))
        self.DDreadRegValShowText.setMinimumSize(QtCore.QSize(0, 0))
        self.DDreadRegValShowText.setMaximumSize(QtCore.QSize(675, 700))
        self.DDreadRegValShowText.setObjectName("DDreadRegValShowText")
        self.TabMainWindow.addTab(self.tabDDLog, "")
        self.horizontalLayout.addWidget(self.TabMainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabMainWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB Monitor 2.0.4"))
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
        self.groupBox.setTitle(_translate("MainWindow", "Project"))
        self.conmment.setText(_translate("MainWindow", "New project:"))
        self.pathSavePushButton.setText(_translate("MainWindow", "Save as a project"))
        self.conmment_2.setText(_translate("MainWindow", "Select project:"))
        self.settingRemove.setText(_translate("MainWindow", "Remove"))
        self.settingRemoveLabel.setText(_translate("MainWindow", "Del project"))
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
        self.hideShowVirtual.setText(_translate("MainWindow", "ShowVKey"))
        self.shutDown.setText(_translate("MainWindow", "ShutDown"))
        self.screenRecord.setText(_translate("MainWindow", "ScreenRecord"))
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
        self.showRawdataUI.setText(_translate("MainWindow", "Show Rawdata UI"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tabOptions), _translate("MainWindow", "ADB cmd"))
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

    # TODO: add functions for all widgets
    def bindEventFunc(self):
        self.hintMessages()

        # settings
        self.pathV1RadioButton.clicked.connect(self.chooseDriverVersion)
        self.pathV2RadioButton.clicked.connect(self.chooseDriverVersion)
        self.pathSavePushButton.clicked.connect(self.saveSettingsToProject)
        self.settingsProComboBox.currentIndexChanged.connect(self.selectProjectItemEvent)
        self.settingRemove.clicked.connect(lambda :self.dialogSelectFilesWin('./project/', 'Remove', True))

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
        self.screenRecord.clicked.connect(self.screenRecordFunc)
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
        self.openBlight.clicked.connect(self.backlight)

        # options
        self.diagArr.clicked.connect(self.touchDiagArrFunc)
        self.updateFW.clicked.connect(self.touchUpdateFWFunc)

        # rawdata show
        self.showRawdataUI.clicked.connect(self.showRawdataUIFunc)

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

    # TODO: hint some key messages
    def hintMessages(self):
        self.wifiConnect.setToolTip("You should connect <b style='color:red'>USB</b> and <b>WIFI</b>,\nthen click this")
        self.showRawdataUI.setToolTip("<h3 style='color:black'>It will check <b style='color:red'>rx and tx num</b>,\nand then show rawdata UI</h3>")
        self.settingRemove.setToolTip("<b style='color:blue'>Delete project what you selected</b>")
        self.opencmd.setToolTip('<b>Open windows cmd.exe</b>')
        self.screenShot.setToolTip("The picture will be saved\nin this monitor.exe's path")
        self.G1AddrlineEdit.setToolTip("<b style='color:blue'>B90009:</b><br/>B9:ddregister<br/>00:bank<br/>0A:length")

    # TODO: settings page functions
    def selectProjectItemEvent(self):
        name = self.settingsProComboBox.currentText()
        if self.readProjectInfo(name):
            self.fillTouchConfig()
            self.initEchoMethod(self.driverVersionMode)

    # TODO: fill touch config in settings page
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
            self.pathDiagLineEdit.setDisabled(False)
            self.pathRegLineEdit.setText(self.v1RegisterPath)
            self.pathRegLineEdit.setDisabled(False)
            self.pathIntenLineEdit.setText(self.v1IntEnPath)
            self.pathIntenLineEdit.setDisabled(False)
            self.pathResetLineEdit.setText(self.v1ResetPath)
            self.pathResetLineEdit.setDisabled(False)
            self.pathSenseonoffLineEdit.setText(self.v1SenseOnOffPath)
            self.pathSenseonoffLineEdit.setDisabled(False)
            self.pathDiagarrLineEdit.setText(self.v1DiagArrPath)
            self.pathDiagarrLineEdit.setDisabled(False)
            self.pathStackLineEdit.clear()
            self.pathStackLineEdit.setDisabled(True)
        elif self.driverVersionMode == 2:
            self.pathV1RadioButton.setChecked(False)
            self.pathV2RadioButton.setChecked(True)

            self.pathStackLineEdit.setText(self.v2ReadStackPath)
            self.pathStackLineEdit.setDisabled(False)
            self.pathDiagLineEdit.clear()
            self.pathDiagLineEdit.setDisabled(True)
            self.pathRegLineEdit.clear()
            self.pathRegLineEdit.setDisabled(True)
            self.pathIntenLineEdit.clear()
            self.pathIntenLineEdit.setDisabled(True)
            self.pathResetLineEdit.clear()
            self.pathResetLineEdit.setDisabled(True)
            self.pathSenseonoffLineEdit.clear()
            self.pathSenseonoffLineEdit.setDisabled(True)
            self.pathDiagarrLineEdit.clear()
            self.pathDiagarrLineEdit.setDisabled(True)

    # TODO: read project file and reconfig touch info
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

    # TODO: init all input widgets rule
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

    # TODO: when new project was created or one project removed, it will be called
    def initSelectProjectItems(self, init):
        if not init:
            self.settingsProComboBox.blockSignals(True)
            self.settingsProComboBox.clear()

        _translate = QtCore.QCoreApplication.translate
        projectList = self.findProjectFilesName('./project/')
        if not projectList:
            return

        for i in range(len(projectList)):
            self.settingsProComboBox.addItem("")

        i = len(projectList) - 1
        while i >= 0:
            self.settingsProComboBox.setItemText(len(projectList) - 1 - i, _translate("MainWindow", projectList[i]))
            i = i - 1

        if not init:
            self.settingsProComboBox.blockSignals(False)

    # TODO: load latest project one time while start this app
    def loadLatestTouchInfoConfig(self):
        path = self.findProjectDocFilesPath()
        if not path:
            return

        self.v2ReadStackPath = ''

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

    # TODO: init common commands to distinguish v1 or v2 driver mode
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
        name = self.dialogInputgWin("Please enter project name", False)
        if name == '':
            return

        if not os.path.exists("./project"):
            os.mkdir("project")

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
        self.selectProjectItemEvent()

    def findProjectFilesName(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

        fileNames = os.listdir(path)

        if len(fileNames) == 0:
            self.dialogWin("No find project files!")
            return None

        return fileNames

    def findProjectDocFilesPath(self):
        path = "./project/"
        fullfilename = ''
        fileNames = self.findProjectFilesName(path)
        if not fileNames:
            return None

        for name in fileNames:
            fullfilename = os.path.join(path, name)

        return fullfilename

    def outputVRTablefile(self, one, two):
        avg = 0
        ret = ''

        tmp1 = self.readAVGRawdata(one)
        tmp2 = self.readAVGRawdata(two)

        if len(tmp1) != len(tmp2):
            self.dialogWin("data was not match,\nplease choose two same project file")
            return

        for i in range(len(tmp2)):
            tmp2[i] = tmp2[i] - tmp1[i]

        for i in range(len(tmp2)):
            tmp1[i] = tmp2[i]/tmp1[i]
            avg += tmp1[i]

        avg =avg/len(tmp1)

        for i in range(len(tmp1)):
            tmp1[i] = 128 * tmp1[i] / avg
            tmp1[i] = round(tmp1[i])
            if (i + 1) % window.ui.transTX == 0:
                ret += str(tmp1[i]) + ',' + '\n'
            else:
                ret += str(tmp1[i]) + ','

        ret = time.strftime("Time:%Y-%m-%d %H:%M:%S\n", time.localtime()) + ret
        pyperclip.copy(ret)
        pyperclip.paste()
        self.dialogWin("output data was already copied,\nnow you can paste")

    # def writeDataToNewFile(self, path, name):
    def readAVGRawdata(self, name):
        if not os.path.exists(name):
            return

        file = open(name, 'r')
        ret = file.read()

        index = ret.find('VALUE')
        ret = ret[index + 7:-1]
        ret = ret.split()

        for i in range(len(ret)):
            ret[i] = int(ret[i])

        return ret

    def selectAllProject(self, path):
        files = self.findProjectFilesName(path)
        fileNum = len(files)
        if self.checkbox0.isChecked():
            for i in range(fileNum):
                m = getattr(self, "checkbox%d" % (i + 1))
                m.setChecked(True)
        else:
            for i in range(fileNum):
                m = getattr(self, "checkbox%d" % (i + 1))
                m.setChecked(False)

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

    # TODO: dialog window functions
    def dialogWin(self, string):
        self.dialog = QDialog()
        self.dialog.resize(300, 115)
        self.dialog.setMaximumSize(QtCore.QSize(300, 115))
        self.labelTmp = QtWidgets.QLabel(self.dialog)
        self.labelTmp.setGeometry(QtCore.QRect(5, 11, 295, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelTmp.setFont(font)
        self.labelTmp.setObjectName("labelTmp")
        self.labelTmp.setText(string)
        self.labelTmp.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(self.dialog)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.dialog.exec_()

    def dialogInputgWin(self, title, numFlag):
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
        font.setPointSize(16)
        self.inputName.setFont(font)
        self.inputName.setAlignment(QtCore.Qt.AlignCenter)

        if numFlag:
            reg = QRegExp('[0-9]{0,3}')
            self.inputName.setPlaceholderText("Time < 180")
        else:
            reg = QRegExp('[a-zA-Z0-9_]*')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.inputName.setValidator(pValidator)

        self.retranslateUi(self.dialog)
        self.buttonBoxTmp.accepted.connect(self.dialog.accept)
        self.buttonBoxTmp.rejected.connect(self.dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", title))
        if self.dialog.exec_() == QDialog.Accepted:
            # check file name is right or not
            if self.inputName.text() == '':
                return ''
            else:
                return self.inputName.text()
        else:
            return ''

    def dialogSelectFilesWin(self, path, title, remove):
        files = self.findProjectFilesName(path)
        if not files:
            return
        fileNum = len(files)

        self.dialog = QDialog()
        self.dialog.resize(180, 60 + 20 * fileNum)
        self.girdLayout = QtWidgets.QGridLayout()
        self.girdLayout.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        if remove:
            self.checkbox0 = QtWidgets.QCheckBox()
            self.selectAllFiles = QtWidgets.QLabel()
            self.selectAllFiles.setText("All")
            self.girdLayout.addWidget(self.checkbox0, 0, 0)
            self.girdLayout.addWidget(self.selectAllFiles, 0, 1)

        for i in range(fileNum):
            setattr(self, "checkbox%d" % (i + 1), QtWidgets.QCheckBox())
            setattr(self, "filename%d" % (i + 1), QtWidgets.QLabel())
            m = getattr(self, "checkbox%d" % (i + 1))
            n = getattr(self, "filename%d" % (i + 1))
            n.setText(files[i])
            self.girdLayout.addWidget(m, (i + 1), 0)
            self.girdLayout.addWidget(n, (i + 1), 1)

        self.dialog.setLayout(self.girdLayout)

        self.buttonBoxTmp1 = QtWidgets.QDialogButtonBox(self.dialog)
        self.buttonBoxTmp1.setGeometry(QtCore.QRect(0, 30 + 20 * fileNum, 150, 30))
        self.buttonBoxTmp1.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxTmp1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxTmp1.setObjectName("buttonBoxTmp1")

        self.retranslateUi(self.dialog)
        self.buttonBoxTmp1.accepted.connect(self.dialog.accept)
        self.buttonBoxTmp1.rejected.connect(self.dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        # bind event
        if remove:
            self.checkbox0.clicked.connect(lambda :self.selectAllProject(path))

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", title))

        if self.dialog.exec_() == QDialog.Accepted:
            if remove:
                for i in range(fileNum):
                    m = getattr(self, "checkbox%d" % (i + 1))
                    n = getattr(self, "filename%d" % (i + 1))
                    if m.isChecked():
                        os.remove(path + n.text())

                self.initSelectProjectItems(False)
            else:
                # TODO: read selected files to calculate vr table
                selectedFiles = []
                one = ''
                two = ''
                for i in range(fileNum):
                    m = getattr(self, "checkbox%d" % (i + 1))
                    n = getattr(self, "filename%d" % (i + 1))
                    if m.isChecked():
                        selectedFiles.append('./log/' + n.text())

                if len(selectedFiles) != 2:
                    self.dialogWin("You can only selected two files")
                    return
                else:
                    if selectedFiles[0].find('min') != -1:
                        one = selectedFiles[0]
                    elif selectedFiles[0].find('max') != -1:
                        two = selectedFiles[0]

                    if selectedFiles[1].find('min') != -1:
                        one = selectedFiles[1]
                    elif selectedFiles[1].find('max') != -1:
                        two = selectedFiles[1]

                    if one == '' or two == '':
                        self.dialogWin("files were not match")
                        return

                    self.outputVRTablefile(one, two)

    # TODO: DD Reg page functions
    def reverseBackgroundColor(self, before, now, n):
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
            self.reverseBackgroundColor(self.beforeRead, ret, n)
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
            adbtool.shell(cmd, "SHELL")
            cmd = self.echoWriteRegister % ('900000FC', 'CC' + addr)
            self.DDreadRegValShowText.append(cmd)
            adbtool.shell(cmd, "SHELL")
            cmd = self.echoReadRegister % (localAddr + '80')
            self.DDreadRegValShowText.append(cmd)
            adbtool.shell(cmd, "SHELL")
            cmd = self.catRegister
            self.DDreadRegValShowText.append(cmd)
            ret = adbtool.shell(cmd, "SHELL")
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
        adbtool.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)

        cmd = self.echoReadRegister % "10007F80"
        adbtool.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)

        cmd = self.catRegister
        ret = adbtool.shell(cmd, "SHELL")
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

    # TODO: TP Reg page functions
    def initHistoryFunc(self):
        # self.openBlight.setDisabled(True)

        self.ret = ''
        self.beforeRead = ''
        self.historyFile = './settings/register_history'
        self.device_ip = ""
        self.device_ip_port = ""
        self.port = ""

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
            adbtool.shell(cmd, "SHELL")
            readRegInfo = adbtool.shell(self.catRegister, "SHELL")

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

    def writeRegister(self, regAddress, writeValue):
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


        # Deal with value for set as 8
        while len(writeValue) < 8 and len(writeValue) != 0:
            writeValue = "0" + writeValue

        if len(regAddress) == 8 and len(writeValue) != 0:
            cmd = self.echoWriteRegister % (regAddress, writeValue)
            self.readRegValShowText.append(cmd)
            adbtool.shell(cmd, "SHELL")

    # TODO: trans rawdata pattern
    def transRawdataPattern(self):
        # check rx and tx num is or not match
        self.commonFlag = True
        adbtool.shell(window.ui.echoDiag % '1', "SHELL")
        ret = adbtool.shell(window.ui.catDiag, "SHELL")
        # print(ret)
        # check device connect status
        if ret == '' or ret.find('error') != -1 or ret.find('ChannelStart') == -1:
            window.ui.dialogWin("Not found devices")
            return False

        # check the rawdata pattern is common or custom
        if ret.find('[00]') == -1:
            self.commonFlag = False
        else:
            self.commonFlag = True

        # check rx tx
        rx = ret[ret.find('ChannelStart'):ret.find('\n')].split(':')[1].split(',')[0]
        tx = ret[ret.find('ChannelStart'):ret.find('\n')].split(':')[1].split(',')[1]
        if int(rx) != window.ui.rxnum:
            window.ui.dialogWin("Project rx/tx num wrong")
            return False

        rawdata = ret[ret.find('\n')+2:ret.find('ChannelEnd')]
        rawdata = rawdata[:rawdata.find('\n')].split()

        if self.commonFlag:
            self.transTX = len(rawdata) + 1
            if (self.transTX - 2) == window.ui.txnum:
                self.transRX = window.ui.rxnum + 2
            else:
                self.transRX = window.ui.txnum + 2
        else:
            self.transTX = len(rawdata)
            if (self.transTX - 1) == window.ui.txnum:
                self.transRX = window.ui.rxnum + 1
            else:
                self.transRX = window.ui.txnum + 1

        return True

    # TODO: show rawdata UI function
    def showRawdataUIFunc(self):
        if not self.transRawdataPattern():
            return

        child.ui.mainwindow.resize(self.transTX * window.rawdataWidth,
                                   self.transRX * window.rawdataHeight + 45)
        child.ui.MainRawdataShowtableWidget.setGeometry(QtCore.QRect(0, 40, window.rawdataWidth * self.transTX,
                                                                     window.rawdataHeight * self.transRX))
        child.ui.initRawdataUI(self.transRX, self.transTX)
        child.show()
        self.disableFunctions(True)

    # TODO: disable some functions when show rawdata UI
    def disableFunctions(self, disable):
        self.tabSettings.setDisabled(disable)

    # TODO: options page, touch functions
    def touchDiagArrFunc(self):
        name = self.diagArrText.text()
        if name == '':
            self.rawdataShowText.append("please set value!")
            return

        if self.driverVersionMode == 1:
            cmd = "echo %s > " % name + self.v1DiagArrPath
        else:
            cmd = "echo diag_arr,%s > " % name + self.debugPath
        adbtool.shell(cmd, "SHELL")

        self.rawdataShowText.append(cmd)

    def touchSenseOnFunc(self):
        if self.senseon.text() == 'SenseOn':
            self.senseon.setText('SenseOff')
            adbtool.shell(self.echoSenseOff, "SHELL")
            self.rawdataShowText.append(self.echoSenseOff)
        else:
            self.senseon.setText('SenseOn')
            adbtool.shell(self.echoSenseOn, "SHELL")
            self.rawdataShowText.append(self.echoSenseOn)

    def touchSelfTestFunc(self):
        self.selftestThread = Thread(target=self.selftestThreadFunc)
        self.selftestThread.start()

    def selftestThreadFunc(self):
        ret = adbtool.shell(self.catSelfTest, "SHELL")
        self.rawdataShowText.append(ret)
        self.rawdataShowText.update()

    def touchFWVersionFunc(self):
        adbtool.shell(self.echoFWVersion % "v", "SHELL")
        ret = adbtool.shell(self.catFWVersion, "SHELL")
        self.rawdataShowText.append(ret)

    def touchResetFunc(self):
        adbtool.shell(self.echoReset % "1", "SHELL")
        self.rawdataShowText.append(self.echoReset % "1")

    def touchIntenFunc(self):
        if self.inten0.text() == 'Int_en':
            self.inten0.setText('Int_dis')
            adbtool.shell(self.echoIntEn % "0", "SHELL")
            self.rawdataShowText.append("disable irq")
        else:
            self.inten0.setText('Int_en')
            adbtool.shell(self.echoIntEn % "1", "SHELL")
            self.rawdataShowText.append("enable irq")

    def touchFlashDumpFunc(self):
        self.rawdataShowText.append("will be add flash dump func\n")

    def touchUpdateFWFunc(self):
        fw_path = self.updateFWText.toPlainText()
        if fw_path == "":
            self.rawdataShowText.append("please choose fw file!")
            return
        ret = adbtool.shell("adb push '%s' " % fw_path + self.fwPath)
        self.rawdataShowText.append(ret)
        ret = adbtool.shell("echo t Himax_firmware.bin > " + self.debugPath, "SHELL")
        self.rawdataShowText.append(ret)

    def touchDebugTypeFunc(self):
        adbtool.shell("echo %s > " % self.debugComboBox.currentText() + self.debugPath, 'SHELL')
        ret = adbtool.shell("cat " + self.debugPath, 'SHELL')
        self.rawdataShowText.append(ret)

    # TODO: options page, display functions
    def display1129Func(self):
        if self.driverVersionMode == 1:
            cmd1 = "echo w:x30011000 > " + self.v1RegisterPath
            cmd2 = "echo w:x30029000 > " + self.v1RegisterPath
        else:
            cmd1 = "echo register,w:x30011000 > " + self.debugPath
            cmd2 = "echo register,w:x30029000 > " + self.debugPath

        adbtool.shell(cmd1, "SHELL")
        adbtool.shell("sleep 1", "SHELL")
        adbtool.shell(cmd2, "SHELL")
        self.rawdataShowText.append(cmd1)
        self.rawdataShowText.append(cmd2)

    def display2810Func(self):
        if self.driverVersionMode == 1:
            cmd1 = "echo w:x30028000 > " + self.v1RegisterPath
            cmd2 = "echo w:x30010000 > " + self.v1RegisterPath
        else:
            cmd1 = "echo register,w:x30028000 > " + self.debugPath
            cmd2 = "echo register,w:x30010000 > " + self.debugPath

        adbtool.shell(cmd1, "SHELL")
        adbtool.shell("sleep 1", "SHELL")
        adbtool.shell(cmd2, "SHELL")
        self.rawdataShowText.append(cmd1)
        self.rawdataShowText.append(cmd2)

    # TODO: options page, WIFI functions
    def wifiConnectFunc(self):
        self.threadWifiConnect = Thread(target=self.waitConnectFunc)
        self.threadWifiConnect.start()

    def waitConnectFunc(self):
        self.PORT_NUM = '8888'
        self.wifi_connect_status = 1

        # set btn disabled
        self.wifiStatus.setText("Connect..")
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0)")
        self.wifiConnect.setDisabled(True)
        # self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")

        # check two devices
        devices = (adbtool.shell("adb devices"))
        self.rawdataShowText.append(devices)
        device_list = devices.split()
        if devices.find("192.168") > 0 and device_list.count("device") > 1:
            self.rawdataShowText.append("Disconnect wifi adb")
            adbtool.shell("adb disconnect")

        devices = (adbtool.shell("adb devices"))
        self.rawdataShowText.append(devices)

        self.rawdataShowText.append("Start...")
        device_info = (adbtool.shell("adb devices"))
        self.rawdataShowText.append(device_info)

        try:
            device_list = device_info.split()
            device_list.remove("List")
            device_list.remove("of")
            device_list.remove("devices")
            device_list.remove("attached")
            device_list.remove("device")
        except:
            self.rawdataShowText.append("Please connect device")
            return False

        device_name = device_list[0]
        self.rawdataShowText.append(device_name)

        # Get device ip & set port
        cmd = "adb -s %s shell ip -f inet addr show wlan0" % (device_name)
        self.rawdataShowText.append(cmd)

        ip = adbtool.shell(cmd)
        self.rawdataShowText.append(ip)
        ip = ip[ip.find("inet 1") + 5:ip.find("/")]
        self.rawdataShowText.append(ip)
        cmd = "adb -s %s tcpip %s" % (device_name, self.PORT_NUM)
        self.rawdataShowText.append(cmd)
        ret = adbtool.shell(cmd)
        self.rawdataShowText.append(ret)

        if self.wifi_connect_status == 0:
            return

        # Connect
        self.device_ip = ip
        self.device_ip_port = str(ip) + ":" + self.PORT_NUM
        cmd = "adb connect %s:%s" % (self.device_ip, self.PORT_NUM)
        self.rawdataShowText.append(cmd)

        response = ""
        while response.find("already") < 0 and self.wifi_connect_status != 0:
            response = (adbtool.shell(cmd))
            self.rawdataShowText.append(response)
        if self.wifi_connect_status == 0:
            return

        # Polling wait unplugin
        devices = (adbtool.shell("adb devices"))
        self.rawdataShowText.append(devices)

        response = ""

        self.rawdataShowText.append("Unplugin")

        while devices.find(device_name) < 0 and self.wifi_connect_status != 0:
            devices = (adbtool.shell("adb devices"))
            self.rawdataShowText.append(devices)

        if self.wifi_connect_status == 0:
            return

        # Connect
        cmd = "adb connect %s:%s" % (self.device_ip, self.PORT_NUM)
        self.rawdataShowText.append(cmd)

        while response.find("already") < 0 and self.wifi_connect_status != 0:
            response = (adbtool.shell(cmd))
            self.rawdataShowText.append(response)
        if self.wifi_connect_status == 0:
            return

        self.rawdataShowText.append("Wifi Connect Done")
        self.wifiStatus.setText("Connected")
        self.wifiStatus.setStyleSheet("color:rgb(0, 255, 0)")

    def wifiReconnectFunc(self):
        cmd = "adb connect %s:%s" % (self.device_ip, self.port)
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

    def wifiDisconnectFunc(self):
        self.wifiStatus.setText("Disconnect")
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0)")
        self.wifiConnect.setDisabled(False)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
        self.wifiConnectFlag = 0
        self.wifi_connect_status = 0
        self.device_ip = ""
        self.device_ip_port = ""
        adbtool.shell("adb disconnect")
        self.rawdataShowText.append("adb disconnect")

    # TODO: options page, ADB functions
    def rootFunc(self):
        ret = adbtool.shell("adb devices")
        self.rawdataShowText.append(ret)
        # need check adb connect status
        ret = adbtool.shell("adb root")
        self.rawdataShowText.append(ret)
        if ret == '' or 'error' in ret:
            self.adbStatus.setText('Failed')
            self.adbStatus.setStyleSheet("color: rgb(255, 0, 0);")
            return
        else:
            self.adbStatus.setText('OK')
            self.adbStatus.setStyleSheet("color: rgb(0, 255, 0);")
            self.showRawdataUI.setDisabled(False)

        ret = adbtool.shell("adb remount")
        self.rawdataShowText.append(ret)
        adbtool.shell("adb shell setenforce 0")
        self.rawdataShowText.append('setenforce 0')

    def homeKeyFunc(self):
        cmd = "adb shell input keyevent KEYCODE_HOME"
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

    def backKeyFunc(self):
        cmd = "adb shell input keyevent KEYCODE_BACK"
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

    def volUpFunc(self):
        cmd = "adb shell input keyevent KEYCODE_VOLUME_UP"
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

    def volDownFunc(self):
        cmd = "adb shell input keyevent KEYCODE_VOLUME_DOWN"
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

    def hideShowVirtualFunc(self):
        if self.hideShowVirtual.text() == 'ShowVKey':
            self.hideShowVirtual.setText("HideVKey")
            cmd = "adb shell settings put global policy_control immersive.full=*"
            adbtool.shell(cmd)
            self.rawdataShowText.append(cmd)
        else:
            self.hideShowVirtual.setText("ShowVKey")
            cmd = "adb shell settings put global policy_control null"
            adbtool.shell(cmd)
            self.rawdataShowText.append(cmd)

    def powerKeyFunc(self):
        adbtool.shell(None, "KEYEVENT", 26)
        adbtool.shell(None, "KEYEVENT", 82)

    def openClosePointFunc(self):
        if self.openClosePoint.text() == 'OpenPoint':
            self.openClosePoint.setText("ClosePoint")
            cmd = "settings put system pointer_location 0"
            adbtool.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
            cmd = "settings put system show_touches 0"
            adbtool.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
        else:
            self.openClosePoint.setText("OpenPoint")
            cmd = "settings put system pointer_location 1"
            adbtool.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)
            cmd = "settings put system show_touches 1"
            adbtool.shell(cmd, "SHELL")
            self.rawdataShowText.append(cmd)

    def screenShotFunc(self):
        path = 'screen\\'
        if not os.path.exists(path):
            os.mkdir(path)

        name = time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) + ".png"
        cmd = "adb wait-for-device shell screencap /sdcard/%s" % name
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)
        cmd = "adb pull /sdcard/%s " % name + path[:-1]
        adbtool.shell(cmd)
        self.rawdataShowText.append(cmd)

        if os.path.exists(path + name):
            os.startfile(path + name)

    def screenRecordFunc(self):
        if self.screenRecord.text() == 'ScreenRecord':
            recordTime = self.dialogInputgWin("Please enter time", True)
            if recordTime == '' or int(recordTime) > 180:
                self.dialogWin("time was not right")
                return

            path = 'screen\\'
            if not os.path.exists(path):
                os.mkdir(path)

            self.screenRecord.setDisabled(True)
            self.screenRecordName = time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) + ".mp4"
            a = Thread(target=self.screenRecordThread, args=(self.screenRecordName, recordTime))
            a.start()
            b = Thread(target=self.screenRecordSetTime, args=(self.screenRecordName, recordTime, path))
            b.start()

    def screenRecordSetTime(self, name, recordTime, path):
        if not os.path.exists(path):
            os.mkdir(path)

        i = 0
        while i < int(recordTime):
            self.screenRecord.setText(recordTime + ':%d' % i)
            time.sleep(1)
            self.screenRecord.update()
            i += 1
            if i == int(recordTime):
                time.sleep(1)
                self.screenRecord.setText('ScreenRecord')
                self.screenRecord.setDisabled(False)
                adbtool.shell("adb pull /sdcard/%s " % name + path[:-1])

                if os.path.exists(path + name):
                    os.startfile(path + name)

                break

    def screenRecordThread(self, name, recordTime):
        cmd = "adb wait-for-device shell screenrecord --time-limit " + recordTime + " /sdcard/%s" % name
        self.rawdataShowText.append(cmd)
        adbtool.shell(cmd)

    def shutDownFunc(self):
        adbtool.shell("adb shell reboot -p")
        self.rawdataShowText.append("adb shell reboot -p")

    def rebootFunc(self):
        adbtool.shell("adb reboot")

    def openCMDFunc(self):
        cmd = "C:\Windows\System32\cmd.exe"
        os.startfile(cmd)

    def backlight(self):
        if self.openBlight.text() == 'OpenBlight':
            self.openBlight.setText('CloseBlight')
            self.rawdataShowText.append(self.echoWriteRegister % ('30053000', '00002000'))
            adbtool.shell(self.echoWriteRegister % ('30053000', '00002000'), "SHELL")
        else:
            self.openBlight.setText('OpenBlight')
            self.rawdataShowText.append(self.echoWriteRegister % ('30051000', '00ff0f00'))
            adbtool.shell(self.echoWriteRegister % ('30051000', '00ff0f00'), "SHELL")
            self.rawdataShowText.append(self.echoWriteRegister % ('30053000', '00002400'))
            adbtool.shell(self.echoWriteRegister % ('30053000', '00002400'), "SHELL")


class ChildWindow(QMainWindow):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.ui = Ui_ChildWindow()
        self.ui.setupUi(self)
        self.ui.bindEventFunc()
        self.ui.setRegExp()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()

        if key == QtCore.Qt.Key_C:
            ret = ''
            for i in range(window.ui.transRX):
                for j in range(window.ui.transTX):
                    try:
                        ret += '\t' + self.ui.MainRawdataShowtableWidget.item(i, j).text() + ','
                    except:
                        window.ui.dialogWin("unexcept wrong")
                        return
                ret += '\n'
            pyperclip.copy(ret)
            pyperclip.paste()
            window.ui.dialogWin("Copy ok")

        if key == QtCore.Qt.Key_S:
            ret = self.ui.origRawdata
            pyperclip.copy(ret)
            pyperclip.paste()
            window.ui.dialogWin("Copy orig ok")

        if key == QtCore.Qt.Key_M:
            self.ui.keepMax = True
            self.ui.keepMin = False
            window.ui.dialogWin("Keep max")

        if key == QtCore.Qt.Key_N:
            self.ui.keepMax = False
            self.ui.keepMin = True
            window.ui.dialogWin("Keep min")

        if key == QtCore.Qt.Key_B:
            self.ui.keepMax = False
            self.ui.keepMin = False
            self.ui.keepFlag = False

    def closeEvent(self, *args, **kwargs):
        window.ui.disableFunctions(False)
        child.ui.rawdataReadFunc(True)


class Ui_ChildWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainRawdataShowtableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.MainRawdataShowtableWidget.setFont(font)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.setColumnCount(0)
        self.MainRawdataShowtableWidget.setRowCount(0)
        self.MainRawdataShowtableWidget.verticalHeader().setVisible(False)
        self.rawdataRead = QtWidgets.QPushButton(self.centralwidget)
        self.rawdataRead.setGeometry(QtCore.QRect(0, 0, 40, 40))
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
        self.radioDC = QtWidgets.QRadioButton(self.centralwidget)
        self.radioDC.setGeometry(QtCore.QRect(50, 5, 50, 30))
        self.radioDC.setMaximumSize(QtCore.QSize(50, 30))
        self.radioDC.setObjectName("radioDC")
        self.radioIIR = QtWidgets.QRadioButton(self.centralwidget)
        self.radioIIR.setGeometry(QtCore.QRect(100, 5, 50, 30))
        self.radioIIR.setMaximumSize(QtCore.QSize(50, 30))
        self.radioIIR.setObjectName("radioIIR")
        self.radioTmp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioTmp.setGeometry(QtCore.QRect(150, 5, 15, 30))
        self.radioTmp.setMaximumSize(QtCore.QSize(15, 30))
        self.radioTmp.setText("")
        self.radioTmp.setObjectName("radioTmp")
        self.textEditDiag = QtWidgets.QLineEdit(self.centralwidget)
        self.textEditDiag.setGeometry(QtCore.QRect(170, 5, 40, 30))
        self.textEditDiag.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEditDiag.setFont(font)
        self.textEditDiag.setObjectName("textEditDiag")
        self.log = QtWidgets.QPushButton(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(220, 5, 40, 30))
        self.log.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.logTimesBtn = QtWidgets.QLineEdit(self.centralwidget)
        self.logTimesBtn.setGeometry(QtCore.QRect(260, 5, 50, 30))
        self.logTimesBtn.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.logTimesBtn.setFont(font)
        self.logTimesBtn.setObjectName("logTimesBtn")
        self.logTimesBtn.setPlaceholderText("mseconds")
        self.calcAverage = QtWidgets.QPushButton(self.centralwidget)
        self.calcAverage.setEnabled(True)
        self.calcAverage.setGeometry(QtCore.QRect(320, 5, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcAverage.sizePolicy().hasHeightForWidth())
        self.calcAverage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calcAverage.setFont(font)
        self.calcAverage.setObjectName("calcAverage")
        self.frameTimes = QtWidgets.QLineEdit(self.centralwidget)
        self.frameTimes.setGeometry(QtCore.QRect(400, 5, 50, 30))
        self.frameTimes.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frameTimes.setFont(font)
        self.frameTimes.setObjectName("frameTimes")
        self.vrTable = QtWidgets.QPushButton(self.centralwidget)
        self.vrTable.setEnabled(True)
        self.vrTable.setGeometry(QtCore.QRect(470, 5, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vrTable.sizePolicy().hasHeightForWidth())
        self.vrTable.setSizePolicy(sizePolicy)
        self.vrTable.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vrTable.setFont(font)
        self.vrTable.setObjectName("vrTable")
        self.removeVRTable = QtWidgets.QPushButton(self.centralwidget)
        self.removeVRTable.setEnabled(True)
        self.removeVRTable.setGeometry(QtCore.QRect(560, 5, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeVRTable.sizePolicy().hasHeightForWidth())
        self.removeVRTable.setSizePolicy(sizePolicy)
        self.removeVRTable.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeVRTable.setFont(font)
        self.removeVRTable.setObjectName("removeVRTable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mainwindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Rawdata UI"))
        self.radioDC.setText(_translate("MainWindow", "DC"))
        self.radioIIR.setText(_translate("MainWindow", "IIR"))
        self.textEditDiag.setPlaceholderText(_translate("MainWindow", "Type"))
        self.log.setText(_translate("MainWindow", "Log"))
        self.calcAverage.setText(_translate("MainWindow", "VRCollect"))
        self.frameTimes.setPlaceholderText(_translate("MainWindow", "Frames"))
        self.vrTable.setText(_translate("MainWindow", "VRTable"))
        self.removeVRTable.setText(_translate("MainWindow", "Remove"))

    def bindEventFunc(self):
        # self.logFlag = False
        # self.logFlag_s = False
        self.logTimes = 0
        self.origRawdata = ''
        self.showRawdataFlag = 0

        self.keepMax = False
        self.keepMin = False

        self.hintMsg()

        self.rawdataRead.clicked.connect(self.rawdataReadFunc)
        self.log.clicked.connect(self.logFunc)
        self.radioDC.clicked.connect(self.chooseRawdataType)
        self.radioIIR.clicked.connect(self.chooseRawdataType)
        self.radioTmp.clicked.connect(self.chooseRawdataType)
        self.calcAverage.clicked.connect(self.calcAverageFunc)
        self.vrTable.clicked.connect(self.calcVRTable)
        self.removeVRTable.clicked.connect(self.removeVRTableFunc)

    def removeVRTableFunc(self):
        window.ui.dialogSelectFilesWin('./log/', 'Remove', True)

    def calcVRTable(self):
        window.ui.dialogSelectFilesWin('./log', 'Get VR Table', False)

    def hintMsg(self):
        self.textEditDiag.setToolTip("Sram:11 or 12\nStack:1 or 2")
        self.calcAverage.setToolTip("Collect N frames rawdata and calculate average")
        self.frameTimes.setToolTip("<h3 style='color:red'>Frames less 200</h3>")
        self.vrTable.setToolTip("You need select <b>min(0Ω)</b> and <b>max(10kΩ)</b> files,then calculate and output VR table")

    def calcAverageFunc(self):
        times = self.frameTimes.text()
        if times == '' or int(times) > 200:
            window.ui.dialogWin("Frame num was not right")
            return

        path = 'log\\'
        if not os.path.exists(path):
            os.mkdir(path)

        value = window.ui.dialogInputgWin("Enter name include 'max/min'", False)
        if value == '' or (value.find('max') == -1 and value.find('min') == -1):
            window.ui.dialogWin("You need set name\ninclude 'max' or 'min'")
            return

        self.calcAverage.setDisabled(True)
        self.calcAverage.setText("Ing.")
        self.calcAverage.setStyleSheet("color:rgb(255, 0, 0)")
        self.calcAverageThread = Thread(target=self.calcAverageFuncThread, args=(times, value, path))
        self.calcAverageThread.start()

    def calcAverageFuncThread(self, times, value, path):
        beforeRawdata = []
        rawdata = []
        adbtool.shell(window.ui.echoDiag % '2', "SHELL")
        adbtool.shell(window.ui.catDiag, "SHELL")
        name = time.strftime("avg_%Y%m%d_%H-%M-%S_", time.localtime()) + value + ".txt"
        file = open(path + name, 'a+')

        for k in range(int(times)):
            ret = adbtool.shell(window.ui.catDiag, "SHELL")
            tmpRawdata = self.analysisRawdata(ret)
            if tmpRawdata == '':
                window.ui.dialogWin("data wrong")
                return

            for i in range(window.ui.transRX + 2):
                for j in range(window.ui.transTX + 2):
                    if i == 0 or i == window.ui.transRX + 1 or j == 0 or j == window.ui.transTX + 1:
                        continue
                    else:
                        rawdata.append(int(tmpRawdata[i*(window.ui.transTX + 2) + j]))

            if k == 0:
                beforeRawdata = rawdata
            else:
                for m in range(len(rawdata)):
                    beforeRawdata[m] += rawdata[m]

            # write every rawdata to file
            strRawdata = ''
            for l in range(len(rawdata)):
                if (l + 1) % window.ui.transTX == 0:
                    strRawdata += str(rawdata[l]) + '\n'
                else:
                    strRawdata += str(rawdata[l]) + ' '

            file.write("Frame %d:\n" % (k + 1) + strRawdata + '\n')

            # clear rawdata
            rawdata = []

        strRawdata = ''
        for n in range(len(beforeRawdata)):
            beforeRawdata[n] = beforeRawdata[n]//int(times)
            if (n + 1) % window.ui.transTX == 0:
                strRawdata += str(beforeRawdata[n]) + '\n'
            else:
                strRawdata += str(beforeRawdata[n]) + ' '

        file.write("%s AVERAGE VALUE:\n" % value + strRawdata)
        file.close()
        self.calcAverage.setDisabled(False)
        self.calcAverage.setText("VRCollect")
        self.calcAverage.setStyleSheet("color:rgb(0, 0, 0)")

        if os.path.exists(path + name):
            os.startfile(path + name)

    """ rawdata show """
    def chooseRawdataType(self):
        self.keepMax = False
        self.keepMin = False
        if self.radioDC.isChecked():
            adbtool.shell(window.ui.echoDiag % '2', "SHELL")

        elif self.radioIIR.isChecked():
            adbtool.shell(window.ui.echoDiag % '1', "SHELL")
        elif self.radioTmp.isChecked():
            type = self.textEditDiag.text()
            if type == '':
                return False
            adbtool.shell(window.ui.echoDiag % type, "SHELL")
        else:
            return False
        return True

    def rawdataReadFunc(self, reset):
        # choose rawdata type
        if not reset:
            if not self.chooseRawdataType():
                window.ui.dialogWin("Please set type")
                return

        if reset:
            self.rawdataRead.setObjectName('rawdataReadStop')

        if self.rawdataRead.objectName() == 'rawdataRead':
            self.rawdataRead.setObjectName('rawdataReadStop')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/stop_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rawdataRead.setIcon(icon)
            self.rawdataRead.setIconSize(QtCore.QSize(39, 39))

            # init first data
            ret = adbtool.shell(window.ui.catDiag, "SHELL")
            data = self.analysisRawdata(ret)
            if data == '' or len(data) != window.ui.transTX * window.ui.transRX:
                print("error")
                return
            self.keepRawdata = self.getFirstFrameRawdata(data)

            # cat diag
            self.readRawdataThread = Thread(target=self.showRawdata)
            self.readRawdataThread.start()
        elif self.rawdataRead.objectName() == 'rawdataReadStop':
            self.rawdataRead.setObjectName('rawdataRead')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/start_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.rawdataRead.setIcon(icon)
            self.rawdataRead.setIconSize(QtCore.QSize(39, 39))

            self.showRawdataFlag = 0

            adbtool.shell(window.ui.echoDiag % '0', "SHELL")

    def showRawdata(self):
        self.showRawdataFlag = 1
        length = window.ui.transTX * window.ui.transRX

        while self.showRawdataFlag:
            ret = adbtool.shell(window.ui.catDiag, "SHELL")
            self.origRawdata = ret
            data = self.analysisRawdata(ret)
            if data == '' or len(data) != length:
                print("error")
                return

            if self.keepMax or self.keepMin:
                data = self.keepMaxOrMinRawdata(data)
                data = self.transMaxOrMinRawdata(data)

            self.fillRawdataToTable(data)
            self.MainRawdataShowtableWidget.reset()

    def analysisRawdata(self, rawdata):
        index0 = rawdata.find('ChannelStart')
        index00 = rawdata.find("\n", index0)
        index1 = rawdata.find('ChannelEnd')
        if index0 == -1 or index1 == -1:
            return ''

        index = rawdata.find('[00]')
        if index != -1: # common driver
            rawdata = rawdata[index:index1]
            rawdata = rawdata.split()
            rawdata.insert(window.ui.transTX - 1, '0')
            rawdata.insert(window.ui.transTX * (window.ui.transRX - 1), '0')
            rawdata.insert(window.ui.transTX * window.ui.transRX, '0')
        else:
            rawdata = rawdata[index00:index1]
            rawdata = rawdata.split()
            rawdata.insert(window.ui.transTX * window.ui.transRX, '0')

        return rawdata

    def getFirstFrameRawdata(self, rawdata):
        for i in range(window.ui.transRX):
            for j in range(window.ui.transTX):
                if i == 0 or j == 0 or (j == window.ui.transTX-1 and i == window.ui.transRX-1):
                    pass
                else:
                    rawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
        return rawdata

    def sumRawdata(self, sum, rawdata):
        for i in range(window.ui.rxnum):
            for j in range(window.ui.txnum):
                sum[i * window.ui.txnum + j] += rawdata[i * window.ui.txnum + j]
        return sum

    def userPatternToMutual(self, rawdata):
        if window.ui.commonFlag:
            ret = [None] * window.ui.rxnum * window.ui.txnum
            k = 0
            for i in range(window.ui.transRX):
                for j in range(window.ui.transTX):
                    if i == 0 or j == 0 or i == window.ui.transRX - 1 or j == window.ui.transTX - 1:
                        pass
                    else:
                        ret[k] = int(rawdata[i * window.ui.transTX + j])
                        k = k + 1
            return ret
        else:
            pass

    def keepMaxOrMinRawdata(self, rawdata):
        # char to int
        for i in range(window.ui.transRX):
            for j in range(window.ui.transTX):
                if window.ui.commonFlag:
                    if i == 0 or j == 0 or (j == window.ui.transTX - 1 and i == window.ui.transRX - 1):
                        pass
                    else:
                        rawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
                        if self.keepMax:
                            if int(rawdata[i * window.ui.transTX + j]) > int(self.keepRawdata[i * window.ui.transTX + j]):
                                self.keepRawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
                        else:
                            if int(rawdata[i * window.ui.transTX + j]) < int(self.keepRawdata[i * window.ui.transTX + j]):
                                self.keepRawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
                else:
                    if j == window.ui.transTX - 1 and i == window.ui.transRX - 1:
                        pass
                    else:
                        rawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
                        if self.keepMax:
                            if int(rawdata[i * window.ui.transTX + j]) > int(self.keepRawdata[i * window.ui.transTX + j]):
                                self.keepRawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
                        else:
                            if int(rawdata[i * window.ui.transTX + j]) < int(self.keepRawdata[i * window.ui.transTX + j]):
                                self.keepRawdata[i * window.ui.transTX + j] = int(rawdata[i * window.ui.transTX + j])
        return self.keepRawdata

    def transMaxOrMinRawdata(self, rawdata):
        for i in range(window.ui.transRX):
            for j in range(window.ui.transTX):
                if window.ui.commonFlag:
                    if i == 0 or j == 0 or (j == window.ui.transTX - 1 and i == window.ui.transRX - 1):
                        pass
                    else:
                        rawdata[i * window.ui.transTX + j] = str(rawdata[i * window.ui.transTX + j])
                else:
                    if j == window.ui.transTX - 1 and i == window.ui.transRX - 1:
                        pass
                    else:
                        rawdata[i * window.ui.transTX + j] = str(rawdata[i * window.ui.transTX + j])
        return rawdata

    def fillRawdataToTable(self, rawdata):
        for i in range(window.ui.transRX):
            for j in range(window.ui.transTX):
                a = QTableWidgetItem(rawdata[i * window.ui.transTX + j])
                self.MainRawdataShowtableWidget.setItem(i, j, a)

    def logThread(self):
        self.keepFlag = True
        name = time.strftime("%Y%m%d_%H_%M_%S", time.localtime()) + ".txt"
        path = ' > /sdcard/' + name
        adbtool.shell("adb push ./tools/himax /data/")
        adbtool.shell("chmod 777 /data/himax", "SHELL")
        delayTime = self.logTimesBtn.text()
        if delayTime == '':
            window.ui.dialogWin("please set delay time")
            return

        # if delayTime.find(','):

        delayTime = int(delayTime)*1000

        cmd = './data/himax ' + window.ui.v1DiagPath + ' ' + str(delayTime) + ' 0'
        print('adb shell "' + cmd + '"')
        # adbtool.shell('adb shell "' + cmd + '"')
        p = subprocess.Popen('adb shell "' + cmd + '"', shell=True, stdout=subprocess.PIPE)
        while self.keepFlag:
            l = p.stdout.readline()
            if not l:
                break
            print(l)

        self.log.setDisabled(False)
        self.log.setText("Log")
        self.log.setStyleSheet("color: rgb(0, 0, 0)")

        # adbtool.shell("adb shell rm -rf /data/himax")

    def logFunc(self):
        pass
        self.log.setDisabled(True)
        self.log.setText("Ing.")
        self.log.setStyleSheet("color: rgb(255, 0, 0)")

        if not os.path.exists("./log"):
            os.mkdir("log")

        log = Thread(target=self.logThread)
        log.start()

    def initRawdataUI(self, rx, tx):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.MainRawdataShowtableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MainRawdataShowtableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        sizePolicy.setHeightForWidth(self.MainRawdataShowtableWidget.sizePolicy().hasHeightForWidth())
        self.MainRawdataShowtableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.MainRawdataShowtableWidget.setSizePolicy(sizePolicy)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.setRowCount(rx)
        self.MainRawdataShowtableWidget.setColumnCount(tx)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.verticalHeader().setVisible(False)
        self.MainRawdataShowtableWidget.horizontalHeader().setVisible(False)
        self.MainRawdataShowtableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.MainRawdataShowtableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.MainRawdataShowtableWidget.verticalHeader().setDefaultSectionSize(10)
        self.MainRawdataShowtableWidget.verticalHeader().setMinimumSectionSize(10)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MainRawdataShowtableWidget.setFont(font)

        for i in range(tx):
            self.MainRawdataShowtableWidget.setColumnWidth(i, window.rawdataWidth)
        for i in range(rx):
            self.MainRawdataShowtableWidget.setRowHeight(i, window.rawdataHeight)

    def setRegExp(self):
        # rawdata type, time
        reg = QRegExp('[0-9]{2}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.textEditDiag.setValidator(pValidator)

        reg = QRegExp('[1-9][0-9]{2}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.frameTimes.setValidator(pValidator)

        reg = QRegExp('[0-9,]{8}')
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)
        self.logTimesBtn.setValidator(pValidator)


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.login = Ui_LoginWindow()
        self.login.initUI(self)
        self.login.centralwidget.setMouseTracking(True)
        self.enterTimes = 1

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Enter or key == 16777220:
            self.login.loginFunc()
            self.enterTimes += 1

        if key == QtCore.Qt.Key_Escape:
            self.close()

        if key == QtCore.Qt.Key_M:
            login.close()
            window.show()


class Ui_LoginWindow(object):
    def initUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.resize(300, 150)
        MainWindow.setStyleSheet("background-color:rgb(193, 255, 193)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.girdLayout = QtWidgets.QGridLayout()
        self.girdLayout.setAlignment(QtCore.Qt.AlignVCenter)
        self.titleLabel = QtWidgets.QLabel()
        self.copyrightLabel = QtWidgets.QLabel()
        self.empty = QtWidgets.QLabel()
        self.loginPwd = QtWidgets.QLabel()
        self.status = QtWidgets.QLabel()
        self.ps = QtWidgets.QLabel()
        self.loginPwdLineEdit = QtWidgets.QLineEdit()
        self.loginPwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.titleLabel.setText("<b><font size='5'>ADB Monitor </font>2.0.4</b>")
        self.copyrightLabel.setText("<a style='color:rgb(102, 102, 102)'>Copyright 2019 Himax Technologies, Inc. mc")
        self.loginPwd.setText("PWD:")
        self.status.setText("<a style='color:rgb(0, 0, 130)'>Input pwd, then click <b>Enter</b> or Esc exit!</a>")
        self.ps.setText("Welcome! support v1 or v2 but old")
        self.girdLayout.addWidget(self.titleLabel, 0, 1)
        self.girdLayout.addWidget(self.empty, 1, 1)
        self.girdLayout.addWidget(self.loginPwd, 2, 0)
        self.girdLayout.addWidget(self.loginPwdLineEdit, 2, 1)
        self.girdLayout.addWidget(self.status, 3, 1)
        self.girdLayout.addWidget(self.ps, 4, 1)
        self.girdLayout.addWidget(self.empty, 5, 1)
        self.girdLayout.addWidget(self.copyrightLabel, 6, 1)

        self.loginPwdLineEdit.installEventFilter(MainWindow)

        self.centralwidget.setLayout(self.girdLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))

    def loginFunc(self):
        pwdTime = time.strftime("%Y%m%d", time.localtime())[2:]
        pwd = self.loginPwdLineEdit.text()
        if pwd == 'himax':
            login.close()
            window.ui.TabMainWindow.removeTab(2)
            window.ui.TabMainWindow.removeTab(2)
            window.ui.TabMainWindow.removeTab(2)
            child.ui.log.hide()
            child.ui.calcAverage.hide()
            child.ui.frameTimes.hide()
            child.ui.vrTable.hide()
            child.ui.removeVRTable.hide()
            window.show()
        elif pwd == 'himax' + pwdTime:
            login.close()
            window.show()
        else:
            if 5 > login.enterTimes > 2:
                self.status.setText("Congratulations! You have a bad memory!")
            elif login.enterTimes >= 5:
                self.status.setText("Badly!")
            else:
                self.status.setText("Pwd was wrong!")
            self.loginPwdLineEdit.clear()
            self.status.setStyleSheet("color:rgb(255, 0, 0)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    window = MainWindow()
    child = ChildWindow()
    sys.exit(app.exec_())
