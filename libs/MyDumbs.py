from model.Employee import Employee


class MyDumps:
    @staticmethod
    def gen_employees_dataset():
        employees=[]
        employees.append(Employee("Emp1","HR Manager","Qanh","1505"))
        employees.append(Employee("Emp2", "Front Office Manager", "Trân", "1509"))
        employees.append(Employee("Emp3", "Customer Service Manager", "Duyên", "0210"))
        employees.append(Employee("Emp4", "Housekeeping Manager", "Tâm", "1803"))
        employees.append(Employee("Emp5", "Operations Manager", "Nguyên", "789"))
        return employees
    @staticmethod
    def gen_login(emp):
        employees=MyDumps.gen_employees_dataset()
        for e in employees:
            if e.UserName==emp.UserName and \
                    e.Password==emp.Password:
                return e#login ok
        return None
