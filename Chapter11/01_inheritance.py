class Employee: #base/ parent class
    company = "ITC"
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")


class Programmer(Employee): #child / inherited class
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name of employee is {self.name} and salary {self.salary}")

a = Employee
b = Programmer
print(a.company, b.company)