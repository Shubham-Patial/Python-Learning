# Ques:- Repeat program 4 for a list of such words to be censored.
words = ["Banana", "sugar", "shake", "mango"] # initializing the list
with open("file_5.txt") as f:
    content = f.read() # reading the content of the file
for word in words: # searching the word in the list which is words
    content = content.replace(word, "#" * (len(words) + 1)) # replacing 

with open("file_5.txt", "w") as f:
    f.write(content)