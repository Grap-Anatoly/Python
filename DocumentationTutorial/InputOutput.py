# Fancier Output Formatting ---------------------------------------------------------------------------
# So far we’ve encountered two ways of writing values: expression statements and the print() function.
# (A third way is using the write() method of file objects; the standard output file can be referenced as sys.stdout.
# See the Library Reference for more information on this.)

# Often you’ll want more control over the formatting of your output than simply printing space-separated values.
# There are several ways to format output.

# To use formatted string literals, begin a string with f or F before the opening quotation mark.
# Inside this string, you can write a Python expression between { and } characters
# that can refer to variables or literal values.

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# The str.format() method of strings requires more manual effort.
# You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives,
# but you’ll also need to provide the information to be formatted.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# Finally, you can do all the string handling yourself by using string slicing and concatenation operations
# to create any layout you can imagine.
# The string type has some methods that perform useful operations for padding strings to a given column width.

# When you don’t need fancy output but just want a quick display of some variables for debugging purposes,
# you can convert any value to a string with the repr() or str() functions.
#
# The str() function is meant to return representations of values which are fairly human-readable,
# while repr() is meant to generate representations which can be read by the interpreter
# (or will force a SyntaxError if there is no equivalent syntax).
# For objects which don’t have a particular representation for human consumption,
# str() will return the same value as repr().
# Many values, such as numbers or structures like lists and dictionaries,
# have the same representation using either function. Strings, in particular, have two distinct representations.

s = 'Hello, world.'

print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'

print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)

print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

# Formatted String Literals ------------------------------------------------------------------------

# Formatted string literals (also called f-strings for short)
# let you include the value of Python expressions inside a string by prefixing the string with f or F
# and writing expressions as {expression}.

import math

print(f'The value of pi is approximately {math.pi:.3f}.')

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
# This is useful for making columns line up.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# The String format() Method -----------------------------------------------------------------------

# Basic usage of the str.format() method looks like this:

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields)
# are replaced with the objects passed into the str.format() method.
# A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

# If keyword arguments are used in the str.format() method,
# their values are referred to by using the name of the argument.

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# Positional and keyword arguments can be arbitrarily combined:

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

# If you have a really long format string that you don’t want to split up,
# it would be nice if you could reference the variables to be formatted by name instead of by position.
# This can be done by simply passing the dict and using square brackets '[]' to access the keys.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# As an example, the following lines produce an aligned set of columns giving integers and their squares and cubes:

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#  Manual String Formatting --------------------------------------------------------------------------

# Here’s the same table of squares and cubes, formatted manually:

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

# The str.rjust() method of string objects right-justifies a
# string in a field of a given width by padding it with spaces on the left.
# There are similar methods str.ljust() and str.center().
# These methods do not write anything, they just return a new string.
# If the input string is too long, they don’t truncate it,
# but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative,
# which would be lying about a value.
# (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)
#
# There is another method, str.zfill(),
# which pads a numeric string on the left with zeros. It understands about plus and minus signs

# Old string formatting ------------------------------------------------------------------------

# The % operator (modulo) can also be used for string formatting. Given 'string' % values,
# instances of % in string are replaced with zero or more elements of values.
# This operation is commonly known as string interpolation. For example:

print('The value of pi is approximately %5.3f.' % math.pi)

# Reading and Writing Files ----------------------------------------------------------------------------------------

# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

f = open('workfile', 'w')

# The first argument is a string containing the filename.
# The second argument is another string containing a few characters describing the way in which the file will be used.
# mode can be 'r' when the file will only be read,
# 'w' for only writing (an existing file with the same name will be erased),
# and 'a' opens the file for appending; any data written to the file is automatically added to the end.
# 'r+' opens the file for both reading and writing.
# The mode argument is optional; 'r' will be assumed if it’s omitted.

# It is good practice to use the with keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes,
# even if an exception is raised at some point.
# Using with is also much shorter than writing equivalent try-finally blocks:

with open('workfile') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
# print(f.closed)

# Methods of File Objects ------------------------------------------------------------------

# To read a file’s contents, call f.read(size),
# which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).
# size is an optional numeric argument.
# When size is omitted or negative, the entire contents of the file will be read and returned;
# it’s your problem if the file is twice as large as your machine’s memory.
# Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned.
# If the end of the file has been reached, f.read() will return an empty string ('').

f.read()

# f.readline() reads a single line from the file;
# a newline character (\n) is left at the end of the string,
# and is only omitted on the last line of the file if the file doesn’t end in a newlin

f.readline()

# For reading lines from a file, you can loop over the file object.
# This is memory efficient, fast, and leads to simple code:

for line in f:
    print(line, end='')

# f.write(string) writes the contents of string to the file, returning the number of characters written.

f.write('This is a test\n')

# Other types of objects need to be converted – either to a string (in text mode)
# or a bytes object (in binary mode) – before writing them:

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)

# f.tell() returns an integer giving the file object’s current position in the file represented
# as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

# To change the file object’s position, use f.seek(offset, whence).

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file

f.read(1)

f.seek(-3, 2)  # Go to the 3rd byte before the end

f.read(1)

#  Saving structured data with json ------------------------------------------------------------------------------

# Strings can easily be written to and read from a file.
# Numbers take a bit more effort, since the read() method only returns strings,
# which will have to be passed to a function like int(),
# which takes a string like '123' and returns its numeric value 123.
# When you want to save more complex data types like nested lists and dictionaries,
# parsing and serializing by hand becomes complicated.

# Rather than having users constantly writing and debugging code to save complicated data types to files,
# Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation).
# The standard module called json can take Python data hierarchies,
# and convert them to string representations; this process is called serializing.
# Reconstructing the data from the string representation is called deserializing.
# Between serializing and deserializing,
# the string representing the object may have been stored in a file or data,
# or sent over a network connection to some distant machine.

import json

# if you have an object x, you can view its JSON string representation with a simple line of code
json.dumps([1, 'simple', 'list'])

# Another variant of the dumps() function, called dump(),
# simply serializes the object to a text file. So if f is a text file object opened for writing.

json.dump(x, f)

# To decode the object again, if f is a text file object which has been opened for reading:

x = json.load(f)






