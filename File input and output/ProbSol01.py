# Ques:- Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

f = open("poems.txt")
fille = f.read()
if ("twinkle" in fille):
    print("Word found in file")
else:
    print("Word not found in file")

f.close()