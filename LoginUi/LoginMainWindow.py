# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\LoginUi\LoginMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 603)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 170, 501, 61))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"#9Slide04 Prata\";\n"
"font: 75 25pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(128, 0, 2);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 240, 201, 31))
        self.label_2.setStyleSheet("font: 75 20pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(64, 0, 128);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 300, 101, 31))
        self.label_3.setStyleSheet("font: 75 20pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(64, 0, 128);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 171, 51))
        self.label_4.setStyleSheet("font: 75 20pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(64, 0, 128);\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(270, 240, 351, 41))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(270, 360, 351, 41))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(240, 430, 131, 61))
        self.pushButtonLogin.setStyleSheet("font: 75 20pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(128, 0, 2);")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(490, 430, 121, 61))
        self.pushButtonExit.setStyleSheet("font: 75 20pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(128, 0, 2);")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 10, 151, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\LoginUi\\../images/logo hotel.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBoxRole = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBoxRole.setGeometry(QtCore.QRect(270, 300, 351, 41))
        self.comboBoxRole.setObjectName("comboBoxRole")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonExit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login Hotel Management"))
        self.label_2.setText(_translate("MainWindow", "User Name:"))
        self.label_3.setText(_translate("MainWindow", "Role:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Log In"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
