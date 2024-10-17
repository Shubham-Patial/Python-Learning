# Ques:- Write a program to find out whether a file is idential & matches the content of another file

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

    if content == content2:
        print("The content of both the files are same")
    else:
        print("NO the content of both the files are diff")