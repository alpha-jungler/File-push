class Parent:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname, self.lname)

class Child(Parent):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
X=Child("Rikesh", "Magiya")
X.printname()


class Grandparent():

    def showGp(self):
        print("Grandparent")
class parent(Grandparent):
   pass

class child(parent):

    pass
obj=child()
obj.showGp()

class Vehicle:
    def show(self):
        print("this is a vehicle")


class car(Vehicle):
    pass

class bike(Vehicle):
    pass

car().show()
bike().show()


class A():
    def showA(self):
        print("A")

class B():
    def showB(self):
        print("B")


class C(A, B):
    pass

m=C
obj=m()
obj.showA()
obj.showB()


    

