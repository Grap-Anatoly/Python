# Inheritance is the process by which one class takes on the attributes and methods
# of another. Newly formed classes are called child classes,
# and the classes that child classes are derived from are called parent classes.

# Child classes can override or extend the attributes and methods of parent classes.
# In other words, child classes inherit all of the parent’s attributes and methods
# but can also specify attributes and methods that are unique to themselves.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# Each breed of dog has slightly different behaviors. For example, bulldogs have a low bark that sounds like woof,
# but dachshunds have a higher-pitched bark that sounds more like yap.

# print(buddy.speak("Yap"))
#
# print(jim.speak("Woof"))

# Let’s create a child class for each of the three breeds mentioned above:
# Jack Russell Terrier, Dachshund, and Bulldog.

# Remember, to create a child class, you create new class with its own name
# and then put the name of the parent class in parentheses.

class JackRussellTerrier(Dog):

    def speak(self, sound="Arf"):
        return super().speak(sound)
    # You can access the parent class from inside a method of a child class by using super()

class Dachshund(Dog):

    def speak(self, sound="Grr"):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    pass

# Instances of child classes inherit all of the attributes and methods of the parent class

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)

print(buddy.name)

print(jack)

print(jim.speak("Woof"))

# To determine which class a given object belongs to, you can use the built-in type()

print(type(miles))

# What if you want to determine if miles is also an instance of the Dog class?
# You can do this with the built-in isinstance():

print(isinstance(miles,Dog))

print(isinstance(miles,Bulldog))

# Since different breeds of dogs have slightly different barks, you want to provide a default value for the sound argument of their respective .speak() methods.
# To do this, you need to override .speak() in the class definition for each breed.

print(miles.speak())
print(buddy.speak())
print(jim.speak("Woof"))


