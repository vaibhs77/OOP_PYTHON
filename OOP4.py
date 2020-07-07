class Bookstore:
    value = 0

    def __init__ (self, name, author):
        self.name = name
        self.author = author

    def displa (self):
        Bookstore.value += 1
        print ( "The name of book is", self.name, "the name pf author is",self.author,".no of book",
                Bookstore.value )


obj1 = Bookstore ( "abc", "ygc" )
obj1.displa ()
obj2 = Bookstore ( "uuu", "iii" )
obj2.displa ()
