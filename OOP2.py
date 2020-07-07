class demo:
    def __init__ (self, value1, value2):
        print ( "Inside init method" )

        self.i = value1
        self.j = value2
    def fun(self):
        print("inside fun ")

        print(self.i,self.j)
    def gun(self):
        print("inside gun")
        print(self.i,self.j)

obj1 = demo(11,21)
print(obj1.i)
print(obj1.j)
obj1.fun()
obj1.gun()
obj2 = demo(50,20)
print(obj2.i)
print(obj2.j)
obj2.fun()
obj2.gun()


