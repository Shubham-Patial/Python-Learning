# Question:- Write a recursive function to calculate the sum of first n natural number

def sum(number): # function definition accepting one parameter
    if (number == 1): # conditional statement
        return 1
    return sum(number-1) + number
    
number = int(input("Enter any natural number = ")) # accepting user input
print(sum(number)) # function call with one argument