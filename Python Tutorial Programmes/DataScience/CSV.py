# Reading data from CSV(comma separated values) is a fundamental necessity in Data Science.
# Often, we get data from various sources which can get exported to CSV format so that they can be used by other systems.
# The Panadas library provides features using which we can read the CSV file in full
# as well as in parts for only a selected group of columns and rows.

# The read_csv function of the pandas library is used read the content
# of a CSV file into the python environment as a pandas DataFrame.

import pandas as pd
data = pd.read_csv('input.csv')
print(data)

# The read_csv function of the pandas library can also be used to read some specific rows for a given column.

print(data[0:5]['name'])

# The read_csv function of the pandas library can also be used to read some specific columns.
# We use the multi-axes indexing method called .loc() for this purpose.

print (data.loc[:,['name']])

# The read_csv function of the pandas library can also be used to read some specific columns and a range of rows.

print (data.loc[2:6,['salary','name']])