class Employee:
    a = 1 # class attribute
    
    @classmethod # if we comment out this and don't use classmethod then the show method will print 45 as the value because e.a = 45 instance variable so it will print that value but using classmethod will help you print the value of class attribute 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # used to show like it is just a property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # used to set the value
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45 # instance variable

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()