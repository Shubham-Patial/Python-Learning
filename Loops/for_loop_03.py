# Question:- Write a program to find whether a given number is prime or not

number = int(input("Enter the number you want to check is prime or not = "))

for i in range (2, number): # starts from 2 till number - 1. Remember the loop exceeds the last number so if the value of variable number is is 10 the loop will start from 2 to 9
    if (number % i == 0): # checks condition
        print("The given number is not a prime number")
        break
else: # if the upper condition fails this runs
    print("The given number is a prime number")