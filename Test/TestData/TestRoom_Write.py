from libs.FileFactory import JsonFileFactory
from model.Room import Room

rooms = []

# Giả lập danh sách phòng từ 101 đến 909
for floor in range(1, 10):  # Tầng từ 1 đến 9
    for num in range(1, 10):  # Phòng từ 1 đến 9
        room_code = f"{floor}0{num}"  # Định dạng số phòng, VD: 101, 102, ..., 909
        room_name = f"Room{room_code}"
        room_type = "VIP" if floor % 2 != 0 else "Regular"  # Tầng lẻ là VIP, tầng chẵn là Regular
        rooms.append(Room(room_code, room_name, room_type))

print("Lists of rooms:")
for r in rooms:
    print(r)

jff = JsonFileFactory()
filename = "../../dataset/rooms.json"
jff.write_data(rooms, filename)
