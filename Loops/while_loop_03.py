# Question:- Write a program to calculate the factorial of a given number using for loop

fact_num = int(input("Enter the number you want to find factorial of = ")) # user input

i = 1 
product = 1
while(i <= fact_num): # loop runs till i is less than or equal to fact_num
    product *= i 
    i += 1
print(f"The factorial of {fact_num} numbers is = ",product)