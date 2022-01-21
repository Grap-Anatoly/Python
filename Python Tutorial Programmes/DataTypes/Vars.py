# Variables are containers for storing data values.
# Variables do not need to be declared with any particular type

x = 5  # Integer
y = "Hello" # String

print(x)
print(y)

# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function.

print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes
# Variable names are case-sensitive.

a = 4
A = "Hello"
#A will not overwrite a

# Names ---------------------

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal vars
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi words variables types

# Camel case
myVariableName = "John"
# Pascal case
MyVariableName = "John"
# Snake case
my_variable_name = "John"

# Assing multiple values ------------------------

# Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line

x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc.
# Python allows you extract the values into variables.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output ------------------------

# The Python print statement is often used to output variables.

x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable

x = "Python is "
y = "awesome"
z =  x + y
print(z)

# For numbers, the + character works as a mathematical operator

x = 5
y = 10
print(x + y)

# Global Variables ------------------------

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)