from abc import abstractmethod,ABC
class Bank(ABC):

    @abstractmethod       #decorator
    def cal_bal(self):
        pass

b1 =Bank()
print(id(b1))  
'''
TypeError: Can't instantiate abstract class Bank 
without an implementation for abstract method 'cal_bal'
''' 