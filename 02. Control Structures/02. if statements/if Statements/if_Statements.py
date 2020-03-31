# if Statements

# You can use if statements to run code if a certain condition holds.
# If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out.
# An if statement looks like this: 

# if expression:
#   statments

# Python uses indentation (white space at the beginning of a line) to delimit blocks of code. 
# Other languages, such as C, use curly braces to accomplish this, but in Python indentation is mandatory; programs won't work without it.
# As you can see, the statements in the if should be indented

if 10 > 5:
    print("10 is greater than 5")

print("Program ended")

# The expression determines whether 10 is greater than five. 
# Since it is, the indented statement runs, and "10 greater than 5" is output. 
# Then, the unindented statement, which is not part of the if statement, is run, and "Program ended" is displayed. 

# To perform more complex checks, if statements can be nested, one inside the other.
# This means that the inner if statement is the statement part of the outer one. 
# This is one way to see whether multiple conditions are satisfied. 

num = 15
if num > 10:
    print(str(num) + " is bigger than 10")
    if num < 20:
        print(str(num) + " is between 10 and 20")


###########################################################################################

# else Statements

# An else statement follows an if statement, and contains code that is called when the if statement evaluates to False.
# As with if statements, the code inside the block should be indented.

if 5 == 4:
    print("5 is equal to 4")
else:
    print("5 isn't equal to 4")

# You can chain if and else statements to determine which option in a series of possibilities is true.
# For example:

x = int(input("Enter a number \n"))
if num == 1:
    print("num is one")
else:
    if num == 2:
        print("Num is 2")
    else:
        print("This could go on for ever")


# elif Statements

# The elif (short for else if) statement is a shortcut to use when chaining if and else statements.
# A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.
# For example:

num = int(input("Enter another Number plese: \n"))
if num == 5:
    print(5)
elif num == 6:
    print(6)
elif num == 7:
    print(7)
elif num == 8:
    print(8)
else:
    print(num)



