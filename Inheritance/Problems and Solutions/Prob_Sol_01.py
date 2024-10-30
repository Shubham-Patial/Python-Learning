# Create a class (2D -vector) and use it to create another class representing a 3-D vector

class TwoD_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeD_vector(TwoD_vector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

two = TwoD_vector(1, 2)
two.show()
three = ThreeD_vector(1,2,3)
three.show()