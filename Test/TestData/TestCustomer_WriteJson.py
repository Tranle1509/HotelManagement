import random

from libs.FileFactory import JsonFileFactory
from model.Customer import Customer

customers=[]
for i in range(1,1001):
    customer_code=f"cus{i}"
    customer_name=f"Customer{i}"
    customer_phone='0' +'9' + ''.join(random.choices('0123456789', k=8))
    customer_email=f"customer{i}@gmail.com"
    customer_identity='0' + ''.join(random.choices('0123456789', k=11))
    c=Customer(customer_code,customer_name,customer_phone,customer_email,customer_identity)
    customers.append(c)
for c in customers:
    print(c)

jff = JsonFileFactory()
filename = "../../dataset/customers.json"
jff.write_data(customers, filename)