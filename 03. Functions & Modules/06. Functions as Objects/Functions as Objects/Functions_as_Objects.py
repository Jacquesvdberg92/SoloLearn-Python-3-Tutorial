# Functions

# Although they are created differently from normal variables, functions are just like any other kind of value.
# They can be assigned and reassigned to variables, and later referenced by those names.
def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))
#28

# The example above assigned the function multiply to a variable operation. 
# Now, the name operation can also be used to call the function.

# Functions can also be used as arguments of other functions.
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
#30

# As you can see, the function do_twice takes a function as its argument and calls it in its body.
