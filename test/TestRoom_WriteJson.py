from libs.JsonFileFactory import JsonFileFactory
from models.Room import Room

rooms=[]
rooms.append(Room("101","Room1","VIP"))
rooms.append(Room("102","Room2","Regular"))
rooms.append(Room("103","Room3","VIP"))
rooms.append(Room("104","Room4","VIP"))
rooms.append(Room("105","Room5","VIP"))
rooms.append(Room("201","Room6","Regular"))
rooms.append(Room("202","Room7","Regular"))
rooms.append(Room("203","Room8","Regular"))
rooms.append(Room("204","Room9","Regular"))
rooms.append(Room("205","Room10","Regular"))
rooms.append(Room("301","Room11","Regular"))
rooms.append(Room("302","Room12","Regular"))
rooms.append(Room("303","Room13","Regular"))
rooms.append(Room("304","Room14","Regular"))
rooms.append(Room("305","Room15","Regular"))
rooms.append(Room("401","Room16","Regular"))
rooms.append(Room("402","Room17","Regular"))
rooms.append(Room("403","Room18","Regular"))
rooms.append(Room("404","Room19","Regular"))
rooms.append(Room("405","Room20","Regular"))
rooms.append(Room("501","Room21","VIP"))
rooms.append(Room("502","Room22","VIP"))
rooms.append(Room("503","Room23","VIP"))
rooms.append(Room("504","Room24","VIP"))
rooms.append(Room("505","Room25","VIP"))
print("Lists of rooms:")
for r in rooms:
    print(r)
jff=JsonFileFactory()
filename= "../dataset/rooms.json"
jff.write_data(rooms,filename)