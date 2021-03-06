# Comments

# Comments are annotations to code used to make it easier to understand. 
# They don't affect how code is run.
# In Python, a comment is created by inserting an octothorpe (otherwise known as a number sign or hash symbol: #). 
# All text after it on that line is ignored.
# For example:
x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment
#1

# Python doesn't have general purpose multiline comments, as do programming languages such as C.


# Docstrings

# Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. 
# However, they are more specific and have a different syntax. 
# They are created by putting a multiline string containing an explanation of the function below the function's first line.
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
    
shout("spam")
#spam!

# Unlike conventional comments, docstrings are retained throughout the runtime of the program. 
# This allows the programmer to inspect these comments at run time.
