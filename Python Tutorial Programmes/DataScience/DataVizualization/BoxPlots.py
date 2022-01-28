# Boxplots are a measure of how well distributed the data in a data set is.
# It divides the data set into three quartiles.
# This graph represents the minimum, maximum, median, first quartile and third quartile in the data set.
# It is also useful in comparing the distribution of data across data sets by drawing boxplots for each of them.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')
