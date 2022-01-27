# The data that is already present in a row and column format or which can be easily converted to rows and columns so
# that later it can fit nicely into a database is known as structured data. Examples are CSV, TXT, XLS files etc.
# These files have a delimiter and either fixed or variable width where
# the missing values are represented as blanks in between the delimiters.
# But sometimes we get data where the lines are not fixed width, or they are just HTML, image or pdf files.
# Such data is known as unstructured data.
# While the HTML file can be handled by processing the HTML tags, a feed from twitter or a plain text document
# from a news feed can without having a delimiter does not have tags to handle.
# In such scenario we use different in-built functions from various python libraries to process the file.

# In the below example we take a text file and read the file segregating each of the lines in it.
# Next we can divide the output into further lines and words

filename = 'info.txt'

with open(filename) as fn:

# Read each line
   ln = fn.readline()

# Keep count of lines
   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1

# Counting Word Frequency
# We can count the frequency of the words in the file using the counter function as follows.

from collections import Counter

with open(r'info.txt') as f:
               p = Counter(f.read().split())
               print(p)