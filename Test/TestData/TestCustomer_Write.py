import random

from libs.FileFactory import JsonFileFactory
from model.Customer import Customer

customers=[]
for i in range(1,20):
    code=f"{i}"
    name=f"Customer{i}"
    phone='0' +'9' + ''.join(random.choices('0123456789', k=8))
    email=f"customer{i}@gmail.com"
    c=Customer(code,name,phone,email)
    customers.append(c)
    for c in customers:
        print(c)

jff = JsonFileFactory()
filename = "../dataset/customers.json"
jff.write_data(customers, filename)