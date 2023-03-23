
primes = [2, 3, 5, 7, 11]
print(primes)

empty_list = []

# adding lists

items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# data types of lists

numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]

# add to the end of the list

orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']

# list indexes

names = ['Roger', 'Rafael', 'Andy', 'Novak']

# In Python, list index begins at zero and ends at the length of the list minus one.
# For example, in this list, 'Andy' is found at index 2.

berries = ["blueberry", "cranberry", "raspberry"]

berries[0]   # "blueberry"
berries[2]   # "raspberry"

# Negative indices for lists in Python can be used to reference elements in
# relation to the end of a list.


soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'

# 2D lists

# A 2D list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# The sublist of Jenny is at index 0. The hobby is at index 1 of the sublist.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

# Output
# [["Jenny", "Meditation"], ["Alexus", "Photography"]

# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]
print(noelles_height)

# Output
# 61

# .remove()

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)

# Output
# ["Cole", "Kip", "Sylvana", "Chris"]

# .count()

backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')

print(numPen)
# Output: 3

# .len()

knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size)
# Output: 5

# .sort()

exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
# Output: [1, 2, 3, 4]

# slicing

tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] # ['hammer', 'lever']
tools_slice[0] = 'nail'

# Original list is unaltered:
print(tools) # ['pen', 'hammer', 'lever']

# sorted

# The Python sorted() function accepts a list as an argument, and will return a new,
# sorted list containing the same elements as the original.

unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)
print(sortedList)
# Output: [1, 2, 3, 4]

# .insert()


# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")

print(store_line)
# Output: ['Karla', 'Maxium', 'Vikor'

# .pop()


cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

# Pop the last element
removed_element = cs_topics.pop()

print(cs_topics)
print(removed_element)

# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'

# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)

# Output:
# ['Python', 'Data Structures', 'Algorithms']
