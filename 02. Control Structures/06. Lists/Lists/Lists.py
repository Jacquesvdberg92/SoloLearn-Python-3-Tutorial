# Lists
# lists are another type of object in Python. They are used to store an indexed list of items.
# A list is created using square brackets with commas separating items.
# The certain item in the list can be accessed by using its index in square brackets.
# For example:

words = ["Hello", "World", "!"]
print(words[0])
# Hello
print(words[1])
# World
print(words[2])
# !

# PLEASE NOTE IT STARTS COUNTING FROM 0

# an empty list is created with an empty pair of square brackets.

empty_list = []
print(empty_list)

# Typically, a list will contain items of a single item type, but its also possible to include several different types.
# Lists can also be nested within other lists.

number = 3
things = ["string", 0,[1, 2, number], 4.56]
print(things[1])
# 0
print(things[2])
# [1, 2, 3]
print(things[2][2])
# 3

# Lists of lists are often used to represent 2D grids, as Python lacks the multidimensional arrays that would be used for this in other languages.


# Indexing out of the bounds of possible list values causes an IndexError.
# Some types, such as strings, can be indexed like lists. Indexing strings behaves as though you are indexing a list containing each character in the string.
# For other types, such as integers, indexing them isn't possible, and it causes a TypeError.

str = "Hello World!"
print(str[6])
# W