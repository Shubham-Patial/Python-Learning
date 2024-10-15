# Question:- Write a program to print multiplication table of n using for loop in reversed order

n = int(input("Enter the number you want to print reverse table of = "))

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")
