# Create an empty dicitonary. Allow 4 friends to enter their favorite language as values and keys as their names. Assume that the names are unique

lang_dict = {}
name = input("Enter your name:- ")
lang = input("Enter your fav language:- ")
lang_dict.update({name:lang})
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