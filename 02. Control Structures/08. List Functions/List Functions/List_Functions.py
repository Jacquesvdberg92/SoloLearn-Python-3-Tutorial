# List Functions
# Another way of altering lists is using the append method.
# This adds an item to the end of an esxiting list

nums = [1, 2, 3]
nums.append(4)
print(nums)
# [1, 2, 3, 4]

# To get the number of items in the list you can use the 'len' function
nums2 = [2,1,5,4,3]
print(len(nums2))
# 5

# The insert method is similar to the append, except that it allows you to add a new item at any position in the list, as opposed to just the end.
words = ["Python", "Fun"]
index = 1 # note that index is acting as a place holder
words.insert(index, "is")
print(words)
# ['Pythin', 'is', 'fun']

# The index method finds the first occurrence of a list item and returns its index.
# if the item isn't in the list, it raises a ValueError

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
# 2
print(letters.index('p'))
# 0 - as its the first occurrence
# print(letters.index('z'))
# ValueError: 'z' is not in list

# There are a few more useful functions and methods for lists.

# max - returns the list item with the maximum value
nums3 = [1,2,3,4,5,6,7,8,9,0]
print(max(nums3))
# 9

# min - returns the list item with the minimum value
nums3 = [1,2,3,4,5,6,7,8,9,0]
print(min(nums3))
# 0

# list.count(obj) - returns the amount of times an item occurs in a list
nums3 = [1,2,1,4,1,6,1,8,1,0]
print(nums3.count(1))
# 5

# list.remove(obj) - removes an object from the list
nums3 = [1,2,3,4,5,6,7,8,9,0]
nums3.remove(5)
print(nums3)
# [1,2,3,4,6,7,8,9,0]

# list.reverse() - reverses the objects in the list
nums3 = [1,2,3,4,5,6,7,8,9,0]
nums3.reverse()
print(nums3)
# [0,9,8,7,6,5,4,3,2,1]