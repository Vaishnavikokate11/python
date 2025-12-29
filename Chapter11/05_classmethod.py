class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class method is {cls.a}")

e = Employee()
e.a = 445
e.show()
# print(f"The class method is {e.a}")