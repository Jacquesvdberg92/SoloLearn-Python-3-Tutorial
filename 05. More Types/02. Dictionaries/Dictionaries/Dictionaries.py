# Dictionaries

# Dictionaries are data structures used to map arbitrary keys to values.
# Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
# Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
#24
#42

# Trying to index a key that isn't part of the dictionary returns a KeyError.
# Example:
primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])
print(primary["yellow"])
#[255, 0, 0]
#
#KeyError: 'yellow'

# As you can see, a dictionary can store any types of data as values.
# An empty dictionary is defined as {}.

# Only immutable objects can be used as keys to dictionaries. 
# Immutable objects are those that can't be changed. 
# So far, the only mutable objects you've come across are lists and dictionaries. 
# Trying to use a mutable object as a dictionary key causes a TypeError.
bad_dict = {
  [1, 2, 3]: "one two three", 
}
#TypeError: unhashable type: 'list'

