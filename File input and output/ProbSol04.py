# Ques:- A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.
with open("multiple_words.txt") as f:
    content = f.read()

updated_file = content.replace("Donkey", "######")

with open("multiple_words.txt", "w") as f:
    f.write(updated_file)