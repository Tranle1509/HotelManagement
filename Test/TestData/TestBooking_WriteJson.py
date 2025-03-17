
import random
from datetime import datetime, timedelta

from libs.FileFactory import JsonFileFactory
from model.Booking import Booking

bookings = []
room_codes = [f"{i}0{j}" for i in range(1, 6) for j in range(1, 6)]  # Danh sách mã phòng
existing_bookings = set()  # Set để kiểm tra đặt phòng trùng lặp

for i in range(1, 1001):
    while True:
        customer_code = f"cus{i}"
        room_code = random.choice(room_codes)  # Chọn một mã phòng ngẫu nhiên
        start_date = datetime(2025, random.randint(1, 12), random.randint(1, 20))
        end_date = start_date + timedelta(days=random.randint(1, 10))

        # Tạo khóa duy nhất để kiểm tra trùng lặp (room_code, khoảng thời gian)
        booking_key = (room_code, start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))

        if booking_key not in existing_bookings:  # Nếu chưa có thì thêm vào danh sách
            existing_bookings.add(booking_key)
            booking = Booking(customer_code, room_code, start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))
            bookings.append(booking)
            break  # Thoát vòng lặp nếu đặt phòng hợp lệ

# Hiển thị danh sách đặt phòng
print("List of Bookings:")
for booking in bookings:
    print(booking)

# Ghi dữ liệu vào tệp JSON
jff = JsonFileFactory()
filename = "../../dataset/bookings.json"
jff.write_data(bookings, filename)
