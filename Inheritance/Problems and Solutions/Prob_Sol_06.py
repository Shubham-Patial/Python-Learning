# Write a __str__() method to print the vector as follow:-

# 7i + 10j + 5k

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        result = Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)
        return result

    def __mul__(self, v2):
        result = self.i * v2.i + self.j * v2.j + self.k * v2.k
        return result

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50