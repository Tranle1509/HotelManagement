from libs.FileFactory import JsonFileFactory
from model.Employee import Employee

employees=[]
employees.append(Employee("Emp1","Manager","Qanh","1505"))
employees.append(Employee("Emp2", "Manager", "Tran", "1509"))
employees.append(Employee("Emp3", "Officer", "Duyen", "0210"))
employees.append(Employee("Emp4", "Officer", "Tam", "1803"))
employees.append(Employee("Emp5", "Officer", "Nguyen", "1512"))
employees.append(Employee("Emp6", "Staff", "Bao", "1811"))
employees.append(Employee("Emp7", "Staff", "Khoa", "1705"))
employees.append(Employee("Emp8", "Staff", "Huy", "0507"))

print("List of Employee")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename= "../../dataset/employees.json"
jff.write_data(employees,filename)
