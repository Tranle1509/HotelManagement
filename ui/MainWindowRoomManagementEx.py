import json
import os
from datetime import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.MainWindowRoomManagement import Ui_MainWindow


class MainWindowRoomManagementEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.rooms = []
        self.customers = []
        self.bookings = []
        self.selected_rooms = []
        self.load_data()
        self.configure_table_appearance()
        self.display_rooms(QDate.currentDate())
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def configure_table_appearance(self):
        """Cấu hình bảng"""
        self.tableWidget_Room.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_Room.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def setupSignalAndSlot(self):
        self.dateEdit_date.dateChanged.connect(self.update_room_status)
        self.pushButton_vip.clicked.connect(self.sort_vip)
        self.pushButton_regular.clicked.connect(self.sort_regular)
        self.pushButton_all.clicked.connect(self.sort_all)
        self.pushButton_booked.clicked.connect(self.sort_booked)
        self.pushButton_vacant.clicked.connect(self.sort_vacant)

    def load_data(self):
        data_folder = "dataset"
        self.load_rooms(os.path.join(data_folder, "../../../dataset/rooms.json"))
        self.load_customers(os.path.join(data_folder, "../../../dataset/customers.json"))
        self.load_bookings(os.path.join(data_folder, "../../../dataset/bookings.json"))

    def load_rooms(self, filename):
        if not os.path.exists(filename):
            self.show_error_message(f"LỖI: Không tìm thấy tệp {filename}")
            self.rooms = []
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.rooms = [Room(room["roomcode"], room["roomname"], room["roomtype"]) for room in data]
        except Exception as e:
            self.show_error_message(f"Lỗi khi tải phòng: {e}")
            self.rooms = []

    def load_customers(self, filename):
        if not os.path.exists(filename):
            self.show_error_message(f"LỖI: Không tìm thấy tệp {filename}")
            self.customers = []
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.customers = [Customer(customer["code"], customer["name"], customer["phone"],
                                           customer["email"], customer["identify"]) for customer in data]
        except Exception as e:
            self.show_error_message(f"Lỗi khi tải khách hàng: {e}")
            self.customers = []

    def load_bookings(self, filename):
        if not os.path.exists(filename):
            self.show_error_message(f"LỖI: Không tìm thấy tệp {filename}")
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
            self.show_error_message(f"Lỗi khi tải đặt phòng: {e}")
            self.bookings = []

    def display_rooms(self, selected_date, rooms_to_display=None):
        self.tableWidget_Room.clearContents()
        rooms_to_display = rooms_to_display or self.rooms
        self.selected_rooms = rooms_to_display
        self.tableWidget_Room.setRowCount(len(rooms_to_display))

        for row, room in enumerate(rooms_to_display):
            # Tạo các item
            items = [
                QTableWidgetItem(room.roomcode),
                QTableWidgetItem("Booked" if self.is_room_booked(room.roomcode, selected_date) else "Ready"),
                QTableWidgetItem(self.get_customer_code_for_room(room.roomcode, selected_date) or "N/A"),
                QTableWidgetItem(room.roomtype)
            ]

            # Đổi màu nền theo trạng thái
            status_color = QColor(255, 218, 185) if items[1].text() == "Booked" else QColor(175, 238, 238)
            for col in range(4):
                items[col].setBackground(QBrush(status_color))
                items[col].setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget_Room.setItem(row, col, items[col])

    def sort_booked(self):
        """Lọc các phòng đang được đặt"""
        booked_rooms = [room for room in self.rooms if self.is_room_booked(room.roomcode, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), booked_rooms)

    def sort_vacant(self):
        """Lọc các phòng còn trống"""
        vacant_rooms = [room for room in self.rooms if
                        not self.is_room_booked(room.roomcode, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), vacant_rooms)

    def is_room_booked(self, room_code, selected_date):
        selected_datetime = datetime(selected_date.year(), selected_date.month(), selected_date.day())
        for booking in self.bookings:
            if booking.room_code == room_code:
                if booking.start_date <= selected_datetime <= booking.end_date:
                    return True
        return False

    def get_customer_code_for_room(self, room_code, selected_date):
        selected_datetime = datetime(selected_date.year(), selected_date.month(), selected_date.day())
        for booking in self.bookings:
            if booking.room_code == room_code:
                if booking.start_date <= selected_datetime <= booking.end_date:
                    return booking.customer_code
        return None

    def update_room_status(self):
        selected_date = self.dateEdit_date.date()
        self.display_rooms(selected_date, self.selected_rooms)

    def sort_vip(self):
        vip_rooms = [room for room in self.rooms if room.roomtype == "VIP"]
        self.display_rooms(self.dateEdit_date.date(), vip_rooms)

    def sort_regular(self):
        regular_rooms = [room for room in self.rooms if room.roomtype == "Regular"]
        self.display_rooms(self.dateEdit_date.date(), regular_rooms)

    def sort_all(self):
        self.display_rooms(self.dateEdit_date.date())

    def show_error_message(self, message):
        QMessageBox.critical(self.MainWindow, "Lỗi", message)
