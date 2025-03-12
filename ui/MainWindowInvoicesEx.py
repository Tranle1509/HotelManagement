import json
from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
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
        self.bookings = self.load_json("D:/FinalProject/dataset/bookings.json")
        self.customers = self.load_json("D:/FinalProject/dataset/customers.json")
        self.rooms = self.load_json("D:/FinalProject/dataset/rooms.json")
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
        booking = next((b for b in self.bookings if b["room_code"] == self.selected_room_code), None)
        if not booking:
            QMessageBox.warning(self, "Thông báo", "Không tìm thấy thông tin đặt phòng.")
            return

        customer = next((c for c in self.customers if c["code"] == booking["customer_code"]), None)
        room = next((r for r in self.rooms if r["roomcode"] == booking["room_code"]), None)

        if customer:
            self.lineEdit_customer.setText(customer["name"])
        self.lineEdit_bookingcode.setText(booking["customer_code"])
        self.lineEdit_issuedate.setText(datetime.today().strftime("%Y-%m-%d"))
        self.lineEdit_numberofdays.setText(str((datetime.strptime(booking["end_date"], "%Y-%m-%d") - datetime.strptime(
            booking["start_date"], "%Y-%m-%d")).days))

        if room:
            self.tableWidget_invoices.setRowCount(1)
            self.tableWidget_invoices.setItem(0, 0, QTableWidgetItem("1"))
            self.tableWidget_invoices.setItem(0, 1, QTableWidgetItem(room["roomtype"]))
            self.tableWidget_invoices.setItem(0, 2, QTableWidgetItem("1"))
            self.tableWidget_invoices.setItem(0, 3, QTableWidgetItem("100"))
            self.tableWidget_invoices.setItem(0, 4, QTableWidgetItem(booking["start_date"]))
            self.tableWidget_invoices.setItem(0, 5, QTableWidgetItem(booking["end_date"]))
    def calculate_total(self):
        subtotal = 0.0
        for row in range(self.tableWidget_invoices.rowCount()):
            try:
                quantity = float(self.tableWidget_invoices.item(row, 1).text()) if self.tableWidget_invoices.item(row, 1) else 0.0
                price = float(self.tableWidget_invoices.item(row, 2).text()) if self.tableWidget_invoices.item(row, 2) else 0.0
                total = quantity * price
                subtotal += total
                self.tableWidget_invoices.setItem(row, 3, QTableWidgetItem(str(total))) # Cập nhật thành tiền
            except ValueError:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập số hợp lệ cho số lượng và đơn giá.")
                return

        tax_rate = 0.1
        tax = subtotal * tax_rate
        total = subtotal + tax

        self.lineEdit_citprice.setText(str(subtotal))
        self.lineEdit_tax.setText(str(tax))
        self.lineEdit_totalprice.setText(str(total))

    def export_invoice(self):
        QMessageBox.information(self, "Xuất hóa đơn", "Hóa đơn đã được xuất thành công!")
