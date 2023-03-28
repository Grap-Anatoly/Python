# Operating System Interface -----------------------------------------------

# The os module provides dozens of functions for interacting with the operating system:

import os
os.getcwd()      # Return the current working directory
'C:\\Python38'
# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell

# For daily file and directory management tasks,
# the shutil module provides a higher level interface that is easier to use:

import shutil

# shutil.copyfile('data.db', 'archive.db')
# 'archive.db'
# shutil.move('/build/executables', 'installdir')

# File Wildcards =-------------------------------------------------------------------------

# The glob module provides a function for making file lists from directory wildcard searches:

import glob

glob.glob('*.py')

# Command Line Arguments -------------------------------------------------------------------

# Common utility scripts often need to process command line arguments.
# These arguments are stored in the sys module’s argv attribute as a list.
# For instance the following output results from running python demo.py one two three at the command line:

import sys

print(sys.argv)

# The argparse module provides a more sophisticated mechanism to process command line arguments.
# The following script extracts one or more filenames and an optional number of lines to be displayed:

import argparse

# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# Error Output Redirection and Program Termination ---------------------------------------------

# The sys module also has attributes for stdin, stdout, and stderr.
# The latter is useful for emitting warnings and error messages
# to make them visible even when stdout has been redirected:

sys.stderr.write('Warning, log file not found starting a new one\n')

# String Pattern Matching ---------------------------------------------------------------------

# The re module provides regular expression tools for advanced string processing.
# For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# Mathematics ----------------------------------------------------------------------------------

# The math module gives access to the underlying C library functions for floating point math:

import math

print(math.cos(math.pi / 4))

print(math.log(1024, 2))

# The random module provides tools for making random selections:

import random

print(random.choice(['apple', 'pear', 'banana']))

# The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(statistics.mean(data))

print(statistics.median(data))

print(statistics.variance(data))

# Internet Access -------------------------------------------------------------------------------

# There are a number of modules for accessing the internet and processing internet protocols.
# Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:

from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()

# Dates and Times ------------------------------------------------------------------------------

# The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
# While date and time arithmetic is supported,
# the focus of the implementation is on efficient member extraction for output formatting and manipulation.
# The module also supports objects that are timezone aware.

from datetime import date

now = date.today()

print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday

print(age.days)

# Data Compression --------------------------------------------------------------------------

# Common data archiving and compression formats are directly supported by modules including:
# zlib, gzip, bz2, lzma, zipfile and tarfile.

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))
b'witch which has which witches wrist watch'
print(zlib.crc32(s))

# Performance Measurement --------------------------------------------------------------------

# Some Python users develop a deep interest in knowing the relative performance
# of different approaches to the same problem.
# Python provides a measurement tool that answers those questions immediately.

from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# Output Formatting ------------------------------------------------------------------------

# The reprlib module provides a version of repr()
# customized for abbreviated displays of large or deeply nested containers:

import reprlib

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# The pprint module offers more sophisticated control over printing both built-in and user defined objects
# in a way that is readable by the interpreter. When the result is longer than one line,
# the “pretty printer” adds line breaks and indentation to more clearly reveal data structure:

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

# The textwrap module formats paragraphs of text to fit a given screen width:

import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

# Templating -----------------------------------------------------------

# The string module includes a versatile Template class
# with a simplified syntax suitable for editing by end-users.
# This allows users to customize their applications without having to alter the application.
#
# The format uses placeholder names formed by $ with valid Python identifiers
# (alphanumeric characters and underscores).
# Surrounding the placeholder with braces allows it to be followed by more alphanumeric
# letters with no intervening spaces. Writing $$ creates a single escaped $:

from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

# The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary
# or a keyword argument.
# For mail-merge style applications, user supplied data may be incomplete and the safe_
# substitute() method may be more appropriate — it will leave placeholders unchanged if data is missing:

# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# t.substitute(d)
# Traceback (most recent call last):
#   ...
# KeyError: 'owner'
# t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'

# Working with Binary Data Record Layouts -----------------------------------------------------------

# The struct module provides pack() and unpack()
# functions for working with variable length binary record formats.
# The following example shows how to loop through header information in a ZIP file without using the zipfile module.
# Pack codes "H" and "I" represent two and four byte unsigned numbers respectively.
# The "<" indicates that they are standard size and in little-endian byte order:

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

# Multi-threading ------------------------------------------------------------------------------------

# Threading is a technique for decoupling tasks which are not sequentially dependent.
# Threads can be used to improve the responsiveness of applications that
# accept user input while other tasks run in the background.
# A related use case is running I/O in parallel with computations in another thread.

# The following code shows how the high level threading module can run tasks in background while
# the main program continues to run:

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

# Logging -------------------------------------------------------------------------

# The logging module offers a full featured and flexible logging system.
# At its simplest, log messages are sent to a file or to sys.stderr:

import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# Weak References -------------------------------------------------------------------

# Python does automatic memory management (reference counting for most objects and garbage collection
# to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

# This approach works fine for most applications but occasionally there is a need to track objects only
# as long as they are being used by something else.
# Unfortunately, just tracking them creates a reference that makes them permanent.
# The weakref module provides tools for tracking objects without creating a reference.
# When the object is no longer needed,
# it is automatically removed from a weakref table and a callback is triggered for weakref objects.
# Typical applications include caching objects that are expensive to creat

#  Tools for Working with Lists ----------------------------------------------------------

# Many data structure needs can be met with the built-in list type.
# However, sometimes there is a need for alternative implementations with different performance trade-offs.

# The array module provides an array() object that is like a list that stores
# only homogeneous data and stores it more compactly.

from array import array

a = array('H', [4000, 10, 700, 22222])
print(sum(a))

print(a[1:3])

# The collections module provides a deque() object that is like a list with
# faster appends and pops from the left side but slower lookups in the middle.

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# In addition to alternative list implementations,
# the library also offers other tools such as the bisect module with functions for manipulating sorted lists:

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))

#  Decimal Floating Point Arithmetic --------------------------------------------------------

# The decimal module offers a Decimal datatype for decimal floating point arithmetic.
# Compared to the built-in float implementation of binary floating point, the class is especially helpful for

# financial applications and other uses which require exact decimal representation,
# control over precision,
# control over rounding to meet legal or regulatory requirements,
# tracking of significant decimal places, or
# applications where the user expects the results to match calculations done by hand.
#
# For example, calculating a 5% tax on a 70 cent phone charge gives different results in decimal floating point
# and binary floating point. The difference becomes significant if the results are rounded to the nearest cent

from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))

print(round(.70 * 1.05, 2))

# The decimal module provides arithmetic with as much precision as needed: