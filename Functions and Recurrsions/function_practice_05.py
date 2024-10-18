# Question:- Write a python function to remove a given word from a list and strip it at the same time

def remove_word(l, word): # function definition accepting two parameter
    n =[]
    for i in l:
        if ( i != word):
            n.append(i.strip(word)) # i.strip is used to remove the particular thing but in this it is used to remove the word which matches the user input and append function is used to add the result of i.strip to the list
    returs

word = input ("Enter the word - ")
l = ["Sam", "Harry", "Shubham", "amber", "am"]
print(remove_word(l, word))