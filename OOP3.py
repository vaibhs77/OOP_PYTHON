class arithmatic:
    def __init__(self,i,j):
         self.i = 0
         self.j = 0
    def accept(self,i,j):
        self.i = i
        self.j =j
    def Add(self):

        print("the addition is ",self.i+self.j)
    def sub(self):

  

        print("the substraction is ",self.i - self.j)
    def mul(self):
        print("the multiplication ",self.i*self.j)
    def div(self):
        print("the divison is ", self.i /self.j)

obj1 = arithmatic(0,0)
obj1.accept(10,20)
obj1.Add()
obj1.sub()
obj1.mul()
obj1.div()



