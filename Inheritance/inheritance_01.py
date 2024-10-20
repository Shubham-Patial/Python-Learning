# Question:- Create a class C 2d vector and use it to create another class representing a 3-d vector

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

two = TwoDVector(1, 2)
two.show()
three = ThreeDVector(3, 4, 5)
three.show()