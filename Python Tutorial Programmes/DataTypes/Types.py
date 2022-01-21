# In Python, the data type is set when you assign a value to a variable

# String
x = "Hello World"
print(type(x))
# Integer
x = 20
print(type(x))
# Float
x = 20.5
print(type(x))
# Copmlex
x = 1j
print(type(x))
# List
x = ["apple", "banana"]
print(type(x))
# Tuple
x = ("apple", "banana")
print(type(x))
# Range
x = range(6)
print(type(x))
# Dictionary
x = {"name" : "John", "age" : 36}
print(type(x))
# Set
x = {"apple", "banana", "cherry"}
print(type(x))
# FrozenSet
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
# Boolean
x = True
print(type(x))
# Byte
x = b"hello"
print(type(x))
# Bytearray
x = bytearray(5)
print(type(x))
# MemoryView
x = memoryview(bytes(5))
print(type(x))

# If you want to specify the data type, you can use the following constructor functions

x = str("Hello World")

x = int(20)

x = float(20.5)

x = complex(1j)

x = list(("apple", "banana", "cherry"))

x = tuple(("apple", "banana", "cherry"))

x = range(6)

x = dict(name="John", age=36)

x = set(("apple", "banana", "cherry"))

x = frozenset(("apple", "banana", "cherry"))

x = bool(5)

x = bytes(5)

x = bytearray(5)

x = memoryview(bytes(5))

# The frozenset() function returns an immutable frozenset object
# initialized with elements from the given iterable.

# The bytes() method returns an immutable bytes object initialized with the given size and data

# The bytearray() method returns a bytearray object which is an array of the given bytes.

# Memoryview allows you to access the internal buffers of an object by creating a memory view object.
