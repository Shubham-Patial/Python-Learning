class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number * self.number}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number * self.number * self.number}")
    def square_root(self):
        print(f"The square of {self.number} is {self.number ** 1/2 }")

cal = Calculator(4)
cal.square()
cal.cube()
cal.square_root()

