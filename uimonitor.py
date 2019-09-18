# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\newmonitor\uimonitor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(685, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 111, 441))
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
        self.LeftMainWindow.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.LeftMainWindow.setObjectName("LeftMainWindow")
        self.pageWifi = QtWidgets.QWidget()
        self.pageWifi.setGeometry(QtCore.QRect(0, 0, 100, 322))
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
        self.pageAdb.setGeometry(QtCore.QRect(0, 0, 100, 322))
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
        self.LeftMainWindow.addItem(self.pageAdb, "")
        self.pageTouch = QtWidgets.QWidget()
        self.pageTouch.setGeometry(QtCore.QRect(0, 0, 100, 322))
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
        self.pageDisplay.setGeometry(QtCore.QRect(0, 0, 100, 322))
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
        self.pageOptions.setGeometry(QtCore.QRect(0, 0, 100, 322))
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 0, 571, 441))
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
        self.rawdataShowText.setGeometry(QtCore.QRect(0, 75, 561, 331))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 561, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
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
        self.pullHXFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pullHXFile.setMaximumSize(QtCore.QSize(100, 29))
        self.pullHXFile.setStyleSheet("color: rgb(0, 0, 0);")
        self.pullHXFile.setObjectName("pullHXFile")
        self.horizontalLayout_2.addWidget(self.pullHXFile)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 39, 561, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.recalled = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.recalled.setEnabled(True)
        self.recalled.setMaximumSize(QtCore.QSize(100, 30))
        self.recalled.setObjectName("recalled")
        self.horizontalLayout_3.addWidget(self.recalled)
        self.sram = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.sram.setMaximumSize(QtCore.QSize(70, 30))
        self.sram.setObjectName("sram")
        self.horizontalLayout_3.addWidget(self.sram)
        self.kmsg = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.kmsg.setMaximumSize(QtCore.QSize(70, 30))
        self.kmsg.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.kmsg.setObjectName("kmsg")
        self.horizontalLayout_3.addWidget(self.kmsg)
        self.textEditKmsg = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEditKmsg.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditKmsg.setObjectName("textEditKmsg")
        self.horizontalLayout_3.addWidget(self.textEditKmsg)
        self.getevent = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.getevent.setMinimumSize(QtCore.QSize(0, 0))
        self.getevent.setMaximumSize(QtCore.QSize(70, 30))
        self.getevent.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.getevent.setObjectName("getevent")
        self.horizontalLayout_3.addWidget(self.getevent)
        self.textEditGetevent = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEditGetevent.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditGetevent.setObjectName("textEditGetevent")
        self.horizontalLayout_3.addWidget(self.textEditGetevent)
        self.TabMainWindow.addTab(self.tab, "")
        self.TabRWRegister = QtWidgets.QWidget()
        self.TabRWRegister.setObjectName("TabRWRegister")
        self.pushButtonRead = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRead.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pushButtonRead.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRead.setObjectName("pushButtonRead")
        self.textEditReadRegAddr = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditReadRegAddr.setGeometry(QtCore.QRect(0, 30, 100, 101))
        self.textEditReadRegAddr.setMaximumSize(QtCore.QSize(150, 170))
        self.textEditReadRegAddr.setObjectName("textEditReadRegAddr")
        self.textEditWriteVal3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal3.setGeometry(QtCore.QRect(350, 105, 120, 30))
        self.textEditWriteVal3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal3.setObjectName("textEditWriteVal3")
        self.textEditWriteVal4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal4.setGeometry(QtCore.QRect(350, 140, 120, 30))
        self.textEditWriteVal4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal4.setObjectName("textEditWriteVal4")
        self.textEditWriteVal2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal2.setGeometry(QtCore.QRect(350, 70, 120, 30))
        self.textEditWriteVal2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal2.setObjectName("textEditWriteVal2")
        self.textEditWriteAddr1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr1.setGeometry(QtCore.QRect(220, 35, 120, 30))
        self.textEditWriteAddr1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr1.setObjectName("textEditWriteAddr1")
        self.textEditWriteAddr2 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr2.setGeometry(QtCore.QRect(220, 70, 120, 30))
        self.textEditWriteAddr2.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr2.setObjectName("textEditWriteAddr2")
        self.textEditWriteAddr0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr0.setGeometry(QtCore.QRect(220, 0, 120, 30))
        self.textEditWriteAddr0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr0.setObjectName("textEditWriteAddr0")
        self.textEditWriteVal1 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal1.setGeometry(QtCore.QRect(350, 35, 120, 30))
        self.textEditWriteVal1.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal1.setObjectName("textEditWriteVal1")
        self.pushButtonRegWrite0 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite0.setGeometry(QtCore.QRect(110, 0, 100, 30))
        self.pushButtonRegWrite0.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite0.setObjectName("pushButtonRegWrite0")
        self.pushButtonRegWrite1 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite1.setGeometry(QtCore.QRect(110, 35, 100, 30))
        self.pushButtonRegWrite1.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite1.setObjectName("pushButtonRegWrite1")
        self.textEditWriteVal0 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteVal0.setGeometry(QtCore.QRect(350, 0, 120, 30))
        self.textEditWriteVal0.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteVal0.setObjectName("textEditWriteVal0")
        self.textEditWriteAddr3 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr3.setGeometry(QtCore.QRect(220, 105, 120, 30))
        self.textEditWriteAddr3.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr3.setObjectName("textEditWriteAddr3")
        self.pushButtonRegWrite2 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite2.setGeometry(QtCore.QRect(110, 70, 100, 30))
        self.pushButtonRegWrite2.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite2.setObjectName("pushButtonRegWrite2")
        self.textEditWriteAddr4 = QtWidgets.QTextEdit(self.TabRWRegister)
        self.textEditWriteAddr4.setGeometry(QtCore.QRect(220, 140, 120, 30))
        self.textEditWriteAddr4.setMaximumSize(QtCore.QSize(150, 30))
        self.textEditWriteAddr4.setObjectName("textEditWriteAddr4")
        self.pushButtonRegWrite4 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite4.setGeometry(QtCore.QRect(110, 140, 100, 30))
        self.pushButtonRegWrite4.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite4.setObjectName("pushButtonRegWrite4")
        self.pushButtonRegWrite3 = QtWidgets.QPushButton(self.TabRWRegister)
        self.pushButtonRegWrite3.setGeometry(QtCore.QRect(110, 105, 100, 30))
        self.pushButtonRegWrite3.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRegWrite3.setObjectName("pushButtonRegWrite3")
        self.label = QtWidgets.QLabel(self.TabRWRegister)
        self.label.setGeometry(QtCore.QRect(5, 140, 50, 20))
        self.label.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.reglength = QtWidgets.QComboBox(self.TabRWRegister)
        self.reglength.setGeometry(QtCore.QRect(70, 140, 30, 22))
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
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 175, 561, 231))
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
        self.LeftMainWindow.setCurrentIndex(1)
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
        self.pullHXFile.setText(_translate("MainWindow", "Pull"))
        self.recalled.setText(_translate("MainWindow", "Re"))
        self.sram.setText(_translate("MainWindow", "SRAM"))
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
