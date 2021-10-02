from acount import Acount
#in this part we open accont for five person with a defined amount of money
Acount(1,1000)
Acount(2,1500)
Acount(3,2000)
Acount(4,20)
Acount(5,500)
#now we transfer 500 from one to two and see the amount af money that each of them have
Acount.transfer(1,2,500)
print(Acount.list_of_client[1].acn_bln)
print(Acount.list_of_client[2].acn_bln)
#now we want to withdrawal 15 from four but we cant because of the limmit
Acount.withdrawal(4,15)
#but we can take 5
Acount.withdrawal(4,5)
print(Acount.list_of_client[4].acn_bln)
#now we deposit 5000 to four and see the emount of money he has
Acount.diposit(4,5000)
print(Acount.list_of_client[4].acn_bln)
