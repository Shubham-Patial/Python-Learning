# Question:- Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is a loyal dog and it one of the favourite pet of many people")

d = Dog()
d.bark()