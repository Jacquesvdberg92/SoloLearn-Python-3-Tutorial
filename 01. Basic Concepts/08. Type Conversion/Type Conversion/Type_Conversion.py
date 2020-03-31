# In Python, it's impossible to complete certain operations due to the types involved. 
# For instance, you can't add two strings containing the numbers 2 and 3 together to produce the integer 5, as the operation will be performed on strings, making the result '23'.
# The solution to this is type conversion.
# In that example, you would use the int function. 

print('2' + '3')
# 23

print(int('2') + int('3'))
# 5

# Another example of type conversion is turning user input (which is a string) to numbers (integers or floats), to allow for the performance of calculations. 

print(float(input("Enter a Number Please: ")) + float(input("Enter another number: ")))
# Will display the sum of the two numbers as float *so with a decimal point