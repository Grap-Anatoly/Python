# Adding Annotations
# Many times, we need to annotate the chart by highlighting the specific locations of the chart.
# In the below example we indicate the sharp change in values in the chart by adding annotations at those points.

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,10)
y = x ^ 2
z = x ^ 3
t = x ^ 4
# Labeling the Axes and Title
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(x,y)

#Annotate
plt.annotate('Second Entry', xy=[2,1])
plt.annotate('Third Entry', xy=[4,6])

# We sometimes need a chart with multiple lines being plotted. Use of legend represents
# the meaning associated with each line. In the below chart we have 3 lines with appropriate legends.

# Adding Legends
plt.plot(x,z)
plt.plot(x,t)
plt.legend(['Race1', 'Race2','Race3'], loc=4)

# We can modify the presentation style of the chart by using different methods from the style package.

#Style the background
plt.style.use('fast')
plt.plot(x,z)

plt.show()