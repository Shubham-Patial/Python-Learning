def name(first_name, last_name): # function definition accepting two parameter
    print(f"{first_name} {last_name}")
    return 0

a = name("Shubham", "Patial") # storing the arguments with function call in variable named as ' a '
print(a) # printing a but basically the function result

def gooday(name, greeting = "How are you"): # function definition with two parameters and here the second parameter named as greeting take the argument which is passed and if there is no argument passed then take "How are you" as the default argument
    print(f"{name} {greeting}") 
    return 1

a = gooday("Shubham", "Wat are you doing man") # storing the arguments with function call in variable named as ' a '
b = gooday("Harry") # storing the arguments with function call in variable named as ' a ' and if only 1 argument is passed and it has 2 parameters it will throw errow but in this case it wont for this read above
print(a) # printing a but basically the function call stored in variable a 
print(b) # printing b but basically the function call stored in variable b