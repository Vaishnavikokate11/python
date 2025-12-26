# add static method print hello

# make calculator 

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"{self.n* self.n}")
    
    def cube(self):
        print(f"{self.n* self.n* self.n}")
    
    def squrroot(self):
        print(f"{self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello")
    


a = Calculator(4)
a.square()
a.cube()
a.squrroot()
a.hello()
        