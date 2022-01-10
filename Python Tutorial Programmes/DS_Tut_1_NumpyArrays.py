# Numpy arrays are great alternatives to Python Lists.
# Some of the key advantages of Numpy arrays are that they are fast, easy to work with,
# and give users the opportunity to perform calculations across entire arrays.
import numpy as np

height = [1.87, 1.94, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Now we can perform element-wise calculations on height and weight.

bmi = np_weight / np_height ** 2

print(bmi)

# Another great feature of Numpy arrays is the ability to subset.
# For instance, if you wanted to know which observations in our BMI array are above 23,
# we could quickly subset it to find out.
bmi > 25

bmi[bmi > 25]

print(bmi)

# --------------------------

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_kg = np.array(weight_kg)

print(np_weight_kg)

np_weight_lbs = np_weight_kg * 2.2

print(np_weight_lbs)
