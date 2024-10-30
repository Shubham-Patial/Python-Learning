n = int(input("Enter the number you wanna print table of:- "))

table = [n*i for i in range(1,11)]

print(table)

with open("tables.txt", "a") as f:
    f.write(f"Table of {n} is = {str(table)} \n") # formatted in a good way to print table