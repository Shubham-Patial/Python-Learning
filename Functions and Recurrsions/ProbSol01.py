# Question:- Write a program using function to find greatest of three numbers

def greatest(a,b,c):
    if (a > b and a > c):
        return a
    if (b > a and b > c):
        return b
    if (c > a and c > b):
        return c

a = int(input("Enter your first number = "))    
b = int(input("Enter your second number = "))    
c = int(input("Enter your third number = "))    
print("The greatest number out of all is = ", greatest(a,b,c))