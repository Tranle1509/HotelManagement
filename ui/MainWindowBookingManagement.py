# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\ui\MainWindowBookingManagement.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 780))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxWarehouse = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxWarehouse.setGeometry(QtCore.QRect(0, 250, 1280, 780))
        self.groupBoxWarehouse.setMinimumSize(QtCore.QSize(1280, 780))
        self.groupBoxWarehouse.setMaximumSize(QtCore.QSize(1280, 780))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBoxWarehouse.setFont(font)
        self.groupBoxWarehouse.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"color: qlineargradient(spread:pad, x1:0.608, y1:0.546091, x2:0.994318, y2:0.960227, stop:0.0681818 rgba(80, 11, 40, 255), stop:1 rgba(210, 26, 48, 243));\n"
"font: 12pt \"#9Slide03 SFU Toledo Bold\";\n"
"    border: 1px solid rgb(60, 60, 60); /* Viền đen */\n"
"    border-radius: 1px; /* Bo góc nhẹ để nhìn mềm mại hơn */\n"
"hover {\n"
"    background-color: rgb(90, 150, 200); /* Màu sáng hơn khi hover */\n"
"}\n"
"")
        self.groupBoxWarehouse.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.groupBoxWarehouse.setFlat(False)
        self.groupBoxWarehouse.setObjectName("groupBoxWarehouse")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: transparent;\n"
" border:transparent;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: transparent; border:transparent;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: transparent; border:transparent;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: transparent; border:transparent;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_11.setGeometry(QtCore.QRect(10, 270, 101, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: transparent; border:transparent;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 81, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent; border:transparent;")
        self.label_12.setObjectName("label_12")
        self.pushButtonUpdate = QtWidgets.QPushButton(parent=self.groupBoxWarehouse)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(40, 440, 91, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.221636, y1:0.171091, x2:0.994318, y2:0.960227,\n"
"                                      stop:0.0681818 rgba(80, 11, 40, 255),\n"
"                                      stop:1 rgba(211, 26, 48, 243)); /* Gradient màu nền */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"\n"
"    /* Viền sáng ở trên & tối ở dưới để tạo hiệu ứng 3D */\n"
"    border: 2px solid rgb(255, 255, 255); /* Viền trắng tổng thể */\n"
"    border-top: 3px solid rgb(255, 255, 255); /* Viền trên sáng hơn */\n"
"    border-left: 3px solid rgb(255, 255, 255);\n"
"    border-bottom: 3px solid rgb(150, 0, 20); /* Viền dưới tối hơn */\n"
"    border-right: 3px solid rgb(150, 0, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 3px solid rgb(150, 0, 20); /* Khi nhấn, đổi viền trên tối hơn */\n"
"    border-left: 3px solid rgb(150, 0, 20);\n"
"    border-bottom: 3px solid rgb(255, 255, 255); /* Viền dưới sáng hơn */\n"
"    border-right: 3px solid rgb(255, 255, 255);\n"
"    background-color: rgb(150, 0, 20); /* Màu nền tối hơn khi nhấn */\n"
"}\n"
"")
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBoxWarehouse)
        self.pushButtonDelete.setGeometry(QtCore.QRect(190, 440, 91, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.221636, y1:0.171091, x2:0.994318, y2:0.960227,\n"
"                                      stop:0.0681818 rgba(80, 11, 40, 255),\n"
"                                      stop:1 rgba(211, 26, 48, 243)); /* Gradient màu nền */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"\n"
"    /* Viền sáng ở trên & tối ở dưới để tạo hiệu ứng 3D */\n"
"    border: 2px solid rgb(255, 255, 255); /* Viền trắng tổng thể */\n"
"    border-top: 3px solid rgb(255, 255, 255); /* Viền trên sáng hơn */\n"
"    border-left: 3px solid rgb(255, 255, 255);\n"
"    border-bottom: 3px solid rgb(150, 0, 20); /* Viền dưới tối hơn */\n"
"    border-right: 3px solid rgb(150, 0, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 3px solid rgb(150, 0, 20); /* Khi nhấn, đổi viền trên tối hơn */\n"
"    border-left: 3px solid rgb(150, 0, 20);\n"
"    border-bottom: 3px solid rgb(255, 255, 255); /* Viền dưới sáng hơn */\n"
"    border-right: 3px solid rgb(255, 255, 255);\n"
"    background-color: rgb(150, 0, 20); /* Màu nền tối hơn khi nhấn */\n"
"}\n"
"")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonReset = QtWidgets.QPushButton(parent=self.groupBoxWarehouse)
        self.pushButtonReset.setGeometry(QtCore.QRect(340, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonReset.setFont(font)
        self.pushButtonReset.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.221636, y1:0.171091, x2:0.994318, y2:0.960227,\n"
"                                      stop:0.0681818 rgba(80, 11, 40, 255),\n"
"                                      stop:1 rgba(211, 26, 48, 243)); /* Gradient màu nền */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"\n"
"    /* Viền sáng ở trên & tối ở dưới để tạo hiệu ứng 3D */\n"
"    border: 2px solid rgb(255, 255, 255); /* Viền trắng tổng thể */\n"
"    border-top: 3px solid rgb(255, 255, 255); /* Viền trên sáng hơn */\n"
"    border-left: 3px solid rgb(255, 255, 255);\n"
"    border-bottom: 3px solid rgb(150, 0, 20); /* Viền dưới tối hơn */\n"
"    border-right: 3px solid rgb(150, 0, 20);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-top: 3px solid rgb(150, 0, 20); /* Khi nhấn, đổi viền trên tối hơn */\n"
"    border-left: 3px solid rgb(150, 0, 20);\n"
"    border-bottom: 3px solid rgb(255, 255, 255); /* Viền dưới sáng hơn */\n"
"    border-right: 3px solid rgb(255, 255, 255);\n"
"    background-color: rgb(150, 0, 20); /* Màu nền tối hơn khi nhấn */\n"
"}\n"
"")
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_14.setGeometry(QtCore.QRect(180, 30, 321, 391))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QWidget {\n"
"    background-color: transparent; /* Nền hoàn toàn trong suốt */\n"
"    border: 2px solid transparent; /* Viền trong suốt */\n"
"    color: rgba(255, 255, 255, 255); /* Giữ màu chữ */\n"
"    font: 10pt \"#9Slide03 SFU Toledo Bold\";\n"
"    border-radius: 2px; /* Bo góc nhẹ */\n"
"}\n"
"\n"
"QWidget:hover {\n"
"    background-color: rgba(90, 150, 200, 100); /* Hover có màu mờ (gần trong suốt) */\n"
"}\n"
"")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/booking.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 90, 291, 31))
        self.lineEdit_3.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBoxWarehouse)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: transparent;\n"
" border:transparent;")
        self.label_15.setObjectName("label_15")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 370, 291, 31))
        self.lineEdit_4.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 150, 291, 31))
        self.lineEdit_5.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 210, 291, 31))
        self.lineEdit_6.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 270, 291, 31))
        self.lineEdit_7.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 320, 291, 31))
        self.lineEdit_8.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.groupBoxWarehouse)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 40, 291, 31))
        self.lineEdit_9.setStyleSheet("border: 2px solid transparent;\n"
"background-color: rgb(255, 255, 255,200);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.groupBoxListProduct = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxListProduct.setGeometry(QtCore.QRect(490, 250, 781, 461))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBoxListProduct.setFont(font)
        self.groupBoxListProduct.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.221636, y1:0.171091, x2:0.994318, y2:0.960227, stop:0.0681818 rgba(80, 11, 40, 255), stop:1 rgba(211, 26, 48, 243));\n"
"font: 75 12pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"")
        self.groupBoxListProduct.setObjectName("groupBoxListProduct")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxListProduct)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBoxListProduct)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Cambria\";\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(119, 139, 206))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(119, 139, 206))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(119, 139, 206))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(119, 139, 206))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(119, 139, 206))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-70, -30, 1361, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/Cover.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 200, 321, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton.setStyleSheet("font: 75 16pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(170, 0, 0);\n"
"\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 220, 421, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_BookingManagement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_BookingManagement.setGeometry(QtCore.QRect(610, 200, 331, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_BookingManagement.setFont(font)
        self.pushButton_BookingManagement.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_BookingManagement.setStyleSheet("font: 75 16pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(170, 0, 0);\n"
"\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"\n"
"background-color: rgb(186, 186, 186);")
        self.pushButton_BookingManagement.setObjectName("pushButton_BookingManagement")
        self.pushButton_RoomManagement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_RoomManagement.setGeometry(QtCore.QRect(300, 200, 331, 51))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_RoomManagement.setFont(font)
        self.pushButton_RoomManagement.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_RoomManagement.setStyleSheet("font: 75 16pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(170, 0, 0);\n"
"\n"
"\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_RoomManagement.setObjectName("pushButton_RoomManagement")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 210, 41, 31))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_3.raise_()
        self.groupBoxWarehouse.raise_()
        self.groupBoxListProduct.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_RoomManagement.raise_()
        self.pushButton_BookingManagement.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " K24411E"))
        self.groupBoxWarehouse.setTitle(_translate("MainWindow", "Customer Details:"))
        self.label_7.setText(_translate("MainWindow", "Email :"))
        self.label_8.setText(_translate("MainWindow", "Check-in Date :"))
        self.label_9.setText(_translate("MainWindow", "Check-out Date :"))
        self.label_10.setText(_translate("MainWindow", "Room Type :"))
        self.label_11.setText(_translate("MainWindow", "Identify :"))
        self.label_12.setText(_translate("MainWindow", "Phone :"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.pushButtonReset.setText(_translate("MainWindow", "Reset"))
        self.label_15.setText(_translate("MainWindow", "Name :"))
        self.groupBoxListProduct.setTitle(_translate("MainWindow", "View Booking Details + Search System"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Phone number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Check-in"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Check-out"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Room type"))
        self.pushButton.setText(_translate("MainWindow", "New reservation"))
        self.pushButton_BookingManagement.setText(_translate("MainWindow", "Booking Management"))
        self.pushButton_RoomManagement.setText(_translate("MainWindow", "Room Management"))
