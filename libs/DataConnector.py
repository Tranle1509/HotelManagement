from libs.FileFactory import JsonFileFactory
from model.Employee import Employee


class DataConnector:
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../../dataset/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def login(self,username,password):
        employees=self.get_all_employees()
        for e in employees:
            if e.UserName==username and e.Password==password:
                return e
        return None













