class Employeee:
    ''' created By Narasimha '''
    org_name="TCS"   #static variable

    def __init__(self,id,name,sal):
        self.emp_id=id
        self.ename=name 
        self.esal=sal

e1=Employeee(101,'RG',45000.45)
e2=Employeee(102,'SG',55000.55)
e3=Employeee(103,'PG',65000.65)

print(Employeee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)