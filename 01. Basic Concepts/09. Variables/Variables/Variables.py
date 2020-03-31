# Variables play a very important role in most programming languages, and Python is no exception. 
# A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.

# To assign a variable, use one equals sign. 
# Unlike most lines of code we've looked at so far, it doesn't produce any output at the Python console.

x = 7
print(x)
# 7

print(x + 3)
# 10

print(x)
# 7


# Variables can be reassigned as many times as you want, in order to change their value.
# In Python, variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable. 

x = 123.456
print(x)
# 123.456

x = "This is string"
print(x + "!")
# This is string!


# Certain restrictions apply in regard to the characters that may be used in Python variable names. 
# The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
# Not following these rules results in errors. 

this_is_a_normal_name = 7

123abc = 7
# This is a syntaxError: invalid syntax

spaces arent allowed
#Also a syntax error


# Certain restrictions apply in regard to the characters that may be used in Python variable names. 
# The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
# Not following these rules results in errors. 

del this_is_a_normal_name