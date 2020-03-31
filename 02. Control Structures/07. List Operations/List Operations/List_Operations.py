# List Operations
# The item at a specific index can be reassigned.
# For example:

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
# [7, 7, 5, 7, 7]

# Lists can be added and multiplied is the same way as strings

num = [1, 2, 3]
print(num + [4,5,6])
# [1, 2, 3,4,5,6]
print(num * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# to check if an item is in a list, the 'in' operator can be used.
# It returns True if the item occurs one or more times in the list, and False if it doesn't

words = ["spam", "eggs", "Spam", "sausage"]
print("spam" in words)
# True
print("egg" in words)
# True
print("Hello World!" in words)
# False

# The in operator is also used to determine whether or not a string is a substring of another string.


# To check if an item is not in a list, you can use the not operator in one of the following ways:

nums = [1, 2, 3]
print(not 4 in nums)
# True
print(4 not in nums)
# True
print(not 3 in nums)
# False
print(3 not in nums)
# False