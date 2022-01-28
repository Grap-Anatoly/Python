# Time series is a series of data points in which each data point is associated with a timestamp.
# A simple example is the price of a stock in the stock market at different points of time on a given day.
# Another example is the amount of rainfall in a region at different months of the year.
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('stock.csv')
df = pd.DataFrame(data, columns = ['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']

df.plot(figsize=(15, 6))
plt.show()