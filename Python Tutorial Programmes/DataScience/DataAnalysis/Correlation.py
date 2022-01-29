# Correlation refers to some statistical relationships involving dependence between two data sets.
# Simple examples of dependent phenomena include the correlation between the physical
# appearance of parents and their offspring, and the correlation between the price for a product and its supplied quantity.

import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

# without regression
sns.pairplot(df, kind="scatter")
plt.show()