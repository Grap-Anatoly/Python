# You can create partial functions in python by using the partial function from the functools library.
# Partial functions allow one to derive a function with x parameters to a function with fewer parameters
# and fixed values set for the more limited function.

from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

# Edit the function provided by calling partial() and replacing the first three variables in func().
# Then print with the new partial function using only one input variable so that the output equals 60.

def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

res = partial(func, 5 , 10 ,4)
print(res(2))

# Using partial when we need multiple usage of same function with most of their
# parameters as same values with difference in one or two values

res = partial(func, 5 , 10 ,4)
# last param is free to input, while 3 before are already set
# 5*4 + 10*3 + 4*2 + x
print(res(4))
print(res(6))
print(res(8))
print(res(10))