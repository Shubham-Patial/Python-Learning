# Question:- Write a program to print multiiplication table of a given number using for loop

number = int(input("Enter the number you want to print table of ")) #user input

for i in range(1,11): # runs loop from 1 to 10 remember the number you write it runs 1 less than that
    print(f"{number} x {i} = ",number * i) # printing