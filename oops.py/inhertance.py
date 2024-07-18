class A:
    def dispalyA(self):
        print ("WELCOME TO MY A WORLD ")

class B:
    def dispalyB(self):
        print ("WELCOME TO MY B WORLD ")        

class C(A,B):
    def dispalyC(self):
        print ("WELCOME TO MY C WORLD ") 

obj=C()
obj.dispalyA()
obj.dispalyB()
obj.displayC()

