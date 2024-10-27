# Ques:- Write a python program to rename a file to "removed_by_python.txt"

with open("old_mean.txt") as f:
    content = f.read() # reading the contents of the file and storing it in content variable

with open("old_mean_renamed.txt","w") as f:
    f.write(content) # writing the content of the old_mean.txt and then writing it in new files. Remember there are other ways to do this by importing some libraries but do that with chatgpt