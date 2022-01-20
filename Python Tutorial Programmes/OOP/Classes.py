# For example, let’s say you want to track employees in an organization.
# You need to store some basic information about each employee,
# such as their name, age, position, and the year they started working.

# List

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# Classes vs Instances
# Classes are used to create user-defined data structures.
# Classes define functions called methods, which identify the behaviors
# and actions that an object created from the class can perform with its data.

# How to Define a Class
# All class definitions start with the class keyword

class EmptyDog:
    pass

# The body of the Dog class consists of a single statement: the pass keyword.
# pass is often used as a placeholder indicating where code will eventually go.

# The properties that all Dog objects must have are defined in a method called
# .__init__(). Every time a new Dog object is created, .__init__() sets the initial state of the object
# by assigning the values of the object’s properties.
# That is, .__init__() initializes each new instance of the class.
#
# You can give .__init__() any number of parameters,
# but the first parameter will always be a variable called self.
# When a new class instance is created, the instance is automatically passed to the self parameter
# in .__init__() so that new attributes can be defined on the object.

class Dog:
    # Class attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Instance attributes

        # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"

        # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

        # Replacing .description
    def __str__(self):
        return f"{self.name} is {self.age} years old"
# Attributes created in .__init__() are called instance attributes.
# An instance attribute’s value is specific to a particular instance of the class.
# All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
#
# On the other hand, class attributes are attributes that have the same value for all class instances.
# You can define a class attribute by assigning a value to a variable name outside of .__init__().

buddy = Dog("Buddy",9)
miles = Dog("Miles",4)

print(buddy.name)
print(miles.age)
print(buddy.species)

# Although the attributes are guaranteed to exist, their values can be changed dynamically:

miles.age = 10

print(miles.age)

miles.species = "Felis silvestris"

print(miles.species)

# Instance Methods
# Instance methods are functions that are defined inside a class and can only be called from an instance of that class.
# Just like .__init__(), an instance method’s first parameter is always self

# print(miles.description())

print(buddy.speak("Woof Woof"))

# In the above Dog class, .description() returns a string containing information about the Dog instance miles.
# When writing your own classes, it’s a good idea to have a method that returns a string
# containing useful information about an instance of the class.

print(miles)

#  You can change what gets printed by defining a special instance method called .__str__().

print(miles)

# Methods like .__init__() and .__str__() are called dunder methods
# because they begin and end with double underscores.

# test

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

first = Car
first.color = "blue"
first.mileage = 20000

# first = Car("Blue", 20000)
second = Car("red", 30000)

print("The %s car har %d miles." % (first.color,first.mileage))
print("The %s car har %d miles." % (second.color,second.mileage))

print(f"The {first.color} car has {first.mileage} miles")
