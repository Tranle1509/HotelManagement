import json
import os
from datetime import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView, QMainWindow
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.MainWindowInvoicesEx import MainWindowInvoicesEx
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
        self.configure_table_appearance()  # Yêu cầu 3
        self.display_rooms(QDate.currentDate())
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def configure_table_appearance(self):
        """Yêu cầu 3: Cấu hình kích thước bảng"""
        self.tableWidget_Room.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_Room.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def setupSignalAndSlot(self):
        self.dateEdit_date.dateChanged.connect(self.update_room_status)
        self.pushButton_vip.clicked.connect(self.sort_vip)
        self.pushButton_regular.clicked.connect(self.sort_regular)
        self.pushButton_all.clicked.connect(self.sort_all)
        self.pushButton_booked.clicked.connect(self.sort_booked)
        self.pushButton_vacant.clicked.connect(self.sort_vacant)
        self.pushButton_checkin.clicked.connect(self.process_checkin)
        self.pushButton_checkout.clicked.connect(self.process_checkout)

    def load_data(self):
        data_folder = "dataset"
        self.load_rooms(os.path.join(data_folder, "D:/FinalProject/dataset/rooms.json"))
        self.load_customers(os.path.join(data_folder, "D:/FinalProject/dataset/customers.json"))
        self.load_bookings(os.path.join(data_folder, "D:/FinalProject/dataset/bookings.json"))

    def load_rooms(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.rooms = [Room(room_data["roomcode"], room_data["roomname"], room_data["roomtype"]) for room_data in
                              data]
        except Exception as e:
            self.show_error_message(f"Lỗi khi tải phòng: {e}")
            self.rooms = []

    def load_customers(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.customers = [Customer(customer_data["code"], customer_data["name"], customer_data["phone"],
                                           customer_data["email"],customer_data["identify"]) for customer_data in data]
        except Exception as e:
            self.show_error_message(f"Lỗi khi tải khách hàng: {e}")
            self.customers = []

    def load_bookings(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.bookings = []
                for booking_data in data:
                    # Sửa định dạng ngày từ "YYYY-MM-DD" sang datetime
                    start_date = datetime.strptime(booking_data["start_date"], "%Y-%m-%d")
                    end_date = datetime.strptime(booking_data["end_date"], "%Y-%m-%d")
                    self.bookings.append(
                        Booking(
                            booking_data["customer_code"],
                            booking_data["room_code"],
                            start_date,
                            end_date
                        )
                    )
        except Exception as e:
            self.show_error_message(f"Lỗi khi tải đặt phòng: {e}")
            self.bookings = []

    def display_rooms(self, selected_date, rooms_to_display=None):
        self.tableWidget_Room.clearContents()
        rooms_to_display = rooms_to_display or self.rooms
        self.selected_rooms = rooms_to_display
        self.tableWidget_Room.setRowCount(len(rooms_to_display))

        for row, room in enumerate(rooms_to_display):
            # Tạo các item và căn giữa
            items = [
                QTableWidgetItem(room.roomcode),
                QTableWidgetItem("Booked" if self.is_room_booked(room.roomcode, selected_date) else "Ready"),
                QTableWidgetItem(self.get_customer_code_for_room(room.roomcode, selected_date) or "N/A"),
                QTableWidgetItem(room.roomtype)
            ]

            # Yêu cầu 2: Đổi màu nền theo trạng thái
            status_color = QColor(255, 0, 0) if items[1].text() == "Booked" else QColor(0, 255, 0)
            for col in range(4):
                items[col].setBackground(QBrush(status_color))
                items[col].setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget_Room.setItem(row, col, items[col])

    def sort_booked(self):
        """Lọc các phòng đang được đặt"""
        booked_rooms = [room for room in self.rooms
                        if self.is_room_booked(room.roomcode, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), booked_rooms)

    def sort_vacant(self):
        """Lọc các phòng còn trống"""
        vacant_rooms = [room for room in self.rooms
                        if not self.is_room_booked(room.roomcode, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), vacant_rooms)

    def is_room_booked(self, room_code, selected_date):
        selected_datetime = datetime(
            selected_date.year(),
            selected_date.month(),
            selected_date.day()
        )
        for booking in self.bookings:
            if booking.room_code == room_code:
                if booking.start_date <= selected_datetime <= booking.end_date:
                    return True
        return False

    def get_customer_code_for_room(self, room_code, selected_date):
        selected_datetime = datetime(
            selected_date.year(),
            selected_date.month(),
            selected_date.day()
        )
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

    def process_checkin(self):
        selected_items = self.tableWidget_Room.selectedItems()
        if not selected_items:
            self.show_error_message("Vui lòng chọn một phòng để check-in.")
            return

        row = selected_items[0].row()
        room_code_item = self.tableWidget_Room.item(row, 0)
        status_item = self.tableWidget_Room.item(row, 1)
        customer_item = self.tableWidget_Room.item(row, 2)
        roomtype_item = self.tableWidget_Room.item(row, 3)

        if not room_code_item or not status_item or not customer_item:
            self.show_error_message("Lỗi khi lấy thông tin phòng.")
            return

        if status_item.text() == "Booked":
            self.show_error_message("Phòng này đã được đặt trước đó.")
            return

        room_code = room_code_item.text()
        confirm = QMessageBox.question(
            self.MainWindow,
            "Xác nhận Check-in",
            f"Xác nhận check-in phòng {room_code}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            new_customer_id = self.generate_new_customer_id()
            status_item.setText("Booked")
            customer_item.setText(new_customer_id)

            # Đổi màu nền thành đỏ
            red_color = QColor(255, 0, 0)
            status_item.setBackground(QBrush(red_color))
            customer_item.setBackground(QBrush(red_color))
            room_code_item.setBackground(QBrush(red_color))
            roomtype_item.setBackground(QBrush(red_color))

            # Thêm dữ liệu đặt phòng mới vào danh sách bookings
            new_booking = Booking(new_customer_id, room_code, datetime.now(), datetime.now())
            self.bookings.append(new_booking)

            QMessageBox.information(self.MainWindow, "Thành công", "Check-in thành công!")

    def generate_new_customer_id(self):
        return f"cus{len(self.customers) + 1:04d}"
    def process_checkout(self):
        selected_items = self.tableWidget_Room.selectedItems()
        if not selected_items:
            self.show_error_message("Vui lòng chọn một phòng để check-out.")
            return

        row = selected_items[0].row()
        room_code_item = self.tableWidget_Room.item(row, 0)
        status_item = self.tableWidget_Room.item(row, 1)
        customer_item = self.tableWidget_Room.item(row, 2)
        roomtype_item = self.tableWidget_Room.item(row, 3)

        if not room_code_item or not status_item or not customer_item:
            self.show_error_message("Lỗi khi lấy thông tin phòng.")
            return

        if status_item.text() != "Booked":
            self.show_error_message("Phòng này chưa được đặt.")
            return

        room_code = room_code_item.text()
        confirm = QMessageBox.question(
            self.MainWindow,
            "Xác nhận Check-out",
            f"Xác nhận check-out phòng {room_code}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            # Cập nhật trạng thái phòng
            status_item.setText("Ready")
            customer_item.setText("N/A")

            # Đổi màu nền thành xanh lá
            green_color = QColor(0, 255, 0)
            status_item.setBackground(QBrush(green_color))
            customer_item.setBackground(QBrush(green_color))
            room_code_item.setBackground(QBrush(green_color))
            roomtype_item.setBackground(QBrush(green_color))

            # Xóa booking khỏi danh sách (nếu cần)
            customer_code = customer_item.text()
            self.bookings = [booking for booking in self.bookings
                             if not (booking.room_code == room_code and booking.customer_code == customer_code)]

            # Hiển thị giao diện hóa đơn
            self.show_invoice_window(room_code, customer_code)  # Gọi hàm hiển thị hóa đơn

    def show_invoice_window(self, room_code, customer_code):
        """Hiển thị giao diện hóa đơn (cần thay thế bằng giao diện thực tế của bạn)."""
        # Ví dụ:
        self.invoice_window = MainWindowInvoicesEx(room_code, customer_code)
        self.invoice_window.show()
        QMessageBox.information(self.MainWindow, "Hóa đơn",
                                f"Hiển thị hóa đơn cho phòng {room_code}, khách hàng {customer_code} (chức năng này chưa được triển khai).")