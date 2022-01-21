# An enumeration is a set of symbolic names (members) bound to unique, constant values.
# Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# The class Color is an enumeration (or enum)
# The attributes Color.RED, Color.GREEN, etc., are enumeration members (or enum members) and are functionally constants.
# The enum members have names and values (the name of Color.RED is RED, the value of Color.BLUE is 3, etc.)

# Even though we use the class syntax to create Enums, Enums are not normal Python classes.
# Enumeration members have human readable string representations

print(Color.RED)

# Their repr has more information

print(repr(Color.RED))

# The type of an enumeration member is the enumeration it belongs to

print(type(Color.RED))

print(isinstance(Color.RED, Color))

# Enum members also have a property that contains just their item name

print(Color.RED.name)

# Enumerations support iteration, in definition order

for c in Color:
    print(c)

# Enumeration members are hashable, so they can be used in dictionaries and sets

apples = {}
apples[Color.RED] = "red apple"
apples[Color.GREEN] = "green apple"

print(apples)

# Programmatic access to enumeration members and their attributes

print(Color(1))

print(Color['RED'])

# If you have an enum member and need its name or value

member = Color.RED

print(member.name)
print(member.value)

# Having two enum members with the same name is invalid
# By default, enumerations allow multiple names as aliases for the same value.
# When this behavior isn’t desired, the following decorator can be used to ensure each value is used only once in the enumeration
# @enum.unique

# from enum import unique
#
# @unique
# class Mistake(Enum):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 3

# If the exact value is unimportant you can use auto

from enum import Enum, auto
class Color(Enum):
     RED = auto()
     BLUE = auto()
     GREEN = auto()

print(list(Color))

# The values are chosen by _generate_next_value_(), which can be overridden

class AutoName(Enum):
     def _generate_next_value_(name, start, count, last_values):
         return name

class Ordinal(AutoName):
     NORTH = auto()
     SOUTH = auto()
     EAST = auto()
     WEST = auto()

print(list(Ordinal))

# Iterating over the members of an enum does not provide the aliases
# The special attribute __members__ is a read-only ordered mapping of names to members.

for name, member in Ordinal.__members__.items():
     print(name, member)

# Enumeration members are compared by identity

print(Color.RED is Color.RED)
print(Color.RED is Color.BLUE)
print(Color.RED is not Color.BLUE)

class Foo(Enum):
     def some_behavior(self):
         pass

class Bar(Foo):
     HAPPY = 1
     SAD = 2
