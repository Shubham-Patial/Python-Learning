# Question:- Write a program to calculate the grade of a student from his marks from the following scheme:
#                            90-100 -> Ex
#                            80-90 -> A
#                            70-80 -> B
#                            60-70 -> C
#                            50-60 -> D
#                            <50 -> F

marks_1 = float(input("Enter your marks in Maths = "))
marks_2 = float(input("Enter your marks in English = "))
marks_3 = float(input("Enter your marks in Science = "))
marks_4 = float(input("Enter your marks in History = "))
marks_5 = float(input("Enter your marks in Computer = "))
marks_5 = float(input("Enter your marks in Geography = "))
marks_6 = float(input("Enter your marks in Arts = "))

percentage = (100 * (marks_1 + marks_2 + marks_3 + marks_4 + marks_5 + marks_6) / 600) # calculates the percentage

if (percentage >= 90):
    print("Your grade is Excellent")
elif (percentage >= 80 and percentage < 90):
    print("Your grade is A")
elif (percentage >= 70 and percentage < 80):
    print("Your grade is B")
elif (percentage >= 60 and percentage < 70):
    print("Your grade is C")
elif (percentage >= 50 and percentage < 60):
    print("Your grade is D")
else:
    print("Your grade is F") # if - elif ladder