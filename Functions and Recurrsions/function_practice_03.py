# Question:- Write a recursive function to calculate the sum of first n natural number

def sum(number):
    if (number == 1):
        return 1
    return sum(number-1) + number
    
number = int(input("Enter any natural number = "))
print(sum(number))