from InsuffientBalError import InsuffientBalErr as LowBalError

acc_Bal=15000
try:
    amount = int(input("Enter Amount"))
    if acc_Bal<amount:
        raise LowBalError("Buddy - Low Bal! Please Check!")
    else:
        print("Please Withdrawl and Enjoy!")

except LowBalError as err:
    print(err)
except:
    print("Check the code! Default Errors")


print("Good Moring")
