# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# For instance, use your favorite text editor to create a file called fibo.py
# in the current directory with the following contents:

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Now we can enter the Python interpreter and import this module with the following command:
# import fibo

# A module can contain executable statements as well as function definitions.
# These statements are intended to initialize the module.
# They are executed only the first time the module name is encountered in an import statement.

# Executing modules as scripts
# When you run a Python module with
# python fibo.py <arguments>

# the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".
# That means that by adding this code at the end of your module

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# you can make the file usable as a script as well as an importable module,
# because the code that parses the command line only runs if the module is executed as the “main” file

# The Module Search Path

# When a module named spam is imported, the interpreter first searches for a built-in module with that name.
# If not found, it then searches for a file named spam.py in a list of directories given by the variable
# sys.path. sys.path is initialized from these locations:

# The directory containing the input script (or the current directory when no file is specified).
# PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# The installation-dependent default.

# “Compiled” Python files

# To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory
# under the name module.version.pyc, where the version encodes the format of the compiled file;
# it generally contains the Python version number.
# For example, in CPython release 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc.
# This naming convention allows compiled modules from different releases and different versions of Python to coexist.

# Standard Modules --------------------------------------------------------------------------------

# Python comes with a library of standard modules, described in a separate document,
# the Python Library Reference (“Library Reference” hereafter). Some modules are built into the interpreter;
# these provide access to operations that are not part of the core of the language but are nevertheless built in,
# either for efficiency or to provide access to operating system primitives such as system calls.
# The set of such modules is a configuration option which also depends on the underlying platform.
# For example, the winreg module is only provided on Windows systems.
# One particular module deserves some attention: sys, which is built into every Python interpreter.

import sys

# The dir() Function -----------------------------------------------------------------------------

# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings

print(dir(sys))

# Without arguments, dir() lists the names you have defined currently

print(dir())

# dir() does not list the names of built-in functions and variables.
# If you want a list of those, they are defined in the standard module builtins

# Packages ----------------------------------------------------------------------------------------
# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
# For example, the module name A.B designates a submodule named B in a package named A.
# Just like the use of modules saves the authors of different modules
# from having to worry about each other’s global variable names,
# the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry
# about each other’s module names.

# Users of the package can import individual modules from the package, for example:

# import sound.effects.echo
# from sound.effects import echo

# Yet another variation is to import the desired function or variable directly:

# from sound.effects.echo import echofilter

# Importing * From a Package

# Now what happens when the user writes from sound.effects import *?
# Ideally, one would hope that this somehow goes out to the filesystem,
# finds which submodules are present in the package, and imports them all.
# This could take a long time and importing sub-modules might have unwanted side-effects that
# should only happen when the sub-module is explicitly imported.

# Intra-package References

# When packages are structured into subpackages (as with the sound package in the example),
# you can use absolute imports to refer to submodules of siblings packages.
# For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package,
# it can use from sound.effects import echo.
#
# You can also write relative imports, with the from module import name form of import statement.
# These imports use leading dots to indicate the current and parent packages involved in the relative import.
# From the surround module for example, you might use:

# from . import echo
# from .. import formats
# from ..filters import equalizer