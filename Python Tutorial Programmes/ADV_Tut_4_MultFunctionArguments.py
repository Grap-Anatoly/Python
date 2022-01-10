# Every function in Python receives a predefined number of arguments,
# if declared normally, like this:

def func (first, seoond, third):
    print("First %s, Second %s, Third %s" % (first,seoond,third))

func("1", "2", "3")

# It is possible to declare functions which receive a variable number of arguments,
# using the following syntax (*name of the arguments list):

def secondFunc(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

secondFunc("1", "2", "3", "4", "5", "6", "7")

# It is also possible to send functions arguments by keyword,
# so that the order of the argument does not matter, using the following syntax
# (** key word)

def bar (first, second, third, **options):
    if options.get("action") == "sum":
        print("the sum is %d" % (first + second + third))

    if options.get("number") == "first":
        return first

result = bar (1, 2, 3, action="sum", number="first")
print("Result is %d!" % result)

# ---------------
# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received. The bar must return
# True if the argument with the keyword magicnumber is worth 7, and False otherwise.

def foo(a, b, c, *arguments):
    return len(list(arguments))

def bar(a, b, c, **keyword):
        if keyword.get("magicnumber") == 7:
            return True
        else:
            return False



# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")