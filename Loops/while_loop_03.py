# Question:- Write a program to calculate the factorial of a given number using for loop

fact_num = int(input("Enter the number you want to find factorial of = "))

i = 1 
product = 1
while(i <= fact_num):
    product *= i 
    i += 1
print(f"The factorial of {fact_num} numbers is = ",product)