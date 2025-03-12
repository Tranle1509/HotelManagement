class Room:
    def __init__(self, room_code, room_name, room_type):
        self.room_code=room_code
        self.room_name=room_name
        self.room_type=room_type
    def __str__(self):
        return f"{self.room_code}\t{self.room_name}\t{self.room_type}"