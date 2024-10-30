# Ques:- Write a program to make a copy of a text file "this.txt"

with open ("this.txt") as f:
    content = f.read() # reading the content of the this.txt

with open ("this_copy.txt", "w") as f:
    f.write(content) # writing the content of this.txt file stored in variable content in this_copy.txt
