# if statement

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for statement

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#Code that modifies a collection while iterating over that same collection can be tricky to get right.
# Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection
users = {}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# .range()

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

# To iterate over the indices of a sequence, you can combine range() and len()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# break and continue Statements, and else Clauses on Loops

# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause;
# it is executed when the loop terminates through exhaustion of the iterable (with for)
# or when the condition becomes false (with while), but not when the loop is terminated by a break statement.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# The continue statement, also borrowed from C, continues with the next iteration of the loop

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action.

# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# Defining Functions -----------------------------------------


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

# The keyword def introduces a function definition. It must be followed by the function name
# and the parenthesized list of formal parameters.
# The statements that form the body of the function start at the next line, and must be indented.

# A function definition associates the function name with the function object in the current symbol table.
# The interpreter recognizes the object pointed to by that name as a user-defined function.
# Other names can also point to that same function object and can also be used to access the function

print(fib)

f = fib
f(100)

# It is also possible to define functions with a variable number of arguments.
# There are three forms, which can be combined.

# Default Argument Values
# The most useful form is to specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments than it is defined to allow.

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# This function can be called in several ways:
    # giving only the mandatory argument: ask_ok('Do you really want to quit?')
    # giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
    # or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# The default values are evaluated at the point of function definition in the defining scope

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# Important warning: The default value is evaluated only once.

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Keyword Arguments
# Functions can also be called using keyword arguments of the form kwarg=value

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict)
# containing all keyword arguments except for those corresponding to a formal parameter.
# This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a
# tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# * - single arguments, ** dictionary, means key=parameter

# Special parameters

# By default, arguments may be passed to a Python function either by position or explicitly by keyword.
# For readability and performance, it makes sense to restrict the way arguments can be passed so that a
# developer need only look at the function definition to determine if items are passed by position,
# by position or keyword, or by keyword.

# def ex(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     pass

# Positional-or-Keyword Arguments¶
# If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword

# Positional-Only Parameters
# Positional-only parameters are placed before a / (forward-slash).
# The / is used to logically separate the positional-only parameters from the rest of the parameters.
# If there is no / in the function definition, there are no positional-only parameters.

# Keyword-Only Arguments
# To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument,
# place an * in the arguments list just before the first keyword-only parameter.

# Exmples

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg): # (arg, /)
    print(arg)

def kwd_only_arg(*, arg):
   print(arg)

def combined_example(pos_only, standard, *, kwd_only): # (pos_only, /, standard, *, kwd_only)
   print(pos_only, standard, kwd_only)


standard_arg(1)
standard_arg(arg = 1)

pos_only_arg(2)
# pos_only_arg(arg = 1)

kwd_only_arg(arg = 3)

combined_example(1, standard=2, kwd_only=3)

# Arbitrary Argument Lists

# Finally, the least frequently used option is to specify that a function
# can be called with an arbitrary number of arguments.
# These arguments will be wrapped up in a tuple (see Tuples and Sequences).
# Before the variable number of arguments, zero or more normal arguments may occur.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# Lambda Expressions

# Small anonymous functions can be created with the lambda keyword.
# This function returns the sum of its two arguments: lambda a, b: a+b.
# Lambda functions can be used wherever function objects are required.
# They are syntactically restricted to a single expression.

def make_incrementor(n):
    return lambda x: x + n

# The above example uses a lambda expression to return a function.
# Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# Documentation Strings

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

