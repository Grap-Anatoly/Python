# In Linear Regression these two variables are related through an equation,
# where exponent (power) of both these variables is 1.
# Mathematically a linear relationship represents a straight line when plotted as a graph.
# A non-linear relationship where the exponent of any variable is not equal to 1 creates a curve.


import seaborn as sb
from matplotlib import pyplot as plt

df = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = df)
plt.show()