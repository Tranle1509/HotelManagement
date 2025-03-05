from libs.FileFactory import JsonFileFactory
from model.Employee import Employee

employees=[]
employees.append(Employee("Emp1","HR Manager","Qanh","1505"))
employees.append(Employee("Emp2", "Front Office Manager", "Tran", "1509"))
employees.append(Employee("Emp3", "Customer Service Manager", "Duyen", "0210"))
employees.append(Employee("Emp4", "Housekeeping Manager", "Tam", "1803"))
employees.append(Employee("Emp5", "Operations Manager", "Nguyen", "1512"))
employees.append(Employee("Emp6", "Staff_Vip", "Bao", "1811"))
employees.append(Employee("Emp7", "Cleaner_Vip", "Khoa", "1705"))
employees.append(Employee("Emp8", "Security", "Huy", "0507"))
employees.append(Employee("Emp9", "Staff_Regular", "Thao", "0810"))
employees.append(Employee("Emp10", "Cleaner_Regular", "PAnh", "1002"))
employees.append(Employee("Emp11", "Security", "Dong", "0708"))
print("Danh sách Employee:")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename= "../../dataset/employees.json"
jff.write_data(employees,filename)
