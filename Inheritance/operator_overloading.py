class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # this is overloading which is used to overload operators like + - * / and so on and in this we are adding two object
        return self.n + num.n # self.n receives the valus of n and num.n receives value of object m

n = Number(1)
m = Number(2)

print(n + m)