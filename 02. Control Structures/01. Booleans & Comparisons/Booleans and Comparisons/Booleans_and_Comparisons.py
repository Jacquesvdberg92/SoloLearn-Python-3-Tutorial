# Booleans

# Another type in Python is the Boolean type. 
# There are two Boolean values: True and False.
# They can be created by comparing values, for instance by using the equal operator ==. 

my_boolean = True
print(my_boolean)
# true

print(2 == 3)
# False

print("Hello" == "Hello")
#true

# Another comparison operator, the not equal operator (!=), 
# evaluates to True if the items being compared aren't equal, and False if they are.

print(1 != 1)
# False

print("eleven" != "seven")
# true

print(2 != 10)
# True

# Python also has operators that determine whether one number (float or integer) is greater than or smaller than another. 
# These operators are > and < respectively.

print( 7 > 5)
# True

print( 10 < 10)
# False


# The greater than or equal to, and smaller than or equal to operators are >= and <=.
# They are the same as the strict greater than and smaller than operators, except that they return True when comparing equal numbers. 

print(7 <= 8)
# True

print(9 >= 9.0)
# true