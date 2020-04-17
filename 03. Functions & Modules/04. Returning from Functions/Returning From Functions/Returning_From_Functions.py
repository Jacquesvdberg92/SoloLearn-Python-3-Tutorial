# Returning from Functions

# Certain functions, such as int or str, return a value that can be used later.
# To do this for your defined functions, you can use the return statement.
# For example:
def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)
#7
#8

# The return statement cannot be used outside of a function definition.

# Once you return a value from a function, it immediately stops being executed. 
# Any code after the return statement will never happen.
# For example:
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))
#9
