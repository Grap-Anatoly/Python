# DateTime
import datetime

feb_16_2019 = datetime.date(year=2019, month=2, day=16)
feb_16_2019 = datetime.date(2019, 2, 16)
print(feb_16_2019) #2019-02-16

time_13_48min_5sec = datetime.time(hour=13, minute=48, second=5)
time_13_48min_5sec = datetime.time(13, 48, 5)
print(time_13_48min_5sec) #13:48:05

timestamp= datetime.datetime(year=2019, month=2, day=16, hour=13, minute=48, second=5)
timestamp = datetime.datetime(2019, 2, 16, 13, 48, 5)
print(timestamp) #2019-01-02 13:48:05

# Aliasing matplotlib.pyplot as plt
from matplotlib import pyplot as plt
# plt.plot(x, y)

# Aliasing calendar as c
import calendar as c
print(c.month_name[1])

# Three different ways to import modules:
# First way
# import module
# module.function()
#
# # Second way
# from module import function
# function()
#
# # Third way
# from module import *
# function()

# Returns a random integer N in a given range, such that start <= N <= end
# random.randint(start, end)
import random

r1 = random.randint(0, 10)
print(r1) # Random integer where 0 <= r1 <= 10

# Prints a random element from a sequence
seq = ["a", "b", "c", "d", "e"]
r2 = random.choice(seq)
print(r2) # Random element in the sequence