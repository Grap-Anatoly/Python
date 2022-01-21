# open(filename, mode)
# Where the following mode is supported:
#
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will not be deleted.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

f = open("test.txt", "r")

print(f)

for each in f:
     print(each)

# There is more than one way to read a file in Python. If you need to extract a
# string that contains all characters in the file then we can use file.read().

f1 = open("test.txt", "r")
print(f1.read())

# Another way to read a file is to call a certain number of characters like in the following code
# the interpreter will read the first five characters of stored data and return it as a string

f2 = open("test.txt", "r")
print(f2.read(4))

# Creating a file using write()

w = open("test.txt", "w")
w.write("Write example ")
w.write("Testing posibilities ")
w.close()

# Working of append()

w = open("test.txt", "a")
w.write("Append example ")
w.close()

# There are also various other commands in file handling that is used to handle various tasks like:

# rstrip(): This function strips each line of a file off spaces from the right-hand side.
# lstrip(): This function strips each line of a file off spaces from the left-hand side.

# Python code to illustrate with()
with open("test.txt") as file:
    data = file.read()

with open("file.txt", "w") as f:
    f.write("Hello World!!!")