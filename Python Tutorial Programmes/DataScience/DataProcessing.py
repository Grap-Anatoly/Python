# Data Operations in Numpy
# The most important object defined in NumPy is an N-dimensional array type called ndarray.
# It describes the collection of items of the same type.
# Items in the collection can be accessed using a zero-based index.

import numpy as np

# more than one dimensions
a = np.array([[1,2],[3,4]])
print(a)

# minimum dimensions
a = np.array([1, 2, 3, 4, 5], ndmin = 2)
print(a)

# dtype parametr
a = np.array([1, 2, 3, 4, 5], dtype= complex)
print(a)

# Pandas handles data through Series,Data Frame, and Panel.
import pandas as pd

data = np.array(['a', 'b', 'd', 'e'])
s = pd.Series(data)
print(s)

# Pandas DataFrame
# A Data frame is a two-dimensional data structure, i.e.,
# data is aligned in a tabular fashion in rows and columns.

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

