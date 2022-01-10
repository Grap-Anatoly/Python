# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.
class MyClass:
    var = "abc"

    def func(self):
        print ("Hello!")

obj = MyClass()
obj1 = MyClass()

obj1.var = "cde"

print (obj.var)
print (obj1.var)

obj.func()
# The __init__() function, is a special function that is called when the class is being initiated.
# It's used for asigning values in a class.
# By using the "self" keyword we can access the attributes and methods of the class in python.

class NumberHolder:

    def __init__(self, number):
        self.number = number

# -----------------

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())