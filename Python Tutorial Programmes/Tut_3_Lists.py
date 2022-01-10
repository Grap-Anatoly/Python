mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print (mylist[0])
print (mylist[1])
print (mylist[2])

for x in mylist:
    print (x)

# ------------------

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print (numbers)
print (strings)
print ("The second name on the names list is %s" % second_name)