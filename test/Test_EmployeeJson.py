from libs.FileFactory import JsonFileFactory
from libs.MyDumbs import MyDumps

gen_employees=MyDumps.gen_employees_dataset()
for emp in gen_employees:
    print(emp)
file_name="employees.json"
jff=JsonFileFactory()
jff.write_data(gen_employees,f"../dataset/{file_name}")


