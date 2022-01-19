# When looping through dictionaries,
# the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k,v)

# When looping through a sequence, the position index and corresponding value
# can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using set() on a sequence eliminates duplicate elements.
# The use of sorted() in combination with set() over a sequence is
# an idiomatic way to loop over unique elements of the sequence in sorted order.

for i in sorted(set(basket)):
    print(i)

