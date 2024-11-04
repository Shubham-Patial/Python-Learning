from functools import reduce

def greater(a, b):
    if a>b:
         return a
    return b

my_list = [34,3232,34324,3241,23453,34]

print (reduce(greater, my_list))