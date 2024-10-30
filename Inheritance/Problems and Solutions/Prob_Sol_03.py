# Create a class "Employee" and add salary and increment properties to it
# Write a method "SalaryAfterIncrement" method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    salary = 500
    increment = 15

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1) * 100




emp = Employee()
print(emp.salaryAfterIncrement)
emp.salaryAfterIncrement = 575
print(emp.increment)