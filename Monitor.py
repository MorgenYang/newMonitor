from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import adb
from threading import Thread
import time
import subprocess

PORT = 8888


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bindEventFunc()

        self.uiThreadRoot = Thread(target=self.ui.rootFunc)
        self.uiThreadInitPath = Thread(target=self.ui.initPath)
        self.uiThreadInitHistory = Thread(target=self.ui.initHistoryFunc)
        self.uiThreadRoot.start()
        self.uiThreadInitPath.start()
        self.uiThreadInitHistory.start()
        self.statusBar().addWidget(QLabel("Ready"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(737, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 111, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(5, 3, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LeftMainWindow = QtWidgets.QToolBox(self.verticalLayoutWidget)
        self.LeftMainWindow.setMaximumSize(QtCore.QSize(100, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LeftMainWindow.setFont(font)
        self.LeftMainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LeftMainWindow.setStyleSheet("background-color: rgb(85, 170, 127); color: rgb(255, 255, 255);")
        self.LeftMainWindow.setObjectName("LeftMainWindow")
        self.pageWifi = QtWidgets.QWidget()
        self.pageWifi.setGeometry(QtCore.QRect(0, 0, 100, 352))
        self.pageWifi.setStyleSheet("background-color: rgb(202, 204, 183);")
        self.pageWifi.setObjectName("pageWifi")
        self.wifiConnect = QtWidgets.QPushButton(self.pageWifi)
        self.wifiConnect.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.wifiConnect.setMaximumSize(QtCore.QSize(100, 25))
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiConnect.setObjectName("wifiConnect")
        self.wifiDisconnect = QtWidgets.QPushButton(self.pageWifi)
        self.wifiDisconnect.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.wifiDisconnect.setMaximumSize(QtCore.QSize(100, 25))
        self.wifiDisconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiDisconnect.setCheckable(False)
        self.wifiDisconnect.setObjectName("wifiDisconnect")
        self.wifiReconnect = QtWidgets.QPushButton(self.pageWifi)
        self.wifiReconnect.setGeometry(QtCore.QRect(0, 50, 100, 25))
        self.wifiReconnect.setMaximumSize(QtCore.QSize(100, 25))
        self.wifiReconnect.setStyleSheet("color: rgb(0, 0, 0);")
        self.wifiReconnect.setCheckable(False)
        self.wifiReconnect.setObjectName("wifiReconnect")
        self.wifiStatus = QtWidgets.QLabel(self.pageWifi)
        self.wifiStatus.setGeometry(QtCore.QRect(0, 80, 100, 25))
        self.wifiStatus.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wifiStatus.setFont(font)
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.wifiStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.wifiStatus.setWordWrap(False)
        self.wifiStatus.setObjectName("wifiStatus")
        self.LeftMainWindow.addItem(self.pageWifi, "")
        self.pageAdb = QtWidgets.QWidget()
        self.pageAdb.setGeometry(QtCore.QRect(0, 0, 100, 352))
        self.pageAdb.setStyleSheet("background-color: rgb(202, 204, 183);")
        self.pageAdb.setObjectName("pageAdb")
        self.homekey = QtWidgets.QPushButton(self.pageAdb)
        self.homekey.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.homekey.setMinimumSize(QtCore.QSize(100, 25))
        self.homekey.setMaximumSize(QtCore.QSize(100, 25))
        self.homekey.setStyleSheet("color: rgb(0, 0, 0);")
        self.homekey.setObjectName("homekey")
        self.backkey = QtWidgets.QPushButton(self.pageAdb)
        self.backkey.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.backkey.setMaximumSize(QtCore.QSize(100, 25))
        self.backkey.setStyleSheet("color: rgb(0, 0, 0);")
        self.backkey.setObjectName("backkey")
        self.volUp = QtWidgets.QPushButton(self.pageAdb)
        self.volUp.setGeometry(QtCore.QRect(0, 50, 100, 25))
        self.volUp.setMaximumSize(QtCore.QSize(100, 25))
        self.volUp.setStyleSheet("color: rgb(0, 0, 0);")
        self.volUp.setObjectName("volUp")
        self.volDown = QtWidgets.QPushButton(self.pageAdb)
        self.volDown.setGeometry(QtCore.QRect(0, 75, 100, 25))
        self.volDown.setMaximumSize(QtCore.QSize(100, 25))
        self.volDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.volDown.setObjectName("volDown")
        self.getprop = QtWidgets.QPushButton(self.pageAdb)
        self.getprop.setGeometry(QtCore.QRect(0, 100, 100, 25))
        self.getprop.setMaximumSize(QtCore.QSize(100, 25))
        self.getprop.setStyleSheet("color: rgb(0, 0, 0);")
        self.getprop.setObjectName("getprop")
        self.interrupts = QtWidgets.QPushButton(self.pageAdb)
        self.interrupts.setGeometry(QtCore.QRect(0, 125, 100, 25))
        self.interrupts.setMaximumSize(QtCore.QSize(100, 25))
        self.interrupts.setStyleSheet("color: rgb(0, 0, 0);")
        self.interrupts.setObjectName("interrupts")
        self.checkDevice = QtWidgets.QPushButton(self.pageAdb)
        self.checkDevice.setGeometry(QtCore.QRect(0, 150, 100, 25))
        self.checkDevice.setMaximumSize(QtCore.QSize(100, 25))
        self.checkDevice.setStyleSheet("color: rgb(0, 0, 0);")
        self.checkDevice.setObjectName("checkDevice")
        self.hideShowVirtual = QtWidgets.QPushButton(self.pageAdb)
        self.hideShowVirtual.setGeometry(QtCore.QRect(0, 175, 100, 25))
        self.hideShowVirtual.setMaximumSize(QtCore.QSize(100, 25))
        self.hideShowVirtual.setStyleSheet("color: rgb(0, 0, 0);")
        self.hideShowVirtual.setObjectName("hideShowVirtual")
        self.powerKey = QtWidgets.QPushButton(self.pageAdb)
        self.powerKey.setGeometry(QtCore.QRect(0, 200, 100, 25))
        self.powerKey.setMaximumSize(QtCore.QSize(100, 25))
        self.powerKey.setStyleSheet("color: rgb(0, 0, 0);")
        self.powerKey.setObjectName("powerKey")
        self.openClosePoint = QtWidgets.QPushButton(self.pageAdb)
        self.openClosePoint.setGeometry(QtCore.QRect(0, 225, 100, 25))
        self.openClosePoint.setMaximumSize(QtCore.QSize(100, 25))
        self.openClosePoint.setStyleSheet("color: rgb(0, 0, 0);")
        self.openClosePoint.setObjectName("openClosePoint")
        self.screenShot = QtWidgets.QPushButton(self.pageAdb)
        self.screenShot.setGeometry(QtCore.QRect(0, 250, 100, 25))
        self.screenShot.setMaximumSize(QtCore.QSize(100, 25))
        self.screenShot.setStyleSheet("color: rgb(0, 0, 0);")
        self.screenShot.setObjectName("screenShot")
        self.shutDown = QtWidgets.QPushButton(self.pageAdb)
        self.shutDown.setGeometry(QtCore.QRect(0, 275, 100, 25))
        self.shutDown.setMaximumSize(QtCore.QSize(100, 25))
        self.shutDown.setStyleSheet("color: rgb(0, 0, 0);")
        self.shutDown.setObjectName("shutDown")
        self.reboot = QtWidgets.QPushButton(self.pageAdb)
        self.reboot.setGeometry(QtCore.QRect(0, 300, 100, 25))
        self.reboot.setMaximumSize(QtCore.QSize(100, 25))
        self.reboot.setStyleSheet("color: rgb(0, 0, 0);")
        self.reboot.setObjectName("reboot")
        self.pullHXFile = QtWidgets.QPushButton(self.pageAdb)
        self.pullHXFile.setGeometry(QtCore.QRect(0, 325, 100, 25))
        self.pullHXFile.setMaximumSize(QtCore.QSize(100, 25))
        self.pullHXFile.setStyleSheet("color: rgb(0, 0, 0);")
        self.pullHXFile.setObjectName("pullHXFile")
        self.LeftMainWindow.addItem(self.pageAdb, "")
        self.pageTouch = QtWidgets.QWidget()
        self.pageTouch.setGeometry(QtCore.QRect(0, 0, 100, 352))
        self.pageTouch.setStyleSheet("background-color: rgb(202, 204, 183);")
        self.pageTouch.setObjectName("pageTouch")
        self.fwVersion = QtWidgets.QPushButton(self.pageTouch)
        self.fwVersion.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.fwVersion.setMaximumSize(QtCore.QSize(100, 25))
        self.fwVersion.setStyleSheet("color: rgb(0, 0, 0);")
        self.fwVersion.setObjectName("fwVersion")
        self.reset = QtWidgets.QPushButton(self.pageTouch)
        self.reset.setGeometry(QtCore.QRect(0, 30, 100, 25))
        self.reset.setMaximumSize(QtCore.QSize(100, 25))
        self.reset.setStyleSheet("color: rgb(0, 0, 0);")
        self.reset.setObjectName("reset")
        self.senseon = QtWidgets.QPushButton(self.pageTouch)
        self.senseon.setGeometry(QtCore.QRect(0, 60, 100, 25))
        self.senseon.setMaximumSize(QtCore.QSize(100, 25))
        self.senseon.setStyleSheet("color: rgb(0, 0, 0);")
        self.senseon.setObjectName("senseon")
        self.senseoff = QtWidgets.QPushButton(self.pageTouch)
        self.senseoff.setGeometry(QtCore.QRect(0, 90, 100, 25))
        self.senseoff.setMaximumSize(QtCore.QSize(100, 25))
        self.senseoff.setStyleSheet("color: rgb(0, 0, 0);")
        self.senseoff.setObjectName("senseoff")
        self.selftest = QtWidgets.QPushButton(self.pageTouch)
        self.selftest.setGeometry(QtCore.QRect(0, 120, 100, 25))
        self.selftest.setMaximumSize(QtCore.QSize(100, 25))
        self.selftest.setStyleSheet("color: rgb(0, 0, 0);")
        self.selftest.setObjectName("selftest")
        self.inten0 = QtWidgets.QPushButton(self.pageTouch)
        self.inten0.setGeometry(QtCore.QRect(0, 150, 100, 25))
        self.inten0.setMaximumSize(QtCore.QSize(100, 25))
        self.inten0.setStyleSheet("color: rgb(0, 0, 0);")
        self.inten0.setObjectName("inten0")
        self.inten1 = QtWidgets.QPushButton(self.pageTouch)
        self.inten1.setGeometry(QtCore.QRect(0, 180, 100, 25))
        self.inten1.setMaximumSize(QtCore.QSize(100, 25))
        self.inten1.setStyleSheet("color: rgb(0, 0, 0);")
        self.inten1.setObjectName("inten1")
        self.driverVersion = QtWidgets.QPushButton(self.pageTouch)
        self.driverVersion.setGeometry(QtCore.QRect(0, 210, 100, 25))
        self.driverVersion.setMaximumSize(QtCore.QSize(100, 25))
        self.driverVersion.setStyleSheet("color: rgb(0, 0, 0);")
        self.driverVersion.setObjectName("driverVersion")
        self.flashDump = QtWidgets.QPushButton(self.pageTouch)
        self.flashDump.setGeometry(QtCore.QRect(0, 240, 100, 25))
        self.flashDump.setMaximumSize(QtCore.QSize(100, 25))
        self.flashDump.setStyleSheet("color: rgb(0, 0, 0);")
        self.flashDump.setObjectName("flashDump")
        self.LeftMainWindow.addItem(self.pageTouch, "")
        self.pageDisplay = QtWidgets.QWidget()
        self.pageDisplay.setGeometry(QtCore.QRect(0, 0, 100, 352))
        self.pageDisplay.setStyleSheet("background-color: rgb(202, 204, 183);")
        self.pageDisplay.setObjectName("pageDisplay")
        self.d1129 = QtWidgets.QPushButton(self.pageDisplay)
        self.d1129.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.d1129.setMaximumSize(QtCore.QSize(100, 25))
        self.d1129.setStyleSheet("color: rgb(0, 0, 0);")
        self.d1129.setObjectName("d1129")
        self.d2810 = QtWidgets.QPushButton(self.pageDisplay)
        self.d2810.setGeometry(QtCore.QRect(0, 30, 100, 25))
        self.d2810.setMaximumSize(QtCore.QSize(100, 25))
        self.d2810.setStyleSheet("color: rgb(0, 0, 0);")
        self.d2810.setObjectName("d2810")
        self.openBlight = QtWidgets.QPushButton(self.pageDisplay)
        self.openBlight.setGeometry(QtCore.QRect(0, 60, 100, 25))
        self.openBlight.setMaximumSize(QtCore.QSize(100, 25))
        self.openBlight.setStyleSheet("color: rgb(0, 0, 0);")
        self.openBlight.setObjectName("openBlight")
        self.LeftMainWindow.addItem(self.pageDisplay, "")
        self.pageOptions = QtWidgets.QWidget()
        self.pageOptions.setGeometry(QtCore.QRect(0, 0, 100, 352))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pageOptions.setFont(font)
        self.pageOptions.setStyleSheet("background-color: rgb(202, 204, 183);")
        self.pageOptions.setObjectName("pageOptions")
        self.diagArrText = QtWidgets.QTextEdit(self.pageOptions)
        self.diagArrText.setGeometry(QtCore.QRect(0, 30, 99, 30))
        self.diagArrText.setMaximumSize(QtCore.QSize(100, 30))
        self.diagArrText.setStyleSheet("color: rgb(0, 0, 0);")
        self.diagArrText.setObjectName("diagArrText")
        self.updateFWText = QtWidgets.QTextEdit(self.pageOptions)
        self.updateFWText.setGeometry(QtCore.QRect(0, 120, 99, 30))
        self.updateFWText.setMaximumSize(QtCore.QSize(100, 30))
        self.updateFWText.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFWText.setObjectName("updateFWText")
        self.diagArr = QtWidgets.QPushButton(self.pageOptions)
        self.diagArr.setGeometry(QtCore.QRect(0, 0, 100, 25))
        self.diagArr.setMaximumSize(QtCore.QSize(100, 25))
        self.diagArr.setStyleSheet("color: rgb(0, 0, 0);")
        self.diagArr.setObjectName("diagArr")
        self.updateFW = QtWidgets.QPushButton(self.pageOptions)
        self.updateFW.setGeometry(QtCore.QRect(0, 90, 100, 25))
        self.updateFW.setMaximumSize(QtCore.QSize(100, 25))
        self.updateFW.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateFW.setObjectName("updateFW")
        self.LeftMainWindow.addItem(self.pageOptions, "")
        self.verticalLayout.addWidget(self.LeftMainWindow)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 0, 621, 471))
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
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.rawdataShowText = QtWidgets.QTextBrowser(self.tab)
        self.rawdataShowText.setGeometry(QtCore.QRect(0, 35, 611, 401))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 611, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rawdataRead = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
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
        self.horizontalLayout_2.addWidget(self.rawdataRead)
        self.radioDC = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioDC.setMaximumSize(QtCore.QSize(50, 30))
        self.radioDC.setObjectName("radioDC")
        self.horizontalLayout_2.addWidget(self.radioDC)
        self.radioIIR = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioIIR.setMaximumSize(QtCore.QSize(50, 30))
        self.radioIIR.setObjectName("radioIIR")
        self.horizontalLayout_2.addWidget(self.radioIIR)
        self.radioTmp = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioTmp.setMaximumSize(QtCore.QSize(15, 30))
        self.radioTmp.setText("")
        self.radioTmp.setObjectName("radioTmp")
        self.horizontalLayout_2.addWidget(self.radioTmp)
        self.textEditDiag = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEditDiag.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditDiag.setObjectName("textEditDiag")
        self.horizontalLayout_2.addWidget(self.textEditDiag)
        self.stop = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.stop.setMaximumSize(QtCore.QSize(70, 30))
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.log = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.log.setMaximumSize(QtCore.QSize(70, 30))
        self.log.setObjectName("log")
        self.horizontalLayout_2.addWidget(self.log)
        self.sram = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.sram.setMaximumSize(QtCore.QSize(70, 30))
        self.sram.setObjectName("sram")
        self.horizontalLayout_2.addWidget(self.sram)
        self.recalled = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.recalled.setMaximumSize(QtCore.QSize(100, 30))
        self.recalled.setObjectName("recalled")
        self.horizontalLayout_2.addWidget(self.recalled)
        self.kmsg = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.kmsg.setMaximumSize(QtCore.QSize(70, 30))
        self.kmsg.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.kmsg.setObjectName("kmsg")
        self.horizontalLayout_2.addWidget(self.kmsg)
        self.textEditKmsg = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEditKmsg.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditKmsg.setObjectName("textEditKmsg")
        self.horizontalLayout_2.addWidget(self.textEditKmsg)
        self.getevent = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.getevent.setMinimumSize(QtCore.QSize(0, 0))
        self.getevent.setMaximumSize(QtCore.QSize(70, 30))
        self.getevent.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.getevent.setObjectName("getevent")
        self.horizontalLayout_2.addWidget(self.getevent)
        self.textEditGetevent = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEditGetevent.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditGetevent.setObjectName("textEditGetevent")
        self.horizontalLayout_2.addWidget(self.textEditGetevent)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TabMainWindow.addTab(self.tab, "")
        self.TabRWRegister = QtWidgets.QWidget()
        self.TabRWRegister.setObjectName("TabRWRegister")
        self.pushButtonRead = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRead.setGeometry(QtCore.QRect(0, 5, 100, 30))
        self.pushButtonRead.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRead.setObjectName("pushButtonRead")
        self.textEditReadRegAddr = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditReadRegAddr.setGeometry(QtCore.QRect(0, 40, 100, 101))
        self.textEditReadRegAddr.setMaximumSize(QtCore.QSize(150, 170))
        self.textEditReadRegAddr.setObjectName("textEditReadRegAddr")
        self.textEditWriteVal3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal3.setGeometry(QtCore.QRect(350, 110, 120, 30))
        self.textEditWriteVal3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal3.setObjectName("textEditWriteVal3")
        self.textEditWriteVal4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal4.setGeometry(QtCore.QRect(350, 145, 120, 30))
        self.textEditWriteVal4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal4.setObjectName("textEditWriteVal4")
        self.textEditWriteVal2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal2.setGeometry(QtCore.QRect(350, 75, 120, 30))
        self.textEditWriteVal2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal2.setObjectName("textEditWriteVal2")
        self.textEditWriteAddr1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr1.setGeometry(QtCore.QRect(220, 40, 120, 30))
        self.textEditWriteAddr1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr1.setObjectName("textEditWriteAddr1")
        self.textEditWriteAddr2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr2.setGeometry(QtCore.QRect(220, 75, 120, 30))
        self.textEditWriteAddr2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr2.setObjectName("textEditWriteAddr2")
        self.textEditWriteAddr0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr0.setGeometry(QtCore.QRect(220, 5, 120, 30))
        self.textEditWriteAddr0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr0.setObjectName("textEditWriteAddr0")
        self.textEditWriteVal1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal1.setGeometry(QtCore.QRect(350, 40, 120, 30))
        self.textEditWriteVal1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal1.setObjectName("textEditWriteVal1")
        self.pushButtonRegWrite0 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite0.setGeometry(QtCore.QRect(110, 5, 100, 30))
        self.pushButtonRegWrite0.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite0.setObjectName("pushButtonRegWrite0")
        self.pushButtonRegWrite1 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite1.setGeometry(QtCore.QRect(110, 40, 100, 30))
        self.pushButtonRegWrite1.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite1.setObjectName("pushButtonRegWrite1")
        self.textEditWriteVal0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal0.setGeometry(QtCore.QRect(350, 5, 120, 30))
        self.textEditWriteVal0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal0.setObjectName("textEditWriteVal0")
        self.textEditWriteAddr3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr3.setGeometry(QtCore.QRect(220, 110, 120, 30))
        self.textEditWriteAddr3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr3.setObjectName("textEditWriteAddr3")
        self.pushButtonRegWrite2 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite2.setGeometry(QtCore.QRect(110, 75, 100, 30))
        self.pushButtonRegWrite2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite2.setObjectName("pushButtonRegWrite2")
        self.textEditWriteAddr4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr4.setGeometry(QtCore.QRect(220, 145, 120, 30))
        self.textEditWriteAddr4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr4.setObjectName("textEditWriteAddr4")
        self.pushButtonRegWrite4 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite4.setGeometry(QtCore.QRect(110, 145, 100, 30))
        self.pushButtonRegWrite4.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite4.setObjectName("pushButtonRegWrite4")
        self.pushButtonRegWrite3 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite3.setGeometry(QtCore.QRect(110, 110, 100, 30))
        self.pushButtonRegWrite3.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite3.setObjectName("pushButtonRegWrite3")
        self.label = QtWidgets.QLabel(self.TabRWRegister)
        self.label.setGeometry(QtCore.QRect(5, 150, 50, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.reglength = QtWidgets.QComboBox(self.TabRWRegister)
        self.reglength.setGeometry(QtCore.QRect(70, 150, 30, 22))
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
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 180, 581, 241))
        self.readRegValShowText.setObjectName("readRegValShowText")
        self.TabMainWindow.addTab(self.TabRWRegister, "")
        self.TabSwiplines = QtWidgets.QWidget()
        self.TabSwiplines.setObjectName("TabSwiplines")
        self.TabMainWindow.addTab(self.TabSwiplines, "")
        self.TabHelp = QtWidgets.QWidget()
        self.TabHelp.setObjectName("TabHelp")
        self.TabHelpSubMain = QtWidgets.QTabWidget(self.TabHelp)
        self.TabHelpSubMain.setGeometry(QtCore.QRect(0, 0, 801, 461))
        self.TabHelpSubMain.setObjectName("TabHelpSubMain")
        self.TabAbout = QtWidgets.QWidget()
        self.TabAbout.setObjectName("TabAbout")
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
        self.LeftMainWindow.setCurrentIndex(0)
        self.LeftMainWindow.layout().setSpacing(0)
        self.TabMainWindow.setCurrentIndex(0)
        self.TabHelpSubMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADB Monitor 2.0.0"))
        self.wifiConnect.setText(_translate("MainWindow", "WiFi Connect"))
        self.wifiDisconnect.setText(_translate("MainWindow", "WiFi disconnect"))
        self.wifiReconnect.setText(_translate("MainWindow", "Reconnect"))
        self.wifiStatus.setText(_translate("MainWindow", "WiFi Status"))
        self.LeftMainWindow.setItemText(self.LeftMainWindow.indexOf(self.pageWifi), _translate("MainWindow", "WIFI"))
        self.homekey.setText(_translate("MainWindow", "Home"))
        self.backkey.setText(_translate("MainWindow", "Back"))
        self.volUp.setText(_translate("MainWindow", "Vol up"))
        self.volDown.setText(_translate("MainWindow", "Vol down"))
        self.getprop.setText(_translate("MainWindow", "Getprop"))
        self.interrupts.setText(_translate("MainWindow", "Interrupts"))
        self.checkDevice.setText(_translate("MainWindow", "CheckDevices"))
        self.hideShowVirtual.setText(_translate("MainWindow", "ShowVirtual"))
        self.powerKey.setText(_translate("MainWindow", "PowerKey"))
        self.openClosePoint.setText(_translate("MainWindow", "OpenPoint"))
        self.screenShot.setText(_translate("MainWindow", "ScreenShot"))
        self.shutDown.setText(_translate("MainWindow", "ShutDown"))
        self.reboot.setText(_translate("MainWindow", "Reboot"))
        self.pullHXFile.setText(_translate("MainWindow", "PullHXFile"))
        self.LeftMainWindow.setItemText(self.LeftMainWindow.indexOf(self.pageAdb), _translate("MainWindow", "ADB"))
        self.fwVersion.setText(_translate("MainWindow", "FWVersion"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.senseon.setText(_translate("MainWindow", "SenseOn"))
        self.senseoff.setText(_translate("MainWindow", "SenseOff"))
        self.selftest.setText(_translate("MainWindow", "SelfTest"))
        self.inten0.setText(_translate("MainWindow", "Int_en_0"))
        self.inten1.setText(_translate("MainWindow", "Int_en_1"))
        self.driverVersion.setText(_translate("MainWindow", "V2"))
        self.flashDump.setText(_translate("MainWindow", "FlashDump"))
        self.LeftMainWindow.setItemText(self.LeftMainWindow.indexOf(self.pageTouch), _translate("MainWindow", "Touch"))
        self.d1129.setText(_translate("MainWindow", "1129"))
        self.d2810.setText(_translate("MainWindow", "2810"))
        self.openBlight.setText(_translate("MainWindow", "OpenBlight"))
        self.LeftMainWindow.setItemText(self.LeftMainWindow.indexOf(self.pageDisplay), _translate("MainWindow", "Display"))
        self.diagArr.setText(_translate("MainWindow", "DiagArr"))
        self.updateFW.setText(_translate("MainWindow", "UpdateFW"))
        self.LeftMainWindow.setItemText(self.LeftMainWindow.indexOf(self.pageOptions), _translate("MainWindow", "Options"))
        self.rawdataRead.setText(_translate("MainWindow", "Read"))
        self.radioDC.setText(_translate("MainWindow", "DC"))
        self.radioIIR.setText(_translate("MainWindow", "IIR"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.log.setText(_translate("MainWindow", "Log"))
        self.sram.setText(_translate("MainWindow", "SRAM"))
        self.recalled.setText(_translate("MainWindow", "Recall"))
        self.kmsg.setText(_translate("MainWindow", "Kmsg"))
        self.getevent.setText(_translate("MainWindow", "Gevent"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tab), _translate("MainWindow", "Rawdata log"))
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
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabRWRegister), _translate("MainWindow", "R/W register"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabSwiplines), _translate("MainWindow", "Swipe"))
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
        self.pullHXFile.clicked.connect(self.pullHXFileFunc)

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

        # swipe lines
        # help
        print("bind end")

    def rootFunc(self):
        print("start root")
        adb.shell("adb root")
        adb.shell("adb remount")
        adb.shell("adb shell setenforce 0")
        adb.shell("adb shell chmod 777 /proc/android_touch/*")
        adb.shell("adb shell chmod 777 /proc/android_touch/diag/*")
        print("execute root, remount, setenforce 0, chmod")

    def getRawdataLogFunc(self):
        pass

    # register read write
    def initHistoryFunc(self):
        self.textEditKmsg.append("HX")
        self.sram.setDisabled(True)
        self.d1129.setDisabled(True)
        self.d2810.setDisabled(True)
        self.openBlight.setDisabled(True)
        self.flashDump.setDisabled(True)
        self.pullHXFile.setDisabled(True)

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
        addr = self.textEditWriteAddr0.toPlainText()
        val = self.textEditWriteVal0.toPlainText()
        if addr == '' or val == '':
            return
        self.writeRegister(addr, val)
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

    # rawdata show
    def rawdataReadFunc(self):
        # choose rawdata type
        if self.radioDC.isChecked():
            adb.shell(self.echoDiag % '2', "SHELL")
        elif self.radioIIR.isChecked():
            adb.shell(self.echoDiag % '1', "SHELL")
        elif self.radioTmp.isChecked():
            type = self.textEditDiag.toPlainText()
            if type == '':
                print("value null")
                return
            adb.shell(self.echoDiag % type, "SHELL")
        else:
            print("please set diag type")
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
            print(ret)
            if self.logFlag:
                self.logFile.write(ret)

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
        print("will be delete")

    def logFunc(self):
        if self.showRawdataFlag == 0:
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
        arg = self.textEditKmsg.toPlainText()
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

    # touch
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
        self.defineFile = './DEFINE_SETTING'
        self.historyFile = './HISTORY'
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

            "PORT_NUM"]

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
        name = self.diagArrText.toPlainText()
        print(name)
        if self.driverVersionMode == 1:
            adb.shell("echo %s > " % name + self.v1DiagArrPath, "SHELL")
        elif self.driverVersionMode == 2:
            adb.shell("echo diag_arr,%s > " % name + self.debugPath, "SHELL")

    def touchSenseOnFunc(self):
        adb.shell(self.echoSenseOn, "SHELL")

    def touchSenseOffFunc(self):
        adb.shell(self.echoSenseOff, "SHELL")

    def touchSelfTestFunc(self):
        ret = adb.shell(self.catSelfTest, "SHELL")
        # ret = str(ret, encoding='utf-8')
        self.rawdataShowText.append(ret)

    def touchFWVersionFunc(self):
        adb.shell(self.echoFWVersion % "v", "SHELL")
        ret = adb.shell(self.catFWVersion, "SHELL")
        # ret = str(ret, encoding='utf-8')
        self.rawdataShowText.append(ret)

    def touchResetFunc(self):
        adb.shell(self.echoReset % "1", "SHELL")
        self.rawdataShowText.append("toggle reset pin\n")

    def touchInten0Func(self):
        adb.shell(self.echoIntEn % "0", "SHELL")

    def touchInten1Func(self):
        adb.shell(self.echoIntEn % "1", "SHELL")

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
            return
        ret = adb.shell("adb push %s " % fw_path + self.fwPath)
        print(ret)
        ret = adb.shell("echo t Himax_firmware.bin > " + self.debugPath, "SHELL")
        print(ret)

    # display
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

    # wifi func
    def wifiConnectFunc(self):
        self.threadWifiConnect = Thread(target=self.waitConnectFunc)
        self.threadWifiConnect.start()

    def waitConnectFunc(self):
        print("Start...")
        self.port = 8888
        self.wifiConnect.setDisabled(True)
        self.wifiConnect.setStyleSheet("color: rgb(105, 105, 105)")
        self.wifiConnectFlag = 1
        deviceInfo = (adb.shell("adb devices"))
        print(deviceInfo)
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
            self.wifiConnect.setDisabled(False)
            self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
            return False

        deviceName = device_list[0]
        print(deviceName)
        self.wifiStatus.setText("Connect...")

        # Get device ip & set port
        cmd = "adb -s %s shell ip -f inet addr show wlan0" % deviceName
        ip = adb.shell(cmd)
        # ip = str(ip, encoding='utf-8')
        ip = ip[ip.find("inet 1") + 5:ip.find("/")]
        cmd = "adb -s %s tcpip %s" % (deviceName, self.port)
        print(adb.shell(cmd))
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

        print("Unplugin")
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

        print("Wifi Connect Done")
        self.wifiStatus.setText("Connected")
        self.wifiStatus.setStyleSheet("color: rgb(0, 255, 0)")
        self.wifiConnect.setDisabled(False)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")

    def wifiReconnectFunc(self):
        cmd = "adb connect %s:%s" % (self.device_ip, self.port)
        print(cmd)
        adb.shell(cmd)

    def wifiDisconnectFunc(self):
        adb.shell("adb disconnect")
        self.wifiStatus.setText("Disconnect")
        self.wifiStatus.setStyleSheet("color: rgb(255, 0, 0)")
        self.wifiConnect.setDisabled(False)
        self.wifiConnect.setStyleSheet("color: rgb(0, 0, 0)")
        self.wifiConnectFlag = 0
        self.device_ip = ""
        self.device_ip_port = ""

    # adb
    def homeKeyFunc(self):
        adb.shell("adb shell input keyevent KEYCODE_HOME")

    def backKeyFunc(self):
        adb.shell("adb shell input keyevent KEYCODE_BACK")

    def volUpFunc(self):
        adb.shell("adb shell input keyevent KEYCODE_VOLUME_UP")

    def volDownFunc(self):
        adb.shell("adb shell input keyevent KEYCODE_VOLUME_DOWN")

    def getpropFunc(self):
        ret = adb.shell("adb shell getprop")
        print(ret)

    def interruptsFunc(self):
        ret = adb.shell("adb shell cat /proc/interrupts")
        print(ret)

    def checkDeviceFunc(self):
        res = adb.shell("adb devices")
        print(res)

    def hideShowVirtualFunc(self):
        if self.hideShowVirtual.text() == 'ShowVirtual':
            self.hideShowVirtual.setText("HideVirtual")
            adb.shell("adb shell settings put global policy_control immersive.full=*")
        else:
            self.hideShowVirtual.setText("ShowVirtual")
            adb.shell("adb shell settings put global policy_control null")

    def powerKeyFunc(self):
        adb.shell(None, "KEYEVENT", 26)

    def openClosePointFunc(self):
        if self.openClosePoint.text() == 'OpenPoint':
            self.openClosePoint.setText("ClosePoint")
            adb.shell("settings put system pointer_location 1", "SHELL")
            adb.shell("settings put system show_touches 1", "SHELL")
        else:
            self.openClosePoint.setText("OpenPoint")
            adb.shell("settings put system pointer_location 0", "SHELL")
            adb.shell("settings put system show_touches 0", "SHELL")

    def screenShotFunc(self):
        print("Screen Shot...")
        name = time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) + ".png"
        cmd = "adb wait-for-device shell screencap -p /sdcard/%s" % (name)
        adb.shell(cmd)
        cmd = "adb pull /sdcard/%s" % name
        adb.shell(cmd)
        print("Screen Shot Done")

    def shutDownFunc(self):
        adb.shell("adb shell reboot -p")

    def rebootFunc(self):
        adb.shell("adb reboot")

    def pullHXFileFunc(self):
        print("will be add")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
