# Ques:- Write a program to find out whether a file is idential & matches the content of another file

with open("this.txt") as f:
    content = f.read() # reading the content of this.txt file and storing it in content

with open("this_copy.txt") as f:
    content2 = f.read() # reading the content of this_copy.txt file and storing it in content

    if content == content2: # checks if the contents of both of the files are same?
        print("The content of both the files are same")
    else:
        print("NO the content of both the files are diff")