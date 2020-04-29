# Working with Files

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
# This ensures that the file is always closed, even if an error occurs.

# An alternative way of doing this is using with statements. 
# This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement. 
with open("filename.txt") as f:
   print(f.read())
#The file is automatically closed at the end of the with statement, even if exceptions occur within it.