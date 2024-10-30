# Create a class "Pets" from a class "Animals" and furthur create a class "Dog" from Pets. Add a method "Bark" to class "Dog"

class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")


d = Dog()

d.bark()