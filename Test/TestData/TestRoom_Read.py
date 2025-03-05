from libs.FileFactory import JsonFileFactory
from model.Room import Room

jff=JsonFileFactory()
filename="../dataset/rooms.json"
categories=jff.read_data(filename,Room)
print("List of Room from Json:")
for cate in categories:
    print(cate)