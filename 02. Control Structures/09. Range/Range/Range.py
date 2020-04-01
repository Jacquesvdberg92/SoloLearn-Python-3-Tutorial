# Range

# The range function creates a sequential list of numbers.
# The code below generates a list containing all of the integers, up to 10

numbers = list(range(10))
print(numbers)
# [0,1,2,3,4,5,6,7,8,9]

#The call to 'list' is necessary because 'range' by itself creates a 'range object', and this must be converted to a 'list' if you want to use it as one

# if 'range' is called with one argument, it produces an object with values from 0 to the argument.
# if its called with two arguments it will produce values from the first to the second

numbers = list(range(3,8))
print(numbers)
# [3,4,5,6,7]

nums = list(range(8))
print(nums)
# [0,1,2,3,4,5,6,7]


# 'range' can have a third argument, which determines the interval of the sequence produced. This third argument must be an integer

num = list(range(2,10,2)) # variableName = list(range(startpoint, endpoint, intervals)
print(num)
# [2,4,6,8]


