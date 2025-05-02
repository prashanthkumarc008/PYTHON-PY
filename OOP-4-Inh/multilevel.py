class GrandParent:
    def m1(self):
        print("GP class m1 method") 
    def m2(self):
        print("GP class m2 method") 

class Parent(GrandParent):
    def m3(self):
        print("Parent class m3 method")  

class Child(Parent):
    def m4(self):
        print("Child class m4 method")  
c1=Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
