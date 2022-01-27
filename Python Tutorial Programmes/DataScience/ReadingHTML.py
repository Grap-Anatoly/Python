# library known as beautifulsoup.
# Using this library, we can search for the values of html tags and
# get specific data like title of the page and the list of headers in the page.

#  install Beautifulsoup

# In the below example we make a request to an url to be loaded into the python environment.
# Then use the html parser parameter to read the entire html file

# Fetch the html file
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm[:225])

# Extracting tag value

response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print (soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

# Extracting all tags

response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all('b'): print(x.string)

