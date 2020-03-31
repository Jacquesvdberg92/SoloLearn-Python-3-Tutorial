# Floats are used in Python to represent numbers that aren't integers.
# Some examples of numbers that are represented as floats are 0.5 and -7.8237591.
# They can be created directly by entering a number with a decimal point, or by using operations such as division on integers. Extra zeros at the number's end are ignored. 

print(3/7)
# 0.75

print(9.8765000)
# 9.8765

########################################################################################################

# As you saw previously, dividing any two integers produces a float.
# A float is also produced by running an operation on two floats, or on a float and an integer.

print(8/2)
# 4.0

print(6*7.0)
# 42.0

print(4 + 1.65)
# 5.65

# A float can be added to an integer, because Python silently converts the integer to a float. 
# However, this implicit conversion is the exception rather the rule in Python - usually you have to convert values manually if you want to operate on them.