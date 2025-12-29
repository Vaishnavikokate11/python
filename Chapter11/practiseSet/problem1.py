class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i} + {self.j}")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i} + {self.j} + {self.k}")

o = TwoDVector(1,2)
o2 = ThreeDVector(3,4,5)
o.show()
o2.show()
# print(o.i, o.j)
# print(o2.i,o2.j,o2.k)
