my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
print(my_dictionary["song"])

# Merging

dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)

# dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}

# Value Types

dictionary = {
  1: 'hello',
  'two': True,
  '3': [1, 2, 3],
  'Four': {'fun': 'addition'},
  5.0: 5.5
}

# Key - Value

ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex_dict.keys()
# dict_keys(["a","b","c"])

ex_dict.values()
# dict_values(["anteater", "bumblebee", "cheetah"])

ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])

# .get()

# without default
{"name": "Victor"}.get("name")
# returns "Victor"

{"name": "Victor"}.get("nickname")
# returns None

# with default
{"name": "Victor"}.get("nickname", "nickname is not a key")
# returns "nickname is not a key"

# .pop()

famous_museums = {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre', 'Athens': 'The Acropolis Museum'}
famous_museums.pop('Athens')
print(famous_museums) # {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}