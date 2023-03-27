# Errors and Exceptions

# Until now error messages haven’t been more than mentioned,
# but if you have tried out the examples you have probably seen some.
# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

# Syntax Errors ---------------------------------------------------------------------

# Syntax errors, also known as parsing errors,
# are perhaps the most common kind of complaint you get while you are still learning Python:

# >>> while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
#                    ^
# SyntaxError: invalid syntax

# The parser repeats the offending line and displays a little ‘arrow’
# pointing at the earliest point in the line where the error was detected.

# Exceptions ------------------------------------------------------------------------

# Even if a statement or expression is syntactically correct,
# it may cause an error when an attempt is made to execute it.
# Errors detected during execution are called exceptions and are not unconditionally fatal:
# you will soon learn how to handle them in Python programs.
# Most exceptions are not handled by programs, however, and result in error messages as shown here:

# >>> 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't convert 'int' object to str implicitly

# Handling Exceptions ----------------------------------------------------------

# It is possible to write programs that handle selected exceptions

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# The try statement works as follows.

# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.

# If an exception occurs during execution of the try clause, the rest of the clause is skipped.
# Then if its type matches the exception named after the except keyword,
# the except clause is executed, and then execution continues after the try statement.

# If an exception occurs which does not match the exception named in the except clause,
# it is passed on to outer try statements; if no handler is found,
# it is an unhandled exception and execution stops with a message as shown above.

# A class in an except clause is compatible with an exception if it is the same class or a base class thereof
# (but not the other way around — an except clause listing a derived class is not compatible with a base class).
# For example, the following code will print B, C, D in that order:

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
# It is useful for code that must be executed if the try clause does not raise an exception. For example:

import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# Raising Exceptions -------------------------------------------------------------------------------

# The raise statement allows the programmer to force a specified exception to occur.

# raise NameError('HiThere')
#
# raise ValueError  # shorthand for 'raise ValueError()'

# If you need to determine whether an exception was raised but don’t intend to handle it,
# a simpler form of the raise statement allows you to re-raise the exception:

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# User-defined Exceptions -------------------------------------------------------------------

# Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes).
# Exceptions should typically be derived from the Exception class, either directly or indirectly.

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# Defining Clean-up Actions -------------------------------------------------------------------

# The try statement has another optional clause which is intended to define clean-up actions
# that must be executed under all circumstances. For example:


try:
   raise KeyboardInterrupt
finally:
   print('Goodbye, world!')


# If a finally clause is present,
# the finally clause will execute as the last task before the try statement completes.
# The finally clause runs whether or not the try statement produces an exception.
# The following points discuss more complex cases when an exception occurs:

# If an exception occurs during execution of the try clause, the exception may be handled by an except clause.
# If the exception is not handled by an except clause,
# the exception is re-raised after the finally clause has been executed.

# An exception could occur during execution of an except or else clause.
# Again, the exception is re-raised after the finally clause has been executed.
#
# If the try statement reaches a break, continue or return statement,
# the finally clause will execute just prior to the break, continue or return statement’s execution.
#
# If a finally clause includes a return statement, the returned value will be the one from the finally clause’s
# return statement, not the value from the try clause’s return statement.

# Predefined Clean-up Actions ---------------------------------------------------------------------------

# Some objects define standard clean-up actions to be undertaken when the object is no longer needed,
# regardless of whether or not the operation using the object succeeded or failed.
# Look at the following example, which tries to open a file and print its contents to the screen.

for line in open("myfile.txt"):
    print(line, end="")

# The problem with this code is that it leaves the file open for an indeterminate amount of time after
# this part of the code has finished executing.
# This is not an issue in simple scripts, but can be a problem for larger applications.
# The with statement allows objects like files to be used
# in a way that ensures they are always cleaned up promptly and correctly.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
        
# After the statement is executed, the file f is always closed,
# even if a problem was encountered while processing the lines.
# Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.