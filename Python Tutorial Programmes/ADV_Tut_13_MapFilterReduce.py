# Map, Filter, and Reduce are paradigms of functional programming.
# hey allow the programmer to write simpler, shorter code,
# without neccessarily needing to bother about intricacies like loops and branching.

# The map() function in python has the following syntax:
# map(func, *iterables)

# Where func is the function on which each element in iterables (as many as they are)
# would be applied on. Notice the asterisk(*) on iterables? It means there can be as many iterables as possible,
# in so far func has that exact number as required input arguments

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    uppered_pets.append(pet.upper())

print(uppered_pets)

# with map

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# just usage of str.upper to each element of my_pets list

# Python already blesses us with the round() built-in function that takes two arguments
# -- the number to round up and the number of decimal places to round the number up to.
# So, since the function requires two arguments, we need to pass in two iterables

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

# To consolidate our knowledge of the map() function, we are going to use it to implement our own custom zip() function.
# The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the elements in the iterables.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

# ----------------------

# While map() passes each element in the iterable through a function and returns the result of all elements having passed through the function,
# filter(), first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function,
# "filtering" away those that are false. It has the following syntax:

# filter(func, iterable)

# The following points are to be noted regarding filter():

# Unlike map(), only one iterable is required.
# The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

#The next example will be a palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same backwards as forwards

dromes = ("demigod", "dad", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
# ----------------------

# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument.
# It has the following syntax:
# reduce(func, iterable[, initial])

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

# As usual, it's all about iterations: reduce takes the first and second elements in numbers and passes them to custom_sum respectively.
# custom_sum computes their sum and returns it to reduce.
# reduce then takes that result and applies it as the first element to custom_sum and takes the next element (third) in numbers as the second element to custom_sum.
# It does this continuously (cumulatively) until numbers is exhausted.

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)

# The result, as you'll expect, is 78 because reduce, initially, uses 10 as the first argument to custom_sum.

# -------------------------

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round((x**2),3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7 , my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)

# So, map its using function on each element in list,
# filter ,much the same but func should return boolean
# reduce takes list and applies function with multilying result like in last examle