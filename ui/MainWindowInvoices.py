# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\ui\MainWindowInvoices.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(812, 720))
        MainWindow.setMaximumSize(QtCore.QSize(812, 720))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 130, 761, 81))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255,50);\n"
" border-radius: 15px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_customercode = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_customercode.setGeometry(QtCore.QRect(120, 10, 191, 20))
        self.lineEdit_customercode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_customercode.setObjectName("lineEdit_customercode")
        self.lineEdit_issuedate = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_issuedate.setGeometry(QtCore.QRect(120, 40, 191, 20))
        self.lineEdit_issuedate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_issuedate.setObjectName("lineEdit_issuedate")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_customer = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_customer.setGeometry(QtCore.QRect(530, 10, 191, 20))
        self.lineEdit_customer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_customer.setObjectName("lineEdit_customer")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(420, 10, 101, 21))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_numberofdays = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_numberofdays.setGeometry(QtCore.QRect(530, 40, 191, 20))
        self.lineEdit_numberofdays.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_numberofdays.setObjectName("lineEdit_numberofdays")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(420, 40, 111, 21))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_8.setObjectName("label_8")
        self.tableWidget_invoices = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget_invoices.setGeometry(QtCore.QRect(20, 220, 761, 271))
        self.tableWidget_invoices.setStyleSheet("background-color: rgb(255, 255, 255,100);\n"
" border-radius: 15px;")
        self.tableWidget_invoices.setObjectName("tableWidget_invoices")
        self.tableWidget_invoices.setColumnCount(6)
        self.tableWidget_invoices.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoices.setHorizontalHeaderItem(5, item)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 500, 761, 141))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255,50);\n"
" border-radius: 15px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_citprice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_citprice.setGeometry(QtCore.QRect(120, 10, 621, 20))
        self.lineEdit_citprice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_citprice.setObjectName("lineEdit_citprice")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_tax = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_tax.setGeometry(QtCore.QRect(120, 40, 621, 20))
        self.lineEdit_tax.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tax.setObjectName("lineEdit_tax")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_totalprice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_totalprice.setGeometry(QtCore.QRect(120, 70, 621, 20))
        self.lineEdit_totalprice.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_totalprice.setObjectName("lineEdit_totalprice")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 101, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"#9Slide03 Montserrat\";")
        self.label_11.setObjectName("label_11")
        self.pushButton_calculate = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_calculate.setGeometry(QtCore.QRect(220, 100, 121, 31))
        self.pushButton_calculate.setStyleSheet("font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));")
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.pushButton_close = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_close.setGeometry(QtCore.QRect(420, 100, 121, 31))
        self.pushButton_close.setStyleSheet("font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));")
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 781, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 75 30pt \"#9Slide03 SFU Toledo Bold\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 781, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"#9Slide03 SFU Toledo Bold\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 781, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"#9Slide03 SFU Toledo Bold\";\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 3, 791, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/HomePage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(6, 3, 801, 681))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/login.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.tableWidget_invoices.raise_()
        self.groupBox_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
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
        self.label_5.setText(_translate("MainWindow", "Customer code:"))
        self.label_6.setText(_translate("MainWindow", "Issue Date:"))
        self.label_7.setText(_translate("MainWindow", "Customer:"))
        self.label_8.setText(_translate("MainWindow", "Number of days:"))
        item = self.tableWidget_invoices.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_invoices.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_invoices.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_invoices.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.tableWidget_invoices.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Roomtype"))
        item = self.tableWidget_invoices.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget_invoices.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit price"))
        item = self.tableWidget_invoices.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Check in date"))
        item = self.tableWidget_invoices.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Check out date"))
        self.label_9.setText(_translate("MainWindow", "CIT price:"))
        self.label_10.setText(_translate("MainWindow", "Tax:"))
        self.label_11.setText(_translate("MainWindow", "Total Price:"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "D\'anteria Exclusive"))
        self.label_3.setText(_translate("MainWindow", "Dhaalu Atoll, Kandima Island, 20066, Kudahuvadhoo, Maldives"))
        self.label_4.setText(_translate("MainWindow", "Contact: (+960) 676-0077"))
