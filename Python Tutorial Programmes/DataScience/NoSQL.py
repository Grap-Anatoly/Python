# As more and more data become available as unstructured or semi-structured,
# the need of managing them through NoSql database increases.
# Python can also interact with NoSQL databases in a similar way as is interacts with Relational databases.

# In order to connect to MongoDB, python uses a library known as pymongo.
# You can add this library to your python environment, using the below command from the Anaconda environment.

# conda install pymongo

# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient()

# Connect to the test db
db=client.test

# Use the employee collection
employee = db.employee
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

# Use the insert method
result = employee.insert_one(employee_details)

# Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)
