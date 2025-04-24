from random import randint,choices
lottery_num=[]
for x in range(10):
    lottery_num.append(randint(100,999))
print(lottery_num)
print(choices(lottery_num))