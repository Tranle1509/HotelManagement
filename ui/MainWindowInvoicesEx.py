from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.MainWindowInvoices import Ui_MainWindow


class MainWindowInvoicesEx(QMainWindow, Ui_MainWindow):
    def __init__(self, selected_room_code, customer_code, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.customer_code = customer_code
        self.selected_room_code = selected_room_code
        self.customer_filename = "../../dataset/customers.json"
        self.booking_filename = "../../dataset/bookings.json"
        self.room_filename = "../../dataset/rooms.json"
        self.jff = JsonFileFactory()

        self.load_data()
        self.load_invoice_data()

        self.pushButton_calculate.clicked.connect(self.calculate_total)

    def load_data(self):
        """Tải dữ liệu từ JSON"""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []

    def load_invoice_data(self):
        """Tải dữ liệu hóa đơn dựa trên customer_code và room_code"""
        booking = next((b for b in self.bookings
                        if b.customer_code == self.customer_code and b.room_code == self.selected_room_code), None)
        if not booking:
            QMessageBox.warning(self, "Not found", "Cannot find Booking information for this customer!")
            return

        # Tìm thông tin khách hàng
        customer = next((c for c in self.customers if c.customer_code == self.customer_code), None)
        if customer:
            self.lineEdit_customer.setText(customer.customer_name)
            self.lineEdit_customercode.setText(customer.customer_code)
        else:
            QMessageBox.warning(self, "Not found", "Customer information is missing!")
            return

            # Tìm thông tin phòng
        room = next((r for r in self.rooms if r.room_code == self.selected_room_code), None)
        if not room:
            QMessageBox.warning(self, "Not found", "Room information is missing!")
            return

            # Tính số ngày ở
        fmt = "%Y/%m/%d"
        try:
            checkin = datetime.strptime(booking.start_date, fmt)
            checkout = datetime.strptime(booking.end_date, fmt)
            days = max((checkout - checkin).days, 1)
        except Exception as e:
            days = 1
            QMessageBox.warning(self, "Error", f"Invalid date format: {e}")

        self.lineEdit_numberofdays.setText(str(days))
        self.lineEdit_issuedate.setText(datetime.now().strftime("%Y/%m%d"))

        # Cập nhật bảng hóa đơn
        self.tableWidget_invoices.setRowCount(1)  # Chỉ có 1 dòng cho phòng này
        self.tableWidget_invoices.setItem(0, 0, QTableWidgetItem("1"))  # STT
        self.tableWidget_invoices.setItem(0, 1, QTableWidgetItem(room.room_type))  # Loại phòng
        self.tableWidget_invoices.setItem(0, 2, QTableWidgetItem(str(days)))  # Số ngày
        price = 3000000 if room.room_type == "VIP" else 1000000
        self.tableWidget_invoices.setItem(0, 3, QTableWidgetItem(f"{price} VND"))
        self.tableWidget_invoices.setItem(0, 4, QTableWidgetItem(booking.start_date))  # Ngày Check-in
        self.tableWidget_invoices.setItem(0, 5, QTableWidgetItem(booking.end_date))  # Ngày Check-out


    def calculate_total(self):
        """Tính tổng tiền hóa đơn dựa trên dữ liệu trong tableWidget"""
        subtotal = 0.0
        tax_rate = 0.1  # Thuế VAT 10%

        # Kiểm tra xem bảng có dữ liệu không
        if self.tableWidget_invoices.rowCount() == 0:
            QMessageBox.warning(self, "Error", "No data for analyzing!")
            return

        try:
            # Lấy dữ liệu từ bảng
            price_item = self.tableWidget_invoices.item(0, 3)
            days_item = self.tableWidget_invoices.item(0, 2)

            # Kiểm tra ô trống
            if not price_item or not days_item:
                QMessageBox.warning(self, "Error", "Lack of data!")
                return

            # Xử lý chuỗi số (loại bỏ dấu phẩy và ký tự không cần thiết)
            price_str = price_item.text().replace(",", "").replace(" VND", "").strip()
            days_str = days_item.text().strip()

            # Chuyển sang kiểu số
            price = int(price_str)
            days = int(days_str)

            # Tính toán
            subtotal = price * days

            # Cập nhật tổng tiền vào cột 6 (định dạng có dấu phẩy)
            self.tableWidget_invoices.setItem(0, 6, QTableWidgetItem(f"{subtotal:,} VND"))

        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Invalid data: {str(e)}")
            return

        # Tính thuế và tổng
        tax = subtotal * tax_rate
        total_price = subtotal + tax

        # Hiển thị lên giao diện (thêm định dạng tiền tệ)
        self.lineEdit_citprice.setText(f"{subtotal:,.0f} VND")
        self.lineEdit_tax.setText(f"{tax:,.0f} VND")
        self.lineEdit_totalprice.setText(f"{total_price:,.0f} VND")