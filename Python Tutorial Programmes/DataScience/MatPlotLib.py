# Matplotlib

# Matplotlib is a python library used to create 2D graphs and plots by using python scripts.
# It has a module named pyplot which makes things easy for plotting by providing feature to control line styles,
# font properties, formatting axes etc.

from matplotlib import pyplot as plt
import numpy as np

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()

