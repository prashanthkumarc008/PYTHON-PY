from InsuffientBalError import InsuffientBalErr

amount=int(input("Enter Amount:"))
acc_Bal = 15000

if acc_Bal < amount:
    #print("Low Balance")
    raise InsuffientBalErr("Low Balance")
else:
    print("Withdrawl and Enjoy")

print("Good Morning")