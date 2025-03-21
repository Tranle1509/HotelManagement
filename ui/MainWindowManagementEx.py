import json
import os
from datetime import datetime

import numpy as np
import pandas as pd
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QTableWidgetItem, QInputDialog
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

from libs.DataConnector import DataConnector
from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
from ui.HomePageMainWindowEx import HomePageMainWindowEx
from ui.MainWindowInvoicesEx import MainWindowInvoicesEx
from ui.MainWindowManagement import Ui_MainWindow


class MainWindowManagementEx(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.customers = []
        self.rooms = []
        self.bookings = []
        self.jff = JsonFileFactory()
        self.customer_filename = "D:/FinalProject/dataset/customers.json"
        self.booking_filename = "D:/FinalProject/dataset/bookings.json"
        self.room_filename = "../../dataset/rooms.json"

        self.setupUi(self)
        self.configure_table_appearance()  # 🔹 Cấu hình bảng sau khi UI đã load
        self.load_data()  # 🔹 Load dữ liệu từ file JSON
        self.display_rooms(QDate.currentDate())  # 🔹 Gọi hiển thị phòng sau khi UI sẵn sàng
        self.setupSignalAndSlot()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.load_data()
        self.configure_table_appearance()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Save.clicked.connect(self.save_data)
        self.pushButton_Logout.clicked.connect(self.logout)
        self.dateEdit_date.dateChanged.connect(self.update_room_status)
        self.pushButton_vip.clicked.connect(self.sort_vip)
        self.pushButton_regular.clicked.connect(self.sort_regular)
        self.pushButton_all.clicked.connect(self.sort_all)
        self.pushButton_booked.clicked.connect(self.sort_booked)
        self.pushButton_vacant.clicked.connect(self.sort_vacant)
        self.pushButton_checkin.clicked.connect(self.process_checkin)
        self.pushButton_checkout.clicked.connect(self.process_checkout)
        self.tableWidget.itemClicked.connect(self.display_selected_row_data)
        self.pushButtonUpdate.clicked.connect(self.update_selected_row)
        self.pushButtonDelete.clicked.connect(self.delete_selected_row)
        self.pushButtonsearch.clicked.connect(self.search_booking)
        self.pushButton_Clear.clicked.connect(self.clear_reservation_data)
        self.pushButtonReport.clicked.connect(self.show_report)

    def load_data(self):
        """Tải dữ liệu từ JSON và cập nhật bảng."""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []
        self.display_data()

    def display_data(self):
        """Hiển thị dữ liệu khách hàng và đặt phòng trên bảng với kích thước cố định."""
        self.tableWidget.clearContents()

        total_rows = max(len(self.customers), len(self.bookings))
        self.tableWidget.setRowCount(total_rows)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Check-in", "Check-out", "Room code"])

        for row in range(total_rows):
            # 🔹 Hiển thị số thứ tự (STT) ở cột đầu tiên
            self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(str(row + 1)))

            customer = self.customers[row] if row < len(self.customers) else None
            if customer:
                self.set_table_item(row, 0, customer.customer_name)
                self.set_table_item(row, 1, customer.customer_phone)
                self.set_table_item(row, 2, customer.customer_email)
            else:
                for col in range(3):
                    self.set_table_item(row, col, "N/A")

            booking = next((b for b in self.bookings if customer and b.customer_code == customer.customer_code), None)
            if booking:
                self.set_table_item(row, 3, booking.start_date)
                self.set_table_item(row, 4, booking.end_date)

                room = next((r for r in self.rooms if r.room_code == booking.room_code), None)
                self.set_table_item(row, 5, room.room_code if room else "N/A")
            else:
                for col in range(3, 6):
                    self.set_table_item(row, col, "N/A")

        # 🔹 Cố định kích thước cột (đơn vị: pixel)
        self.tableWidget.setColumnWidth(0, 100)  # Name
        self.tableWidget.setColumnWidth(1, 100)  # Phone
        self.tableWidget.setColumnWidth(2, 180)  # Email
        self.tableWidget.setColumnWidth(3, 100)  # Check-in
        self.tableWidget.setColumnWidth(4, 100)  # Check-out
        self.tableWidget.setColumnWidth(5, 100)  # Room code

        # 🔹 Cố định kích thước hàng (cao hơn để dễ nhìn)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        # 🔹 Căn giữa nội dung của bảng
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # 🔹 Tắt tự động điều chỉnh kích thước để giữ cố định
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

    def display_selected_row_data(self, item):
        """Hiển thị thông tin của hàng được chọn lên các ô bên trái"""
        row = item.row()  # Lấy số hàng được chọn

        # Lấy dữ liệu từ từng cột của hàng
        customer_name = self.tableWidget.item(row, 0).text()
        phone = self.tableWidget.item(row, 1).text()
        email = self.tableWidget.item(row, 2).text()
        checkin_date = self.tableWidget.item(row, 3).text()
        checkout_date = self.tableWidget.item(row, 4).text()
        room_code = self.tableWidget.item(row, 5).text()
        customer_code = ""
        for customer in self.customers:  # Duyệt danh sách đối tượng khách hàng
            if customer.customer_name == customer_name:  # So sánh thuộc tính
                customer_code = customer.customer_code  # Lấy mã khách hàng
                break  # Thoát vòng lặp nếu tìm thấy
        # Hiển thị dữ liệu lên các ô nhập bên trái
        self.lineEdit_CusCode2.setText(customer_code)
        self.lineEdit_Phone_2.setText(phone)
        self.lineEditCusName2.setText(customer_name)
        self.lineEdit_CusEmail2.setText(email)
        self.lineEdit_CheckIn.setText(checkin_date)
        self.lineEdit_CheckOut.setText(checkout_date)
        self.lineEdit_RoomCodeB.setText(room_code)

    def update_selected_row(self):
        """Cập nhật dữ liệu của hàng đang chọn mà không xóa hàng cũ, đồng thời lưu vào dataset."""

        selected_row = self.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "Please choose a row to update!")
            return

        # Lấy dữ liệu từ các ô nhập
        customer_code = self.lineEdit_CusCode2.text().strip()  # Giữ nguyên customer_code
        customer_name = self.lineEditCusName2.text().strip()
        phone = self.lineEdit_Phone_2.text().strip()
        email = self.lineEdit_CusEmail2.text().strip()
        checkin_date = self.lineEdit_CheckIn.text().strip()
        checkout_date = self.lineEdit_CheckOut.text().strip()
        room_code = self.lineEdit_RoomCodeB.text().strip()

        # Cập nhật dữ liệu trên giao diện bảng (tableWidget)
        self.tableWidget.setItem(selected_row, 0, QTableWidgetItem(customer_name))
        self.tableWidget.setItem(selected_row, 1, QTableWidgetItem(phone))
        self.tableWidget.setItem(selected_row, 2, QTableWidgetItem(email))
        self.tableWidget.setItem(selected_row, 3, QTableWidgetItem(checkin_date))
        self.tableWidget.setItem(selected_row, 4, QTableWidgetItem(checkout_date))
        self.tableWidget.setItem(selected_row, 5, QTableWidgetItem(room_code))

        # Cập nhật dataset (customer.json & booking.json)
        self.update_json_after_update(customer_code, customer_name, phone, email, checkin_date, checkout_date,
                                      room_code)

        QMessageBox.information(self, "Successful", "Data is updated!")
        self.load_data()  # Reload dữ liệu để đảm bảo bảng cập nhật

    def update_json_after_update(self, customer_code, customer_name, phone, email, checkin_date, checkout_date,
                                 room_code):
        """Cập nhật thông tin khách hàng và đặt phòng trong JSON mà không xóa dữ liệu"""
        try:
            updated_customers = []
            updated_bookings = []

            # --- CẬP NHẬT CUSTOMER.JSON ---
            if os.path.exists(self.customer_filename):
                with open(self.customer_filename, "r", encoding="utf-8") as file:
                    customers = json.load(file)

                for customer in customers:
                    if customer["customer_code"] == customer_code:
                        # Cập nhật thông tin khách hàng
                        customer["customer_name"] = customer_name
                        customer["customer_phone"] = phone
                        customer["customer_email"] = email
                    updated_customers.append(customer)  # Giữ lại khách hàng khác

                # Ghi lại file customer.json đã cập nhật
                with open(self.customer_filename, "w", encoding="utf-8") as file:
                    json.dump(updated_customers, file, indent=4, ensure_ascii=False)

            # --- CẬP NHẬT BOOKING.JSON ---
            if os.path.exists(self.booking_filename):
                with open(self.booking_filename, "r", encoding="utf-8") as file:
                    bookings = json.load(file)

                for booking in bookings:
                    if booking["customer_code"] == customer_code:
                        # Cập nhật thông tin đặt phòng
                        booking["start_date"] = checkin_date
                        booking["end_date"] = checkout_date
                        booking["room_code"] = room_code
                    updated_bookings.append(booking)  # Giữ lại các booking khác

                # Ghi lại file booking.json đã cập nhật
                with open(self.booking_filename, "w", encoding="utf-8") as file:
                    json.dump(updated_bookings, file, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"Error when updating JSON file: {e}")

    def delete_selected_row(self):
        """Xóa khách hàng khỏi bảng và cập nhật JSON"""
        selected_row = self.tableWidget.currentRow()

        if selected_row < 0:
            return  # Không có dòng nào được chọn

        # Lấy customer_name của khách hàng cần xóa từ cột trong bảng
        customer_code = self.lineEdit_CusCode2.text()  # Giả sử cột 0 chứa customer_name

        # Xóa dòng khỏi giao diện bảng
        self.tableWidget.removeRow(selected_row)

        # Tìm customer_code từ customer_name, sau đó cập nhật JSON
        self.update_json_after_delete(customer_code)
        self.clear_customer_details()
        # Cập nhật lại bảng phòng (Room Management) để xóa thông tin khách hàng khỏi phòng
        self.display_rooms(self.dateEdit_date.date())

    def clear_customer_details(self):
        """Xóa thông tin khách hàng trên giao diện"""
        self.lineEdit_CusCode2.clear()
        self.lineEditCusName2.clear()

        self.lineEdit_Phone_2.clear()
        self.lineEdit_CheckIn.clear()
        self.lineEdit_CheckOut.clear()
        self.lineEdit_Cusname.clear()
        self.lineEdit_RoomCodeB.clear()
        self.lineEdit_CusEmail2.clear()

    def update_json_after_delete(self, customer_code):
        """Xóa khách hàng & đặt phòng liên quan dựa trên customer_code"""
        try:
            updated_customers = []
            updated_bookings = []

            # 🔹 Xử lý customers.json
            if os.path.exists(self.customer_filename):
                with open(self.customer_filename, "r", encoding="utf-8") as file:
                    customers = json.load(file)

                # Lọc danh sách, giữ lại khách hàng không trùng customer_code
                updated_customers = [customer for customer in customers if customer["customer_code"] != customer_code]

                # Ghi lại file customers.json đã cập nhật
                with open(self.customer_filename, "w", encoding="utf-8") as file:
                    json.dump(updated_customers, file, indent=4, ensure_ascii=False)

            # 🔹 Xử lý bookings.json
            if os.path.exists(self.booking_filename):
                with open(self.booking_filename, "r", encoding="utf-8") as file:
                    bookings = json.load(file)

                # Lọc danh sách booking, giữ lại các booking không trùng customer_code
                updated_bookings = [b for b in bookings if b["customer_code"] != customer_code]

                # Ghi lại file bookings.json đã cập nhật
                with open(self.booking_filename, "w", encoding="utf-8") as file:
                    json.dump(updated_bookings, file, indent=4, ensure_ascii=False)

            # 🔹 Cập nhật lại giao diện sau khi xóa
            self.load_data()  # Load lại dữ liệu mới
            self.display_rooms(self.dateEdit_date.date())  # Hiển thị lại danh sách phòng

        except Exception as e:
            print(f"Error when updating JSON file: {e}")

    def search_booking(self):
        """Tìm kiếm thông tin khách hàng theo Customer Code -> Lấy Customer Name -> Hiển thị dòng phù hợp."""
        cuscode = self.lineEdit_CusCode2.text().strip().lower()  # Lấy mã khách hàng từ ô nhập

        if not cuscode:  # Nếu không nhập gì thì hiển thị tất cả dòng
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.showRow(row)
            return

        # Tìm Customer Name dựa trên Customer Code trong dataset (giả sử self.customers chứa dữ liệu)
        customer_name = None
        for customer in self.customers:
            if customer.customer_code.lower() == cuscode:
                customer_name = customer.customer_name
                break

        if not customer_name:  # Nếu không tìm thấy mã khách hàng, ẩn hết các dòng
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.hideRow(row)
            return

        # Duyệt bảng để hiển thị dòng có Customer Name khớp
        for row in range(self.tableWidget.rowCount()):
            cusname_item = self.tableWidget.item(row, 0)  # Cột 0 chứa Customer Name

            if cusname_item and cusname_item.text().lower() == customer_name.lower():
                self.tableWidget.showRow(row)  # Hiển thị dòng tìm thấy
            else:
                self.tableWidget.hideRow(row)  # Ẩn dòng không khớp

    def logout(self):
        reply = QMessageBox.question(self.MainWindow, "Logout", "Are you sure?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()  # Đóng cửa sổ hiện tại

            # Mở lại màn hình chính (HomePageMainWindowEx)
            self.mainwindow = QMainWindow()
            self.myui = HomePageMainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()

    def set_table_item(self, row, col, text):
        """Thiết lập ô chỉ đọc với nội dung cụ thể."""
        item = QTableWidgetItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(row, col, item)

    def configure_table_appearance(self):
        self.tableWidget_Room.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_Room.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def display_rooms(self, selected_date, rooms_to_display=None):
        self.tableWidget_Room.clearContents()
        rooms_to_display = rooms_to_display or self.rooms
        self.selected_rooms = rooms_to_display
        self.tableWidget_Room.setRowCount(len(rooms_to_display))

        for row, room in enumerate(rooms_to_display):
            items = [
                QTableWidgetItem(room.room_code),
                QTableWidgetItem("Booked" if self.is_room_booked(str(room.room_code), selected_date) else "Ready"),
                QTableWidgetItem(self.get_customer_code_for_room(str(room.room_code), selected_date) or "N/A"),
                QTableWidgetItem(room.room_type)
            ]

            status_color = QColor(255, 145, 144) if items[1].text() == "Booked" else QColor(207, 244, 210)
            for col in range(4):
                items[col].setBackground(QBrush(status_color))
                items[col].setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget_Room.setItem(row, col, items[col])

    def is_room_booked(self, room_code, selected_date):
        selected_datetime = datetime(
            selected_date.year(),
            selected_date.month(),
            selected_date.day()
        )

        for booking in self.bookings:
            if booking.room_code == room_code:
                try:
                    # 🔹 Chỉ hỗ trợ định dạng "yyyy/M/d"
                    start_date = datetime.strptime(booking.start_date, "%Y/%m/%d") if isinstance(booking.start_date,
                                                                                                 str) else booking.start_date
                    end_date = datetime.strptime(booking.end_date, "%Y/%m/%d") if isinstance(booking.end_date,
                                                                                             str) else booking.end_date

                    if start_date <= selected_datetime <= end_date:
                        return True
                except ValueError as e:
                    print(f"⚠ Invalid date format in booking: {booking.start_date}, {booking.end_date} - {e}")
                    continue

        return False

    def get_customer_code_for_room(self, room_code, selected_date):
        """Lấy customer_code của khách hàng trong khoảng thời gian đặt phòng"""
        selected_datetime = datetime(selected_date.year(), selected_date.month(), selected_date.day())

        # Lấy danh sách customer_code từ danh sách đối tượng Customer
        valid_customer_codes = {c.customer_code for c in self.customers}

        for booking in self.bookings:
            if booking.room_code == room_code:
                try:
                    # Chuyển đổi ngày từ chuỗi sang datetime nếu cần
                    start_date = datetime.strptime(booking.start_date, "%Y/%m/%d") if isinstance(booking.start_date,
                                                                                                 str) else booking.start_date
                    end_date = datetime.strptime(booking.end_date, "%Y/%m/%d") if isinstance(booking.end_date,
                                                                                             str) else booking.end_date

                    # Kiểm tra ngày hợp lệ và customer_code tồn tại
                    if start_date <= selected_datetime <= end_date and booking.customer_code in valid_customer_codes:
                        return booking.customer_code

                except ValueError as e:
                    print(f"Invalid date format in booking: {booking.start_date}, {booking.end_date} - {e}")
                    continue

        return None  # Không tìm thấy customer_code hợp lệ

    def sort_vacant(self):
        """Lọc các phòng còn trống"""
        vacant_rooms = [room for room in self.rooms
                        if not self.is_room_booked(room.room_code, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), vacant_rooms)

    def update_room_status(self):
        selected_date = self.dateEdit_date.date()
        self.display_rooms(selected_date, self.selected_rooms)

    def sort_vip(self):
        vip_rooms = [room for room in self.rooms if room.room_type == "VIP"]
        self.display_rooms(self.dateEdit_date.date(), vip_rooms)

    def sort_regular(self):
        regular_rooms = [room for room in self.rooms if room.room_type == "Regular"]
        self.display_rooms(self.dateEdit_date.date(), regular_rooms)

    def sort_all(self):
        self.display_rooms(self.dateEdit_date.date())

    def sort_booked(self):
        """Lọc các phòng đang được đặt"""
        booked_rooms = [room for room in self.rooms
                        if self.is_room_booked(room.room_code, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), booked_rooms)

    def process_checkin(self):
        selected_items = self.tableWidget_Room.selectedItems()
        if not selected_items:
            self.show_error_message("Please select a room to check in")
            return

        row = selected_items[0].row()
        room_code_item = self.tableWidget_Room.item(row, 0)
        status_item = self.tableWidget_Room.item(row, 1)
        customer_item = self.tableWidget_Room.item(row, 2)
        roomtype_item = self.tableWidget_Room.item(row, 3)

        if not room_code_item or not status_item or not customer_item:
            self.show_error_message("Error retrieving room information.")
            return

        if status_item.text() == "Booked":
            self.show_error_message("This room has already been booked.")
            return

        room_code = room_code_item.text()
        confirm = QMessageBox.question(
            self.MainWindow,
            "Check-in Confirmation",
            f"Do you confirm the check-in for room {room_code}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            # ✅ Hiển thị hộp thoại để nhập Customer ID
            new_customer_id, ok = QInputDialog.getText(self, "Enter Customer ID", "Customer ID:")

            if not ok or not new_customer_id.strip():  # Nếu bấm "Hủy" hoặc để trống
                self.show_error_message("Please enter a valid Customer ID.")
                return

            new_customer_id = new_customer_id.strip()

            status_item.setText("Booked")
            customer_item.setText(new_customer_id)

            # Đổi màu nền thành đỏ
            red_color = QColor(255, 145, 144)
            status_item.setBackground(QBrush(red_color))
            customer_item.setBackground(QBrush(red_color))
            room_code_item.setBackground(QBrush(red_color))
            roomtype_item.setBackground(QBrush(red_color))

            QMessageBox.information(self.MainWindow, "Success", "Check-in Successfully!")

    def get_selected_room_code(self):
        """Lấy room_code từ dòng được chọn trong bảng."""
        selected_row = self.tableWidget_Room.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a room!")
            return None

        room_item = self.tableWidget_Room.item(selected_row, 0)  # Lấy room_code ở cột đầu tiên
        if not room_item:
            QMessageBox.warning(self, "Error", "No room code found in this row!")
            return None

        return room_item.text()

    def process_checkout(self):
        selected_items = self.tableWidget_Room.selectedItems()
        if not selected_items:
            self.show_error_message("Please select a room to check out.")
            return

        row = selected_items[0].row()
        room_code_item = self.tableWidget_Room.item(row, 0)
        status_item = self.tableWidget_Room.item(row, 1)
        customer_item = self.tableWidget_Room.item(row, 2)
        roomtype_item = self.tableWidget_Room.item(row, 3)

        if not room_code_item or not status_item or not customer_item:
            self.show_error_message("Error retrieving room information.")
            return

        if status_item.text() != "Booked":
            self.show_error_message("This room is available.")
            return

        room_code = room_code_item.text()
        customer_code = customer_item.text()  # Lấy mã khách trước khi cập nhật

        # Nếu phòng chưa có khách, không thực hiện check-out
        if customer_code == "N/A":
            self.show_error_message("No valid customer found for this room.")
            return

        confirm = QMessageBox.question(
            self.MainWindow,
            "Confirm Check-out",
            f"Confirm check-out for room {room_code}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            # Cập nhật trạng thái phòng
            status_item.setText("Ready")
            customer_item.setText("N/A")

            # Đổi màu nền thành xanh lá
            green_color = QColor(207, 244, 210)
            for item in [status_item, customer_item, room_code_item, roomtype_item]:
                if item:
                    item.setBackground(QBrush(green_color))

            # Gọi hóa đơn nếu có khách
            self.show_invoice_window(room_code, customer_code)

    def show_invoice_window(self, room_code, customer_code):
        """Hiển thị giao diện hóa đơn (cần thay thế bằng giao diện thực tế của bạn)."""
        # Ví dụ:
        self.invoice_window = MainWindowInvoicesEx(room_code, customer_code)
        self.invoice_window.show()

    def show_error_message(self, message):
        QMessageBox.critical(self.MainWindow, "ERROR", message)

    def save_data(self):
        """Lưu dữ liệu vào JSON và kiểm tra phòng trống trước khi cập nhật bảng"""
        try:
            customer_code = self.lineEdit_Cuscode.text().strip()
            customer_phone = self.lineEdit_Phone.text().strip()
            customer_name = self.lineEdit_Cusname.text().strip()
            customer_email = self.lineEdit_Email.text().strip()
            customer_identity = self.lineEdit_Identify.text().strip()
            room_code = self.lineEdit_Roomcode.text().strip()
            start_date = self.CheckIn.text().strip()
            end_date = self.CheckOut.text().strip()

            # Kiểm tra các trường bắt buộc
            if not customer_code or not customer_name or not room_code:
                QMessageBox.warning(self.MainWindow, "Warning",
                                    "Customer Code, Customer Name, and Room Code cannot be empty!")
                return

            customers = self.jff.read_data(self.customer_filename, Customer)
            bookings = self.jff.read_data(self.booking_filename, Booking)

            # Chuyển đổi ngày thành dạng datetime để so sánh
            start_date_dt = datetime.strptime(start_date, "%Y/%m/%d")
            end_date_dt = datetime.strptime(end_date, "%Y/%m/%d")

            # Kiểm tra xem phòng đã có đặt trước chưa
            for booking in bookings:
                if booking.room_code == room_code:
                    booked_start = datetime.strptime(booking.start_date, "%Y/%m/%d")
                    booked_end = datetime.strptime(booking.end_date, "%Y/%m/%d")

                    # Nếu ngày đặt phòng mới bị trùng với khoảng thời gian đã có
                    if not (end_date_dt < booked_start or start_date_dt > booked_end):
                        QMessageBox.warning(self.MainWindow, "Warning", "Room is already booked for this period!")
                        return  # Dừng lưu nếu phòng đã có khách

            # Nếu phòng trống, tạo booking mới
            booking = Booking(customer_code, room_code, start_date, end_date)
            bookings.append(booking)

            # Kiểm tra xem khách hàng đã tồn tại chưa
            existing_customer = next((c for c in customers if c.customer_code == customer_code), None)
            if not existing_customer:
                c = Customer(customer_code, customer_name, customer_phone, customer_email, customer_identity)
                customers.append(c)

            # Lưu dữ liệu vào file JSON
            self.jff.write_data(customers, self.customer_filename)
            self.jff.write_data(bookings, self.booking_filename)

            QMessageBox.information(self.MainWindow, "Successful", "Data was saved!")
            self.load_data()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Error saving data:\n{str(e)}")

    def clear_reservation_data(self):
        """ Xóa nội dung của các ô nhập liệu """
        self.lineEdit_Cuscode.clear()
        self.lineEdit_Phone.clear()
        self.lineEdit_Cusname.clear()
        self.lineEdit_Email.clear()
        self.lineEdit_Identify.clear()

        self.lineEdit_Roomcode.clear()
        self.lineEdit_Requirement.clear()

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