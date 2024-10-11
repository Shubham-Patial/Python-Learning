a  = ()
print(type(a)) # used to see the type of a
# a = (1) #This is not a tuple, this is integer to python because there is no comma after 1 so to make it a tuple remember put a comma and difference a = (1, 43, 464, 223, "Shubham", False, 33.2)between tuple and list is the way we put brackets
a = (1, 43, 464, 223, "Shubham", False, 33.2, 43)
print(a)
b = a.count(43) # used to count the value in the tuple
print(b)
c = a.index("Shubham") # used to find the index of the value in the tuple
print(c)
# tuple is immutable like string REMEMBER