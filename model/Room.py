class Room:
    def __init__(self, roomcode, roomname, roomtype):
        self.roomcode=roomcode
        self.roomname=roomname
        self.roomtype=roomtype
    def __str__(self):
        return f"{self.roomcode}\t{self.roomname}\t{self.roomtype}"