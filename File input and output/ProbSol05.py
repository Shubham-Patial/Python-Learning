# Ques:- Repeat program 4 for a list of such words to be censored.
words = ["Banana", "sugar", "shake"]
with open("file_5.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(words))

with open("file_5.txt", "w") as f:
    f.write(content)