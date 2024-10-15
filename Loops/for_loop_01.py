# Question:- Write a program to print multiiplication table of a given number using for loop

number = int(input("Enter the number you want to print table of "))

for i in range(1,11):
    print(f"{number} x {i} = ",number * i)