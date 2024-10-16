# Question:- Write a python program using function to print multiplication table of a given number

def multiplication(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter the number you want to print table of = "))
multiplication(n)