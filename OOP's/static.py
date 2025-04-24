class Employee:
    org_Name='TCS'
    
    def __init__(self,id,name,sal):
        self.emp_eId=id
        self.emp_ename=name
        self.emp_esal=sal
        
print(Employee.__dict__)
e1=Employee(100,"Rahul",40000)
e2=Employee(101,"ananda",30000)
e3=Employee(102,"dinesha",20000)

print(e1.__dict__)