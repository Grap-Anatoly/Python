myint = 7
print (myint)
# ------------------
myfloat = 7.0
print (myfloat)

myfloatSecond = float(7)
print (myfloatSecond)
# ------------------
mystring = 'hello'
print (mystring)

mystringSecond = "hello"
print (mystringSecond)
# ------------------
mystringAp = "Don`t worry about apostrophes"
print (mystringAp)
# ------------------
one = 1
two = 2
three = one + two
print (three)

hello = "Hello"
world = "world"
helloworld = hello + " " + world
print (helloworld)
# ------------------
a, b = 3, 4
print (a, b, hello)
# ------------------
testmystring = "hello"
testmyfloat = 10.0
testmyint = 20

if testmystring == "hello":
    print ("String: %s" % testmystring)
if isinstance(testmyfloat, float) and testmyfloat == 10.0:
    print ("Float: %f" % testmyfloat)
if isinstance(testmyint, int) and testmyint == 20:
    print ("Integer: %d" % testmyint)