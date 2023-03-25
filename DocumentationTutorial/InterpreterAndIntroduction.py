# The Python interpreter is usually installed as /usr/local/bin/python3.8 on those machines where it is available;

# When commands are read from a tty, the interpreter is said to be in interactive mode.
# In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (>>>);
# for continuation lines it prompts with the secondary prompt, by default three dots (...).

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

# By default, Python source files are treated as encoded in UTF-8.
# In that encoding, characters of most languages in the world can be used simultaneously in string literals,
# identifiers and comments — although the standard library only uses ASCII characters for identifiers,
# a convention that any portable code should follow.
# To display all these characters properly, your editor must recognize that the file is UTF-8,
# and it must use a font that supports all the characters in the file.

# Simple numbers -------------------------------------------------

print(2 + 2)

print(50 - 5 * 6)

print((50 - 5 * 6) / 4)

# Division always returns floating number

print(8 / 5)

# classic division returns a float

print(17 / 3)

# double symbol division discards the fractional part

print(17 // 3)

# the % operator returns the remainder of the division

print(17 % 3)

# Powers

# Squared
print(5 ** 2)

# power of 7
print(5 ** 7)

# = used to assign value to a variable

width = 20
height = 5 * 9

print(width * height)

# calling not defined value will cause an error

# Strings -------------------------------------------------

print('spam eggs')

# use \' to escape the single quote...
print('doesn\'t')

# ...or use double quotes instead

print("doesn't")

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

# If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote

print('C:\some\name')

print(r'C:\some\name')

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
# End of lines are automatically included in the string,
# but it’s possible to prevent this by adding a \ at the end of the line.

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *

print(3 * 'un' + 'ium')

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

# This only works with two literals though, not with variables or expressions
# If you want to concatenate variables or a variable and a literal, use +

print(text + " Concatenation")

# Strings can be indexed (subscripted), with the first character having index 0.

word = "Python"

print(word[0])
print(word[5])

# Indices may also be negative numbers, to start counting from the right

print(word[-1])
print(word[-2])

# Note that since -0 is the same as 0, negative indices start from -1.

# In addition to indexing, slicing is also supported.

print(word[0:2])
print(word[1:4])

# Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s

print(word[:2] + word[2:])

# Python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string results in an error

# If you need a different string, you should create a new one

print('J' + word[1:])

# The built-in function len() returns the length of a string

print(len(word))

# Lists -------------------------------------------------

squares = [1, 4, 9, 16, 25]

print(squares)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced

print(squares[0])
print(squares[-1])
print(squares[-3:])

# slicing returns a new list

# All slice operations return a new list containing the requested elements.

print(squares[:])

# Lists also support operations like concatenation

print(squares + [36, 49, 64])

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content

cubes = [1, 8, 27, 65, 125]
print(cubes)

cubes[3] = 64
print(cubes)

# You can also add new items at the end of the list, by using the append() method

cubes.append(216)
print(cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely

# It is possible to nest lists (create lists containing other lists)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)

# First steps ------------------------------
# Fibonacci series

a,b = 0,1

while a < 10:
    print(a)
    a, b = b, a + b

