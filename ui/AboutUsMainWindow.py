# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\ui\AboutUsMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 753)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1081, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/aboutus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(40, 630, 121, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setStyleSheet("font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));")
        self.pushButtonBack.setObjectName("pushButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonBack.setText(_translate("MainWindow", "Back"))
