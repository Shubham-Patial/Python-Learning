# Create an empty dicitonary. Allow 4 friends to enter their favorite language as values and keys as their names. Assume that the names are unique

lang_dict = {} # empty dictionary
name = input("Enter your name:- ")
lang = input("Enter your fav language:- ")
lang_dict.update({name:lang}) # update method is used to add or update the value in the dict
name = input("Enter your name:- ")
lang = input("Enter your fav language:- ")
lang_dict.update({name:lang})
name = input("Enter your name:- ")
lang = input("Enter your fav language:- ")
lang_dict.update({name:lang})
name = input("Enter your name:- ")
lang = input("Enter your fav language:- ")
lang_dict.update({name:lang})

print(lang_dict)