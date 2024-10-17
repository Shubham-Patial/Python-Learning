# Ques:- Write a program to mine a log file and find out whether it contains 'python'

with open("log.txt") as f:
    search_word = f.read()

if ("python" in search_word):
    print("Word found in log file")
else:
    print("Word not found in the log file")