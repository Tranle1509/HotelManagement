import json
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


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
        self.pushButton_export.clicked.connect(self.export_invoice)

    def load_json(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu từ {file_path}: {e}")
            return []

    def load_invoice_data(self):
        """Tải dữ liệu hóa đơn dựa trên room_code và customer_code"""
        booking = next((b for b in self.bookings if b.room_code == self.selected_room_code), None)

        if booking is None:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin đặt phòng!")
            return  # Thoát khỏi hàm nếu không có booking hợp lệ

        # Tìm khách hàng và phòng
        customer = next((c for c in self.customers if c.customer_code == self.customer_code), None)
        room = next((r for r in self.rooms if r.room_code == booking.room_code), None)

        # Hiển thị thông tin khách hàng nếu tìm thấy
        if customer:
            self.lineEdit_customer.setText(customer.customer_name)  # 🔹 Sử dụng thuộc tính thay vì key dict

        # Cập nhật thông tin booking vào giao diện
        self.lineEdit_bookingcode.setText(booking.customer_code)  # 🔹 Truy xuất đúng thuộc tính
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
            self.tableWidget_invoices.setItem(0, 2, QTableWidgetItem("1"))
            self.tableWidget_invoices.setItem(0, 3, QTableWidgetItem("100"))  # Giá tạm thời
            self.tableWidget_invoices.setItem(0, 4, QTableWidgetItem(booking.start_date))
            self.tableWidget_invoices.setItem(0, 5, QTableWidgetItem(booking.end_date))

    def calculate_total(self):
        """Tính tổng tiền hóa đơn dựa trên loại phòng"""
        subtotal = 0.0
        tax_rate = 0.1  # Thuế VAT 10%

        for row in range(self.tableWidget_invoices.rowCount()):
            try:
                room_type = self.tableWidget_invoices.item(row, 1).text() if self.tableWidget_invoices.item(row,
                                                                                                            1) else ""

                # Xác định giá theo loại phòng
                if room_type == "Regular":
                    price = 1_000_000
                elif room_type == "VIP":
                    price = 9_000_000
                else:
                    price = 0  # Nếu không xác định được loại phòng

                # Lấy số lượng ngày ở
                days = int(self.lineEdit_numberofdays.text()) if self.lineEdit_numberofdays.text().isdigit() else 1

                total = price * days  # Tổng tiền cho phòng đó
                subtotal += total

                # Cập nhật vào bảng
                self.tableWidget_invoices.setItem(row, 2, QTableWidgetItem(str(days)))
                self.tableWidget_invoices.setItem(row, 3, QTableWidgetItem(str(price)))
                self.tableWidget_invoices.setItem(row, 4, QTableWidgetItem(str(total)))

            except ValueError:
                QMessageBox.warning(self, "Lỗi", "Dữ liệu không hợp lệ! Kiểm tra số ngày và loại phòng.")
                return

        tax = subtotal * tax_rate  # Tính thuế
        total_price = subtotal + tax  # Tổng tiền sau thuế

        # Hiển thị lên giao diện
        self.lineEdit_citprice.setText(f"{subtotal:,.0f} VND")
        self.lineEdit_tax.setText(f"{tax:,.0f} VND")
        self.lineEdit_totalprice.setText(f"{total_price:,.0f} VND")

    def export_invoice(self):
        """Xuất hóa đơn ra file PDF"""
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        # Tiêu đề
        pdf.cell(200, 10, "HÓA ĐƠN THANH TOÁN", ln=True, align="C")
        pdf.ln(10)

        # Thông tin khách hàng
        pdf.set_font("Arial", "", 12)
        pdf.cell(50, 10, f"Khách hàng: {self.lineEdit_customer.text()}", ln=True)
        pdf.cell(50, 10, f"Mã đặt phòng: {self.lineEdit_bookingcode.text()}", ln=True)
        pdf.cell(50, 10, f"Ngày xuất hóa đơn: {self.lineEdit_issuedate.text()}", ln=True)
        pdf.cell(50, 10, f"Số ngày ở: {self.lineEdit_numberofdays.text()} ngày", ln=True)
        pdf.ln(5)

        # Bảng chi tiết hóa đơn
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(30, 10, "STT", 1, 0, "C", True)
        pdf.cell(50, 10, "Loại phòng", 1, 0, "C", True)
        pdf.cell(30, 10, "Số ngày", 1, 0, "C", True)
        pdf.cell(40, 10, "Giá/ngày (VND)", 1, 0, "C", True)
        pdf.cell(40, 10, "Thành tiền", 1, 1, "C", True)

        pdf.set_font("Arial", "", 12)
        for row in range(self.tableWidget_invoices.rowCount()):
            pdf.cell(30, 10, str(row + 1), 1, 0, "C")
            pdf.cell(50, 10, self.tableWidget_invoices.item(row, 1).text(), 1, 0, "C")
            pdf.cell(30, 10, self.tableWidget_invoices.item(row, 2).text(), 1, 0, "C")
            pdf.cell(40, 10, self.tableWidget_invoices.item(row, 3).text(), 1, 0, "C")
            pdf.cell(40, 10, self.tableWidget_invoices.item(row, 4).text(), 1, 1, "C")

        # Tổng tiền
        pdf.ln(5)
        pdf.cell(100, 10, "Tổng tiền trước thuế:", 0, 0)
        pdf.cell(40, 10, self.lineEdit_citprice.text(), 0, 1, "R")

        pdf.cell(100, 10, "Thuế (10%):", 0, 0)
        pdf.cell(40, 10, self.lineEdit_tax.text(), 0, 1, "R")

        pdf.cell(100, 10, "Tổng tiền thanh toán:", 0, 0, "B")
        pdf.cell(40, 10, self.lineEdit_totalprice.text(), 0, 1, "RB")

        # Lưu file PDF
        file_path = "D:/demo/dataset/invoice.pdf"
        try:
            pdf.output(file_path)
            QMessageBox.information(self, "Xuất hóa đơn", f"Hóa đơn đã được lưu tại: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể lưu hóa đơn: {e}")
    def load_data(self):
        """Tải dữ liệu từ JSON và cập nhật bảng."""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []

