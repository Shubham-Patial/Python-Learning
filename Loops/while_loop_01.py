# Question:- Attempt problem 1 using while loop

number = int(input("Enter the number you want to print table of = ")) # user input
i = 1
while (i < 11): # loop runs till i is less than 10
    print(f"{number} x {i} =", number * i) 
    i += 1 # increment the value of i each time it iterates
    