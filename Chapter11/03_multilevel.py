class Employee:
    a = 1

class Programmer(Employee):
    b = 3

class Manager(Programmer):
    c =7

o = Employee()
print(o.a)
#print(o.b)  shows error
p = Programmer()
print(p.a, p.b)
m = Manager()
print(m.a, m.b, m.c)