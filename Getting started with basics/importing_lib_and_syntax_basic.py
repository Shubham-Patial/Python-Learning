# Question:- Write a python program to print the contents of the directory using OS module. Search Online for the function which does that

import os 
directory_path = '/Users/shubh/Downloads'
contents = os.listdir(directory_path)
for item in contents:
    print(item)

# Don't stress out if you don't understand this cause it was just a fun. Use chatgpt to get the explaination of this part of code