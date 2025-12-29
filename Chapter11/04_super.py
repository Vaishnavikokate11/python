class Employee:
    def __init__(self):
        print("This is Employee Constactor")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("This is Programmer Constactor")
    b = 3

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("This is Manager Constactor")
    c =7

# o = Employee()
# print(o.a)
#print(o.b)  shows error
# p = Programmer()
# print(p.a, p.b)
m = Manager()
print(m.a, m.b, m.c)