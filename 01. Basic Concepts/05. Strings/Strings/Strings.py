# Strings

# If you want to use text in Python, you have to use a string.
# A string is created by entering text between two single or double quotation marks.

# When the Python console displays a string, it generally uses single quotes. 
# The delimiter used for a string doesn't affect how it behaves in any way.

print("Python is fun!")
# Python is fun!

print('Always look on the bright side of life')
# Always look on the bright side of life

# Some characters can't be directly included in a string.
# For instance, double quotes can't be directly included in a double quote string; this would cause it to end prematurely.

# Characters like these must be escaped by placing a backslash before them.
# Other common characters that must be escaped are newlines and backslashes.
# Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.

print('Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!')
# Brian's mother: He's not the Messiah. He's a very naughty boy!

###################################################################################################################

# Newlines

# Python provides an easy way to avoid manually writing "\n" to escape newlines in a string. 
# Create a string with three sets of quotes, and newlines that are created by pressing Enter are automatically escaped for you.

print( """Customer: Good morning.
Owner: Good morning, Sir. Welcome to the National Cheese Emporium.""")