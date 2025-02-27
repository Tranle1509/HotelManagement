from libs.JsonFileFactory import JsonFileFactory
from models.Booking import Booking

jff=JsonFileFactory()
filename="../dataset/categories.json"
categories=jff.read_data(filename,Booking)
print("List off Categories from Json:")
for cate in categories:
    print(cate)