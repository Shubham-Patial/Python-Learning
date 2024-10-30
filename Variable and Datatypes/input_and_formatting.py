# Write a python program to calculate square of a number entered by the user

a = int(input("Enter the number you find the square of = ")) # int is used to convert the user input to int. we can also write float to convert it into float data type
b, c =  a * a , a ** 3 # a**3 is the symbol of saying raised to the power and the power is after ** . a * a * a is also right but the thing is sometimes its like raised to the power 30 so in that case it is best option to use a **. So b has b = a * a and c has c = a ** 3 
# b = a * a The same thing as above
# c = a ** 3 The same thing as above
print(f"{a} raised to the power of 3 is = {c}") # The f-string here is used to print the values of the variables inside the curly brackets. This one of the best way to print the values of the variables. Remember to put the variables inside the curly bracket and if there is no f-string used, the values of the variables inside the curly bracket won't be printed.
print("The square of {} is = ".format(a),b) # This is the another way to perform the same task as mentioned above but by the use of format method.
print(f"The square of {a} is = ",b) # The similar way as mentioned in line no. 7