class Account:
    '''claass created by Narasimha'''
    def __init__(self,id,name,amount):
        self.acc_Id=id;
        self.acc_Name=name;
        self.acc_Amount=amount;
        
    def check_Bal(self):
        print(self.acc_Amount)
        
    def open_account(self):
        print("Account Opened Successfully")
    def deposit_amount(self,amount):
        print("Amount Deposited Successfully")
        print(amount)
        self.acc_Amount=self.acc_Amount+amount;
    @classmethod
    def update_min_bal(cls,amount):
        print("Amount Updated  Successfully") 
    @staticmethod
    def cal_interest():
        print("Utility Method")
a1=Account(100,'rahul',1000);
a2=Account(200,'modi',2000);

print(a1.__dict__)
print(a2.__dict__)

a1.deposit_amount(100);
a2.deposit_amount(200);

print(a1.__dict__)
print(a2.__dict__)



