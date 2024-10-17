f = open("Aditya.txt", "a") # This is the way to open the file and write in the file
learn = f.write("Aditya is a bad boy") # 
f.close()
s = "Aditya is a bad boy" #Another way of writing into the file
f = open("Aditya.txt", "w")
f.write(s)
f.close()

f = open("Shubham.txt")
print(f.read())
f.close()

f = open("file.txt")
lines = f.readlines() # To get the lines in the files in the form of list
print(lines, type(lines))
f.close()

f = open("file.txt")
line1 = f.readline()
print(line1)
line1 = f.readline()
print(line1)
line1 = f.readline()
print(line1)
line1 = f.readline()
print(line1)
line1 = f.readline()
print(line1)
line1 = f.readline()
f.close()

f = open("file.txt")
line = f.readline() 
while line != "":
    print(line)  
line = f.readline() #doing same thing like upper just in loop

f.close()

s = "\nI also love to play Badminton"
f = open("file.txt", "a") #used to add the text in the file at end
f.write(s)
f.close()

f = open("file.txt")
with open("file.txt") as ff:
     print(ff.read())

