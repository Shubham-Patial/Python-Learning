# Ques:- Write a python program to rename a file to "removed_by_python.txt"

with open("old_mean.txt") as f:
    content = f.read()

with open("old_mean_renamed.txt","w") as f:
    f.write(content) #there are other ways to do this by importing some libraries but do that with chatgpt