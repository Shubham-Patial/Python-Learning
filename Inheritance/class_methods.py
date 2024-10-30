class Employee:
    a = 1 # class attribute
    
    @classmethod # if we comment out this and don't use classmethod then the show method will print 45 as the value because e.a = 45 instance variable so it will print that value but using classmethod will help you print the value of class attribute 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45 # instance variable

e.show()