# Question:- Label the program written in question 4 with comments

import os

# Select the directory you wanna see the content of 
directory_path = '/Users/shubh/OneDrive - Seneca'

# Use the os module to list the directory path
contents = os.listdir(directory_path)

# print the contents of the directory in 2 different way and you can see the both outputs
# 1st way:-
# for item in contents:
#     print(item)
# 2nd way:-
print(contents) 