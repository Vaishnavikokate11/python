
class Employees: 
    language= "Python"  
    salary = 1200000

    def __init__(self, name, lagnguage, salary):
        self.name = name
        self.language = lagnguage
        self.salary = salary
        print("i am object")  # dunder method this is automatically call no need to call 
    
    def getInfo(self):
        print(f"The language is{self.language} and salary is {self.salary}")

vaishu = Employees("vaishu", "js", 120000) 
# vaishu.name = "vaishu" 
print(vaishu.name ,vaishu.language, vaishu.salary)
vaishu.getInfo()