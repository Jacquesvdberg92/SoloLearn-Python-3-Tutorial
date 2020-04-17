# Raising Exceptions

# You can raise exceptions by using the raise statement.
print(1)
raise ValueError
print(2)
#1
#ValueError

# Exceptions can be raised with arguments that give detail about them.
# For example:
name = "123"
raise NameError("Invalid name!")
#NameError: Invalid name!

# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
# For example:
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
#An error occurred
#ZeroDivisionError: division by zero

