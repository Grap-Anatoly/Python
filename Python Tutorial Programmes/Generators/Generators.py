# generator functions are a special kind of function that return a lazy iterator.
# hese are objects that you can loop over like a list.
# However, unlike lists, lazy iterators do not store their contents in memory.

# A common use case of generators is to work with data streams or large files, like CSV files.
# These text files separate data into columns by using commas.

# Generating an Infinite Sequence

a = range(5)
print(list(a))

# Using yield will result in a generator object.
# Using return will result in the first line of the file only.

# Generating an infinite sequence, however, will require the use of a generator, since your computer memory is finite

def infinite_sequence():
    num = 0
    while True:
        yield num
        num +=1

# for i in infinite_sequence():
#      print(i, end=" ")

# gen = infinite_sequence()
# next(gen)

# You can use infinite sequences in many ways, but one practical use for them is in building palindrome detectors.
# A palindrome detector will locate all sequences of letters or numbers that are palindromes.

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

# for i in infinite_sequence():
#      pal = is_palindrome(i)
#      if pal:
#          print(i)

# ---------------------------

# Generator functions look and act just like regular functions, but with one defining characteristic.
# Generator functions use the Python yield keyword instead of return.

# This looks like a typical function definition, except for the Python yield statement and the code that follows it.
# yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.

# Instead, the state of the function is remembered. That way, when next() is called on a generator object
# (either explicitly or implicitly within a for loop),
# the previously yielded variable num is incremented, and then yielded again.

# Like list comprehensions, generator expressions allow you to quickly create a generator object in just a few lines of code.
# They’re also useful in the same cases where list comprehensions are used, with an added benefit:
# you can create them without building and holding the entire object in memory before iteration.
# In other words, you’ll have no memory penalty when you use generator expressions.

nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

print(nums_squared_lc)
print(nums_squared_gc)

# You learned earlier that generators are a great way to optimize memory.
# While an infinite sequence generator is an extreme example of this optimization,
# let’s amp up the number squaring examples you just saw and inspect the size of the resulting objects.

import sys
nums_squared_lc = [i * 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

# There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory,
# then list comprehensions can be faster to evaluate than the equivalent generator expression.

# In this case, the list you get from the list comprehension is 87,624 bytes, while the generator object is only 120.

import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')

cProfile.run('sum((i * 2 for i in range(10000)))')

# ------------------------------

# yield

def multi_yield():
     yield_str = "This will print the first string"
     yield yield_str
     yield_str = "This will print the second string"
     yield yield_str

multi_obj = multi_yield()

print(next(multi_obj))
print(next(multi_obj))

#  In addition to yield, generator objects can make use of the following methods:
#
# .send()
# .throw()
# .close()

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

# This allows you to manipulate the yielded value.
# More importantly, it allows you to .send() a value back to the generator.

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))

# .throw() allows you to throw exceptions with the generator.

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))

# As its name implies, .close() allows you to stop a generator.

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))