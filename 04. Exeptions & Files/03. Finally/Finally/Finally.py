# finally

# To ensure some code runs no matter what errors occur, you can use a finally statement. The finally statement is placed at the bottom of a try/except statement. Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")
#Hello
#Divided by zero
#This code will run no matter what

# Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.
try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print(unknown_var)
finally:
   print("This is executed last")
#1
#This is executed last

#ZeroDivisionError: division by zero
#During handling of the above exception, another exception occurred:
#NameError: name 'unknown_var' is not defined
