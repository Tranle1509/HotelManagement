import json
import os
from datetime import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from libs.DataConnector import DataConnector
from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.MainWindowBookingManagement import Ui_MainWindow


class MainWindowBookingManagementEx(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.customers = []
        self.rooms = []
        self.bookings = []
        self.jff = JsonFileFactory()  # Đối tượng xử lý file JSON
        self.customer_filename = "../../dataset/customers.json"
        self.booking_filename = "../../dataset/bookings.json"
        self.room_filename = "../../dataset/rooms.json"

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

        # Load dữ liệu khi mở giao diện
        self.load_data()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass

    def load_data(self):
        """Tải dữ liệu từ JSON vào danh sách đối tượng"""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []

        # Hiển thị danh sách khách hàng và đặt phòng sau khi load dữ liệu
        self.display_data()


    def load_customers(self, filename):
        """ Đọc danh sách khách hàng từ file JSON """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.customers = [Customer(c["code"], c["phone"], c["email"], c["name"], c.get("identity", "")) for c in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Lỗi khi đọc file {filename}: {e}")
            self.customers = []

    def load_bookings(self, filename):
        if not os.path.exists(filename):
            self.bookings = []
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.bookings = [
                    Booking(
                        booking["customer_code"],
                        booking["room_code"],
                        datetime.strptime(booking["start_date"], "%Y-%m-%d"),
                        datetime.strptime(booking["end_date"], "%Y-%m-%d")
                    ) for booking in data
                ]
        except Exception as e:
            self.bookings = []
    def load_rooms(self, filename):
        """ Đọc danh sách phòng từ file JSON """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.rooms = [Room(room["roomcode"], room["roomname"], room["roomtype"]) for room in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Lỗi khi đọc file {filename}: {e}")
            self.rooms = []

    from PyQt6.QtWidgets import QTableWidgetItem
    from PyQt6.QtCore import Qt

    from PyQt6.QtCore import Qt

    def display_data(self):
        """Hiển thị dữ liệu khách hàng và đặt phòng trên bảng."""
        self.tableWidget.clearContents()

        # Xác định số lượng hàng cần hiển thị
        total_rows = max(len(self.customers), len(self.bookings))
        self.tableWidget.setRowCount(total_rows)
        self.tableWidget.setColumnCount(6)  # 6 cột: Name, Phone, Email, Check-in, Check-out, Room type

        self.tableWidget.setHorizontalHeaderLabels(
            ["Name", "Phone number", "Email", "Check-in", "Check-out", "Room type"])

        for row in range(total_rows):
            # Lấy dữ liệu khách hàng nếu có
            if row < len(self.customers):
                customer = self.customers[row]
                self.set_table_item(row, 0, customer.name)
                self.set_table_item(row, 1, customer.phone)
                self.set_table_item(row, 2, customer.email)
            else:
                # Nếu không có khách hàng, điền "N/A"
                for col in range(3):
                    self.set_table_item(row, col, "N/A")

            # Tìm booking tương ứng
            booking = next((b for b in self.bookings if b.customer_code == self.customers[row].code),
                           None) if row < len(self.customers) else None

            if booking:
                # self.set_table_item(row, 3, booking.start_date.strftime("%Y-%m-%d"))
                # self.set_table_item(row, 4, booking.end_date.strftime("%Y-%m-%d"))

                # Tìm phòng tương ứng
                room = next((r for r in self.rooms if r.roomcode == booking.room_code), None)
                self.set_table_item(row, 5, room.roomtype if room else "N/A")
            else:
                # Nếu không có đặt phòng, điền "N/A"
                for col in range(3, 6):
                    self.set_table_item(row, col, "N/A")

    def set_table_item(self, row, col, text):
        """Thiết lập ô chỉ đọc với nội dung cụ thể."""
        item = QTableWidgetItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)  # Chỉ cho phép xem, không cho chỉnh sửa
        self.tableWidget.setItem(row, col, item)
