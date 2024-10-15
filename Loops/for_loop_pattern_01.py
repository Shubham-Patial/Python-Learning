# Question:- Write a program to print the following star pattern
#        *
#       ***
#      *****        for n = 3

n = int(input("Enter the number :- ")) #user input
for i in range(1, n+1): # loop runs from 1 to n. As we know in for loop it excludes the last number so if the value of variable n is 10 it will run from 1 to 9 but n + 1 means 9+1 which means loop will run from 1 to 10
    print(" "*(n-i), end="") # end method is used to prevent a new line as print method in python has a new line automatically after it is executed
    print("*"*(2*i-1), end="") # end method is used to prevent a new line as print method in python has a new line automatically after it is executed
    print("")

#It was a bit complex
