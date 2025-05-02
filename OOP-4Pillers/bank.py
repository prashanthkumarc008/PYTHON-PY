from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass 