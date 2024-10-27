# Ques:- Write a program to mine a log file and find out whether it contains 'python'

with open("log.txt") as f:
    search_word = f.read() # reading the content of the file

if ("python" in search_word): # searching for word python in the file and based on it performs the conditional statement
    print("Word found in log file")
else:
    print("Word not found in the log file")