# Question:- Write a program to input eight numbers from the user and display all the unique numbers(once)

unique_set = set()
number= int(input("Enter the first number :- "))
unique_set.add(int(number))
number= int(input("Enter the second number :- "))
unique_set.add(int(number))
number= int(input("Enter the third number :- "))
unique_set.add(int(number))
number= int(input("Enter the fourth number :- "))
unique_set.add(int(number))
number= int(input("Enter the fifth number :- "))
unique_set.add(int(number))
number= int(input("Enter the sixth number :- "))
unique_set.add(int(number))
number= int(input("Enter the seventh number :- "))
unique_set.add(int(number))
number= int(input("Enter the eighth number :- "))
unique_set.add(int(number))

print(unique_set)