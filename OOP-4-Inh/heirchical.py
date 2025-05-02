class GrandParnet:
    def m1(self):
        print("GP class m1 Method") 

class Parent1(GrandParnet):
    def m2(self):
        print("Parent1 class m2 Method") 

class Parent2(GrandParnet):
    def m3(self):
        print("Parent2 class m3 Method")  

class Child(Parent1,Parent2):
    def m4(self):
        print("Child class m4 Method") 

c1 = Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
