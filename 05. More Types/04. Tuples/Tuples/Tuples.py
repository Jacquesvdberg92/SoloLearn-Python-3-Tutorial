# Tuples

# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
# Example:
words = ("spam", "eggs", "sausages",)
# You can access the values in the tuple with their index, just as you did with lists:
print(words[0])

# Trying to reassign a value in a tuple causes a TypeError.
words[1] = "cheese"
#TypeError: 'tuple' object does not support item assignment

# Tuples can be created without the parentheses, by just separating the values with commas.
# Example:
my_tuple = "one", "two", "three"
print(my_tuple[0])
#one

# An empty tuple is created using an empty parenthesis pair.
tpl = ()
# Tuples are faster than lists, but they cannot be changed.