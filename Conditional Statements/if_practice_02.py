# Question:- Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

subject_1 = int(input("Enter the makrs of the English subject = "))
subject_2 = int(input("Enter the makrs of the Maths subject = "))
subject_3 = int(input("Enter the makrs of the Science subject = "))

percentage = (100 * (subject_1 + subject_2 + subject_3)) / 300

if (subject_1 < 33):
    print("You failed in English subject")
elif (subject_2 < 33):
    print("You failed in Maths subject")
elif (subject_3 < 33):
    print("You failed in Science subject")
elif(percentage < 40):
    print("You average is below 40% so you failed in overall")
else:
    print("You Passed in this course with good marks in all subjects!!")