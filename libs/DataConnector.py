from libs.FileFactory import JsonFileFactory
from model.Booking import Booking
from model.Customer import Customer
from model.Employee import Employee
from model.Room import Room


class DataConnector:
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def login(self,username,password):
        employees=self.get_all_employees()
        for e in employees:
            if e.UserName==username and e.Password==password:
                return e
        return None

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
        filename = "../dataset/bookings.json"
        eas = jff.read_data(filename, Booking)
        return eas







