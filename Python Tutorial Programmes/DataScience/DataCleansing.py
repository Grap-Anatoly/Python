# Missing data is always a problem in real life scenarios.
# Areas like machine learning and data mining face severe issues in the accuracy of their model predictions because
# of poor quality of data caused by missing values.
# In these areas, missing value treatment is a major point of focus to make their models more accurate and valid.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],
                                         columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)

# Using reindexing, we have created a DataFrame with missing values.
# In the output, NaN means Not a Number.

# To make detecting missing values easier (and across different array dtypes),
# Pandas provides the isnull() and notnull() functions

print(df['one'].isnull())

# Cleaning / Filling Missing Data
# Pandas provides various methods for cleaning the missing values.

print ("NaN replaced with '0':")
print(df.fillna(0))

# Fill NA Forward and Backward
# Using the concepts of filling discussed in the
# ReIndexing Chapter we will fill the missing values.

print(df.fillna(method='pad'))

# Drop Missing Values
# If you want to simply exclude the missing values,
# then use the dropna function along with the axis argument.

print(df.dropna())

# Replace Missing (or) Generic Values
# Many times, we have to replace a generic value with some specific value.
# We can achieve this by applying the replace method.

df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})

print(df)
print(df.replace({1000:10,2000:60}))
