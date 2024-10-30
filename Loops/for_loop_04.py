# Question:- Write a program to print multiplication table of n using for loop in reversed order

n = int(input("Enter the number you want to print reverse table of = ")) # user input

for i in range(1,11): # loops run from 1 to 10
    print(f"{n} x {11-i} = {n*(11-i)}") # prints the table
