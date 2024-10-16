# Recursion is a function which calls itself

# for eg:- for n = 6 , 

# 6! = 1 x 2 x 3.........(n -1) x n

# For example if we talk about finding the factorial of n number

# def facctorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     return facctorial(n - 1) * n

# n = int(input("Enter the number you want to find the factorial of = "))

# print(facctorial(n))
# Use Recursion to print the fibonacci series of n numbers

# 0, 1, 1, 2, 3, 5, 8, 13, 21 ..........., n

# def fibonacci(n):
#     if (n == 0):
#         return 0
#     elif (n == 1 or n == 2):
#         return 1
#     else:
#         return fibonacci(n -1) + fibonacci(n-2)

# i = True
# while(i):
#     n = int( input("Enter the number you want to find the fibonacci series of = "))
#     if (n >= 0):
#         i = False
#     else:
#         print ("You have entered a number which is less than 0 and thus we cannot do the fibonacci series for a number which is less than 0!!!\n")
#         i = True
#     print (fibonacci(n))


# Write a program to reverse a user given string but the catch is that you have to only use recursion and iteration

# def reverse(name):
#      if len(name) == 0  or len(name) == 1:
#           return name
#      else:
#           return reverse(name[1:]) + name[0]
     
# name = input("Enter the String you want to get reversed = ").strip()
# print(reverse(name))

# + -------------------------------------+

# This is an iterative way to reverse a string
# name = input("Enter the String you want to get reversed = ")
# updated_name = ''
# l = len(name)
# i = (l - 1)
# while(i >= 0):
#     updated_name += name[i]
#     i -= 1
# print(updated_name)

# + -------------------------------------+
# Another iterative way to reverse a string

# def reverse_string(s):
#     result = ''
#     for i in s:
#         result = i + result  # Prepend each character to the result
#     return result

# s = input("Enter the String you want to get reversed = ")
# print(reverse_string(s))

