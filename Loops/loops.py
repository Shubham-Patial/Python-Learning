# Question:- Write a program to print numbers from 1 to 50 using while loop

i = 1
while(i<51):
    print(i)
    i += 1
print("\n\n")
# Question:- Write a program to print the content of a list using while loop

l = [1,3,True,4,"Shubham", 54.64,"Aditya"]

i=0
while(i<len(l)):
    print(l[i])
    i += 1
print("\n\n")

for i in range(1,11): #this means loop will start from 1 and end at 10
    print(i)
print("\n")

for i in range(11): #if there is nothing it means the loop will start from 0 and end at 10
    print("i")
print("\n")

for i in range(1, 11, 2): # This means the counting will start from 1 to 10 with missing 2 number after each iteration hence printing all odd numbers from 1 to 10.
    print(i) 
print("\n")

l = [11,22,33,44,55,66]
for i in l: # used l instead of range cause we wanna go till the length of the list.
    print(i)
print("\n")

t = (66,55,44,33,22,11)
for i in t: # used t instead of range cause we wanna go till the length of the tuple.
    print(i)
print("\n")

name = 'Shubham Patial'
for i in name:
    print(i) # Printing my name but with newline after each character
print("\n")

name = 'Shubham Patial'
for i in name:
    print(i, end="") # end="" is used to prevent newline after each character
print("\n")

