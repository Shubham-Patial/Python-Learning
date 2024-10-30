# Override the __len__() method on vector on problem 05 to display the dimensions of the vector

class Vector:
    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

v1 = Vector([1, 2, 3, 4])
print(len(v1))