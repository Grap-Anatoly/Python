# Tuples and Sequences¶
# We saw that lists and strings have many common properties, such as indexing and slicing operations.
# They are two examples of sequence data types (see Sequence Types — list, tuple, range).
# Since Python is an evolving language, other sequence data types may be added.
# There is also another standard sequence data type: the tuple.

# A tuple consists of a number of values separated by commas, for instance:

t = 12345, 54321, 'hello!'
print(t)
# can be nested
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable
# t[0] = 888888
# we will get an error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
# Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
# Tuples are immutable (fixed values), and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# (see later in this section) or indexing (or even by attribute in the case of namedtuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

# A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these.
# Empty tuples are constructed by an empty pair of parentheses;
# a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses).
# Ugly, but effective. For example:

empty = ()
singleton = "hello",

print(len(empty))
print(len(singleton))
print(singleton)
# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!' are packed together in a tuple.
# The reverse operation is also possible:
x , y ,z = t
print(x)
print(y)
print(z)