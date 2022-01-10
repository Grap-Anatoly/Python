# true or false after evaluation statements
x = 2
print (x == 2)
print (x == 3)
print (x < 3)
# ----------------
name = "John"
age = 23
if name == "John" and age == 23:
    print ("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print ("Your name is either John or Rick.")
# default if statement
# ----------------
if name in ["John", "Rick"]:
    print ("Your name is either John or Rick.")
# The "in" operator could be used to check if
# a specified object exists within an iterable object container, such as a list
# ----------------
statement = False
another_statement = True
if statement is True:
    print (1)
    pass
elif another_statement is True:
    print (2)
    pass
else:
    print (3)
    pass
# if,elif,else; is can be ==
# ----------------
x = 2
if x == 2:
    print ("X equals two!")
else:
    print ("X does not equals two.")
# Unlike the double equals operator "==",
# the "is" operator does not match the values of the variables,
# but the instances themselves. For example:
# ----------------
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
# ----------------
print (not False)
print (not True)
# not before bollean inverts it
# ----------------
number = 16
second_number = False
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")