from abc import ABC
class Bank(ABC):

    def cal_bal(self):
        print("cal_bal method")

b1 = Bank()
print(id(b1)) #2082363914288
