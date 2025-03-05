from libs.JsonFileFactory import JsonFileFactory
from models.Customer import Customer

jff=JsonFileFactory()
filename="../dataset/customers.json"
customers = jff.read_data(filename,Customer)
print("List of Customer :")
for c in customers :
    print(c)
