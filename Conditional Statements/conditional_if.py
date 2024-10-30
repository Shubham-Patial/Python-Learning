age = int(input("Enter your age:- "))

# if elif else ladder

if(age >= 18): #checks if the age entered by the user is greater than or equal to 18 and if yes, then runs the other two print statements which are within the blocks of if 
    print("You are eligible for driving license")
    print("Happy!!")

elif(age<=0): #if the if statement was wrong or false then it will check this piece of code and if the condition is true it will run this block of code
    print("Are you ok? Have you ever seen this age")
else: # if none of the if statement is right then this it will run this piece of code
    print("You are not eligible for driving license") 