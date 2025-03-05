from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Room import Room


class DataConnector:
    def get_all_rooms(self):
        jff = JsonFileFactory()
        filename = "../dataset/rooms.json"
        employees = jff.read_data(filename,Room)
        return employees
    def get_all_customers(self):
        jff = JsonFileFactory()
        filename = "../dataset/customers.json"
        assets = jff.read_data(filename, Customer)
        return assets
    def get_all_bookings(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee_assets.json"
        eas = jff.read_data(filename, Booking)
        return eas