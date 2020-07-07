class cicle:
    pi = 3.14

    def __init__ (self, r, a, c):
        self.r = 0
        self.a = 0
        self.c = 0
    def accept(self,r):
        self.r = r
    def area (self):

        self.a = (self.r * self.r) * cicle.pi
        print ( self.a )

    def cicum (self):
        self.c = (2 * self.r )*cicle.pi
        print(self.a)

    def display(self):
        print("the radius is",self.r,"the area is",self.a,"the circumfernce is",self.c)
obj1 = cicle(0,0,0)
obj1.accept(4)
obj1.area()
obj1.cicum()
obj1.display()

