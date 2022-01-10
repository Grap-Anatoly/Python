primes = [2, 3, 5, 7]
for prime in primes:
    print (prime)
# For loops can iterate over a sequence of numbers using the "range"
# and "xrange" functions. The difference between range and xrange is
# that the range function returns a new list with numbers of that
# specified range, whereas xrange returns an iterator,
# which is more efficient.
# ------------------------

for x in range(5):
    print (x)
for x in range(3,6):
    print (x)
for x in range(3,8,2):
    print (x)
# (start,end,step)
# ------------------------

count = 0
while count < 5:
    print (count)
    count += 1
# default while
# ------------------------

count = 0
while True:
    print (count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    else:
        print (x)
# default break and continue
# ------------------------

count = 0
while count < 5:
    print (count)
    count += 1
else:
    print ("Count value raached %d" %(count))

for i in range(1,10):
    if i % 5 == 0:
        break
    else:
        print (i)
else:
    print("this is not printed because for loop is terminated "
          "because of break but not due to fail in condition")

# Unlike languages like C,CPP.. we can use else for loops.
# When the loop condition of "for" or "while" statement fails
# then code part in "else" is executed.
# If a break statement is executed inside the for loop then the "else" part is skipped.
# Note that the "else" part is executed even if there is a continue statement.
# ------------------------

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number % 2 == 0:
        print (number)
    elif number is 237:
        break