from PyQt6.QtWidgets import QMainWindow, QMessageBox

from LoginUi.LoginMainWindow import Ui_MainWindow
from libs.DataConenctors import DataConnector


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.comboBoxRole.mousePressEvent = lambda event: self.process_show_EmployeeRole()
    def process_login(self):
        dc=DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)
        '''if emp != None:
            self.MainWindow.close()#close login window
            self.mainwindow = QMainWindow()
            self.myui = MainWindow85Ext()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Login Failed")
            self.msg.exec()'''

    def process_show_EmployeeRole(self):
        dc=DataConnector()
        # Xóa danh sách cũ trong ComboBox trước khi cập nhật
        self.comboBoxRole.clear()

        # Lấy danh sách tất cả category từ DataConnector
        employees = self.dc.get_all_employees()

        # Thêm từng category ID vào comboBoxCateId
        for emp in employees:
            self.comboBoxRole.addItem(str(emp.EmployeeRole))

        # Hiển thị dropdown
        self.comboBoxRole.showPopup()


