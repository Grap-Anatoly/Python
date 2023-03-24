# Class
class Car:
  "This is an empty class"
  pass

# Class Instantiation
ferrari = Car()

# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")

# Create a new instance
charlie = Dog()

# Call the method
charlie.bark()
# This will output "Ham-Ham"

# Class variable
class my_class:
    class_variable = "I am a Class Variable!"


x = my_class()
y = my_class()

print(x.class_variable)  # I am a Class Variable!
print(y.class_variable)  # I am a Class Variable!

# __init__

class Animal:
  def __init__(self, voice):
    self.voice = voice

# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow

dog = Animal('Woof')
print(dog.voice) # Output: Woof

# .type()

a = 1
print(type(a)) # <class 'int'>

a = 1.1
print(type(a)) # <class 'float'>

a = 'b'
print(type(a)) # <class 'str'>

a = None
print(type(a)) # <class 'NoneType'>

# .dir()

class Employee:
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print("Hi, I'm " + self.name)


print(dir())
# ['Employee', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'new_employee']

print(dir(Employee))
# ['__doc__', '__init__', '__module__', 'print_name']

# In Python, __main__ is an identifier used to reference the current file context. When a module is read from standard input, a script, or from an interactive prompt, its __name__ is set equal to __main__.
#
# Suppose we create an instance of a class called CoolClass. Printing the type() of the instance will result in:
#
# <class '__main__.CoolClass'>
# This means that the class CoolClass was defined in the current script file.

# The Python __repr__() method is used to tell Python what the string representation of the class should be.
# It can only have one parameter, self, and it should return a string.

