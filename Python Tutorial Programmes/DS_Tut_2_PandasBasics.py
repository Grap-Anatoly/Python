# Pandas is a high-level data manipulation tool developed by Wes McKinney.
# It is built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

# Convert dictionaries into tables
import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)

# The firs column (key) is index, chage default index:
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv(Comma-separated values) file using Pandas.
# Now, the csv cars.csv is stored and can be imported using pd.read_csv:

cars = pd.read_csv('cars.csv')

print(cars)
# Indexing data frames

# cars = pd.read_csv('cars.csv', index_col=0)
#
# print(cars['cars_per_cap'])
#
# # Print out country column as Pandas DataFrame
# print(cars[['cars_per_cap']])
#
# # Print out DataFrame with country and drives_right columns
# print(cars[['cars_per_cap', 'country']])

# Square brackets can also be used to access observations (rows) from a DataFrame.

print(brics[0:4])

# from first to fourth

print(brics[2:5])

# from third to fifth

# You can also use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
# iloc is integer index based, so you have to specify rows and columns by their integer index

print(brics.iloc[2])

print(brics.loc[["IN", "CH"]])