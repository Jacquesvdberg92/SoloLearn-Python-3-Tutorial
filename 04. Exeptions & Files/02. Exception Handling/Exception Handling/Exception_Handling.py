# Exception Handling

# To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
# The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.
# For example:
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")
#An error occurred
#due to zero division

# In the code above, the except statement defines the type of exception to handle (in our case, the ZeroDivisionError).

# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parentheses, 
# to have the except block handle all of them.
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")
#Error occurred

# An except statement without any exception specified will catch all errors. 
# These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
# For example:
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")
#An error occurred

