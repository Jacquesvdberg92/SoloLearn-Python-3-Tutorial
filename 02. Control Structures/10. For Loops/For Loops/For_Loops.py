
# Loops

# Sometimes, you need to perform code on each item in a list.
# This is called iteration, and it can be accomplished with a while loop and a counter variable.
# For example:

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1
#hello!
#world!
#spam!
#eggs!


# for Loop

# Iterating through a list using a while loop requires quite a lot of code,
# so Python provides the for loop as a shortcut that accomplishes the same thing.
# The same code from the previous example can be written with a for loop, as follows: 

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
#hello!
#world!
#spam!
#eggs!

# The for loop is commonly used to repeat some code a certain number of times. 
# This is done by combining for loops with range objects.

for i in range(5):
  print("hello!")
#hello!
#hello!
#hello!
#hello!
#hello!

