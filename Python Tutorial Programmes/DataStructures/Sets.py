# Sets
# Python also includes a data type for sets.
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# Note: to create an empty set you have to use set(), not {};
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
# fast membership testing

# # Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a)
# unique letters in a
print(a-b)
# letters in a but not in b
print(a|b)
# letters in a or b or both
print(a&b)
# letters in both a and b
print(a^b)
# letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)