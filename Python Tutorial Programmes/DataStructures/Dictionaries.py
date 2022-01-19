# Another useful data type built into Python is the dictionary (see Mapping Types — dict).
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
# which can be any immutable type; strings and numbers can always be keys.

tel = {'jack': 4098,
       'sape': 4139}

tel['guido'] = 4127

print(tel)
print(tel['sape'])

del tel['sape']
tel['irv'] = 4127

print(tel)

print(list(tel))

print(sorted(tel))

print("guido" in tel)

print("jack" not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
b = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(b)
# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})
# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
c = dict(sape=4139, guido=4127, jack=4098)
print(c)

