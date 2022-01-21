# This module implements specialized container datatypes providing alternatives
# to Python’s general purpose built-in containers,dict, list, set, and tuple.

# namedtuple()
# factory function for creating tuple subclasses with named fields
#
# deque
# list-like container with fast appends and pops on either end
#
# ChainMap
# dict-like class for creating a single view of multiple mappings
#
# Counter
# dict subclass for counting hashable objects
#
# OrderedDict
# dict subclass that remembers the order entries were added
#
# defaultdict
# dict subclass that calls a factory function to supply missing values
#
# UserDict
# wrapper around dictionary objects for easier dict subclassing
#
# UserList
# wrapper around list objects for easier list subclassing
#
# UserString
# wrapper around string objects for easier string subclassing

# ChainMap---------------------

# A ChainMap class is provided for quickly linking a number of mappings
# so they can be treated as a single unit.
# It is often much faster than creating a new dictionary and running multiple update() calls.

from collections import ChainMap

print (ChainMap())

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

cm = ChainMap(numbers,letters)
print (cm)

print(cm["one"])

print(cm["b"])

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}

pets = ChainMap(for_adoption, vet_treatment)

print(pets["cats"])
print(pets["dogs"])

# In you have duplicate keys, first one will be printed

for key in pets:
     print(key, "->", pets[key])

# Counter--------------------

# A counter tool is provided to support convenient and rapid counting

from collections import Counter

cnt = Counter()

# Tally occurrences of words in a list
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] +=1

print(cnt)

# Find the ten most common words in Hamlet
# import re
# words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# Counter(words).most_common(10)

# Elements are counted from an iterable or initialized from another mapping (or counter)

c = Counter()
print(c)

c = Counter('gallahad')
print(c)

c = Counter({'red': 4, 'blue': 2})
print(c)

c = Counter(cats=4, dogs=8)
print(c)

# Counter objects have a dictionary interface except
# that they return a zero count for missing items instead of raising a KeyError:

c = Counter(['eggs', 'ham'])
print(c["bacon"])

# Setting a count to zero does not remove an element from a counter.
# Use del to remove it entirely

# elements()
# Return an iterator over elements repeating each as many times as its count.
# Elements are returned in the order first encountered.

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))

# most_common([n])
# Return a list of the n most common elements and their counts from the most common to the least.

c = Counter('abracadabra').most_common(2)
print(c)

# subtract([iterable-or-mapping])
# Elements are subtracted from an iterable or from another mapping (or counter).

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

c.subtract(d)

print(c)

# Deque------------------

# class collections.deque([iterable[, maxlen]])
# Returns a new deque object initialized left-to-right (using append()) with data from iterable.
# If iterable is not specified, the new deque is empty.

# appendleft(x)
# Add x to the left side of the deque.

from collections import deque

c = [1,2,3,4]
d = deque(c)

d.appendleft(2)

print(d)

# extendleft(iterable)
# Extend the left side of the deque by appending elements from iterable. Note, the series of left a
# ppends results in reversing the order of elements in the iterable argument.

d.extendleft(c)

print(d)

# popleft()
# Remove and return an element from the left side of the deque.

d.popleft()

print(d)

# NamedTuple--------------

# namedtuple() Factory Function for Tuples with Named Fields
# Named tuples assign meaning to each position in a tuple and allow for more readable,
# self-documenting code. They can be used wherever regular tuples are used,
# and they add the ability to access fields by name instead of position index.

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point (11 , y=22)
print(p[0]+p[1])

x, y = p
print(x, y)

print(p.x + p.y)

# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules

# OrderedDictionaries-------

# OrderedDict
# Ordered dictionaries are just like regular dictionaries
# but have some extra capabilities relating to ordering operations.

# Some differences from dict still remain:
#
# The regular dict was designed to be very good at mapping operations.
# Tracking insertion order was secondary.
# The OrderedDict was designed to be good at reordering operations. Space efficiency,
# iteration speed, and the performance of update operations were secondary.
# Algorithmically, OrderedDict can handle frequent reordering operations better than dict.
# This makes it suitable for tracking recent accesses (for example in an LRU cache).
# The equality operation for OrderedDict checks for matching order.
# The popitem() method of OrderedDict has a different signature.
# It accepts an optional argument to specify which item is popped.
# OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.
# Until Python 3.8, dict lacked a __reversed__() method.

# UserDict,List,String

# The class, UserDict, UserList, UserString acts as a wrapper around mentioned objects

