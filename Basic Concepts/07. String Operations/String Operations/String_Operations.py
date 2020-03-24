# As with integers and floats, strings in Python can be added, using a process called concatenation, which can be done on any two strings.
# When concatenating strings, it doesn't matter whether they've been created with single or double quotes. 

print ("Spam" + 'Eggs')
# SpamEggs

print("First String" + ", " + "Second String")
#First String, Second String

# Even if your strings contain numbers, they are still added as strings rather than integers. 
# Adding a string to a number produces an error, as even though they might look similar, they are two different entities.

print("2" + "2")
# 22

print(1 + "2" + 3 + '4')
# This will produce an error

# Strings can also be multiplied by integers. 
# This produces a repeated version of the original string. 
# The order of the string and the integer doesn't matter, but the string usually comes first.
# Strings can't be multiplied by other strings. 
# Strings also can't be multiplied by floats, even if the floats are whole numbers.

print("String"*3)
# StringStringString

print(4 * '2')
# 2222

# The followint 2 will produce errors
print('17' * '87')

print('Python' * 7.0)
