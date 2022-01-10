# Sets are lists with no duplicate entries.

print(set("my name is Eric and Eric is my name".split()))

# This will print out a list containing "my", "name", "is", "Eric", and finally "and".
# Since the rest of the sentence uses words which are already in the set,
# they are not inserted twice.

a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

# Next methods like joins from SQL,inner join, right join, left join ,

# To find out which members attended both events, you may use the "intersection"
print(a.intersection(b))

# To find out which members attended only one of the events, use the "symmetric_difference"
print(a.symmetric_difference(b))

# To find out which members attended only one event and not the other, use the "difference"
print((a.difference(b)))

# To receive a list of all participants, use the "union" (without duplicates)
print(a.union(b))
