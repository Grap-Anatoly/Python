def sum(a,b):
    return a+ b

a = 1
b = 2
c = sum(a,b)
print(c)
# we can use python's lambda functions, which are inline functions defined at the same place we use it.
# So we don't need to declare a function somewhere and revisit the code just for a single time use.
# They don't need to have a name, so they also called anonymous functions.
# We define a lambda function using the keyword lambda.

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

# -----------------------
# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    result = lambda i : i % 2
    if result(i) == 0:
        print("True")
    else:
        print("False")

# my_lambda = lambda x : (x % 2) == 1
# print(my_lambda(i))
