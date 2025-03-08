from libs.DataConnector import DataConnector

dc=DataConnector()
#Lấy toàn bộ nhân viên:
employees=dc.get_all_employees()
print("List of Employee:")
for e in employees:
    print(e)

#Test chức năng đăng nhập hệ thống:
uid="tran"
pwd="1509"
emp=dc.login(uid,pwd)
if emp!=None:
    print("Login successful")
else:
    print("Login Failed")