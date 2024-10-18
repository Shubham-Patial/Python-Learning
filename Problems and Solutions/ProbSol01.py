class Programmer:
    company = "Microsoft"

    def __init__(self, name, city, language_of_work):
        self.name = name
        self.city = city
        self.language_of_work = language_of_work

sam = Programmer("Sam", "Brampton", "Python")
print(sam.name, sam.city, sam.language_of_work)
adi = Programmer("Adi", "Brampton", "Java")
print(adi.name, adi.city, adi.language_of_work)

