# Question:- Write a program to greet all the person names stored in a list l1 and which starts with S
            #   l1 =["Harry","Soham","Sachin","Rahul"]


l1 =["Harry","Soham","Sachin","Rahul"]
for i in l1: # to check each each item in list
     if(i.startswith("S")): #startswith method is used to find whether the given value starts with that particular word or letter mentioned in startswith method
         print(f"Hello {i}, Welcome to this Program. This program is being written by Shubham the Coder")

