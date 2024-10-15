# Question:- write a program to print the following star patter

# *****
# *   *
# *****         for n = 5
# *   *
# *****

n = int(input("Enter the number you want to print reverse table of = "))

for i in range(1, n+1):
    if (i % 2 == 0):
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    else:
        print("*"*n,end="")
    print(" ",end="")
    print("")