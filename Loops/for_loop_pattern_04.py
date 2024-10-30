# Question:- write a program to print the following star patter

# *****
# *   *
# *   *         for n = 5
# *   *
# *****

n = int(input("Enter the number you want to print reverse table of = "))

for i in range(1, n+1): # loop runs from 1 to n. As we know in for loop it excludes the last number so if the value of variable n is 10 it will run from 1 to 9 but n + 1 means 9+1 which means loop will run from 1 to 10
    if (i == 1 or i == n):
        print("*"* n, end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="") # end method is used to prevent a new line as print method in python has a new line automatically after it is executed
    print("")