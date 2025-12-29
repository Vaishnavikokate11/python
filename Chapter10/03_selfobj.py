
class Employees: 
    language= "Python"  
    salary = 1200000

    def getInfo(self):
        print(f"The language is{self.language} and salary is {self.salary}")

    # this is static method
    @staticmethod
    def greet():
        print("Good morning")

vaishu = Employees() 
#vaishu.language = "js"
vaishu.greet()
vaishu.getInfo()
# Employees.getInfo(vaishu) 

