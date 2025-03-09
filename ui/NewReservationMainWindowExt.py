from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton

from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from ui.MainWindowBookingManagementExt import MainWindowBookingManagementEx
from ui.New_reservationMainWindow import Ui_MainWindow


class MainWindow_NewReservationExt(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.jff = JsonFileFactory()  # Đối tượng xử lý file JSON
        self.customer_filename = "../../dataset/customers.json"
        self.booking_filename = "../../dataset/bookings.json"
        self.hotel_management_window = None  # Biến để lưu cửa sổ Hotel Management
        self.setupUi(self)  # Gọi hàm setup UI từ file Qt Designer

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Kết nối nút Save với phương thức save_data
        self.pushButton_Save.clicked.connect(self.save_data)
        self.pushButton_Close.clicked.connect(self.close)
        self.pushButton_Clear.clicked.connect(self.clear_data)
        self.pushButton_BookingManagement.clicked.connect(self.open_hotel_management)
    def showWindow(self):
        self.MainWindow.show()

    def close(self):
        self.MainWindow.close()

    def save_data(self):
        """ Lưu thông tin khách hàng và đặt phòng vào JSON """
        try:
            # ===== Lấy dữ liệu từ giao diện =====
            # Lấy thông tin khách hàng
            cus_code = self.lineEdit_Cuscode.text().strip()
            cus_phone = self.lineEdit_Phone.text().strip()
            cus_name = self.lineEdit_Cusname.text().strip()
            cus_email = self.lineEdit_Email.text().strip()
            cus_identify = self.lineEdit_Identify.text().strip()

            # Lấy thông tin đặt phòng
            room_code = self.lineEdit_Roomcode.text().strip()
            start_date = self.CheckIn.text().strip()
            end_date = self.CheckOut.text().strip()

            # Kiểm tra nếu thiếu mã khách hàng hoặc mã phòng -> không lưu
            if not cus_code or not room_code:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Mã khách hàng và mã phòng không được để trống!")
                return

            # ======= Đọc dữ liệu cũ từ file JSON =======
            customers = self.jff.read_data(self.customer_filename, Customer)
            bookings = self.jff.read_data(self.booking_filename, Booking)

            # ======= Thêm dữ liệu mới vào danh sách =======


            # Thêm booking mới
            booking = Booking(cus_code, room_code, start_date, end_date)
            bookings.append(booking)

            customer=Customer(cus_code,cus_phone,cus_email,cus_name,cus_identify)
            customers.append(customer)

            # ======= Lưu lại vào file JSON =======
            self.jff.write_data(customers, self.customer_filename)
            self.jff.write_data(bookings, self.booking_filename)

            # Hiển thị thông báo thành công
            QMessageBox.information(self.MainWindow, "Thành công", "Dữ liệu đã được lưu!")

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lưu dữ liệu thất bại:\n{str(e)}")



    def clear_data(self):
        """ Xóa nội dung của các ô nhập liệu """
        self.lineEdit_Cuscode.clear()
        self.lineEdit_Phone.clear()
        self.lineEdit_Cusname.clear()
        self.lineEdit_Email.clear()
        self.lineEdit_Identify.clear()
        self.lineEdit_Roomcode.clear()
        self.lineEditChildren.clear()
        self.lineEditAdult.clear()
        self.lineEdit_Requirement.clear()
        self.lineEdit_BookingCode.clear()
        self.lineEdit_Roomname.clear()

    def open_hotel_management(self):
        """ Mở cửa sổ Hotel Management """
        if self.hotel_management_window is None:
            self.hotel_management_window = QMainWindow()
            self.hotel_management_ui = MainWindowBookingManagementEx()
            self.hotel_management_ui.setupUi(self.hotel_management_window)
        self.hotel_management_window.show()