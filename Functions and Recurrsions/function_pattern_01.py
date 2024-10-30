# Question:- Write a python function to print first n lines of the following pattern

# ***
# **              for n = 3
# *

def pattern(n): # function definition accepting one parameter
    if ( n == 0):  # Base case: if n is 0, return (stop the recursion from going into infinity loop)
        return
    print("*" * n)
    pattern(n-1) # Recursively call the pattern function with n-1 to print the next line

n = int(input("Enter the number of lines = "))
print(pattern(n)) # calls the function with one argument