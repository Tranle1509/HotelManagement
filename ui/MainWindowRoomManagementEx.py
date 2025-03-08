from libs.DataConnector import DataConnector
from ui.MainWindowRoomManagement import Ui_MainWindow


class MainWindowRoomManagementEx(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.selected_cate=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass
"""
    def load_data(self):
        self.load_rooms("rooms.json")
        self.load_customers("customers.json")
        self.load_bookings("bookings.json")

    def load_rooms(self, filename):
        #Tải danh sách phòng từ file JSON.
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for room_data in data:
                    room = Room(
                        room_data["roomcode"],
                        room_data["roomname"],
                        room_data["roomtype"]
                    )
                    self.rooms.append(room)
        except FileNotFoundError:
            print(f"Không tìm thấy file: {filename}")
        except json.JSONDecodeError:
            print(f"Lỗi giải mã JSON trong file: {filename}")

    def load_customers(self, filename):
        #Tải danh sách khách hàng từ file JSON.
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for customer_data in data:
                    customer = Customer(
                        customer_data["code"],
                        customer_data["name"],
                        customer_data["phone"],
                        customer_data["email"]
                    )
                    self.customers.append(customer)
        except FileNotFoundError:
            print(f"Không tìm thấy file: {filename}")
        except json.JSONDecodeError:
            print(f"Lỗi giải mã JSON trong file: {filename}")

    def load_bookings(self, filename):
        #Tải danh sách đặt phòng từ file JSON.
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for booking_data in data:
                    booking = Booking(
                        booking_data["customer_code"],
                        booking_data["room_code"],
                        QDate.fromString(booking_data["start_date"], "yyyy-MM-dd"),
                        QDate.fromString(booking_data["end_date"], "yyyy-MM-dd")
                    )
                    self.bookings.append(booking)
        except FileNotFoundError:
            print(f"Không tìm thấy file: {filename}")
        except json.JSONDecodeError:
            print(f"Lỗi giải mã JSON trong file: {filename}")

    def display_rooms(self):
        #Hiển thị thông tin phòng trên bảng.

        # Xác định số lượng hàng (số phòng trên mỗi tầng) và số cột (số tầng)
        rooms_per_floor = 5
        number_of_floors = 5  # Có 5 tầng

        self.room_table.setRowCount(rooms_per_floor)
        self.room_table.setColumnCount(number_of_floors)

        # Thiết lập header cho các cột (tên tầng)
        headers = [f"Tầng {i + 1}" for i in range(number_of_floors)]
        self.room_table.setHorizontalHeaderLabels(headers)

        # Duyệt qua các phòng và thêm chúng vào bảng
        for floor in range(1, number_of_floors + 1):
            for room_number in range(1, rooms_per_floor + 1):
                # Tạo room_code
                room_code = f"{floor}0{room_number}" if room_number < 10 else f"{floor}{room_number}"

                # Tìm phòng trong danh sách
                room = next((r for r in self.rooms if r.roomcode == room_code), None)

                if room:
                    # Tạo một QTableWidgetItem với room_code
                    item = QTableWidgetItem(room.roomcode)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa chữ

                    # Thêm item vào bảng
                    row = room_number - 1  # Số hàng (bắt đầu từ 0)
                    column = floor - 1  # Số cột (bắt đầu từ 0)
                    self.room_table.setItem(row, column, item)

                    # Cập nhật màu sắc của ô
                    self.update_room_color(item, room.roomcode)

    def update_room_color(self, item, room_code):
        #Cập nhật màu sắc của ô dựa trên trạng thái phòng.
        if self.is_room_in_house(room_code):
            item.setBackground(QColor("red"))  # Đỏ: In House
        elif self.is_room_cleaning(room_code):
            item.setBackground(QColor("orange"))  # Cam: Cleaning
        else:
            item.setBackground(QColor("green"))  # Xanh: Ready

    def is_room_in_house(self, room_code):
        #Kiểm tra xem phòng có đang được sử dụng hay không (dựa vào ngày hiện tại).
        today = QDate.currentDate()
        return any(
            booking.room_code == room_code and
            booking.start_date <= today <= booking.end_date
            for booking in self.bookings
        )

    def is_room_cleaning(self, room_code):
        # TODO: Thêm logic để xác định phòng nào đang được dọn dẹp
        # Ví dụ: bạn có thể có một danh sách các phòng đang được dọn dẹp
        cleaning_rooms = ["303", "401"]  # Ví dụ: phòng 303 và 401 đang dọn dẹp
        return room_code in cleaning_rooms
"""