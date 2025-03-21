import numpy as np
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from matplotlib.colors import LinearSegmentedColormap

from libs.DataConnector import DataConnector
from ui.LoginMainWindow import Ui_MainWindow
from ui.MainWindowManagementEx import MainWindowManagementEx
from matplotlib import pyplot as plt
import seaborn as sns


class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.employees = self.dc.get_all_employees()
        self.selected_role = None
        self.report_window = None
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

        # Kiểm tra username và password
        emp = next((e for e in employees if e.UserName == uid and e.Password == pwd), None)

        if emp is None:
            self.show_message("Login Failed! Invalid username or password.")
        elif emp.EmployeeRole != role:
            self.show_message("Login Failed! Incorrect role selected.")
        else:
            self.show_message("Login Successful!")
            self.open_main_window(role)

    def open_main_window(self, role):
        """ Mở giao diện chính và thiết lập quyền dựa trên vai trò """
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowManagementEx()
        self.myui.setupUi(self.mainwindow)

        if role == "Officer":
            self.restrict_officer_permissions()  # Chặn chỉnh sửa nếu là Staff
        elif role == "Staff":
            self.restrict_staff_permissions()
        self.myui.showWindow()

    def restrict_officer_permissions(self):
        """ Chặn quyền chỉnh sửa của Officer, nhưng vẫn cho phép xem Booking và ấn Report """
        disable_list = [self.myui.pushButtonDelete, self.myui.pushButtonUpdate]
        for widget in disable_list:
            widget.setEnabled(False)

        # Đảm bảo nút Report vẫn hoạt động, chỉ kết nối một lần
        try:
            self.myui.pushButtonReport.clicked.disconnect()
        except TypeError:
            pass  # Nếu chưa có kết nối nào, bỏ qua lỗi này

        self.myui.pushButtonReport.setEnabled(True)
        self.myui.pushButtonReport.clicked.connect(self.show_report)

        # Ẩn hoặc vô hiệu hóa các Tab khác ngoài "Booking Management"
        for i in range(self.myui.tabWidget.count()):
            tab_text = self.myui.tabWidget.tabText(i)
            if tab_text != "Booking Management":
                self.myui.tabWidget.setTabEnabled(i, False)  # Chỉ disable, không xóa

        # Chuyển Tab về "Booking Management" khi đăng nhập
        self.myui.tabWidget.setCurrentIndex(self.get_tab_index("Booking Management"))

    def show_report(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Select Report Type")
        msg.setText("How would you like to view the report?")

        # Tạo các nút bấm
        barchart_button = msg.addButton("Barchart", QMessageBox.ButtonRole.AcceptRole)
        heatmap_button = msg.addButton("Heatmap", QMessageBox.ButtonRole.RejectRole)
        cancel_button = msg.addButton("Cancel", QMessageBox.ButtonRole.NoRole)

        msg.exec()  # Hiển thị hộp thoại

        # Kiểm tra nút nào được bấm
        if msg.clickedButton() == barchart_button:
            self.open_booking_report()
        elif msg.clickedButton() == heatmap_button:
            self.open_heatmap_report()

    def open_booking_report(self):
        from RoomBookingReport.MainWindowEx import MainWindowEx
        self.report_window = MainWindowEx()  # Tạo một thể hiện của cửa sổ
        self.report_window.show()  # Hiển thị cửa sổ

    def open_heatmap_report(self):
        # Top 8 countries visiting Maldives Hotels
        countries = ['China', 'India', 'Russia', 'Germany', 'United Kingdom',
                     'Italy', 'United States', 'France']

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # Generate random data for hotel visitors
        np.random.seed(42)
        customer_data = pd.DataFrame(np.random.randint(500, 5000, size=(8, 12)), index=countries, columns=months)

        # Sort by total number of visitors
        customer_data["Total"] = customer_data.sum(axis=1)
        customer_data = customer_data.sort_values(by="Total", ascending=False)
        customer_data = customer_data.drop(columns=["Total"])  # Remove the total column after sorting

        # Custom colormap
        custom_cmap = LinearSegmentedColormap.from_list("custom_palette", [
            '#dbdcd7', '#dddcd7', '#e2c9cc', '#e7627d',
            '#b8235a', '#801357', '#3d1635', '#1c1a27'
        ])

        # Plot heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(customer_data, annot=True, fmt='d', linewidths=.5, cmap=custom_cmap)

        plt.title('Top 8 Countries Visiting Maldives Hotels Over 12 Months', fontsize=14)
        plt.xlabel('Months', fontsize=12)
        plt.ylabel('Country', fontsize=12)
        plt.xticks(rotation=45)  # Rotate month labels for better readability
        plt.show()

    def get_tab_index(self, tab_name):
        """ Trả về index của tab dựa vào tên """
        for i in range(self.myui.tabWidget.count()):
            if self.myui.tabWidget.tabText(i) == tab_name:
                return i
        return 0  # Nếu không tìm thấy, mặc định về tab đầu tiên

    def restrict_staff_permissions(self):
        """ Chặn quyền nhấn nút Report cho Staff nhưng vẫn cho phép các chức năng khác """
        self.myui.pushButtonReport.setEnabled(False)  # Chặn nút Report

    def show_message(self, text):
        """ Hiển thị thông báo """
        msg = QMessageBox(self.MainWindow)
        msg.setText(text)
        msg.exec()

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