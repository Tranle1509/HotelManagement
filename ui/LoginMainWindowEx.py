from PyQt6.QtWidgets import QMainWindow, QMessageBox

from libs.DataConnector import DataConnector

from ui.LoginMainWindow import Ui_MainWindow



class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.employees = self.dc.get_all_employees()
        self.selected_role = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.comboBoxRole.mousePressEvent = lambda event: self.process_show_role()
        self.comboBoxRole.currentIndexChanged.connect(self.filter_role)
        self.pushButtonBack.clicked.connect(self.process_back)
    def process_login(self):
        from ui.NewReservationMainWindowExt import MainWindow_NewReservationExt
        dc = DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)
        if emp is not None:
            self.MainWindow.close()  # Đóng cửa sổ đăng nhập
            self.mainwindow = QMainWindow()
            self.myui = MainWindow_NewReservationExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()

    def process_show_role(self):
        # Xóa danh sách cũ trong ComboBox trước khi cập nhật
        self.comboBoxRole.clear()

        # Lấy danh sách tất cả employees từ DataConnector
        employees = self.dc.get_all_employees()

        # Lấy danh sách role không trùng nhau bằng set
        unique_roles = sorted(set(emp.EmployeeRole.strip() for emp in employees))

        # Thêm danh sách role duy nhất vào comboBoxRole
        self.comboBoxRole.addItems(unique_roles)

        # Hiển thị dropdown
        self.comboBoxRole.showPopup()
    def filter_role(self):
        # Lấy category ID đang được chọn
        selected_role = self.comboBoxRole.currentText().strip()
        if not selected_role:
            return
    def process_back(self):
        from ui.HomePageMainWindowEx import HomePageMainWindowEx
        self.MainWindow.close()  # close login window
        self.mainwindow = QMainWindow()
        self.myui = HomePageMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
