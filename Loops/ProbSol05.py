# Question:- Write a program to find teh sum of first n natural numbers using while loop

number = int(input("Enter the number till what you want to find teh sum of natural numbers = "))

i = 1 
sum = 0
while(i <= number):
    sum += i 
    i += 1
print(f"The sum of {number} natural numbers is = ",sum)