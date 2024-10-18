# Question:- Write a python program using function to convert celsius to fahrenheit

def converter(celcius): # function definition accepting one parameter
    f = (9/5) * celcius +32
    return f # returning the value stored in f 

celcius = float(input("Enter the celcius temperature = "))
print("The temperature after converting it in fahrenheit is = ", converter(celcius)) # function call with one argument