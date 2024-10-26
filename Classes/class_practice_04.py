class Calculator:
    def __init__(self, number):  # defining the init function which is a constructor and it calls itself when function call is made
        self.number = number
    @staticmethod # staticmethod is used when we want to define a function which does not take any argument
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

