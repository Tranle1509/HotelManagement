from PyQt6.QtWidgets import QMainWindow, QMessageBox

from libs.DataConnector import DataConnector
from ui.LoginMainWindow import Ui_MainWindow
from ui.MainWindowManagementEx import MainWindowManagementEx


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
        dc = DataConnector()
        uid = self.lineEditUserName.text().strip()
        pwd = self.lineEditPassword.text().strip()
        role = self.comboBoxRole.currentText().strip()

        employees = dc.get_all_employees()

        # Kiểm tra xem username và password có đúng không
        emp = next((e for e in employees if e.UserName == uid and e.Password == pwd), None)

        if emp is None:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Login Failed! Invalid username or password.")
            self.msg.exec()
        elif emp.EmployeeRole != role:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Login Failed! Incorrect role selected.")
            self.msg.exec()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Login Successful!")
            self.msg.exec()
            self.MainWindow.close()  # Đóng cửa sổ đăng nhập
            self.mainwindow = QMainWindow()
            self.myui = MainWindowManagementEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()

    def process_show_role(self):
        # Xóa danh sách cũ trước khi cập nhật
        self.comboBoxRole.clear()

        # Lấy danh sách tất cả nhân viên từ DataConnector
        employees = self.dc.get_all_employees()

        # Kiểm tra dữ liệu có rỗng không
        if not employees:
            print("No employees found!")  # Debug thông tin
            return

        # Lọc danh sách vai trò không trùng nhau, loại bỏ khoảng trắng và giá trị None
        unique_roles = sorted(set(emp.EmployeeRole.strip() for emp in employees if emp.EmployeeRole))

        # Kiểm tra danh sách role có giá trị không
        if not unique_roles:
            print("No roles available!")  # Debug nếu danh sách role rỗng
            return

        # Thêm danh sách role duy nhất vào comboBoxRole
        self.comboBoxRole.addItems(unique_roles)

        # Mở dropdown (chỉ khi có dữ liệu)
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