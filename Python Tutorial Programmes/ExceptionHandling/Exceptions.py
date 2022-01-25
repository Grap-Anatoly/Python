# It is possible to write programs that handle selected exceptions

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Ooops! That was not valid number. Try again...")

# The try statement works as follows.
#
# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# If an exception occurs during execution of the try clause,
# the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed,
# and then execution continues after the try/except block.
# If an exception occurs which does not match the exception named in the except clause,
# it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

# A try statement may have more than one except clause, to specify handlers for different exceptions.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Ooops! That was not valid number. Try again...")

# A class in an except clause is compatible with an exception if it is the same class or
# a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class).

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# The try … except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception.
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# ------------------------------

# The raise statement allows the programmer to force a specified exception to occur.

# raise NameError("Hi There")

# If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# The raise statement allows an optional from which enables chaining exceptions.

# def func():
#      raise ConnectionError
#
# try:
#      func()
# except ConnectionError as exc:
#      raise RuntimeError('Failed to open database') from exc

# The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.

try:
     raise KeyboardInterrupt
finally:
     print('Goodbye, world!')