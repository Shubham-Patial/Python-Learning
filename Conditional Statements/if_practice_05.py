# Question:- Write a program which finds out whether a given name is present in a list or not.

l = ["Shubham","Aditya","Deep","Rohan","Harry","Shivansh","Yangki"]

name = input("Enter the name you wanna find in the system = ")

if(name in l): # checks if the name input by the user is present in the list or not and if yes then performs the following block of code otherwise the else block of part runs
    print("Name found in the system!!")
else:
    print("This name is not present in the system")