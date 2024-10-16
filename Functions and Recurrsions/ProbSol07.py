# Question:- Write a python function to remove a given word from a list and strip it at the same time

def rem(l, word):
    n =[]
    for i in l:
        if ( i != word):
            n.append(i.strip(word))
    return n

word = input ("Enter the word - ")
l = ["Sam", "Harry", "Shubham", "amber", "am"]
print(rem(l, word))
