# Parent class 1
class Parent1:
    def person_info(self, name, age):
        print('Inside Parent1 class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Parent2:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Child(Parent1, Parent2):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Child()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')