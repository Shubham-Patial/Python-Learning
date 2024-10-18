class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @staticmethod    
    def greet(): # used static method to make the method static so that it doesn't use the self parameter
        print("Hello, I am learing class and other stuff in python here")
    
    def salary(self, salary):
        print(f"Salary of {self.name} is {salary}")

emp = Employee("Sam")
emp.greet()
emp.salary(130000)