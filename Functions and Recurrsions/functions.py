def name(first_name, last_name):
    print(f"{first_name} {last_name}")
    return 0

a = name("Shubham", "Patial")
print(a)

def gooday(name, greeting = "How are you"): #here the second greeting means take the argument which is passed and if there is not argument passed then take "How are you" as the default argument
    print(f"{name} {greeting}")
    return 1

a = gooday("Shubham", "Wat are you doing man")
b = gooday("Harry") #if only 1 argument is passed and it has 2 parameters it will throw errow but in this case it wont for this read above
print(a)
print(b)