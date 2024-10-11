name = "Shubham"

print(name[0:3]) # Print the first three characters of the string 'name' using slicing (0 to 3, but index 3 is excluded so it will slice from 0 to 2 actually giving "Shu" as output but we have to write 1 more index that is from 0 to 3)
print(name[-7: -4]) # Print characters from index -7 to -4 (slicing from the start of the string, moving from left to right) this means the same as above

print(name[:7]) # Print the entire string 'name' from the start (index 0) up to (but not including) index 7