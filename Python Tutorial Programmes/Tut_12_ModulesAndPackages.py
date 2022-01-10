# Modules in Python are simply Python files with a .py extension.
# The name of the module will be the name of the file.
# A Python module can have a set of functions, classes or variables defined and implemented.
import play_game
# We may also import the function draw_game directly into the main script's namespace, by using the from command.
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# We may also use the import * command to import all objects from a specific module

from draw import *

def main():
    result = play_game()
    draw_game(result)
# For example, if you have two draw modules with slighty different names - you may do the following:
# if visual_mode:
    # in visual mode, we draw using graphics
    # import draw_visual as draw
# else:
    # in textual mode, we print out text
    # import draw_textual as draw

# There are a couple of ways we could tell the Python interpreter where to look for modules,
# aside from the default, which is the local directory and the built-in modules.
# You could either use the environment variable PYTHONPATH to specify additional directories to look for modules in, like this:

# PYTHONPATH=/foo python play_game

# Another method is the sys.path.append function.

# sys.path.append("/foo")

# -----------------
# If we want to import the module urllib, which enables us to create read data from URLs
import urllib

# urllib.urlopen()

dir(urllib)
# -----------------

import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))