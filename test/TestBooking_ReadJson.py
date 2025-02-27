from libs.JsonFileFactory import JsonFileFactory
from models.booking import Booking

jff=JsonFileFactory()
filename="../dataset/bookings.json"
categories=jff.read_data(filename,Booking)
print("List of Bookings from Json:")
for cate in categories:
    print(cate)