print ( "This program is related to banking approch" )


class BankAccount:
    ROI = 7.5




    def __init__ (self, Name, Amount, tt,x):
        self.tt = tt
        self.Name = Name
        self.amount = Amount
        self.x = x

    def deposite (self, Amount, lock):
        lock.acquire ()
        self.amount = self.amount + Amount
        lock.release ()
        print ( "The deposited ammount is", self.amount )

    def withdraw (self, Amount,lock,x):
        if self.x == "True":
            lock.acquire ()
            self.amount = self.amount - Amount
            lock.release ()
            print ( "the money after deduction is", self.amount )
        else:
              return(self.deposite())
    def Intrest (self):
                   self.It = (self.amount) * (BankAccount.ROI / 100) * (self.tt / 12)
                   print ( "the intrest over ", self.tt, "is", self.It )




import threading

lock = threading.Lock ()
obj1 = BankAccount ( "Rahul", 5000, 6, x )
obj1.deposite ( 5000, lock )
obj1.(x = str(input("want to widhraw",))
obj1.withdraw ( 200, lock ,x)
obj1.Intrest ()
