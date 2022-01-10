# Decorators allow you to make simple modifications to callable objects like
# functions, methods, or classes.

# As you may have seen, a decorator is just another function which takes a functions and returns one.

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
print(return_num(5)) # should return 15

# Make a decorator factory which returns a decorator that decorates functions with one argument.
# The factory should take one argument, a type, and then returns a decorator that makes function
# should check if the input is the correct type.
# If it is wrong, it should print("Bad Type") (In reality, it should raise an error, but error raising isn't in this tutorial).

def type_check(correct_type):
    def type_check_generator(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print ("Bad Type")
        return new_function
    return type_check_generator  # it returns the new generator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])