# Classes ----------------------------------------------------------------------------------------------------------

# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.

# A Word About Names and Objects

# Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.
# This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python,
# and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples).
# However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects
# such as lists, dictionaries, and most other types.
# This is usually used to the benefit of the program, since aliases behave like pointers in some respects.
# For example, passing an object is cheap since only a pointer is passed by the implementation;
# and if a function modifies an object passed as an argument,
# the caller will see the change — this eliminates the need for two different argument passing mechanisms as in Pascal.

# Python Scopes and Namespaces

# Before introducing classes, I first have to tell you something about Python’s scope rules.
# Class definitions play some neat tricks with namespaces,
# and you need to know how scopes and namespaces work to fully understand what’s going on.
# Incidentally, knowledge about this subject is useful for any advanced Python programmer.

# Let’s begin with some definitions.

# A namespace is a mapping from names to objects.
# Most namespaces are currently implemented as Python dictionaries,
# but that’s normally not noticeable in any way (except for performance),
# and it may change in the future.
# Examples of namespaces are: the set of built-in names (containing functions such as abs(),
# and built-in exception names); the global names in a module; and the local names in a function invocation.
# In a sense the set of attributes of an object also form a namespace.
# The important thing to know about namespaces is that
# there is absolutely no relation between names in different namespaces; for instance,
# two different modules may both define a function maximize without confusion — users
# of the modules must prefix it with the module name.
#
# By the way, I use the word attribute for any name following a dot — for example,
# in the expression z.real, real is an attribute of the object z.
# Strictly speaking, references to names in modules are attribute references:
# in the expression modname.funcname, modname is a module object and funcname is an attribute of it.
# In this case there happens to be a straightforward mapping between the module’s
# attributes and the global names defined in the module: they share the same namespace! 1

# Scopes and Namespaces Example ----------------------------------------------------------------

# This is an example demonstrating how to reference the different scopes and namespaces,
# and how global and nonlocal affect variable binding:

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# A First Look at Classes -----------------------------------------------------------------

# Classes introduce a little bit of new syntax, three new object types, and some new semantics.

# Class Definition Syntax ----------------------------------------------------------------

# The simplest form of class definition looks like this:

class ClassName:
    # Statement 1

    # Statement n
    pass

# Class definitions, like function definitions (def statements) must be executed before they have any effect.
# (You could conceivably place a class definition in a branch of an if statement, or inside a function.)

# In practice, the statements inside a class definition will usually be function definitions,
# but other statements are allowed, and sometimes useful — we’ll come back to this later.
# The function definitions inside a class normally have a peculiar form of argument list,
# dictated by the calling conventions for methods — again, this is explained later.

# When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments
# to local variables go into this new namespace.
# In particular, function definitions bind the name of the new function here.

# Class objects -------------------------------------------------------------------------------

# Class objects support two kinds of operations: attribute references and instantiation.

# Attribute references use the standard syntax used for all attribute references in Python: obj.name.
# Valid attribute names are all the names that were in the class’s namespace when the class object was created.

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

# When a class defines an __init__() method, class instantiation automatically invokes __init__()
# for the newly-created class instance.

    def f(self):
        return 'hello world'

#  MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively.
#  Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment.
#  __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

x = MyClass()

print(x.i)

# - creates a new instance of the class and assigns this object to the local variable x.

# Of course, the __init__() method may have arguments for greater flexibility.
# In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print(x.r, x.i)

# Instance Objects --------------------------------------------------------------------------------

# Now what can we do with instance objects? The only operations understood by instance objects are attribute references.

# There are two kinds of valid attribute names: data attributes and methods.

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)

del x.counter

# Method Objects ---------------------------------------------------------------------------------

# Usually, a method is called right after it is bound:

x = MyClass()
x.f()

# In the MyClass example, this will return the string 'hello world'.
# However, it is not necessary to call a method right away: x.f is a method object,
# and can be stored away and called at a later time. For example:

# xf = x.f
# while True:
#     print(xf())

# will continue to print hello world until the end of time.

# Class and Instance Variables --------------------------------------------------------------------

# Generally speaking,
# instance variables are for data unique to each instance and class variables are for attributes
# and methods shared by all instances of the class

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs

print(d.name)                  # unique to d
print(e.name)                  # unique to e

# As discussed in A Word About Names and Objects,
# shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries.
# For example, the tricks list in the following code should not be used as a class variable because
# just a single list would be shared by all Dog instances:


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)                # unexpectedly shared by all dogs

# Correct design of the class should use an instance variable instead:

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)

# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# Inheritance ------------------------------------------------------------------------------------------

# Of course, a language feature would not be worthy of the name “class” without supporting inheritance.
# The syntax for a derived class definition looks like this:


class Bulldog(Dog):
    # Dog > Bulldog...
    pass

# Execution of a derived class definition proceeds the same as for a base class.
# When the class object is constructed, the base class is remembered.
# This is used for resolving attribute references:
# if a requested attribute is not found in the class, the search proceeds to look in the base class.
# This rule is applied recursively if the base class itself is derived from some other class.

# Derived classes may override methods of their base classes.
# Because methods have no special privileges when calling other methods of the same object,
# a method of a base class that calls another method defined in the same base class
# may end up calling a method of a derived class that overrides it.
# (For C++ programmers: all methods in Python are effectively virtual.)
#
# An overriding method in a derived class may in fact want to extend rather than simply
# replace the base class method of the same name.
# There is a simple way to call the base class method directly:
# just call BaseClassName.methodname(self, arguments).
# This is occasionally useful to clients as well.
# (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

# Python has two built-in functions that work with inheritance:

# Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if
# obj.__class__ is int or some class derived from int.

# Use issubclass() to check class inheritance: issubclass(bool, int)
# is True since bool is a subclass of int.
# However, issubclass(float, int) is False since float is not a subclass of int.

# Multiple Inheritance ------------------------------------------------------------------------

# Python supports a form of multiple inheritance as well.
# A class definition with multiple base classes looks like this:

# class DerivedClassName(Base1, Base2, Base3):
#     pass

# Private Variables ---------------------------------------------------------------------------

# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
# However, there is a convention that is followed by most Python code:
# a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API
# (whether it is a function, a method or a data member).
# It should be considered an implementation detail and subject to change without notice.

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# The above example would work even if MappingSubclass were to introduce a __update identifier since
# it is replaced with _Mapping__update in the Mapping class and
# _MappingSubclass__update in the MappingSubclass class respectively.

#  Odds and Ends ---------------------------------------------------------------------------

# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items. An empty class definition will do nicely:

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# A piece of Python code that expects a particular abstract data type can
# often be passed a class that emulates the methods of that data type instead.
# For instance, if you have a function that formats some data from a file object,
# you can define a class with methods read() and readline() that get the data from a string buffer instead,
# and pass it as an argument.

# Iterators ------------------------------------------------------------------------------

# By now you have probably noticed that most container objects can be looped over using a for statement

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
# for line in open("myfile.txt"):
# #     print(line, end='')

# Having seen the mechanics behind the iterator protocol,
# it is easy to add iterator behavior to your classes.
# Define an __iter__() method which returns an object with a __next__() method.
# If the class defines __next__(), then __iter__() can just return self:

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

for char in rev:
    print(char)

# Generators ----------------------------------------------------------------------------------------------

# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it,
# the generator resumes where it left off (it remembers all the data values and which statement was last executed).
# An example shows that generators can be trivially easy to create:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

# Anything that can be done with generators can also be done with class-based iterators as
# described in the previous section.
# What makes generators so compact is that the __iter__() and __next__() methods are created automatically.

# Another key feature is that the local variables and execution state are automatically saved between calls.
# This made the function easier to write
# and much more clear than an approach using instance variables like self.index and self.data.

# Generator Expressions -----------------------------------------------------------------------------------

# Some simple generators can be coded succinctly as expressions using a syntax similar to list
# comprehensions but with parentheses instead of square brackets.
# These expressions are designed for situations where the generator is used right away by an enclosing function.
# Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory
# friendly than equivalent list comprehensions.

print(sum(i*i for i in range(10)))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
