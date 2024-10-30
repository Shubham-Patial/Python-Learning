# Write a class Vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum() and dot() product of them

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v2):
        result = Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
        return result

    def __mul__(self, v2):
        result = self.x * v2.x + self.y * v2.y + self.z * v2.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50