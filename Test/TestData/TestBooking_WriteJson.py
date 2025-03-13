
import random
from datetime import datetime, timedelta

from libs.FileFactory import JsonFileFactory
from model.Booking import Booking

bookings=[]
room_codes = [f"{i}0{j}" for i in range(1, 4) for j in range(1, 6)]

for i in range(1, 1001):
    customer_code = f"cus{i}"
    room_code = random.choice(room_codes)  # Chọn một mã phòng ngẫu nhiên
    start_date = datetime(2025, random.randint(1,12) ,random.randint(1, 20))
    end_date = start_date + timedelta(days=random.randint(1, 10))
    booking = Booking(customer_code, room_code, start_date.strftime("%Y/%m/%d"), end_date.strftime("%Y/%m/%d"))
    bookings.append(booking)

print("List of Bookings:")
for booking in bookings:
    print(booking)

# Write data to JSON file:
jff = JsonFileFactory()
filename = "../../dataset/bookings.json"
jff.write_data(bookings, filename)