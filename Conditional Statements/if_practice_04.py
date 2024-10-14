# Question:- Write a program to find whetehr a given username conatins less than 10 characters or not.

name = input("Enter the name you want to = ")

if(len(name) < 10):
    print("The name has less than 10 character!!")
else:
    print("The name has more than 10 character")