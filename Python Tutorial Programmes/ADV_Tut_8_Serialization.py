# Python provides built-in JSON libraries to encode and decode JSON.

import json

# There are two basic formats for JSON data.
# Either in a string or the object datastructure.
# The object datastructure, in Python, consists of lists and dictionaries
# nested inside each other. T
# he object datastructure allows one to use python methods (for lists and dictionaries)
# to add, list, search and remove elements from the datastructure.
# The String format is mainly used to pass the data into another program
# or load into a datastructure.

# To load JSON back to a data structure, use the "loads" method.

# To encode a data structure to JSON, use the "dumps" method.

# So dumps into JSON, loads out of JSON

json_string = json.dumps([1, 2, 3, "a", "b", "c"])

print(json.loads(json_string))

# Python supports a Python proprietary data serialization method called pickle
# (and a faster alternative called cPickle).

import pickle

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# The aim of this exercise is to print out the JSON string with
# key-value pair "Me" : 800 added to it.

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it

def add_employee(salaries_json, name, salary):
    temp = json.loads(salaries_json)
    temp[name] = salary
    salaries_json = json.dumps(temp)
    return salaries_json

salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

# json.loads(JSON file), mess with it, json.dumps(List)