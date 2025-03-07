# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\ui\HomePageMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 798)
        MainWindow.setWindowOpacity(2.0)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 141, 131))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/logo hotel.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.hotel2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.hotel2.setGeometry(QtCore.QRect(0, 0, 891, 341))
        self.hotel2.setText("")
        self.hotel2.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/hotel2.png"))
        self.hotel2.setScaledContents(True)
        self.hotel2.setObjectName("hotel2")
        self.pushButtonRoom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRoom.setGeometry(QtCore.QRect(210, 630, 161, 61))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRoom.setFont(font)
        self.pushButtonRoom.setStyleSheet("color: rgb(128, 0, 2);")
        self.pushButtonRoom.setObjectName("pushButtonRoom")
        self.pushButtonBooking = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBooking.setGeometry(QtCore.QRect(520, 630, 161, 61))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBooking.setFont(font)
        self.pushButtonBooking.setStyleSheet("color: rgb(128, 0, 2);")
        self.pushButtonBooking.setObjectName("pushButtonBooking")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 360, 811, 231))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.hotel2.raise_()
        self.pushButtonRoom.raise_()
        self.pushButtonBooking.raise_()
        self.logo.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSystem = QtWidgets.QMenu(parent=self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_data = QtGui.QAction(parent=MainWindow)
        self.actionImport_data.setObjectName("actionImport_data")
        self.actionExport_data = QtGui.QAction(parent=MainWindow)
        self.actionExport_data.setObjectName("actionExport_data")
        self.menuSystem.addSeparator()
        self.menuSystem.addSeparator()
        self.menuSystem.addAction(self.actionImport_data)
        self.menuSystem.addAction(self.actionExport_data)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonRoom.setText(_translate("MainWindow", "Room"))
        self.pushButtonBooking.setText(_translate("MainWindow", "Booking"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'#9Slide03 SFU Toledo Bold\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'GillSans,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:96; font-style:italic; color:#333333; background-color:#f0f1f2;\">At D\'anteria Exclusive, the golden beaches and sparking waters of Main Beach and Gold Coast Broadwater are right at your fingertips. Enjoy the holiday glow that radiates throughout the city which boasts one of the world\'s best coastlines and a delightful climate all year round. Located in the premier playground of blue-water yachting, magnificent fishing and diving, surfing, world-class golfing, tennis, or simply relaxing on the golden sand beaches, the opportunities for adventure and relaxation are endless.</span></p></body></html>"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.actionImport_data.setText(_translate("MainWindow", "Import data"))
        self.actionExport_data.setText(_translate("MainWindow", "Export data"))
