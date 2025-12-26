# make class programmer and info of programmer which working in microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self , name, salary):
        self.name = name
        self.salary = salary

obj1 = Programmer("Raj", 120000)
print(obj1.name, obj1.salary, obj1.company)

obj2 = Programmer("Sham", 12000)
print(obj2.name, obj2.salary, obj2.company)
        