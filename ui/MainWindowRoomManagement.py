# Form implementation generated from reading ui file 'D:\FinalProject\ui\MainWindowRoomManagement.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 817)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollArea.setStyleSheet("font: 75 16pt \"#9Slide03 SFU Toledo Bold\";")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 754))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_Roomstatus = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Roomstatus.setGeometry(QtCore.QRect(150, 50, 221, 21))
        self.lineEdit_Roomstatus.setObjectName("lineEdit_Roomstatus")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_Customer = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Customer.setGeometry(QtCore.QRect(150, 90, 221, 21))
        self.lineEdit_Customer.setObjectName("lineEdit_Customer")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_Bookingcode = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Bookingcode.setGeometry(QtCore.QRect(150, 140, 221, 21))
        self.lineEdit_Bookingcode.setObjectName("lineEdit_Bookingcode")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.dateTimeEdit_checkin = QtWidgets.QDateTimeEdit(parent=self.groupBox_2)
        self.dateTimeEdit_checkin.setGeometry(QtCore.QRect(130, 180, 241, 31))
        self.dateTimeEdit_checkin.setObjectName("dateTimeEdit_checkin")
        self.dateTimeEdit_checkout = QtWidgets.QDateTimeEdit(parent=self.groupBox_2)
        self.dateTimeEdit_checkout.setGeometry(QtCore.QRect(130, 240, 241, 31))
        self.dateTimeEdit_checkout.setObjectName("dateTimeEdit_checkout")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_save.setGeometry(QtCore.QRect(40, 300, 131, 41))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_clear = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_clear.setGeometry(QtCore.QRect(200, 300, 131, 41))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_Sortvip = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Sortvip.setGeometry(QtCore.QRect(30, 40, 131, 41))
        self.pushButton_Sortvip.setStyleSheet("background-color: rgb(255, 215, 0);")
        self.pushButton_Sortvip.setObjectName("pushButton_Sortvip")
        self.pushButton_Sortregular = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Sortregular.setGeometry(QtCore.QRect(210, 40, 131, 41))
        self.pushButton_Sortregular.setStyleSheet("background-color: rgb(255, 252, 246);")
        self.pushButton_Sortregular.setObjectName("pushButton_Sortregular")
        self.pushButton_Sortinhouse = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Sortinhouse.setGeometry(QtCore.QRect(30, 100, 131, 41))
        self.pushButton_Sortinhouse.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_Sortinhouse.setObjectName("pushButton_Sortinhouse")
        self.pushButton_Sortready = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Sortready.setGeometry(QtCore.QRect(210, 100, 131, 41))
        self.pushButton_Sortready.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButton_Sortready.setObjectName("pushButton_Sortready")
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_Bookedrooms = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_Bookedrooms.setGeometry(QtCore.QRect(170, 50, 191, 21))
        self.lineEdit_Bookedrooms.setObjectName("lineEdit_Bookedrooms")
        self.lineEdit_Vacancy = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_Vacancy.setGeometry(QtCore.QRect(170, 90, 191, 21))
        self.lineEdit_Vacancy.setObjectName("lineEdit_Vacancy")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_Totalcustomers = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_Totalcustomers.setGeometry(QtCore.QRect(170, 130, 191, 21))
        self.lineEdit_Totalcustomers.setObjectName("lineEdit_Totalcustomers")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(128, 0, 2);\n"
"color: rgb(255, 215, 0);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("font: 75 8pt \"#9Slide03 SFU Toledo Bold\";\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit.setGeometry(QtCore.QRect(110, 19, 21, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(300, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 19, 21, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 19, 21, 21))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.groupBox_6)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.tableRooms = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableRooms.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("#9Slide04 SFU Toledo")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.tableRooms.setFont(font)
        self.tableRooms.setStyleSheet("font: 57 16pt \"#9Slide04 SFU Toledo\";")
        self.tableRooms.setObjectName("tableRooms")
        self.tableRooms.setColumnCount(5)
        self.tableRooms.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableRooms.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableRooms.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.tableRooms.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRooms.setItem(4, 4, item)
        self.verticalLayout.addWidget(self.tableRooms)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 10000000))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridFrame = QtWidgets.QFrame(parent=self.groupBox)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_checkin = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_checkin.setObjectName("pushButton_checkin")
        self.gridLayout.addWidget(self.pushButton_checkin, 0, 1, 1, 1)
        self.pushButton_checkout = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_checkout.setObjectName("pushButton_checkout")
        self.gridLayout.addWidget(self.pushButton_checkout, 0, 2, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(parent=self.gridFrame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\FinalProject\\ui\\../images/close_red.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 1, 2, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(parent=self.gridFrame)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 1, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.gridFrame)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Detail Info"))
        self.label_6.setText(_translate("MainWindow", "Room Status:"))
        self.label_7.setText(_translate("MainWindow", "Customer:"))
        self.label_8.setText(_translate("MainWindow", "Booking code:"))
        self.label_9.setText(_translate("MainWindow", "Check in:"))
        self.label_10.setText(_translate("MainWindow", "Check out:"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sort Room"))
        self.pushButton_Sortvip.setText(_translate("MainWindow", "VIP"))
        self.pushButton_Sortregular.setText(_translate("MainWindow", "Regular"))
        self.pushButton_Sortinhouse.setText(_translate("MainWindow", "In House"))
        self.pushButton_Sortready.setText(_translate("MainWindow", "Ready"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Statictics"))
        self.label_4.setText(_translate("MainWindow", "Booked rooms:"))
        self.label_11.setText(_translate("MainWindow", "Vancancy:"))
        self.label_12.setText(_translate("MainWindow", "Total customers:"))
        self.label.setText(_translate("MainWindow", "Room Management"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Status"))
        self.label_2.setText(_translate("MainWindow", "In House"))
        self.label_3.setText(_translate("MainWindow", "Ready"))
        self.label_5.setText(_translate("MainWindow", "Cleaning"))
        item = self.tableRooms.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableRooms.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableRooms.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableRooms.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableRooms.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableRooms.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Floor 1"))
        item = self.tableRooms.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Floor 2"))
        item = self.tableRooms.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Floor 3"))
        item = self.tableRooms.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Floor 4"))
        item = self.tableRooms.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Floor 5"))
        __sortingEnabled = self.tableRooms.isSortingEnabled()
        self.tableRooms.setSortingEnabled(False)
        item = self.tableRooms.item(0, 0)
        item.setText(_translate("MainWindow", "101"))
        item = self.tableRooms.item(0, 1)
        item.setText(_translate("MainWindow", "201"))
        item = self.tableRooms.item(0, 2)
        item.setText(_translate("MainWindow", "301"))
        item = self.tableRooms.item(0, 3)
        item.setText(_translate("MainWindow", "401"))
        item = self.tableRooms.item(0, 4)
        item.setText(_translate("MainWindow", "501"))
        item = self.tableRooms.item(1, 0)
        item.setText(_translate("MainWindow", "102"))
        item = self.tableRooms.item(1, 1)
        item.setText(_translate("MainWindow", "202"))
        item = self.tableRooms.item(1, 2)
        item.setText(_translate("MainWindow", "302"))
        item = self.tableRooms.item(1, 3)
        item.setText(_translate("MainWindow", "402"))
        item = self.tableRooms.item(1, 4)
        item.setText(_translate("MainWindow", "502"))
        item = self.tableRooms.item(2, 0)
        item.setText(_translate("MainWindow", "103"))
        item = self.tableRooms.item(2, 1)
        item.setText(_translate("MainWindow", "203"))
        item = self.tableRooms.item(2, 2)
        item.setText(_translate("MainWindow", "303"))
        item = self.tableRooms.item(2, 3)
        item.setText(_translate("MainWindow", "403"))
        item = self.tableRooms.item(2, 4)
        item.setText(_translate("MainWindow", "503"))
        item = self.tableRooms.item(3, 0)
        item.setText(_translate("MainWindow", "104"))
        item = self.tableRooms.item(3, 1)
        item.setText(_translate("MainWindow", "204"))
        item = self.tableRooms.item(3, 2)
        item.setText(_translate("MainWindow", "304"))
        item = self.tableRooms.item(3, 3)
        item.setText(_translate("MainWindow", "404"))
        item = self.tableRooms.item(3, 4)
        item.setText(_translate("MainWindow", "504"))
        item = self.tableRooms.item(4, 0)
        item.setText(_translate("MainWindow", "105"))
        item = self.tableRooms.item(4, 1)
        item.setText(_translate("MainWindow", "205"))
        item = self.tableRooms.item(4, 2)
        item.setText(_translate("MainWindow", "305"))
        item = self.tableRooms.item(4, 3)
        item.setText(_translate("MainWindow", "405"))
        item = self.tableRooms.item(4, 4)
        item.setText(_translate("MainWindow", "505"))
        self.tableRooms.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Functions"))
        self.pushButton_checkin.setText(_translate("MainWindow", "Check in"))
        self.pushButton_checkout.setText(_translate("MainWindow", "Check out"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
