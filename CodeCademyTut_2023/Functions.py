
# Function Parameters

def write_a_book(character, setting, special_skill):
  print(character + " is in " +
        setting + " practicing her " +
        special_skill)

def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I'm ready for school!")

# Indentation is used to identify code blocks

def testfunction(number):
  # This code is part of testfunction
  print("Inside the testfunction")
  sum = 0
  for x in range(number):
    # More indentation because 'for' has a code block
    # but still part of he function
    sum += x
  return sum
print("This is not part of testfunction")

def sales(grocery_store, item_on_sale, cost):
  print(grocery_store + " is selling " + item_on_sale + " for " + cost)

sales("The Farmer’s Market", "toothpaste", "$1")

# Python functions can be defined with named arguments which may have default values provided.
# When function arguments are passed using their names, they are referred to as keyword arguments.

def findvolume(length=1, width=1, depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)

# Multiple returns

def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  # Return all three values:
  return x_squared, y_squared, z_squared

three_squared, four_squared, five_squared = square_point(3, 4, 5)

# Return

def check_leap_year(year):
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."

year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2018 is not a leap year.

# Global variables

a = "Hello"

def prints_a():
    print(a)

# will print "Hello"
prints_a()

# Local variables

def my_function(value):
    print(value)


# Pass the value 7 into the function
my_function(7)

# Causes an error as `value` no longer exists
# print(value)