a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
c = int(input("Enter the third number = "))
d = int(input("Enter the fourth number = "))

if(a > b and a > c and a > d):
    print("First number is the greatest number")
if(b > a and b > c and b > d):
    print("Second number is the greatest number")
if(c > a and c > b and a > d):
    print("Third number is the greatest number")
if(d > a and d > b and a > c):
    print("Fourth number is the greatest number") 