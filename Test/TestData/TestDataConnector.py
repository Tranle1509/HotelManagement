from libs.DataConnector import DataConnector

dc=DataConnector()
#Lấy toàn bộ nhân viên:
employees=dc.get_all_employees()
print("List of Employee:")
for e in employees:
    print(e)

