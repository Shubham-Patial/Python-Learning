class Calculator:
    def __init__(self, number):
        self.number = number
    @staticmethod    
    def greet():
        print("Hello, Good morning and thanks for using this program")
    def square(self):
        print(f"The square of {self.number} is {self.number * self.number}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number * self.number * self.number}")
    def square_root(self):
        print(f"The square of {self.number} is {self.number ** 1/2 }")

cal = Calculator(4)
cal.greet()
cal.square()
cal.cube()
cal.square_root()

