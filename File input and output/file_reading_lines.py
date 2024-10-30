# Ques:- Write a program to find out the line number where python is present from Ques 6


with open("log.txt") as f: 
    lines = f.readlines() # used to get the lines of the files in the form of list
lineno = 1  # counter for counting the line number
for line in lines:
    if ("python" in line):
        print(f"Word found in log file in no. {lineno}")
        break
    lineno += 1
else:
    print("Word not found in the log file")