from libs.DataConenctors import DataConnector

dc=DataConnector()
#Lấy toàn bộ nhân viên:
employees=dc.get_all_employees()
print("List of Employee:")
for e in employees:
    print(e)

#Test chức năng đăng nhập hệ thống:
uid="teo"
pwd="123hhgđghjk"
emp=dc.login(uid,pwd)
if emp!=None:
    print("Login successful")
else:
    print("Login Failed")
