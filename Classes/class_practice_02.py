class Calculator:
    def __init__(self, number): # defining the init function which is a constructor and it calls itself when function call is made
        self.number = number

    def square(self): # defining a square function for calculating the square of the number
        print(f"The square of {self.number} is {self.number * self.number}")
    def cube(self): # defining a cube function for calculating the cube of the number
        print(f"The cube of {self.number} is {self.number * self.number * self.number}")
    def square_root(self): # defining a square root function for calculating the square root of the number
        print(f"The square of {self.number} is {self.number ** 1/2 }")

cal = Calculator(4) # creating the object of the class Calculator
cal.square() # calling the square function of the class Calculator
cal.cube() # calling the cube function of the class Calculator
cal.square_root() # calling the square root function of the class Calculator

