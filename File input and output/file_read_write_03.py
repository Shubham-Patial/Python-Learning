# Ques:- A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.
with open("multiple_words.txt") as f:
    content = f.read() # storing the contents of the file

updated_file = content.replace("Donkey", "######") # replace method is used to replace the following word with the given word in the file and updated file is used to store the updated content of the file 

with open("multiple_words.txt", "w") as f: 
    f.write(updated_file) # writing the updated content stored in updated_file in multiple_words.txt