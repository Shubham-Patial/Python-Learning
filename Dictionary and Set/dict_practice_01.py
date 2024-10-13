# Question:- Write a program to create a dictionary of Hindi words with values as tehir english translation. Provide the user with an option to look it up!

words = {"Kamra":"Room","Kambal":"Blanket","Fonn":"Phone","Kursi":"Chair","Kapde":"Clothes"} # another way to declare the dictionary
meaning = input("Enter any of the following words to know the meaning in english:- 1.) Kamra 2.) Kambal 3.) Fonn 4.) Kursi 5.) Kapde :- ") # taking the user input
print(f"The meaning of the {meaning} is :-",words[meaning])