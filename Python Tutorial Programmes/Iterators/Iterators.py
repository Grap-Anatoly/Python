# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# We can also use a for loop to iterate through an iterable object

for x in mytuple:
  print(x)

for x in mystr:
  print(x)

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
      if self.a <= 20:
          x = self.a
          self.a += 1
          return x
      else:
          # To prevent the iteration to go on forever, we can use the StopIteration statement.
          raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


