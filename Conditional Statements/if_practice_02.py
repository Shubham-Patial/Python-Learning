# Question:- Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

subject_1 = int(input("Enter the makrs of the English subject = "))
subject_2 = int(input("Enter the makrs of the Maths subject = "))
subject_3 = int(input("Enter the makrs of the Science subject = ")) # gets the user input

percentage = (100 * (subject_1 + subject_2 + subject_3)) / 300 # uses maths to calculate the overall percentage of student in 3 subjects

if (subject_1 < 33): # checks conditions and if this condition is true it will run print and exit but if it is false it will jump over to the next block of code
    print("You failed in English subject")
elif (subject_2 < 33):
    print("You failed in Maths subject")
elif (subject_3 < 33):
    print("You failed in Science subject")
elif(percentage < 40):
    print("You average is below 40% so you failed in overall")
else:
    print("You Passed in this course with good marks in all subjects!!")