# Writing Files

# To write to files you use the write method, which writes a string to the file.
# For example:
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
#This has been written to a file

# The "w" mode will create a file, if it does not already exist.

# When a file is opened in write mode, the file's existing content is deleted.
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
#Reading initial contents
#some initial text
#Finished
#Reading new contents
#Some new text
#Finished

# As you can see, the content of the file has been overwritten.

# The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
#12

