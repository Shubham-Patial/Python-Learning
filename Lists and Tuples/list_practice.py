l1 = [7,9.4,"Shubham",] # This is the way we create the list and a list is combination of integers, float and string data types
# print(l1[5]) #this gonna throw error as the list is out of range cause the length of the index is from 0 to 2 which is 3
print(l1[2]) #used to print the member of the list at index 2 which is Shubham 
l2 = [4,54,32,26,21,1]
b = l2.sort() # Sort method is used to sort the list in ascending order
print (b) # to check if it has any return value or not
print("This is the sorted list = ",l2)
a = l2.reverse() # Reverse method is used to reverse the list
print(a) # to check if it has any return value or not
print("This is the reversed list = ",l2)
c = l2.insert(3, "Shubham") # Insert method is used to insert any value in the desired index like in this we add Shubham at index of 3
print(c) # to check if it has any return value or not
print("This is the list which has Shubham inserted at the index of = ",l2)
d = l2.pop(3)
print(l2)
print(d) # To check if it has any return value or not
print("This is the list from which Shubham has been removed = ",l2)
f = l2.remove(54)
print(f) # to check if it has any return value or not
print("This is the list from which 54 is removed = ",l2)
fruits = ["Apple", "Mango", "Pineapple", "Watermelon", 45, 45.3, False, "Aditya", "Shubham"]

print(fruits)

e = fruits.append("Deep") #append function is used to add any value in the last of the list
print(e) # to check if it has any return value or not
print(fruits) # printing the list

# ** Remember list is an mutable thing and they are kinda array 