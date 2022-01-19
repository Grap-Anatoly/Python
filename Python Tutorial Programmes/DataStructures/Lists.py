myList = ["a", "b", "c", "d", "e"]
iterableList = ["1", "2"]

myList.append("Add element to the end of the list")
# Equivalent to a[len(a):] = [x].
myList.extend(iterableList)
# Extend the list by appending all the items from the iterable.
# Equivalent to a[len(a):] = iterable.
myList.insert(2,"Insert item at the given position")
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x)
# is equivalent to a.append(x).
myList.remove("2")
# Remove the first item from the list whose value is equal to x.
myList.pop(0)
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
print(myList.index("Insert item at the given position"))
# Return zero-based index in the list of the first item whose value is equal to x.
# Raises a ValueError if there is no such item.
print(myList)
# -------------
print(myList.count("1"))
# Return the number of times x appears in the list.
myList.sort()
print(myList)
# Sort the items of the list in place (the arguments can be used for sort customization,
# see sorted() for their explanation).
myList.reverse()
print(myList)
# Reverse the elements of the list in place.
copyList = myList.copy()
print(copyList)
# Return a shallow copy of the list. Equivalent to a[:].
myList.clear()
# Remove all items from the list. Equivalent to del a[:].
print(myList)

# Using Lists as Stacks
# The list methods make it very easy to use a list as a stack,
# where the last element added is the first element retrieved (“last-in, first-out”).
# To add an item to the top of the stack, use append().
# To retrieve an item from the top of the stack, use pop() without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
stack.pop()

print(stack)

# Using Lists as Queues
# It is also possible to use a list as a queue,
# where the first element added is the first element retrieved (“first-in, first-out”);
# however, lists are not efficient for this purpose.
# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue)

queue.popleft()
queue.popleft()

print(queue)

# List Comprehensions
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of some operations applied
# to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# Note that this creates (or overwrites) a variable named x that still exists after the loop completes.
# We can calculate the list of squares without any side effects using:
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# map applies action in the first parameter to each element of the list

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal:

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# Nested List Comprehensions¶
# The initial expression in a list comprehension can be any arbitrary expression,
# including another list comprehension.
# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print([[row[i] for row in matrix] for i in range(4)])
# As we saw in the previous section,
# the nested listcomp is evaluated in the context of the for that follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# The del statement
# There is a way to remove an item from a list given its index instead of its value: the del statement.
# This differs from the pop() method which returns a value.
# The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice).

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]

print(a)

del a[2:4]

print(a)

del a[:]

print(a)

# del can also be used to delete entire variables:

del a
