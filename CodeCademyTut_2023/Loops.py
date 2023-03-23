numbers = [0, 254, 2, -1, 3]

for num in numbers:
    if (num < 0):
        print("Negative number detected!")
        break
    print(num)

# 0
# 254
# 2
# Negative number detected!

# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]

print(result)
# [0, 4, 16, 36, 64]

# for loop

# for < temporary variable > in < list variable >:
#     < action statement >
#     < action statement >

# each num in nums will be printed below
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# continue keyword

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

# range

# Print the numbers 0, 1, 2:
for i in range(3):
  print(i)

# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")

# The range() function can be used to create a list that can be used
# to specify the number of iterations in a for loop.

# while
#In Python, a while loop will repeatedly execute
# a code block as long as a condition evaluates to True.

# This loop will only run 1 time
hungry = True
while hungry:
  print("Time to eat!")
  hungry = False

# This loop will run 5 times
i = 1
while i < 6:
  print(i)
  i = i + 1
  
# nested loops


groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)