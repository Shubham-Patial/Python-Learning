# Ques:- Write a program to wipe out the contents of a file using python

with open("this_copy.txt", "w") as f:
    f.write("") # overwrite the content of the files and makes it empty
