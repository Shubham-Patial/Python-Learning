class Employee:
    company = "ITC"
    name = "Shubham"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company name is {self.company}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "ITC Infotech"
    language = "Python"
    def showLanguage(self):
        print(f"The company is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()
b.show()
b.showLanguage()    