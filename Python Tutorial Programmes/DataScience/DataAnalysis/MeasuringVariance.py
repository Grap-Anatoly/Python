# In statistics, variance is a measure of how far a value in a data set lies from the mean value.
# In other words, it indicates how dispersed the values are.

# Standard deviation is square root of variance.
# variance is the average of squared difference of values in a data set from the mean value.

import pandas as pd

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)

# Calculate the standard deviation
print(df.std())

# Measuring Skewness
# It used to determine whether the data is symmetric or skewed

print(df.skew())