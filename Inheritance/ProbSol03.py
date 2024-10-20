# Question:- Create a class Employee and add Salary and increment properties to it. Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 200
    increment = 25

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, incremented_salary):
        self.increment = ((incremented_salary/self.salary) - 1 ) * 100
emp = Employee()
# print(emp.SalaryAfterIncrement)
emp.SalaryAfterIncrement = 300
print(emp.increment)
        
