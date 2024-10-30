d = {} #empty dictionary
marks = {
    "Harry" : 88,
    "Shubham" : 99,
    27 : "Shubham's Birthday",
    2003 : "Shubham's Birth Year"
} # declaring a dictionary
print(marks["Shubham"]) # printing the value of Key
print(marks[2003]) # printing the value of Key
print(marks.items()) # items function is used to display the dictionary in duplet form
print(marks.keys()) # keys function is used to display the keys of the dictionary 
print(marks.values()) # values function is used to display the values of the dictionary
marks.update({"Shubham" : 100, "Aditya" : 70}) # update function is used to update the values in the dictionary as dictionary is mutable and also if ther is no key and value in dictionary which is stated in update it then adds it in the dictionary
print(marks.get("Shubham1")) # Output for this line will be None
print(marks["Shubham1"]) # marks.get() and marks[] they both functions look like same and produce same result but still they are different because when there is no key in the dictionary then marks.get() will give me None as output but marks[] will give me error. output for this line will be error
print(marks) # printing the dictionary