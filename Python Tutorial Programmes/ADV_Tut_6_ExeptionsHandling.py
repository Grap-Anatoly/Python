# Python's solution to errors are exceptions.

# But sometimes you don't want exceptions to completely stop the program.
# You might want to do something special when an exception is raised.
# This is done in a try/except block.

def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3 , 4, 5)

    for i in range (20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()

# -----------------

actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        return actor ["name"].split()[1]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

