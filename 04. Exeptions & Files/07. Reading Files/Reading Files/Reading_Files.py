# Reading Files

# The contents of a file that has been opened in text mode can be read using the read method. 
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
# This will print all of the contents of the file "filename.txt".

# To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte. 
# With no argument, read returns the rest of the file. 
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
# Just like passing no arguments, negative values will return the entire contents.

# After all contents in a file have been read, 
# any attempts to read further from that file will return an empty string, 
# because you are trying to read from the end of the file.
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
#Re-reading
#
#Finished

# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
#For example:
file = open("filename.txt", "r")
print(file.readlines())
file.close()
#['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']

# You can also use a for loop to iterate through the lines in the file: 
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 
#Line 1 text

#Line 2 text

#Line 3 text

#In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.