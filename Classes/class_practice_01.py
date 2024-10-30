class Programmer: # initializing the class
    company = "Microsoft" # attribute. Assigning the value to the attribute of the class

    def __init__(self, name, city, language_of_work): # defining the init function which is a constructor and it calls itself when function call is made
        self.name = name
        self.city = city
        self.language_of_work = language_of_work

sam = Programmer("Sam", "Brampton", "Python") # creating the object of the call and passing the value to the function of the class
print(sam.name, sam.city, sam.language_of_work)
adi = Programmer("Adi", "Brampton", "Java") # creating the object of the call and passing the value to the function of the class
print(adi.name, adi.city, adi.language_of_work)

