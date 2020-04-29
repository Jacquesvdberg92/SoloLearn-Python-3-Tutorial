# String Formatting

# So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings within strings. 
# String formatting uses a string's format method to substitute a number of arguments in the string.
# Example:
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
#Numbers: 4 5 6

# Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.

# String formatting can also be done with named arguments.
# Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)
#5, 12
