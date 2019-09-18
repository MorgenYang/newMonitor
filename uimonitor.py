# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\newMonitor\uimonitor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(585, 415)
        MainWindow.setMinimumSize(QtCore.QSize(585, 415))
        MainWindow.setMaximumSize(QtCore.QSize(585, 415))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 394))
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
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 570, 50))
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
        self.groupBox_2.setGeometry(QtCore.QRect(0, 55, 571, 86))
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
        self.groupBox_3.setGeometry(QtCore.QRect(0, 145, 570, 91))
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
        self.diagArrText = QtWidgets.QTextEdit(self.groupBox_3)
        self.diagArrText.setGeometry(QtCore.QRect(325, 50, 50, 30))
        self.diagArrText.setMaximumSize(QtCore.QSize(100, 30))
        self.diagArrText.setStyleSheet("color: rgb(0, 0, 0);")
        self.diagArrText.setObjectName("diagArrText")
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
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 240, 570, 50))
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
        self.TabMainWindow.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.rawdataShowText = QtWidgets.QTextBrowser(self.tab)
        self.rawdataShowText.setGeometry(QtCore.QRect(0, 75, 571, 286))
        self.rawdataShowText.setObjectName("rawdataShowText")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 571, 31))
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.log = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.log.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.horizontalLayout_2.addWidget(self.log)
        self.pullHXFile = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pullHXFile.setMaximumSize(QtCore.QSize(100, 29))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pullHXFile.setFont(font)
        self.pullHXFile.setStyleSheet("color: rgb(0, 0, 0);")
        self.pullHXFile.setObjectName("pullHXFile")
        self.horizontalLayout_2.addWidget(self.pullHXFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 571, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.recalled = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
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
        self.horizontalLayout_3.addWidget(self.recalled)
        self.sram = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.sram.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sram.setFont(font)
        self.sram.setObjectName("sram")
        self.horizontalLayout_3.addWidget(self.sram)
        self.kmsg = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.kmsg.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kmsg.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.getevent.setFont(font)
        self.getevent.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.getevent.setObjectName("getevent")
        self.horizontalLayout_3.addWidget(self.getevent)
        self.textEditGetevent = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEditGetevent.setMaximumSize(QtCore.QSize(60, 29))
        self.textEditGetevent.setToolTipDuration(0)
        self.textEditGetevent.setObjectName("textEditGetevent")
        self.horizontalLayout_3.addWidget(self.textEditGetevent)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.readRegValShowText.setGeometry(QtCore.QRect(0, 150, 571, 211))
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
        self.groupBox_4.setTitle(_translate("MainWindow", "Display"))
        self.openBlight.setText(_translate("MainWindow", "OpenBlight"))
        self.d1129.setText(_translate("MainWindow", "1129"))
        self.d2810.setText(_translate("MainWindow", "2810"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.tab_2), _translate("MainWindow", "Options"))
        self.rawdataRead.setText(_translate("MainWindow", "Read"))
        self.radioDC.setText(_translate("MainWindow", "DC"))
        self.radioIIR.setText(_translate("MainWindow", "IIR"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.log.setText(_translate("MainWindow", "Log"))
        self.pullHXFile.setText(_translate("MainWindow", "Pull"))
        self.recalled.setText(_translate("MainWindow", "Recall"))
        self.sram.setText(_translate("MainWindow", "SRAM"))
        self.kmsg.setText(_translate("MainWindow", "Kmsg"))
        self.getevent.setText(_translate("MainWindow", "Gevent"))
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
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabSwiplines), _translate("MainWindow", "Swipe"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabAbout), _translate("MainWindow", "About"))
        self.TabHelpSubMain.setTabText(self.TabHelpSubMain.indexOf(self.TabCommands), _translate("MainWindow", "Commands"))
        self.TabMainWindow.setTabText(self.TabMainWindow.indexOf(self.TabHelp), _translate("MainWindow", "Help"))
