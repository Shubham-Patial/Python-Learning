# Ques:- Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.

def tables(n): # function definition which is accepting one parameter
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n" # printing the tables

    with open(f"tables/table_{n}", "w") as f: # creating the folder tables in which each file contains one table of that particular number for examples here it will create table_1 and so on till 20 in tables folder.
        f.write(table) # used to write the table in the files

for i in range(1, 21):
    tables(i) 