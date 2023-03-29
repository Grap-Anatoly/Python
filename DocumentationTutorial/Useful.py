# Floating Point Arithmetic: Issues and Limitations

# Floating-point numbers are represented in computer hardware as base 2 (binary) fractions.
# For example, the decimal fraction

# 0.125
# has value 1/10 + 2/100 + 5/1000, and in the same way the binary fraction

# 0.001
# has value 0/2 + 0/4 + 1/8.
# These two fractions have identical values, the only real difference being that the first is written
# in base 10 fractional notation, and the second in base 2.

# Unfortunately, most decimal fractions cannot be represented exactly as binary fractions.
# A consequence is that, in general,
# the decimal floating-point numbers you enter are only approximated
# by the binary floating-point numbers actually stored in the machine.

# Note that this is in the very nature of binary floating-point:
# this is not a bug in Python, and it is not a bug in your code either.
# You’ll see the same kind of thing in all languages that support your hardware’s floating-point arithmetic
# (although some languages may not display the difference by default, or in all output modes).

# For more pleasant output, you may wish to use string formatting to produce a limited number of significant digits:
import math

format(math.pi, '.12g')  # give 12 significant digits
# '3.14159265359'
format(math.pi, '.2f')   # give 2 digits after the point
# '3.14'
repr(math.pi)
# '3.141592653589793'

# It’s important to realize that this is, in a real sense,
# an illusion: you’re simply rounding the display of the true machine value.

