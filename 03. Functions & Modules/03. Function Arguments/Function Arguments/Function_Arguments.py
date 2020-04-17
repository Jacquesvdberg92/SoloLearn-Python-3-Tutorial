# Arguments

# All the function definitions we've looked at so far have been functions of zero arguments, 
# which are called with empty parentheses.
# However, most functions take arguments.
# The example below defines a function that takes one argument:
def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
#spam!
#eggs!
#python!


# Arguments

# You can also define functions with more than one argument; separate them with commas.
def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)
#13
#13

# Function arguments can be used as variables inside the function definition. 
# However, they cannot be referenced outside of the function's definition. 
# This also applies to other variables created inside a function.
def function(variable):
   variable += 1
   print(variable)

function(7)
print(variable)
#8
#NameError: name 'variable' is not defined

# Technically, parameters are the variables in a function definition, 
# and arguments are the values put into parameters when functions are called.


