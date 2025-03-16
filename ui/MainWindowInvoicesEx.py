import json
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from fpdf import FPDF

from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.MainWindowInvoices import Ui_MainWindow


class MainWindowInvoicesEx(QMainWindow, Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.rooms = []
        self.customers = []
        self.bookings = []
    def __init__(self, selected_room_code,customer_code, parent=None):
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
    def load_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot load data from {file_path}: {e}")
            return []

    def load_invoice_data(self):
        """Tải dữ liệu hóa đơn dựa trên room_code và customer_code"""
        booking = next((b for b in self.bookings if b.room_code == self.selected_room_code), None)

        if booking is None:
            QMessageBox.warning(self, "Not found", "Cannot found Booking information!")
            return

        # Tìm khách hàng và phòng
        customer_code_from_booking = booking.customer_code  # Giả sử booking có thuộc tính customer_code
        customer = next((c for c in self.customers if c.customer_code == customer_code_from_booking), None)

        room = next((r for r in self.rooms if r.room_code == booking.room_code), None)

        # Hiển thị thông tin khách hàng nếu tìm thấy
        if customer:
            self.lineEdit_customer.setText(customer.customer_name)
            self.lineEdit_customercode.setText(customer.customer_code)

        self.lineEdit_issuedate.setText(datetime.today().strftime("%Y-%m-%d"))

        # Chuyển đổi ngày tháng từ string về datetime
        start_date = datetime.strptime(booking.start_date, "%Y/%m/%d")
        end_date = datetime.strptime(booking.end_date, "%Y/%m/%d")

        # Tính số ngày ở
        self.lineEdit_numberofdays.setText(str((end_date - start_date).days))

        # Hiển thị thông tin phòng nếu tìm thấy
        if room:
            self.tableWidget_invoices.setRowCount(1)
            self.tableWidget_invoices.setItem(0, 0, QTableWidgetItem("1"))
            self.tableWidget_invoices.setItem(0, 1, QTableWidgetItem(room.room_type))

            quantity=str((end_date - start_date).days)
            self.tableWidget_invoices.setItem(0, 2, QTableWidgetItem(quantity))

            price = 9000000 if room.room_type == "VIP" else 1000000
            self.tableWidget_invoices.setItem(0, 3, QTableWidgetItem(str(price)))
            self.tableWidget_invoices.setItem(0, 4, QTableWidgetItem(booking.start_date))
            self.tableWidget_invoices.setItem(0, 5, QTableWidgetItem(booking.end_date))

    def calculate_total(self):
        """Tính tổng tiền hóa đơn dựa trên dữ liệu trong tableWidget"""
        subtotal = 0.0
        tax_rate = 0.1  # Thuế VAT 10%

        # Kiểm tra xem bảng có dữ liệu không
        if self.tableWidget_invoices.rowCount() == 0:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu để tính toán!")
            return

        for row in range(self.tableWidget_invoices.rowCount()):
            try:
                # Lấy dữ liệu từ bảng
                price_item = self.tableWidget_invoices.item(row, 3)
                days_item = self.tableWidget_invoices.item(row, 2)

                # Kiểm tra ô trống
                if not price_item or not days_item:
                    QMessageBox.warning(self, "Lỗi", f"Thiếu dữ liệu ở hàng {row + 1}!")
                    return

                # Xử lý chuỗi số (loại bỏ dấu phẩy và ký tự không cần thiết)
                price_str = price_item.text().replace(",", "").replace(" VND", "").strip()
                days_str = days_item.text().strip()

                # Chuyển sang kiểu số
                price = int(price_str)
                days = int(days_str)

                # Tính toán
                total = price * days
                subtotal += total

                # Cập nhật tổng tiền vào cột 4 (định dạng có dấu phẩy)
                self.tableWidget_invoices.setItem(row, 4, QTableWidgetItem(f"{total:,} VND"))

            except ValueError as e:
                QMessageBox.critical(self, "Lỗi", f"Dữ liệu không hợp lệ ở hàng {row + 1}: {str(e)}")
                return

        # Tính thuế và tổng
        tax = subtotal * tax_rate
        total_price = subtotal + tax

        # Hiển thị lên giao diện (thêm định dạng tiền tệ)
        self.lineEdit_citprice.setText(f"{subtotal:,.0f} VND")
        self.lineEdit_tax.setText(f"{tax:,.0f} VND")
        self.lineEdit_totalprice.setText(f"{total_price:,.0f} VND")

    def load_data(self):
        """Tải dữ liệu từ JSON và cập nhật bảng."""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []

