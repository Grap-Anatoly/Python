# Lists -------------------------------------------------------------

# The list data type has some more methods. Here are all of the methods of list objects:

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position.
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
# (The square brackets around the i in the method signature denote that the parameter is optional,
# not that you should type square brackets at that position.
# You will see this notation frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x.
# Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to
# limit the search to a particular subsequence of the list.
# The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place
# (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

# Lists as Stacks

# The list methods make it very easy to use a list as a stack,
# where the last element added is the first element retrieved (“last-in, first-out”).
# To add an item to the top of the stack, use append().
# To retrieve an item from the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()

print(stack)

# Lists as Queues

# It is also possible to use a list as a queue, where the first element added is the first element retrieved
# (“first-in, first-out”); however, lists are not efficient for this purpose.
# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)


#  List Comprehensions

# List comprehensions provide a concise way to create lists.

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))

print(squares)

squares = [x**2 for x in range(10)]

print(squares)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# Statement above is an equivalent to:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

# Nested List Comprehensions

# The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns

print([[row[i] for row in matrix] for i in range(4)])

# Equivalent

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# The del statement -----------------------------------------

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# del can be used to delete entire variables

del a

# Tuples and Sequences ---------------------------------------

# A tuple consists of a number of values separated by commas

t = 12345, 54321, 'hello!'

print(t[0])
print(t[1])
print(t[2])

print(t)

# can be nested

u = t, 1, 2, 3, 4

print(u)

# tuples are immutable
# t[0] = 11111 - error

# Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking
# (see later in this section) or indexing (or even by attribute in the case of namedtuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

empty = ()
single = 'hello', # note comma

print(len(empty))
print(len(single))

print(single)

# also we can unpack tuple into multiple variables

a, b, c = t

print(a)
print(b)
print(c)

# Sets --------------------------------------------------------------------------

# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)  # show that duplicates have been removed

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries ------------------------------------------------------------------

# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
# which can be any immutable type; strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

# It is best to think of a dictionary as a set of key: value pairs,
# with the requirement that the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}.
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary;
# this is also the way dictionaries are written on output.

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)

print(tel['jack'])

del tel['sape']

print(tel)

print(list(tel))

# The dict() constructor builds dictionaries directly from sequences of key-value pair

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions

print({x: x**2 for x in (2, 4, 6)})

# Looping Techniques -----------------------------------------------------------------------

# When looping through dictionaries,
# the key and corresponding value can be retrieved at the same time using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed().

for i in reversed(range(1, 10, 2)):
   print(i)

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list
# while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# More on Conditions -------------------------------------------------------------

# The conditions used in while and if statements can contain any operators, not just comparisons.
#
# The comparison operators in and not in check whether a value occurs (does not occur) in a sequence.
# The operators is and is not compare whether two objects are really the same object; this only matters for mutable
# objects like lists. All comparison operators have the same priority,
# which is lower than that of all numerical operators.
#
# Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
#
# Comparisons may be combined using the Boolean operators and and or,
# and the outcome of a comparison (or of any other Boolean expression) may be negated with not.
# These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest,
# so that A and not B or C is equivalent to (A and (not B)) or C.
# As always, parentheses can be used to express the desired composition.
#
# The Boolean operators and and or are so-called short-circuit operators:
# their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined.
# For example, if A and C are true but B is false, A and B and C does not evaluate the expression C.
# When used as a general value and not as a Boolean,
# the return value of a short-circuit operator is the last evaluated argument.
#
# It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,
#
# >>>
# >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# >>> non_null = string1 or string2 or string3
# >>> non_null
# 'Trondheim'
# Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator :=.
# This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

# Comparing Sequences and Other Types -------------------------------------------------

# Sequence objects typically may be compared to other objects with the same sequence type.
# The comparison uses lexicographical ordering: first the first two items are compared,
# and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared,
# and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type,
# the lexicographical comparison is carried out recursively.
# If all items of two sequences compare equal, the sequences are considered equal.
# If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.
# Lexicographical ordering for strings uses the Unicode code point number to order individual characters.
# Some examples of comparisons between sequences of the same type:
#
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
# Note that comparing objects of different types with < or > is legal
# provided that the objects have appropriate comparison methods.
# For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc.
# Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.



