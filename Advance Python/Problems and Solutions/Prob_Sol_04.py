try:
    a = int(input("Enter your first number = "))
    b = int(input("Enter your second number = "))
    print(a/b)
except Exception as e:
    print("None is allowed to divide number with 0")