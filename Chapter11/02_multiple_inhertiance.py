class Employee: #base/ parent class
    company = "ITC"
    name = ""
    salary = 120000
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")

class Coder:
    language = "Python"
    def printLang(self):
        print(f"Out of other language {self.language} is best")


class Programmer(Employee, Coder): #child / inherited class
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The name of employee is {self.company} and salary {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLang()
