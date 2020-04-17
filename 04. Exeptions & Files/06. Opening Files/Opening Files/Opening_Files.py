# Opening Files

# You can use Python to read and write the contents of files.
# Text files are the easiest to manipulate. 
# Before a file can be edited, it must be opened, using the open function. 
myfile = open("filename.txt")
# The argument of the open function is the path to the file. 
# If the file is in the current working directory of the program, you can specify only its name.

# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.

# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# For example: 
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
# You can use the + sign with each of the modes above to give them extra access to files. 
# For example, r+ opens the file for both reading and writing.

# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object.
file = open("filename.txt", "w")
# do stuff to the file
file.close()