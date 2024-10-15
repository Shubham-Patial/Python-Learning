# Question:- Write a program to find whether a given number is prime or not

number = int(input("Enter the number you want to check is prime or not = "))

for i in range (2, number):
    if (number % i == 0):
        print("The given number is not a prime number")
        break
else:
    print("The given number is a prime number")