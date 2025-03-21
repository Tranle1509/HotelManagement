from libs.FileFactory import JsonFileFactory
from model.Room import Room

jff=JsonFileFactory()
filename="../../dataset/rooms.json"
rooms=jff.read_data(filename,Room)
print("List of Room from Json:")
for r in rooms:
    print(r)