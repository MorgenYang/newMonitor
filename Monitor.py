from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import adb
from threading import Thread
import time
import subprocess
import re
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.initPath()
        self.ui.setupUi(self)
        self.ui.bindEventFunc()

        self.uiThreadRoot = Thread(target=self.ui.rootFunc)
        self.uiThreadInitHistory = Thread(target=self.ui.initHistoryFunc)
        self.uiThreadRoot.start()
        self.uiThreadInitHistory.start()
        self.statusBar().addWidget(QLabel("Ready"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(680, 500)
        MainWindow.setMinimumSize(QtCore.QSize(680, 0))
        MainWindow.setMaximumSize(QtCore.QSize(680, 530))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TabMainWindow = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TabMainWindow.setFont(font)
        self.TabMainWindow.setObjectName("TabMainWindow")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 595, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setToolTipDuration(-1)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox.setObjectName("groupBox")
        self.wifiConnect = QtWidgets.QPushButton(self.groupBox)
        self.wifiConnect.setGeometry(QtCore.QRect(10, 15, 90, 30))
        self.wifiConnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiConnect.setFont(font)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiConnect.setFlat(False)
        self.wifiConnect.setObjectName("wifiConnect")
        self.wifiDisconnect = QtWidgets.QPushButton(self.groupBox)
        self.wifiDisconnect.setGeometry(QtCore.QRect(105, 15, 90, 30))
        self.wifiDisconnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiDisconnect.setFont(font)
        self.wifiDisconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiDisconnect.setCheckable(False)
        self.wifiDisconnect.setObjectName("wifiDisconnect")
        self.wifiReconnect = QtWidgets.QPushButton(self.groupBox)
        self.wifiReconnect.setGeometry(QtCore.QRect(200, 15, 90, 30))
        self.wifiReconnect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wifiReconnect.setFont(font)
        self.wifiReconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiReconnect.setCheckable(False)
        self.wifiReconnect.setObjectName("wifiReconnect")
        self.wifiStatus = QtWidgets.QLabel(self.groupBox)
        self.wifiStatus.setGeometry(QtCore.QRect(300, 15, 100, 30))
        self.wifiStatus.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wifiStatus.setFont(font)
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.wifiStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiStatus.setWordWrap(False)
        self.wifiStatus.setObjectName("wifiStatus")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 50, 595, 86))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setToolTipDuration(-1)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.homekey = QtWidgets.QPushButton(self.groupBox_2)
        self.homekey.setGeometry(QtCore.QRect(10, 50, 70, 30))
        self.homekey.setMinimumSize(QtCore.QSize(0, 0))
        self.homekey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homekey.setFont(font)
        self.homekey.setStyleSheet("color: rgb(0, 0, 0);")
        self.homekey.setObjectName("homekey")
        self.reboot = QtWidgets.QPushButton(self.groupBox_2)
        self.reboot.setGeometry(QtCore.QRect(470, 50, 70, 30))
        self.reboot.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reboot.setFont(font)
        self.reboot.setStyleSheet("color: rgb(0, 0, 0);")
        self.reboot.setObjectName("reboot")
        self.interrupts = QtWidgets.QPushButton(self.groupBox_2)
        self.interrupts.setGeometry(QtCore.QRect(385, 50, 80, 30))
        self.interrupts.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.interrupts.setFont(font)
        self.interrupts.setStyleSheet("color: rgb(0, 0, 0);")
        self.interrupts.setObjectName("interrupts")
        self.volDown = QtWidgets.QPushButton(self.groupBox_2)
        self.volDown.setGeometry(QtCore.QRect(235, 50, 70, 30))
        self.volDown.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volDown.setFont(font)
        self.volDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.volDown.setObjectName("volDown")
        self.backkey = QtWidgets.QPushButton(self.groupBox_2)
        self.backkey.setGeometry(QtCore.QRect(85, 50, 70, 30))
        self.backkey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backkey.setFont(font)
        self.backkey.setStyleSheet("color: rgb(0, 0, 0);")
        self.backkey.setObjectName("backkey")
        self.checkDevice = QtWidgets.QPushButton(self.groupBox_2)
        self.checkDevice.setGeometry(QtCore.QRect(10, 15, 85, 30))
        self.checkDevice.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkDevice.setFont(font)
        self.checkDevice.setStyleSheet("color: rgb(0, 0, 0);")
        self.checkDevice.setObjectName("checkDevice")
        self.volUp = QtWidgets.QPushButton(self.groupBox_2)
        self.volUp.setGeometry(QtCore.QRect(160, 50, 70, 30))
        self.volUp.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volUp.setFont(font)
        self.volUp.setStyleSheet("color: rgb(0, 0, 0);")
        self.volUp.setObjectName("volUp")
        self.powerKey = QtWidgets.QPushButton(self.groupBox_2)
        self.powerKey.setGeometry(QtCore.QRect(195, 15, 80, 30))
        self.powerKey.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.powerKey.setFont(font)
        self.powerKey.setStyleSheet("color: rgb(0, 0, 0);")
        self.powerKey.setObjectName("powerKey")
        self.screenShot = QtWidgets.QPushButton(self.groupBox_2)
        self.screenShot.setGeometry(QtCore.QRect(365, 15, 80, 30))
        self.screenShot.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.screenShot.setFont(font)
        self.screenShot.setStyleSheet("color: rgb(0, 0, 0);")
        self.screenShot.setObjectName("screenShot")
        self.openClosePoint = QtWidgets.QPushButton(self.groupBox_2)
        self.openClosePoint.setGeometry(QtCore.QRect(280, 15, 80, 30))
        self.openClosePoint.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openClosePoint.setFont(font)
        self.openClosePoint.setStyleSheet("color: rgb(0, 0, 0);")
        self.openClosePoint.setObjectName("openClosePoint")
        self.getprop = QtWidgets.QPushButton(self.groupBox_2)
        self.getprop.setGeometry(QtCore.QRect(310, 50, 70, 30))
        self.getprop.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.getprop.setFont(font)
        self.getprop.setStyleSheet("color: rgb(0, 0, 0);")
        self.getprop.setObjectName("getprop")
        self.hideShowVirtual = QtWidgets.QPushButton(self.groupBox_2)
        self.hideShowVirtual.setGeometry(QtCore.QRect(103, 15, 85, 30))
        self.hideShowVirtual.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hideShowVirtual.setFont(font)
        self.hideShowVirtual.setStyleSheet("color: rgb(0, 0, 0);")
        self.hideShowVirtual.setObjectName("hideShowVirtual")
        self.shutDown = QtWidgets.QPushButton(self.groupBox_2)
        self.shutDown.setGeometry(QtCore.QRect(450, 15, 80, 30))
        self.shutDown.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shutDown.setFont(font)
        self.shutDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.shutDown.setObjectName("shutDown")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 135, 595, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.inten0 = QtWidgets.QPushButton(self.groupBox_3)
        self.inten0.setGeometry(QtCore.QRect(10, 50, 75, 30))
        self.inten0.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inten0.setFont(font)
        self.inten0.setStyleSheet("color: rgb(0, 0, 0);")
        self.inten0.setObjectName("inten0")
        self.senseon = QtWidgets.QPushButton(self.groupBox_3)
        self.senseon.setGeometry(QtCore.QRect(178, 15, 75, 30))
        self.senseon.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.senseon.setFont(font)
        self.senseon.setStyleSheet("color: rgb(0, 0, 0);")
        self.senseon.setObjectName("senseon")
        self.driverVersion = QtWidgets.QPushButton(self.groupBox_3)
        self.driverVersion.setGeometry(QtCore.QRect(420, 15, 75, 30))
        self.driverVersion.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.driverVersion.setFont(font)
        self.driverVersion.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.driverVersion.setObjectName("driverVersion")
        self.fwVersion = QtWidgets.QPushButton(self.groupBox_3)
        self.fwVersion.setGeometry(QtCore.QRect(10, 15, 75, 30))
        self.fwVersion.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fwVersion.setFont(font)
        self.fwVersion.setStyleSheet("color: rgb(0, 0, 0);")
        self.fwVersion.setObjectName("fwVersion")
        self.inten1 = QtWidgets.QPushButton(self.groupBox_3)
        self.inten1.setGeometry(QtCore.QRect(88, 50, 75, 30))
        self.inten1.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inten1.setFont(font)
        self.inten1.setStyleSheet("color: rgb(0, 0, 0);")
        self.inten1.setObjectName("inten1")
        self.selftest = QtWidgets.QPushButton(self.groupBox_3)
        self.selftest.setGeometry(QtCore.QRect(340, 15, 75, 30))
        self.selftest.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selftest.setFont(font)
        self.selftest.setStyleSheet("color: rgb(0, 0, 0);")
        self.selftest.setObjectName("selftest")
        self.senseoff = QtWidgets.QPushButton(self.groupBox_3)
        self.senseoff.setGeometry(QtCore.QRect(259, 15, 75, 30))
        self.senseoff.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.senseoff.setFont(font)
        self.senseoff.setStyleSheet("color: rgb(0, 0, 0);")
        self.senseoff.setObjectName("senseoff")
        self.diagArr = QtWidgets.QPushButton(self.groupBox_3)
        self.diagArr.setGeometry(QtCore.QRect(250, 50, 75, 30))
        self.diagArr.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diagArr.setFont(font)
        self.diagArr.setStyleSheet("color: rgb(0, 0, 0);")
        self.diagArr.setObjectName("diagArr")
        self.flashDump = QtWidgets.QPushButton(self.groupBox_3)
        self.flashDump.setGeometry(QtCore.QRect(165, 50, 75, 30))
        self.flashDump.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flashDump.setFont(font)
        self.flashDump.setStyleSheet("color: rgb(0, 0, 0);")
        self.flashDump.setObjectName("flashDump")
        self.updateFWText = QtWidgets.QTextEdit(self.groupBox_3)
        self.updateFWText.setGeometry(QtCore.QRect(455, 50, 50, 30))
        self.updateFWText.setMaximumSize(QtCore.QSize(100, 30))
        self.updateFWText.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFWText.setObjectName("updateFWText")
        self.reset = QtWidgets.QPushButton(self.groupBox_3)
        self.reset.setGeometry(QtCore.QRect(95, 15, 75, 30))
        self.reset.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setStyleSheet("color: rgb(0, 0, 0);")
        self.reset.setObjectName("reset")
        self.updateFW = QtWidgets.QPushButton(self.groupBox_3)
        self.updateFW.setGeometry(QtCore.QRect(380, 50, 75, 30))
        self.updateFW.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.updateFW.setFont(font)
        self.updateFW.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFW.setObjectName("updateFW")
        self.diagArrText = QtWidgets.QLineEdit(self.groupBox_3)
        self.diagArrText.setGeometry(QtCore.QRect(325, 50, 50, 30))
        self.diagArrText.setObjectName("diagArrText")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 225, 595, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.openBlight = QtWidgets.QPushButton(self.groupBox_4)
        self.openBlight.setGeometry(QtCore.QRect(229, 15, 100, 30))
        self.openBlight.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openBlight.setFont(font)
        self.openBlight.setStyleSheet("color: rgb(0, 0, 0);")
        self.openBlight.setObjectName("openBlight")
        self.d1129 = QtWidgets.QPushButton(self.groupBox_4)
        self.d1129.setGeometry(QtCore.QRect(10, 15, 100, 30))
        self.d1129.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1129.setFont(font)
        self.d1129.setStyleSheet("color: rgb(0, 0, 0);")
        self.d1129.setObjectName("d1129")
        self.d2810 = QtWidgets.QPushButton(self.groupBox_4)
        self.d2810.setGeometry(QtCore.QRect(120, 15, 100, 30))
        self.d2810.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d2810.setFont(font)
        self.d2810.setStyleSheet("color: rgb(0, 0, 0);")
        self.d2810.setObjectName("d2810")
        self.rawdataShowText = QtWidgets.QTextBrowser(self.tab_2)
        self.rawdataShowText.setGeometry(QtCore.QRect(10, 275, 585, 178))
        self.rawdataShowText.setMaximumSize(QtCore.QSize(585, 205))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.TabMainWindow.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.MainRawdataShowtableWidget = QtWidgets.QTableWidget(self.tab)
        self.MainRawdataShowtableWidget.setGeometry(QtCore.QRect(42, 0, 630, 450))
        self.MainRawdataShowtableWidget.setMinimumSize(QtCore.QSize(630, 0))
        self.MainRawdataShowtableWidget.setMaximumSize(QtCore.QSize(640, 482))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.MainRawdataShowtableWidget.setFont(font)
        self.MainRawdataShowtableWidget.setObjectName("MainRawdataShowtableWidget")
        self.MainRawdataShowtableWidget.setColumnCount(0)
        self.MainRawdataShowtableWidget.setRowCount(0)

        # morgen
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


        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 41, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rawdataRead = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rawdataRead.setMinimumSize(QtCore.QSize(0, 0))
        self.rawdataRead.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rawdataRead.setFont(font)
        self.rawdataRead.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rawdataRead.setStyleSheet("background-color: rgb(170, 255, 127);")
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
        self.textEditDiag.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEditDiag.setFont(font)
        self.textEditDiag.setObjectName("textEditDiag")
        self.verticalLayout.addWidget(self.textEditDiag)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        self.log = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.log.setMaximumSize(QtCore.QSize(100, 30))
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
        self.recalled.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recalled.setFont(font)
        self.recalled.setObjectName("recalled")
        self.verticalLayout.addWidget(self.recalled)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.sram = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sram.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sram.setFont(font)
        self.sram.setObjectName("sram")
        self.verticalLayout.addWidget(self.sram)
        self.kmsg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kmsg.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kmsg.setFont(font)
        self.kmsg.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.kmsg.setObjectName("kmsg")
        self.verticalLayout.addWidget(self.kmsg)
        self.textEditKmsg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEditKmsg.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEditKmsg.setFont(font)
        self.textEditKmsg.setObjectName("textEditKmsg")
        self.verticalLayout.addWidget(self.textEditKmsg)
        self.getevent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getevent.setMinimumSize(QtCore.QSize(0, 0))
        self.getevent.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.getevent.setFont(font)
        self.getevent.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.getevent.setObjectName("getevent")
        self.verticalLayout.addWidget(self.getevent)
        self.textEditGetevent = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textEditGetevent.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEditGetevent.setFont(font)
        self.textEditGetevent.setObjectName("textEditGetevent")
        self.verticalLayout.addWidget(self.textEditGetevent)
        self.TabMainWindow.addTab(self.tab, "")
        self.TabRWRegister = QtWidgets.QWidget()
        self.TabRWRegister.setObjectName("TabRWRegister")
        self.pushButtonRead = QtWidgets.QPushButton(self.TabRWRegister)
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
        self.textEditReadRegAddr = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditReadRegAddr.setGeometry(QtCore.QRect(0, 27, 100, 101))
        self.textEditReadRegAddr.setMaximumSize(QtCore.QSize(150, 170))
        self.textEditReadRegAddr.setObjectName("textEditReadRegAddr")
        self.textEditWriteVal3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal3.setGeometry(QtCore.QRect(350, 90, 120, 25))
        self.textEditWriteVal3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal3.setObjectName("textEditWriteVal3")
        self.textEditWriteVal4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal4.setGeometry(QtCore.QRect(350, 120, 120, 25))
        self.textEditWriteVal4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal4.setObjectName("textEditWriteVal4")
        self.textEditWriteVal2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal2.setGeometry(QtCore.QRect(350, 60, 120, 25))
        self.textEditWriteVal2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal2.setObjectName("textEditWriteVal2")
        self.textEditWriteAddr1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr1.setGeometry(QtCore.QRect(220, 30, 120, 25))
        self.textEditWriteAddr1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr1.setObjectName("textEditWriteAddr1")
        self.textEditWriteAddr2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr2.setGeometry(QtCore.QRect(220, 60, 120, 25))
        self.textEditWriteAddr2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr2.setObjectName("textEditWriteAddr2")
        self.textEditWriteAddr0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr0.setGeometry(QtCore.QRect(220, 0, 120, 25))
        self.textEditWriteAddr0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr0.setObjectName("textEditWriteAddr0")
        self.textEditWriteVal1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal1.setGeometry(QtCore.QRect(350, 30, 120, 25))
        self.textEditWriteVal1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal1.setObjectName("textEditWriteVal1")
        self.pushButtonRegWrite0 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite0.setGeometry(QtCore.QRect(110, 0, 100, 25))
        self.pushButtonRegWrite0.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite0.setObjectName("pushButtonRegWrite0")
        self.pushButtonRegWrite1 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite1.setGeometry(QtCore.QRect(110, 30, 100, 25))
        self.pushButtonRegWrite1.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite1.setObjectName("pushButtonRegWrite1")
        self.textEditWriteVal0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal0.setGeometry(QtCore.QRect(350, 0, 120, 25))
        self.textEditWriteVal0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal0.setObjectName("textEditWriteVal0")
        self.textEditWriteAddr3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr3.setGeometry(QtCore.QRect(220, 90, 120, 25))
        self.textEditWriteAddr3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr3.setObjectName("textEditWriteAddr3")
        self.pushButtonRegWrite2 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite2.setGeometry(QtCore.QRect(110, 60, 100, 25))
        self.pushButtonRegWrite2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite2.setObjectName("pushButtonRegWrite2")
        self.textEditWriteAddr4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr4.setGeometry(QtCore.QRect(220, 120, 120, 25))
        self.textEditWriteAddr4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr4.setObjectName("textEditWriteAddr4")
        self.pushButtonRegWrite4 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite4.setGeometry(QtCore.QRect(110, 120, 100, 25))
        self.pushButtonRegWrite4.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite4.setObjectName("pushButtonRegWrite4")
        self.pushButtonRegWrite3 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite3.setGeometry(QtCore.QRect(110, 90, 100, 25))
        self.pushButtonRegWrite3.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonRegWrite3.setObjectName("pushButtonRegWrite3")
        self.label = QtWidgets.QLabel(self.TabRWRegister)
        self.label.setGeometry(QtCore.QRect(5, 128, 50, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.reglength = QtWidgets.QComboBox(self.TabRWRegister)
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
        self.readRegValShowText = QtWidgets.QTextBrowser(self.TabRWRegister)
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 150, 625, 303))
        self.readRegValShowText.setMinimumSize(QtCore.QSize(625, 0))
        self.readRegValShowText.setMaximumSize(QtCore.QSize(625, 330))
        self.readRegValShowText.setObjectName("readRegValShowText")
        self.TabMainWindow.addTab(self.TabRWRegister, "")
        self.TabSwiplines = QtWidgets.QWidget()
        self.TabSwiplines.setObjectName("TabSwiplines")
        self.DDpushButtonRegWrite0 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDpushButtonRegWrite0.setGeometry(QtCore.QRect(180, 0, 60, 25))
        self.DDpushButtonRegWrite0.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DDpushButtonRegWrite0.setFont(font)
        self.DDpushButtonRegWrite0.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.DDpushButtonRegWrite0.setObjectName("DDpushButtonRegWrite0")
        self.DDpushButtonRegWrite2 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDpushButtonRegWrite2.setGeometry(QtCore.QRect(180, 60, 60, 25))
        self.DDpushButtonRegWrite2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DDpushButtonRegWrite2.setFont(font)
        self.DDpushButtonRegWrite2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.DDpushButtonRegWrite2.setObjectName("DDpushButtonRegWrite2")
        self.DDRead0 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDRead0.setGeometry(QtCore.QRect(0, 0, 60, 25))
        self.DDRead0.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DDRead0.setFont(font)
        self.DDRead0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DDRead0.setObjectName("DDRead0")
        self.DDreadRegValShowText = QtWidgets.QTextBrowser(self.TabSwiplines)
        self.DDreadRegValShowText.setGeometry(QtCore.QRect(0, 150, 625, 303))
        self.DDreadRegValShowText.setMinimumSize(QtCore.QSize(625, 0))
        self.DDreadRegValShowText.setMaximumSize(QtCore.QSize(625, 330))
        self.DDreadRegValShowText.setObjectName("DDreadRegValShowText")
        self.DDpushButtonRegWrite3 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDpushButtonRegWrite3.setGeometry(QtCore.QRect(180, 90, 60, 25))
        self.DDpushButtonRegWrite3.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DDpushButtonRegWrite3.setFont(font)
        self.DDpushButtonRegWrite3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.DDpushButtonRegWrite3.setObjectName("DDpushButtonRegWrite3")
        self.DDpushButtonRegWrite1 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDpushButtonRegWrite1.setGeometry(QtCore.QRect(180, 30, 60, 25))
        self.DDpushButtonRegWrite1.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DDpushButtonRegWrite1.setFont(font)
        self.DDpushButtonRegWrite1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.DDpushButtonRegWrite1.setObjectName("DDpushButtonRegWrite1")
        self.DDpushButtonRegWrite4 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDpushButtonRegWrite4.setGeometry(QtCore.QRect(180, 120, 60, 25))
        self.DDpushButtonRegWrite4.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DDpushButtonRegWrite4.setFont(font)
        self.DDpushButtonRegWrite4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.DDpushButtonRegWrite4.setObjectName("DDpushButtonRegWrite4")
        self.DDWLineEditAddr0 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditAddr0.setGeometry(QtCore.QRect(250, 0, 60, 25))
        self.DDWLineEditAddr0.setObjectName("DDWLineEditAddr0")
        self.DDWLineEditBank0 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditBank0.setGeometry(QtCore.QRect(320, 0, 60, 25))
        self.DDWLineEditBank0.setObjectName("DDWLineEditBank0")
        self.DDWLineEditLen0 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditLen0.setGeometry(QtCore.QRect(390, 0, 60, 25))
        self.DDWLineEditLen0.setObjectName("DDWLineEditLen0")
        self.DDWLineEditAddr1 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditAddr1.setGeometry(QtCore.QRect(250, 30, 60, 25))
        self.DDWLineEditAddr1.setObjectName("DDWLineEditAddr1")
        self.DDWLineEditBank1 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditBank1.setGeometry(QtCore.QRect(320, 30, 60, 25))
        self.DDWLineEditBank1.setObjectName("DDWLineEditBank1")
        self.DDWLineEditLen1 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditLen1.setGeometry(QtCore.QRect(390, 30, 60, 25))
        self.DDWLineEditLen1.setObjectName("DDWLineEditLen1")
        self.DDWLineEditAddr2 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditAddr2.setGeometry(QtCore.QRect(250, 60, 60, 25))
        self.DDWLineEditAddr2.setObjectName("DDWLineEditAddr2")
        self.DDWLineEditBank2 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditBank2.setGeometry(QtCore.QRect(320, 60, 60, 25))
        self.DDWLineEditBank2.setObjectName("DDWLineEditBank2")
        self.DDWLineEditLen2 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditLen2.setGeometry(QtCore.QRect(390, 60, 60, 25))
        self.DDWLineEditLen2.setObjectName("DDWLineEditLen2")
        self.DDWLineEditAddr3 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditAddr3.setGeometry(QtCore.QRect(250, 90, 60, 25))
        self.DDWLineEditAddr3.setObjectName("DDWLineEditAddr3")
        self.DDWLineEditBank3 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditBank3.setGeometry(QtCore.QRect(320, 90, 60, 25))
        self.DDWLineEditBank3.setObjectName("DDWLineEditBank3")
        self.DDWLineEditLen3 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditLen3.setGeometry(QtCore.QRect(390, 90, 60, 25))
        self.DDWLineEditLen3.setObjectName("DDWLineEditLen3")
        self.DDWLineEditAddr4 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditAddr4.setGeometry(QtCore.QRect(250, 120, 60, 25))
        self.DDWLineEditAddr4.setObjectName("DDWLineEditAddr4")
        self.DDWLineEditBank4 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditBank4.setGeometry(QtCore.QRect(320, 120, 60, 25))
        self.DDWLineEditBank4.setObjectName("DDWLineEditBank4")
        self.DDWLineEditLen4 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditLen4.setGeometry(QtCore.QRect(390, 120, 60, 25))
        self.DDWLineEditLen4.setObjectName("DDWLineEditLen4")
        self.DDWLineEditVal4 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditVal4.setGeometry(QtCore.QRect(460, 120, 60, 25))
        self.DDWLineEditVal4.setObjectName("DDWLineEditVal4")
        self.DDWLineEditVal1 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditVal1.setGeometry(QtCore.QRect(460, 30, 60, 25))
        self.DDWLineEditVal1.setObjectName("DDWLineEditVal1")
        self.DDWLineEditVal0 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditVal0.setGeometry(QtCore.QRect(460, 0, 60, 25))
        self.DDWLineEditVal0.setObjectName("DDWLineEditVal0")
        self.DDWLineEditVal2 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditVal2.setGeometry(QtCore.QRect(460, 60, 60, 25))
        self.DDWLineEditVal2.setObjectName("DDWLineEditVal2")
        self.DDWLineEditVal3 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDWLineEditVal3.setGeometry(QtCore.QRect(460, 90, 60, 25))
        self.DDWLineEditVal3.setObjectName("DDWLineEditVal3")
        self.DDRlineEdit0 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDRlineEdit0.setGeometry(QtCore.QRect(70, 0, 90, 25))
        self.DDRlineEdit0.setObjectName("DDRlineEdit0")
        self.DDRlineEdit2 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDRlineEdit2.setGeometry(QtCore.QRect(70, 60, 90, 25))
        self.DDRlineEdit2.setObjectName("DDRlineEdit2")
        self.DDRlineEdit3 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDRlineEdit3.setGeometry(QtCore.QRect(70, 90, 90, 25))
        self.DDRlineEdit3.setObjectName("DDRlineEdit3")
        self.DDRlineEdit1 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDRlineEdit1.setGeometry(QtCore.QRect(70, 30, 90, 25))
        self.DDRlineEdit1.setObjectName("DDRlineEdit1")
        self.DDRlineEdit4 = QtWidgets.QLineEdit(self.TabSwiplines)
        self.DDRlineEdit4.setGeometry(QtCore.QRect(70, 120, 90, 25))
        self.DDRlineEdit4.setObjectName("DDRlineEdit4")
        self.DDRead4 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDRead4.setGeometry(QtCore.QRect(0, 120, 60, 25))
        self.DDRead4.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DDRead4.setFont(font)
        self.DDRead4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DDRead4.setObjectName("DDRead4")
        self.DDRead1 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDRead1.setGeometry(QtCore.QRect(0, 30, 60, 25))
        self.DDRead1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DDRead1.setFont(font)
        self.DDRead1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DDRead1.setObjectName("DDRead1")
        self.DDRead2 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDRead2.setGeometry(QtCore.QRect(0, 60, 60, 25))
        self.DDRead2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DDRead2.setFont(font)
        self.DDRead2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DDRead2.setObjectName("DDRead2")
        self.DDRead3 = QtWidgets.QPushButton(self.TabSwiplines)
        self.DDRead3.setGeometry(QtCore.QRect(0, 90, 60, 25))
        self.DDRead3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DDRead3.setFont(font)
        self.DDRead3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.DDRead3.setObjectName("DDRead3")
        self.TabMainWindow.addTab(self.TabSwiplines, "")
        self.TabHelp = QtWidgets.QWidget()
        self.TabHelp.setObjectName("TabHelp")
        self.TabHelpSubMain = QtWidgets.QTabWidget(self.TabHelp)
        self.TabHelpSubMain.setGeometry(QtCore.QRect(0, 0, 571, 441))
        self.TabHelpSubMain.setObjectName("TabHelpSubMain")
        self.TabAbout = QtWidgets.QWidget()
        self.TabAbout.setObjectName("TabAbout")
        self.tableView = QtWidgets.QTableView(self.TabAbout)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 561, 411))
        self.tableView.setObjectName("tableView")

        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['序号', '姓名', '年龄', '地址'])

        for row in range(4):
            for column in range(4):
                i = QStandardItem("row %s,column %s" % (row, column))
                self.model.setItem(row, column, i)
        self.tableView.setModel(self.model)


        self.TabHelpSubMain.addTab(self.TabAbout, "")
        self.TabCommands = QtWidgets.QWidget()
        self.TabCommands.setObjectName("TabCommands")
        self.TabHelpSubMain.addTab(self.TabCommands, "")
        self.TabMainWindow.addTab(self.TabHelp, "")
        self.horizontalLayout.addWidget(self.TabMainWindow)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB Monitor 2.0.0"))
        self.groupBox.setTitle(_translate("MainWindow", "WIFI"))
        self.wifiConnect.setText(_translate("MainWindow", "Connect"))
        self.wifiDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.wifiReconnect.setText(_translate("MainWindow", "Reconnect"))
        self.wifiStatus.setText(_translate("MainWindow", "WiFi Status"))
        self.groupBox_2.setTitle(_translate("MainWindow", "ADB"))
        self.homekey.setText(_translate("MainWindow", "Home"))
        self.reboot.setText(_translate("MainWindow", "Reboot"))
        self.interrupts.setText(_translate("MainWindow", "Interrupts"))
        self.volDown.setText(_translate("MainWindow", "Vol down"))
        self.backkey.setText(_translate("MainWindow", "Back"))
        self.checkDevice.setText(_translate("MainWindow", "CheckDevice"))
        self.volUp.setText(_translate("MainWindow", "Vol up"))
        self.powerKey.setText(_translate("MainWindow", "PowerKey"))
        self.screenShot.setText(_translate("MainWindow", "ScreenShot"))
        self.openClosePoint.setText(_translate("MainWindow", "OpenPoint"))
        self.getprop.setText(_translate("MainWindow", "Getprop"))
        self.hideShowVirtual.setText(_translate("MainWindow", "ShowVirtual"))
        self.shutDown.setText(_translate("MainWindow", "ShutDown"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Touch"))
        self.inten0.setText(_translate("MainWindow", "Int_en_0"))
        self.senseon.setText(_translate("MainWindow", "SenseOn"))
        self.driverVersion.setText(_translate("MainWindow", "V2"))
        self.fwVersion.setText(_translate("MainWindow", "FWVersion"))
        self.inten1.setText(_translate("MainWindow", "Int_en_1"))
        self.selftest.setText(_translate("MainWindow", "SelfTest"))
        self.senseoff.setText(_translate("MainWindow", "SenseOff"))
        self.diagArr.setText(_translate("MainWindow", "DiagArr"))
        self.flashDump.setText(_translate("MainWindow", "FlashDump"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.updateFW.setText(_translate("MainWindow", "UpdateFW"))
        self.diagArrText.setPlaceholderText(_translate("MainWindow", "eg:6"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Display"))
        self.openBlight.setText(_translate("MainWindow", "OpenBlight"))
        self.d1129.setText(_translate("MainWindow", "1129"))
        self.d2810.setText(_translate("MainWindow", "2810"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tab_2), _translate("MainWindow", "Options"))
        self.rawdataRead.setText(_translate("MainWindow", "Read"))
        self.radioDC.setText(_translate("MainWindow", "DC"))
        self.radioIIR.setText(_translate("MainWindow", "IIR"))
        self.textEditDiag.setPlaceholderText(_translate("MainWindow", "Type"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.log.setText(_translate("MainWindow", "Log"))
        self.recalled.setText(_translate("MainWindow", "ReL"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Time"))
        self.sram.setText(_translate("MainWindow", "SRAM"))
        self.kmsg.setText(_translate("MainWindow", "Kmsg"))
        self.textEditKmsg.setPlaceholderText(_translate("MainWindow", "HX"))
        self.getevent.setText(_translate("MainWindow", "Gevent"))
        self.textEditGetevent.setPlaceholderText(_translate("MainWindow", "Himax"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tab), _translate("MainWindow", "Rawdata"))
        self.pushButtonRead.setText(_translate("MainWindow", "Read"))
        self.pushButtonRegWrite0.setText(_translate("MainWindow", "Write 0"))
        self.pushButtonRegWrite1.setText(_translate("MainWindow", "Write 1"))
        self.pushButtonRegWrite2.setText(_translate("MainWindow", "Write 2"))
        self.pushButtonRegWrite4.setText(_translate("MainWindow", "Write 4"))
        self.pushButtonRegWrite3.setText(_translate("MainWindow", "Write 3"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.reglength.setItemText(0, _translate("MainWindow", "1"))
        self.reglength.setItemText(1, _translate("MainWindow", "2"))
        self.reglength.setItemText(2, _translate("MainWindow", "3"))
        self.reglength.setItemText(3, _translate("MainWindow", "4"))
        self.reglength.setItemText(4, _translate("MainWindow", "5"))
        self.reglength.setItemText(5, _translate("MainWindow", "6"))
        self.reglength.setItemText(6, _translate("MainWindow", "7"))
        self.reglength.setItemText(7, _translate("MainWindow", "8"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabRWRegister), _translate("MainWindow", "Register"))
        self.DDpushButtonRegWrite0.setText(_translate("MainWindow", "Write 0"))
        self.DDpushButtonRegWrite2.setText(_translate("MainWindow", "Write 2"))
        self.DDRead0.setText(_translate("MainWindow", "Read"))
        self.DDpushButtonRegWrite3.setText(_translate("MainWindow", "Write 3"))
        self.DDpushButtonRegWrite1.setText(_translate("MainWindow", "Write 1"))
        self.DDpushButtonRegWrite4.setText(_translate("MainWindow", "Write 4"))
        self.DDWLineEditAddr0.setPlaceholderText(_translate("MainWindow", "reg"))
        self.DDWLineEditBank0.setPlaceholderText(_translate("MainWindow", "bank"))
        self.DDWLineEditLen0.setPlaceholderText(_translate("MainWindow", "len"))
        self.DDWLineEditVal0.setPlaceholderText(_translate("MainWindow", "value"))
        self.DDRlineEdit0.setPlaceholderText(_translate("MainWindow", "c10008"))
        self.DDRead4.setText(_translate("MainWindow", "Read"))
        self.DDRead1.setText(_translate("MainWindow", "Read"))
        self.DDRead2.setText(_translate("MainWindow", "Read"))
        self.DDRead3.setText(_translate("MainWindow", "Read"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabSwiplines), _translate("MainWindow", "DD"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabAbout), _translate("MainWindow", "About"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabCommands), _translate("MainWindow", "Commands"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabHelp), _translate("MainWindow", "Help"))

    def bindEventFunc(self):
        # wifi
        print("bind start")
        self.wifiConnect.clicked.connect(self.wifiConnectFunc)
        self.wifiDisconnect.clicked.connect(self.wifiDisconnectFunc)
        self.wifiReconnect.clicked.connect(self.wifiReconnectFunc)

        # adb
        self.homekey.clicked.connect(self.homeKeyFunc)
        self.backkey.clicked.connect(self.backKeyFunc)
        self.volUp.clicked.connect(self.volUpFunc)
        self.volDown.clicked.connect(self.volDownFunc)
        self.getprop.clicked.connect(self.getpropFunc)
        self.interrupts.clicked.connect(self.interruptsFunc)
        self.checkDevice.clicked.connect(self.checkDeviceFunc)
        self.hideShowVirtual.clicked.connect(self.hideShowVirtualFunc)
        self.powerKey.clicked.connect(self.powerKeyFunc)
        self.openClosePoint.clicked.connect(self.openClosePointFunc)
        self.screenShot.clicked.connect(self.screenShotFunc)
        self.shutDown.clicked.connect(self.shutDownFunc)
        self.reboot.clicked.connect(self.rebootFunc)

        # touch
        self.fwVersion.clicked.connect(self.touchFWVersionFunc)
        self.reset.clicked.connect(self.touchResetFunc)
        self.senseon.clicked.connect(self.touchSenseOnFunc)
        self.senseoff.clicked.connect(self.touchSenseOffFunc)
        self.selftest.clicked.connect(self.touchSelfTestFunc)
        self.inten0.clicked.connect(self.touchInten0Func)
        self.inten1.clicked.connect(self.touchInten1Func)
        self.driverVersion.clicked.connect(self.touchSwitchDriverVersionFunc)
        self.flashDump.clicked.connect(self.touchFlashDumpFunc)

        # display
        self.d1129.clicked.connect(self.display1129Func)
        self.d2810.clicked.connect(self.display2810Func)
        self.openBlight.clicked.connect(self.touchDiagArrFunc)

        # options
        self.diagArr.clicked.connect(self.touchDiagArrFunc)
        self.updateFW.clicked.connect(self.touchUpdateFWFunc)

        # rawdata show
        self.rawdataRead.clicked.connect(self.rawdataReadFunc)
        self.stop.clicked.connect(self.stopFunc)
        self.sram.clicked.connect(self.sramFunc)
        self.log.clicked.connect(self.logFunc)
        self.kmsg.clicked.connect(self.kmsgFunc)
        self.getevent.clicked.connect(self.geteventFunc)

        # register read write
        self.pushButtonRead.clicked.connect(self.readRegFunc)
        self.pushButtonRegWrite0.clicked.connect(lambda: self.writeRegFunc(0))
        self.pushButtonRegWrite1.clicked.connect(lambda: self.writeRegFunc(1))
        self.pushButtonRegWrite2.clicked.connect(lambda: self.writeRegFunc(2))
        self.pushButtonRegWrite3.clicked.connect(lambda: self.writeRegFunc(3))
        self.pushButtonRegWrite4.clicked.connect(lambda: self.writeRegFunc(4))

        # dd read write register
        self.DDpushButtonRegWrite0.clicked.connect(lambda: self.writeDDRegisterFunc(0))

        # help
        print("bind end")

    def rootFunc(self):
        print("start root")
        ret = adb.shell("adb root")
        if ret == '':
            print("root failed")
            return
        adb.shell("adb remount")
        adb.shell("adb shell setenforce 0")
        adb.shell("adb shell chmod 777 /proc/android_touch/*")
        adb.shell("adb shell chmod 777 /proc/android_touch/diag/*")
        print("execute root, remount, setenforce 0, chmod")
        self.getRXTX()

    def getRXTX(self):
        adb.shell(self.echoDiag % '1', "SHELL")
        ret = adb.shell(self.catDiag, "SHELL")
        if ret == '':
            return
        ret = (' '.join(ret.split()))
        ret = ret[14:20]
        ret = ret.split(', ')
        self.rawdataShowText.append(str(ret))

        if int(ret[0]) != self.rxnum or int(ret[1]) != self.txnum:
            self.rawdataShowText.append("DEFINE_SETTING rx and tx num were not match! please reset file and restart app")

    def showDiag(self):
        width = 25
        height = 15
        self.dialog = QDialog()
        self.dialog.resize(480, 505)
        self.rawdataShowTableWidget = QtWidgets.QTableWidget(self.dialog)
        self.rawdataShowTableWidget.setGeometry(QtCore.QRect(0, 0, 480, 505))
        self.rawdataShowTableWidget.setDisabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.rawdataShowTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rawdataShowTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        sizePolicy.setHeightForWidth(self.rawdataShowTableWidget.sizePolicy().hasHeightForWidth())
        self.rawdataShowTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rawdataShowTableWidget.setSizePolicy(sizePolicy)
        self.rawdataShowTableWidget.setObjectName("rawdataShowTableWidget")
        self.rawdataShowTableWidget.setRowCount(self.rxnum + 1)
        self.rawdataShowTableWidget.setColumnCount(self.txnum + 1)
        self.rawdataShowTableWidget.setObjectName("rawdataShowTableWidget")
        self.rawdataShowTableWidget.verticalHeader().setVisible(False)
        self.rawdataShowTableWidget.horizontalHeader().setVisible(False)
        self.rawdataShowTableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.rawdataShowTableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.rawdataShowTableWidget.verticalHeader().setDefaultSectionSize(10)
        self.rawdataShowTableWidget.verticalHeader().setMinimumSectionSize(10)
        # need setting per col and row
        for i in range(self.txnum + 1):
            self.rawdataShowTableWidget.setColumnWidth(i, width)

        for i in range(self.rxnum + 1):
            self.rawdataShowTableWidget.setRowHeight(i, height)

        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "Show"))
        # self.dialog.setWindowFlags(Qt.FramelessWindowHint)  # set hide menu bar
        self.dialog.exec_()

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

    """ display register read write """
    def readDDRegisterFunc(self, n):
        ret = ""
        if n == 0:
            ret = self.DDRlineEdit0.text()
        elif n == 1:
            ret = self.DDRlineEdit1.text()
        elif n == 2:
            ret = self.DDRlineEdit2.text()
        elif n == 3:
            ret = self.DDRlineEdit3.text()
        elif n == 4:
            ret = self.DDRlineEdit4.text()

        if ret == '':
            self.DDreadRegValShowText.append("you need set value first")
            return
        elif len(ret) != 6:
            self.DDreadRegValShowText.append("value length isn't right")
            return

        # exc read dd register cmd
        val = "AA" + str(ret)
        cmd = self.echoWriteRegister % ("900000FC", val)
        adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)
        # adb.shell(cmd, "SHELL")
        cmd = self.echoReadRegister % "10007F80"
        adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)
        cmd = self.catRegister
        ret = adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(cmd)
        self.DDreadRegValShowText.append(ret)

    def writeDDRegisterFunc(self, n):
        addr = ''
        bank = ''
        length = ''
        val = ''
        if n == 0:
            addr = self.DDWLineEditAddr0.text()
            bank = self.DDWLineEditBank0.text()
            length = self.DDWLineEditLen0.text()
            val = self.DDWLineEditVal0.text()
        elif n == 1:
            addr = self.DDWLineEditAddr1.text()
            bank = self.DDWLineEditBank1.text()
            length = self.DDWLineEditLen1.text()
            val = self.DDWLineEditVal1.text()
        elif n == 2:
            addr = self.DDWLineEditAddr2.text()
            bank = self.DDWLineEditBank2.text()
            length = self.DDWLineEditLen2.text()
            val = self.DDWLineEditVal2.text()
        elif n == 3:
            addr = self.DDWLineEditAddr3.text()
            bank = self.DDWLineEditBank3.text()
            length = self.DDWLineEditLen3.text()
            val = self.DDWLineEditVal3.text()
        elif n == 4:
            addr = self.DDWLineEditAddr4.text()
            bank = self.DDWLineEditBank4.text()
            length = self.DDWLineEditLen4.text()
            val = self.DDWLineEditVal4.text()

        if addr == '' or bank == '' or length == '' or val == '':
            self.DDreadRegValShowText.append("please set value")
            return

        tmpAddr = self.parseInputData(addr)
        tmpBank = self.parseInputData(bank)
        tmpLength = self.parseInputData(length)
        tmpVal = self.parseInputData(val)

        if tmpAddr and tmpBank and tmpLength and tmpVal:
            pass
        else:
            self.DDreadRegValShowText.append("value were not right")
            return

        # first step
        localAddr = '10007f'
        tmp = "AA" + addr + bank + length
        cmd = self.echoWriteRegister % ("900000FC", tmp)
        self.DDreadRegValShowText.append(cmd)
        adb.shell(cmd, "SHELL")
        cmd = self.echoReadRegister % (localAddr + '80')
        self.DDreadRegValShowText.append(cmd)
        adb.shell(cmd, "SHELL")
        cmd = self.catRegister
        self.DDreadRegValShowText.append(cmd)
        ret = adb.shell(cmd, "SHELL")

        if ret == '':
            print("wrong")
            return

        ret = self.parseRegData(ret)
        self.DDreadRegValShowText.append(str(ret))

        # second step
        tmp0 = int(length, 16)
        tmp = tmp0 / 4     # quzheng
        tmp1 = tmp0 % 4    # quyu
        tmp2 = int(tmp) * 4         # qubeishu
        tmp3 = 0x80 + tmp2
        tmp4 = hex(tmp3)
        finalAddr = localAddr + tmp4[2:]
        print(finalAddr)

        # deal write values
        finalVal = ''
        i = 3
        while i >= 0:
            print(ret[tmp2 + i])
            if i == tmp1:
                finalVal += val
            else:
                finalVal += ret[tmp2 + i]
            i = i-1

        cmd = self.echoWriteRegister % (finalAddr, finalVal)
        self.DDreadRegValShowText.append(cmd)
        adb.shell(cmd, "SHELL")
        cmd = self.echoWriteRegister % ('900000FC', 'CC' + addr + bank + length)
        self.DDreadRegValShowText.append(cmd)
        adb.shell(cmd, "SHELL")
        cmd = self.echoReadRegister % (localAddr + '80')
        self.DDreadRegValShowText.append(cmd)
        adb.shell(cmd, "SHELL")
        cmd = self.catRegister
        self.DDreadRegValShowText.append(cmd)
        ret = adb.shell(cmd, "SHELL")
        self.DDreadRegValShowText.append(ret)

    def parseInputData(self, data):
        # 48-57:0-9 / 65-90:A-Z / 97-122:a-z
        flag = 0
        if len(data) != 2:
            return False

        for i in range(len(data)):
            if 48 <= ord(data[i]) <= 57 or 65 <= ord(data[i]) <= 90 or 97 <= ord(data[i]) <= 122:
                flag += 1
            else:
                return False

        if flag == len(data):
            return True

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
        self.d1129.setDisabled(True)
        self.d2810.setDisabled(True)
        self.openBlight.setDisabled(True)
        self.flashDump.setDisabled(True)

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
            print(regInfo)
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

            print(cmd)

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
        print(addr)
        print(val)
        self.writeHistoryFile(addr, val, n)

    def writeRegister(self, regAddress, write_value):
        regAddressList = regAddress.split()

        print(regAddressList)

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

        print("Result:" + regAddress)

        # Deal with value for set as 8 digit
        while len(write_value) < 8 and len(write_value) != 0:
            write_value = "0" + write_value

        if len(regAddress) == 8 and len(write_value) != 0:
            cmd = self.echoWriteRegister % (regAddress, write_value)
            adb.shell(cmd, "SHELL")

    """ rawdata show """
    def rawdataReadFunc(self):
        # choose rawdata type
        if self.radioDC.isChecked():
            adb.shell(self.echoDiag % '2', "SHELL")
        elif self.radioIIR.isChecked():
            adb.shell(self.echoDiag % '1', "SHELL")
        elif self.radioTmp.isChecked():
            type = self.textEditDiag.text()
            if type == '':
                print("value null")
                return
            adb.shell(self.echoDiag % type, "SHELL")
        else:
            string = "Please set diag type!"
            self.dialogWin(string)
            return

        self.rawdataRead.setText("Ing..")
        self.rawdataRead.setStyleSheet("color: rgb(255, 0, 0);background-color: rgb(255, 170, 127);")
        self.rawdataRead.setDisabled(True)

        self.radioDC.setDisabled(True)
        self.radioIIR.setDisabled(True)
        self.radioTmp.setDisabled(True)
        self.textEditDiag.setDisabled(True)

        # cat diag
        self.readRawdataThread = Thread(target=self.showRawdata)
        self.readRawdataThread.start()

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

    def stopFunc(self):
        self.showRawdataFlag = 0
        self.showKmsgFlag = 0
        self.showGeteventFlag = 0

        if self.logFlag:
            self.logFile.close()

        self.radioDC.setDisabled(False)
        self.radioIIR.setDisabled(False)
        self.radioTmp.setDisabled(False)
        self.textEditDiag.setDisabled(False)

        self.kmsg.setDisabled(False)
        self.getevent.setDisabled(False)

        self.logFlag = False
        self.log.setDisabled(False)
        self.log.setText("Log")
        self.log.setStyleSheet("color: rgb(0, 0, 0)")

        self.rawdataRead.setText("Read")
        self.rawdataRead.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(170, 255, 127);")
        self.rawdataRead.setDisabled(False)

        adb.shell(self.echoDiag % '0', "SHELL")

    def sramFunc(self):
        self.showDiag()

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
        self.log.setText("Logging")
        self.log.setStyleSheet("color: rgb(255, 0, 0)")

    def kmsgFunc(self):
        self.kmsgThread = Thread(target=self.getKmsg)
        self.kmsgThread.start()

    def getKmsg(self):
        self.showKmsgFlag = 1
        self.kmsg.setDisabled(True)
        arg = self.textEditKmsg.text()
        cmd = 'adb shell "cat dev/kmsg | grep %s"' % arg
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        while self.showKmsgFlag:
            l = p.stdout.readline()
            if not l:
                break
            l = l[:len(l) - 1]
            #self.rawdataShowText.append(l)
            print(l)

    def geteventFunc(self):
        self.geteventThread = Thread(target=self.getEvent)
        self.geteventThread.start()

    def getEvent(self):
        self.showGeteventFlag = 1
        self.getevent.setDisabled(True)
        cmd = 'adb shell "getevent -lr"'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        while self.showGeteventFlag:
            l = p.stdout.readline()
            if not l:
                break
            l = l[:len(l) - 1]
            #self.rawdataShowText.append(l)
            print(l)

    """ touch """
    def initPath(self):
        # common path
        self.debugPath = ''
        self.selfTestPath = ''
        self.hxFolderPath = ''
        self.flashDumpPath = ''
        self.fwPath = ''

        # common vars
        self.historyValue = []
        self.BT_ID = []
        self.defineFile = './settings/DEFINE_SETTING'
        self.historyFile = './settings/HISTORY'
        self.pathCode = [
            "V1_REG_PATH",
            "V1_DIAG_PATH",
            "V1_INT_EN_PATH",
            "V1_RESET_PATH",
            "V1_SENSEONOFF_PATH",
            "V1_DIAGARR_PATH",

            "V2_BANKS_PATH",
            "V2_DCS_PATH",
            "V2_IIRS_PATH",
            "V2_STACK_PATH",

            "DEBUG_PATH",
            "SELFTEST_PATH",
            "FLASH_DUMP_PATH",
            "HX_FOLDER_PATH",
            "FW_PATH",

            "PORT_NUM",
            "RX",
            "TX"]

        # common v1 path
        self.v1DiagPath = ''
        self.v1RegisterPath = ''
        self.v1IntEnPath = ''
        self.v1ResetPath = ''
        self.v1SenseOnOffPath = ''
        self.v1DiagArrPath = ''

        # common v2 path
        self.v2ReadStackPath = ''

        self.driverVersionMode = 2

        self.setDriverNodePath(self.driverVersionMode)

    def setDriverNodePath(self, mode):
        if mode == 1:
            self.driverVersionMode = 1
        elif mode == 2:
            self.driverVersionMode = 2

        with open(self.defineFile, 'rb') as r:
            for line in r.readlines():
                line = str(line, encoding='UTF-8')
                if line.find('#') >= 0:
                    continue
                l = line.split()
                l = (''.join(l))
                l = l.split('=')

                # get rx tx num
                if l[0] == 'RX':
                    self.rxnum = int(l[1])
                elif l[0] == 'TX':
                    self.txnum = int(l[1])

                if len(l) >= 2:
                    if l[0] in self.pathCode:
                        path = l[1]
                        if path[0] != '/':
                            path = '/' + path
                        if path[-1] == '/':
                            path = path[:-1]
                        # Assign path
                        # common
                        if l[0] == "DEBUG_PATH":
                            self.debugPath = path
                        elif l[0] == 'SELFTEST_PATH':
                            self.selfTestPath = path
                        elif l[0] == 'FLASH_DUMP_PATH':
                            self.flashDumpPath = path
                        elif l[0] == 'HX_FOLDER_PATH':
                            self.hxFolderPath = path
                        elif l[0] == 'FW_PATH':
                            self.fwPath = path

                        # v1 or v2
                        if self.driverVersionMode == 1:
                            if l[0] == "V1_REG_PATH":
                                self.v1RegisterPath = path
                            elif l[0] == "V1_DIAG_PATH":
                                self.v1DiagPath = path
                            elif l[0] == 'V1_INT_EN_PATH':
                                self.v1IntEnPath = path
                            elif l[0] == 'V1_RESET_PATH':
                                self.v1ResetPath = path
                            elif l[0] == 'V1_SENSEONOFF_PATH':
                                self.v1SenseOnOffPath = path
                            elif l[0] == 'V1_DIAGARR_PATH':
                                self.v1DiagArrPath = path

                        elif self.driverVersionMode == 2:
                            if l[0] == "V2_STACK_PATH":
                                self.v2ReadStackPath = path
                        else:
                            print("please check the DEFINE_SETTING file")
                            return

        if self.driverVersionMode == 1:
            self.echoDiag = "echo %s > " + self.v1DiagPath
            self.catDiag = "cat " + self.v1DiagPath

            self.echoWriteRegister = "echo w:x%s:x%s > " + self.v1RegisterPath
            self.echoReadRegister = "echo r:x%s > " + self.v1RegisterPath
            self.catRegister = "cat " + self.v1RegisterPath

            self.echoIntEn = "echo %s > " + self.v1IntEnPath
            self.echoReset = "echo %s > " + self.v1ResetPath

            self.echoSenseOn = "echo 1 > " + self.v1SenseOnOffPath
            self.echoSenseOff = "echo 0 > " + self.v1SenseOnOffPath
        elif self.driverVersionMode == 2:
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
        adb.shell(self.echoSenseOn, "SHELL")
        self.rawdataShowText.append(self.echoSenseOn)

    def touchSenseOffFunc(self):
        adb.shell(self.echoSenseOff, "SHELL")
        self.rawdataShowText.append(self.echoSenseOff)

    def touchSelfTestFunc(self):
        self.selftestThread = Thread(target=self.selftestThreadFunc)
        self.selftestThread.start()

    def selftestThreadFunc(self):
        ret = adb.shell(self.catSelfTest, "SHELL")
        self.rawdataShowText.append(ret)

    def touchFWVersionFunc(self):
        adb.shell(self.echoFWVersion % "v", "SHELL")
        ret = adb.shell(self.catFWVersion, "SHELL")
        # ret = str(ret, encoding='utf-8')
        self.rawdataShowText.append(ret)

    def touchResetFunc(self):
        adb.shell(self.echoReset % "1", "SHELL")
        self.rawdataShowText.append(self.echoReset % "1")

    def touchInten0Func(self):
        adb.shell(self.echoIntEn % "0", "SHELL")
        self.rawdataShowText.append("disable irq")

    def touchInten1Func(self):
        adb.shell(self.echoIntEn % "1", "SHELL")
        self.rawdataShowText.append("enable irq")

    def touchSwitchDriverVersionFunc(self):
        if self.driverVersion.text() == "V2":
            self.driverVersion.setText("V1")
            self.setDriverNodePath(1)
            self.rawdataShowText.append("use v1 driver\n")
        else:
            self.driverVersion.setText("V2")
            self.setDriverNodePath(2)
            self.rawdataShowText.append("use v2 driver\n")

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

    """ display """
    def display1129Func(self):
        print("1129")
        if self.driverVersion == 1:
            adb.shell("echo w:x30011000 > " + self.v1RegisterPath, "SHELL")
            adb.shell("sleep 1", "SHELL")
            adb.shell("echo w:x30029000 > " + self.v1RegisterPath, "SHELL")
        elif self.driverVersion == 2:
            adb.shell("echo register,w:x30011000 > " + self.debugPath, "SHELL")
            adb.shell("sleep 1", "SHELL")
            adb.shell("echo register,w:x30029000 > " + self.debugPath, "SHELL")

    def display2810Func(self):
        print("2810")
        if self.driverVersion == 1:
            adb.shell("echo w:x30028000 > " + self.v1RegisterPath, "SHELL")
            adb.shell("sleep 1", "SHELL")
            adb.shell("echo w:x30010000 > " + self.v1RegisterPath, "SHELL")
        elif self.driverVersion == 2:
            adb.shell("echo register,w:x30028000 > " + self.debugPath, "SHELL")
            adb.shell("sleep 1", "SHELL")
            adb.shell("echo register,w:x30010000 > " + self.debugPath, "SHELL")

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
            print("Please connect device")
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
            # response = str(response, encoding='utf-8')
            print(response)
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

    def getpropFunc(self):
        cmd = "adb shell getprop"
        ret = adb.shell(cmd)
        self.rawdataShowText.append(cmd)
        self.rawdataShowText.append(ret)

    def interruptsFunc(self):
        cmd = "adb shell cat /proc/interrupts"
        ret = adb.shell(cmd)
        self.rawdataShowText.append(cmd)
        self.rawdataShowText.append(ret)

    def checkDeviceFunc(self):
        ret = adb.shell("adb devices")
        self.rawdataShowText.append(ret)

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

    def pullHXFileFunc(self):
        print("will be add")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
