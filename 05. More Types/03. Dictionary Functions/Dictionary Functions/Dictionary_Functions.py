# Dictionaries

# Just like lists, dictionary keys can be assigned to different values.
# However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)
#{1: 1, 2: 4, 3: 9, 4: 16, 8: 64}

# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
# Example:
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
#True
#False
#True

# A useful dictionary method is get. 
# It does the same thing as indexing, 
# but if the key is not found in the dictionary it returns another specified value instead ('None', by default).
# Example:
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
#[2, 3, 4]
#None
#not in dictionary
