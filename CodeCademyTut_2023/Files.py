# A Python file object is created when a file is opened with the open() function.
# You can associate this file object with a variable when you open a file
# using the with and as keywords. For example:

with open('somefile.txt') as file_object:
    print(file_object)
# You can then print the content of the file object, file_object with print().

#To read only one line instead of multiple lines in a Python file,
# use the method .readline() on a file object that is returned from the open() function.
# Every subsequent .readline() will extract the next line in the file if it exists.
with open('story.txt') as story_object:
  print(story_object.readline())

# Use json.load with an opened file object to read the contents into a Python dictionary.

# Contents of file.json
# { 'userId': 10 }

import json

with open('file.json') as json_file:
    python_dict = json.load(json_file)

print(python_dict.get('userId'))
# Prints 10

# Append to file

with open('shopping.txt', 'a') as shop:
  shop.write('Tomatoes, cucumbers, celery\n')

# Write to file

with open('diary.txt','w') as diary:
  diary.write('Special events for today')

# Read some lines

with open('lines.txt') as file_object:
  file_data = file_object.readlines()
print(file_data)

# .read()

with open('mystery.txt') as text_file:
  text_data = text_file.read()
print(text_data)

# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
  writer.writerow({'name': 'Google', 'type': 'Search'})

"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search
"""
