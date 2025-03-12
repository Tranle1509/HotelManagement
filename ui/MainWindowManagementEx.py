import json
from datetime import datetime

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QTableWidgetItem

from libs.DataConnector import DataConnector
from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room
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
        self.customer_filename = "../../dataset/customers.json"
        self.booking_filename = "../../dataset/bookings.json"
        self.room_filename = "../../dataset/rooms.json"

        self.setupUi(self)
        self.configure_table_appearance()  # 🔹 Cấu hình bảng sau khi UI đã load
        self.load_data()  # 🔹 Load dữ liệu từ file JSON
        self.display_rooms(QDate.currentDate())  # 🔹 Gọi hiển thị phòng sau khi UI sẵn sàng
        self.setupSignalAndSlot()

    def configure_table_appearance(self):
        """Yêu cầu 3: Cấu hình kích thước bảng"""
        self.tableWidget_Room.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget_Room.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.load_data()
        self.configure_table_appearance()

    def setupSignalAndSlot(self):
        self.pushButton_Save.clicked.connect(self.save_data)
        self.pushButton_Close.clicked.connect(self.close)
        self.pushButton_Clear.clicked.connect(self.clear_data)
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
        self.pushButtonreset.clicked.connect(self.reset_inputs)

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

    def sort_booked(self):
        """Lọc các phòng đang được đặt"""
        booked_rooms = [room for room in self.rooms
                        if self.is_room_booked(room.room_code, self.dateEdit_date.date())]
        self.display_rooms(self.dateEdit_date.date(), booked_rooms)

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

            status_color = QColor(255, 0, 0) if items[1].text() == "Booked" else QColor(0, 255, 0)
            for col in range(4):
                items[col].setBackground(QBrush(status_color))
                items[col].setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget_Room.setItem(row, col, items[col])

    def generate_new_customer_id(self):
        return f"cus{len(self.customers) + 1:04d}"

    def get_customer_code_for_room(self, room_code, selected_date):
        selected_datetime = datetime(selected_date.year(), selected_date.month(), selected_date.day())

        for booking in self.bookings:
            if booking.room_code == room_code:
                try:
                    # 🔹 Chuyển đổi ngày từ chuỗi sang datetime nếu chưa phải kiểu datetime
                    start_date = datetime.strptime(booking.start_date, "%Y/%m/%d") if isinstance(booking.start_date,
                                                                                                 str) else booking.start_date
                    end_date = datetime.strptime(booking.end_date, "%Y/%m/%d") if isinstance(booking.end_date,
                                                                                             str) else booking.end_date

                    # So sánh thời gian hợp lệ
                    if start_date <= selected_datetime <= end_date:
                        return booking.customer_code
                except ValueError as e:
                    print(f"Lỗi định dạng ngày tháng trong booking: {booking.start_date}, {booking.end_date} - {e}")
                    continue

        return None

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
                    print(f"⚠ Lỗi định dạng ngày tháng trong booking: {booking.start_date}, {booking.end_date} - {e}")
                    continue

        return False

    def showWindow(self):
        self.MainWindow.show()

    def load_data(self):
        """Tải dữ liệu từ JSON và cập nhật bảng."""
        self.customers = self.jff.read_data(self.customer_filename, Customer) or []
        self.bookings = self.jff.read_data(self.booking_filename, Booking) or []
        self.rooms = self.jff.read_data(self.room_filename, Room) or []
        self.display_data()

    def save_data(self):
        """Lưu dữ liệu vào JSON và cập nhật bảng ngay lập tức mà không kiểm tra định dạng."""
        try:
            customer_code = self.lineEdit_Cuscode.text().strip()
            customer_phone = self.lineEdit_Phone.text().strip()
            customer_name = self.lineEdit_Cusname.text().strip()
            customer_email = self.lineEdit_Email.text().strip()
            customer_identity = self.lineEdit_Identify.text().strip()
            room_code = self.lineEdit_Roomcode.text().strip()
            start_date = self.CheckIn.text().strip()
            end_date = self.CheckOut.text().strip()

            customers = self.jff.read_data(self.customer_filename, Customer)
            bookings = self.jff.read_data(self.booking_filename, Booking)

            booking = Booking(customer_code, room_code, start_date, end_date)
            bookings.append(booking)

            existing_customer = next((c for c in customers if c.customer_code == customer_code), None)
            if not existing_customer:
                customer = Customer(customer_code, customer_phone, customer_email, customer_name, customer_identity)
                customers.append(customer)

            self.jff.write_data(customers, self.customer_filename)
            self.jff.write_data(bookings, self.booking_filename)

            QMessageBox.information(self.MainWindow, "Thành công", "Dữ liệu đã được lưu!")
            self.load_data()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lưu dữ liệu thất bại:\n{str(e)}")

    def clear_data(self):
        """Xóa nội dung nhập liệu."""
        self.lineEdit_Cuscode.clear()
        self.lineEdit_Roomcode.clear()
        self.lineEdit_Phone.clear()
        self.lineEdit_Cusname.clear()
        self.lineEdit_Email.clear()
        self.lineEdit_Identify.clear()

    def display_data(self):
        """Hiển thị dữ liệu khách hàng và đặt phòng trên bảng."""
        self.tableWidget.clearContents()
        total_rows = max(len(self.customers), len(self.bookings))
        self.tableWidget.setRowCount(total_rows)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Check-in", "Check-out", "Room type"])

        for row in range(total_rows):
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

                # 🔹 Tìm room_type từ danh sách phòng
                room = next((r for r in self.rooms if r.room_code == booking.room_code), None)
                self.set_table_item(row, 5, room.room_type if room else "N/A")  # Hiển thị room_type nếu có
            else:
                for col in range(3, 6):
                    self.set_table_item(row, col, "N/A")

    def set_table_item(self, row, col, text):
        """Thiết lập ô chỉ đọc với nội dung cụ thể."""
        item = QTableWidgetItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(row, col, item)
# Tab Booking
    def display_selected_row_data(self, item):
        """Hiển thị thông tin của hàng được chọn lên các ô bên trái"""
        row = item.row()  # Lấy số hàng được chọn

        # Lấy dữ liệu từ từng cột của hàng
        customer_name = self.tableWidget.item(row, 0).text()
        phone = self.tableWidget.item(row, 1).text()
        email = self.tableWidget.item(row, 2).text()
        checkin_date = self.tableWidget.item(row, 3).text()
        checkout_date = self.tableWidget.item(row, 4).text()
        room_type = self.tableWidget.item(row, 5).text()
        customer_code = ""
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
        self.lineEdit_Roomtype.setText(room_type)

    def update_selected_row(self):
        """Cập nhật dữ liệu của hàng đang chọn mà không xóa hàng cũ"""
        selected_row = self.tableWidget.currentRow()

        if selected_row < 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để cập nhật!")
            return

        # Lấy dữ liệu từ các ô nhập
        customer_code = self.lineEdit_CusCode2.text()
        customer_name = self.lineEditCusName2.text()
        phone = self.lineEdit_Phone_2.text()
        email = self.lineEdit_CusEmail2.text()
        checkin_date = self.lineEdit_CheckIn.text()
        checkout_date = self.lineEdit_CheckOut.text()
        room_type = self.lineEdit_Roomtype.text()

        # Cập nhật dữ liệu vào hàng đang chọn
        self.tableWidget.setItem(selected_row, 0, QTableWidgetItem(customer_name))
        self.tableWidget.setItem(selected_row, 1, QTableWidgetItem(phone))
        self.tableWidget.setItem(selected_row, 2, QTableWidgetItem(email))
        self.tableWidget.setItem(selected_row, 3, QTableWidgetItem(checkin_date))
        self.tableWidget.setItem(selected_row, 4, QTableWidgetItem(checkout_date))
        self.tableWidget.setItem(selected_row, 5, QTableWidgetItem(room_type))

        QMessageBox.information(self, "Thành công", "Dữ liệu đã được cập nhật!")

    def reset_inputs(self):
        """Xóa tất cả dữ liệu trong các ô nhập"""
        self.lineEdit_CusCode2.clear()
        self.lineEditCusName2.clear()
        self.lineEdit_Phone_2.clear()
        self.lineEdit_CusEmail2.clear()
        self.lineEdit_CheckIn.clear()
        self.lineEdit_CheckOut.clear()
        self.lineEdit_Roomtype.clear()

    import json

    def delete_selected_row(self):
        """Xóa khách hàng khỏi bảng và cập nhật JSON"""
        selected_row = self.tableWidget.currentRow()

        if selected_row < 0:
            return  # Không có dòng nào được chọn

        # Lấy tên khách hàng để xóa trong dataset
        customer_name = self.tableWidget.item(selected_row, 0).text()

        # Xóa dòng khỏi giao diện bảng
        self.tableWidget.removeRow(selected_row)

        # Xóa dữ liệu trong JSON
        self.update_json_after_delete(customer_name)

    def update_json_after_delete(self, customer_name):
        """Cập nhật file JSON sau khi xóa một khách hàng"""
        try:
            with open("customers.json", "r", encoding="utf-8") as file:
                customers = json.load(file)

            # Lọc danh sách để loại bỏ khách hàng bị xóa
            updated_customers = [c for c in customers if c["customer_name"] != customer_name]

            # Ghi lại file JSON đã cập nhật
            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(updated_customers, file, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"Lỗi khi cập nhật JSON: {e}")



