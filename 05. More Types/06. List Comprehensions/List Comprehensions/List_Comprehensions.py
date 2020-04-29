# List Comprehensions

# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
# For example, we can do the following:
# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)
#[0, 1, 8, 27, 64]

# List comprehensions are inspired by set-builder notation in mathematics.

# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
#[0, 4, 16, 36, 64]

# Trying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.
even = [2*i for i in range(10**100)]
#MemoryError

# This issue is solved by generators.
