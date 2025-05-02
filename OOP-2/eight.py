class Test:
    ''' class created by Narasimha'''
    a=10
    def __init__(self):
        self.b=20
        self.c=30

t1=Test()

print(t1.__dict__)   #{'b': 20, 'c': 30}
print(Test.__dict__)  #{'a':10}