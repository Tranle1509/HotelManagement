# Form implementation generated from reading ui file 'D:\KTLT\HotelManagement\ui\New_reservationMainWindow.ui'
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 780))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(850, 680, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy)
        self.pushButton_Clear.setStyleSheet("\n"
"font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));\n"
"    border-radius: 10px;\n"
"")
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(-10, 450, 1381, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SFU Toledo")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 57 12pt \"SFU Toledo\";\n"
"border-color: rgb(182, 182, 182);\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(660, 40, 121, 31))
        self.label_18.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_18.setObjectName("label_18")
        self.label_33 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_33.setGeometry(QtCore.QRect(660, 80, 71, 31))
        self.label_33.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_34.setGeometry(QtCore.QRect(10, 80, 141, 31))
        self.label_34.setStyleSheet("font: 75 11pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_35.setGeometry(QtCore.QRect(10, 150, 91, 41))
        self.label_35.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_36.setGeometry(QtCore.QRect(-30, 450, 221, 61))
        self.label_36.setObjectName("label_36")
        self.lineEdit_Rooms_5 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Rooms_5.setGeometry(QtCore.QRect(220, 460, 281, 31))
        self.lineEdit_Rooms_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lineEdit_Rooms_5.setObjectName("lineEdit_Rooms_5")
        self.label_37 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_37.setGeometry(QtCore.QRect(650, 110, 81, 51))
        self.label_37.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_37.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_37.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_38.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("font: 75 11pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_38.setObjectName("label_38")
        self.lineEdit_Cuscode = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Cuscode.setGeometry(QtCore.QRect(160, 40, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Cuscode.sizePolicy().hasHeightForWidth())
        self.lineEdit_Cuscode.setSizePolicy(sizePolicy)
        self.lineEdit_Cuscode.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Cuscode.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Cuscode.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Cuscode.setObjectName("lineEdit_Cuscode")
        self.CheckInDateOfBirth = QtWidgets.QDateEdit(parent=self.groupBox_6)
        self.CheckInDateOfBirth.setGeometry(QtCore.QRect(800, 40, 450, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckInDateOfBirth.sizePolicy().hasHeightForWidth())
        self.CheckInDateOfBirth.setSizePolicy(sizePolicy)
        self.CheckInDateOfBirth.setMinimumSize(QtCore.QSize(450, 30))
        self.CheckInDateOfBirth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.CheckInDateOfBirth.setObjectName("CheckInDateOfBirth")
        self.label_39 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_39.setGeometry(QtCore.QRect(-10, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_39.setObjectName("label_39")
        self.lineEdit_Cusname = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Cusname.setGeometry(QtCore.QRect(160, 80, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Cusname.sizePolicy().hasHeightForWidth())
        self.lineEdit_Cusname.setSizePolicy(sizePolicy)
        self.lineEdit_Cusname.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Cusname.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Cusname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Cusname.setObjectName("lineEdit_Cusname")
        self.lineEdit_Phone = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Phone.setGeometry(QtCore.QRect(800, 120, 450, 30))
        self.lineEdit_Phone.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Phone.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Phone.setObjectName("lineEdit_Phone")
        self.lineEdit_Identify = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Identify.setGeometry(QtCore.QRect(160, 120, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Identify.sizePolicy().hasHeightForWidth())
        self.lineEdit_Identify.setSizePolicy(sizePolicy)
        self.lineEdit_Identify.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Identify.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Identify.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Identify.setObjectName("lineEdit_Identify")
        self.label_40 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_40.setGeometry(QtCore.QRect(660, 150, 111, 51))
        self.label_40.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_40.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_40.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.lineEdit_Requirement = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Requirement.setGeometry(QtCore.QRect(800, 160, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Requirement.sizePolicy().hasHeightForWidth())
        self.lineEdit_Requirement.setSizePolicy(sizePolicy)
        self.lineEdit_Requirement.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Requirement.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Requirement.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Requirement.setObjectName("lineEdit_Requirement")
        self.comboBoxTypeGender = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBoxTypeGender.setGeometry(QtCore.QRect(160, 160, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxTypeGender.sizePolicy().hasHeightForWidth())
        self.comboBoxTypeGender.setSizePolicy(sizePolicy)
        self.comboBoxTypeGender.setMinimumSize(QtCore.QSize(450, 30))
        self.comboBoxTypeGender.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("SFU Toledo")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.comboBoxTypeGender.setFont(font)
        self.comboBoxTypeGender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBoxTypeGender.setObjectName("comboBoxTypeGender")
        self.comboBoxTypeGender.addItem("")
        self.comboBoxTypeGender.addItem("")
        self.lineEdit_Email = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.lineEdit_Email.setGeometry(QtCore.QRect(800, 80, 450, 30))
        self.lineEdit_Email.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Email.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.pushButton_Save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Save.setGeometry(QtCore.QRect(200, 680, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Save.sizePolicy().hasHeightForWidth())
        self.pushButton_Save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Save.setFont(font)
        self.pushButton_Save.setStyleSheet("\n"
"font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));\n"
"    border-radius: 10px;\n"
"")
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Close.setGeometry(QtCore.QRect(530, 680, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Close.sizePolicy().hasHeightForWidth())
        self.pushButton_Close.setSizePolicy(sizePolicy)
        self.pushButton_Close.setStyleSheet("\n"
"font: 75 15pt \"#9Slide03 SFU Toledo Bold\";\n"
"color: rgb(255, 232, 137);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.527363 rgba(80, 11, 40, 255), stop:1 rgba(187, 23, 43, 255));\n"
"    border-radius: 10px;\n"
"")
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, 250, 1381, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SFU Toledo")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"#9Slide03 SFU Toledo Bold\";\n"
"\n"
"border-color: rgb(182, 182, 182);\n"
"font: 57 12pt \"SFU Toledo\";\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBoxType = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBoxType.setGeometry(QtCore.QRect(160, 160, 450, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxType.sizePolicy().hasHeightForWidth())
        self.comboBoxType.setSizePolicy(sizePolicy)
        self.comboBoxType.setMinimumSize(QtCore.QSize(450, 30))
        self.comboBoxType.setMaximumSize(QtCore.QSize(450, 30))
        font = QtGui.QFont()
        font.setFamily("SFU Toledo")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.comboBoxType.setFont(font)
        self.comboBoxType.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(640, 70, 151, 51))
        self.label_10.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.label_6.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 111, 41))
        self.label_9.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_9.setObjectName("label_9")
        self.label_22 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(-30, 450, 221, 61))
        self.label_22.setObjectName("label_22")
        self.lineEdit_Rooms = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Rooms.setGeometry(QtCore.QRect(220, 460, 281, 31))
        self.lineEdit_Rooms.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.lineEdit_Rooms.setObjectName("lineEdit_Rooms")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(630, 110, 111, 51))
        self.label_23.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_23.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_19.setObjectName("label_19")
        self.lineEdit_BookingCode = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_BookingCode.setGeometry(QtCore.QRect(160, 40, 450, 30))
        self.lineEdit_BookingCode.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_BookingCode.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_BookingCode.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_BookingCode.setObjectName("lineEdit_BookingCode")
        self.CheckIn = QtWidgets.QDateEdit(parent=self.groupBox_2)
        self.CheckIn.setGeometry(QtCore.QRect(800, 40, 450, 31))
        self.CheckIn.setMinimumSize(QtCore.QSize(450, 30))
        self.CheckIn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.CheckIn.setObjectName("CheckIn")
        self.CheckOut = QtWidgets.QDateEdit(parent=self.groupBox_2)
        self.CheckOut.setGeometry(QtCore.QRect(800, 80, 450, 31))
        self.CheckOut.setMinimumSize(QtCore.QSize(450, 30))
        self.CheckOut.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.CheckOut.setObjectName("CheckOut")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("#9Slide03 SFU Toledo Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_21.setObjectName("label_21")
        self.lineEdit_Roomname = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Roomname.setGeometry(QtCore.QRect(160, 80, 450, 30))
        self.lineEdit_Roomname.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Roomname.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Roomname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Roomname.setObjectName("lineEdit_Roomname")
        self.lineEditChildren = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditChildren.setGeometry(QtCore.QRect(800, 120, 450, 30))
        self.lineEditChildren.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEditChildren.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEditChildren.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditChildren.setObjectName("lineEditChildren")
        self.lineEdit_Roomcode = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Roomcode.setGeometry(QtCore.QRect(160, 120, 450, 30))
        self.lineEdit_Roomcode.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEdit_Roomcode.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEdit_Roomcode.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Roomcode.setObjectName("lineEdit_Roomcode")
        self.label_93 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_93.setGeometry(QtCore.QRect(640, 40, 141, 31))
        self.label_93.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_93.setObjectName("label_93")
        self.label_102 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_102.setGeometry(QtCore.QRect(630, 160, 91, 31))
        self.label_102.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_102.setStyleSheet("font: 75 12pt \"#9Slide03 SFU Toledo Bold\";")
        self.label_102.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_102.setObjectName("label_102")
        self.lineEditAdult = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditAdult.setGeometry(QtCore.QRect(800, 160, 450, 30))
        self.lineEditAdult.setMinimumSize(QtCore.QSize(450, 30))
        self.lineEditAdult.setMaximumSize(QtCore.QSize(450, 30))
        self.lineEditAdult.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditAdult.setObjectName("lineEditAdult")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-70, 0, 1361, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\KTLT\\HotelManagement\\ui\\../images/Cover.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_RoomManagement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_RoomManagement.setGeometry(QtCore.QRect(280, 200, 331, 51))
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
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-20, 200, 321, 51))
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
"background-color: rgb(186, 186, 186);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_BookingManagement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_BookingManagement.setGeometry(QtCore.QRect(590, 200, 331, 51))
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
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_BookingManagement.setObjectName("pushButton_BookingManagement")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 210, 41, 31))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, 230, 381, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3.raise_()
        self.groupBox_6.raise_()
        self.pushButton_Clear.raise_()
        self.pushButton_Save.raise_()
        self.pushButton_Close.raise_()
        self.groupBox_2.raise_()
        self.pushButton_RoomManagement.raise_()
        self.pushButton.raise_()
        self.pushButton_BookingManagement.raise_()
        self.line.raise_()
        self.label.raise_()
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Clear.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Remove</span></p><p><br/></p></body></html>"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Customer details"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Date of birth :</p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Email :</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Customer name :</p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Gender :</p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Rooms:</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Phone</p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Customer code :</p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Identify :</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Requirment:</p></body></html>"))
        self.comboBoxTypeGender.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBoxTypeGender.setItemText(1, _translate("MainWindow", "Female"))
        self.pushButton_Save.setText(_translate("MainWindow", "Submit"))
        self.pushButton_Close.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Remove</span></p><p><br/></p></body></html>"))
        self.pushButton_Close.setText(_translate("MainWindow", "Close"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Booking information"))
        self.comboBoxType.setItemText(0, _translate("MainWindow", "VIP"))
        self.comboBoxType.setItemText(1, _translate("MainWindow", "Regular"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Check-out date :</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Room name :</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Room type :</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Rooms:</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Children :</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Booking code :</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Room code :</p></body></html>"))
        self.label_93.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Check-in date :</p><p align=\"center\"><br/></p></body></html>"))
        self.label_102.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Adult :</p></body></html>"))
        self.pushButton_RoomManagement.setText(_translate("MainWindow", "Room Management"))
        self.pushButton.setText(_translate("MainWindow", "New reservation"))
        self.pushButton_BookingManagement.setText(_translate("MainWindow", "Booking Management"))
