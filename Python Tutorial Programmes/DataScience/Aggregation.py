# Aggregation - the formation of a number of things into a cluster.

# Python has several methods are available to perform aggregations on data.
# It is done using the pandas and numpy libraries.
# The data must be available or converted to a dataframe to apply the aggregation functions.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(df)

r = df.rolling(window=3,min_periods=1)
print(r)

# Apply Aggregation on a Whole Dataframe

r = df.rolling(window=3,min_periods=1)
print(r.aggregate(np.sum))

# Apply Aggregation on a single column

r = df.rolling(window=3,min_periods=1)
print(r['A'].aggregate(np.sum))

# Apply Aggregation on a multiple columns

r = df.rolling(window=3,min_periods=1)
print(r[['A','B']].aggregate(np.sum))