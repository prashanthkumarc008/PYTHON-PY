class Parent1:
    def m1(self):
        print("Parent1 class m1 method") 
class Parent2:
    def m2(self):
        print("Parent2 class m2 method")
class child(Parent1,Parent2):
    def m3(self):
        print("Child class m3 method")

c1 = child()
c1.m1()
c1.m2()
c1.m3()