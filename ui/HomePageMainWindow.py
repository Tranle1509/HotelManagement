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
        self.pushButtonNext = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(780, 680, 161, 61))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNext.setFont(font)
        self.pushButtonNext.setStyleSheet("background-color: rgb(255, 255, 255,80);")
        self.pushButtonNext.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNext.setIcon(icon)
        self.pushButtonNext.setIconSize(QtCore.QSize(100, 100))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(20, 680, 161, 61))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setStyleSheet("background-color: rgb(255, 255, 255,80);")
        self.pushButtonBack.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon1)
        self.pushButtonBack.setIconSize(QtCore.QSize(100, 100))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 951, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/HomePage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 391, 641))
        self.groupBox.setStyleSheet("QGroupBox {\n"
";\n"
"    background-color: rgb(0, 0, 0,100);\n"
"    border-radius: 15px;        /* Bo góc */\n"
"    margin-top: 15px;           /* Tạo khoảng trống cho tiêu đề */\n"
"    padding: 10px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 331, 471))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0,100);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Times New Roman\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.logo = QtWidgets.QLabel(parent=self.groupBox)
        self.logo.setGeometry(QtCore.QRect(120, 20, 151, 121))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/logo hotel.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 211, 101))
        self.label_3.setStyleSheet("color: rgb(255, 227, 126);\n"
"font: 75 22pt \"#9Slide03 SFU Toledo Bold\";\n"
"background-color: transparent")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.pushButtonNext.raise_()
        self.pushButtonBack.raise_()
        self.groupBox.raise_()
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
        self.label_2.setText(_translate("MainWindow", "At D\'anteria Exclusive, the golden beaches and sparking waters of Main Beach and Gold Coast Broadwater are right at your fingertips. Enjoy the holiday glow that radiates throughout the city which boasts one of the world\'s best coastlines and a delightful climate all year round. Located in the premier playground of blue-water yachting, magnificent fishing and diving, surfing, world-class golfing, tennis, or simply relaxing on the golden sand beaches, the opportunities for adventure and relaxation are endless."))
        self.label_3.setText(_translate("MainWindow", "About Us"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.actionImport_data.setText(_translate("MainWindow", "Import data"))
        self.actionExport_data.setText(_translate("MainWindow", "Export data"))
