from datetime import date, timedelta
class Ticket:
    travel_cost=100
    def __init__(self,credit):
        self.credit=credit
    def travel(self):
        if self.credit>=Ticket.travel_cost:
            self.credit=self.credit-Ticket.travel_cost
        else:
            print("your credit is not enoough")

class OneWay(Ticket):
    def __init__(self):
      self.credit=Ticket.travel_cost
    def travel(self):
        if self.credit>=Ticket.travel_cost:
            self.credit=self.credit-Ticket.travel_cost
        else:
            print("your ticket already has been used")

class ChargeAble(Ticket):
      travel_cost=90
      def charge(self,charge_amount):
        self.charge_amount=charge_amount
        self.credit+=charge_amount

class ChargeAbleTimeLimit(ChargeAble):
  extention_fee=50
  travel_cost=80
  def __init__(self,credit,time_limit):
    super().__init__(credit)
    time_tuple=tuple(map(int,time_limit.split()))
    self.time_limit=date(time_tuple[0],time_tuple[1],time_tuple[2])
  def travel(self):
    if date.today()>self.time_limit:
      print("you should extend your ticket")
    elif self.credit>=ChargeAbleTimeLimit.travel_cost:
          self.credit=self.credit-ChargeAbleTimeLimit.travel_cost
    else:
          print("your credit is not enough")
#this function is suposed to extend the time limit for number_of_mounth and reduce the credit in exchange
  def extend(self,number_of_mounth):
    self.number_of_mounth=number_of_mounth
    if self.credit>=self.number_of_mounth*ChargeAbleTimeLimit.extention_fee:
      self.credit=self.credit-ChargeAbleTimeLimit.extention_fee*self.number_of_mounth
      self.time_limit=self.time_limit+timedelta(days=self.number_of_mounth*30)
    else:
      print("your credit is not enough for extention you have to charge your acount first")

  

import unittest
class TicketTest(unittest.TestCase):
  def setUp(self):
    self.var_one_way=OneWay
    self.var_chargeable=ChargeAble(10000)
    self.var_chargeable_time_limit=ChargeAbleTimeLimit(10000,"2020 11 11")
  def test_travel(self):
    #test for one way travel
    self.var_one_way.travel()
    self.assertEqual(self.var_one_way.credit,0)
    #one way ticket credit has came to zero after one use
    self.var_one_way.travel()
    self.assertEqual(self.var_one_way.credit,0)
    self.var_one_way.travel()
    self.assertEqual(self.var_one_way.credit,0)
    #one way ticket credit has not changed after one use and it is useless after this
    #test for chargeable
    self.befor_chargeable=self.var_chargeable.credit
    for i in range(5):
      self.var_chargeable.travel()
      self.assertEqual(var_chargeable.credit=self.befor_chargeable-(i+1)*ChargeAble.travel_cost)
    #test for charge able time limit
      self.befor_chargeable_time_limit=self.var_chargeable_time_limit.credit
    for i in range(5):
      self.var_chargeable_time_limit.travel()
      self.assertEqual(var_chargeable_time_limit.credit=self.befor_chargeable_time_limit-(i+1)*ChargeAbleTimeLimit.travel_cost)
    
    def test_charg(self):
      #charge test for chargeable
      self.befor_chargeable=self.var_chargeable.credit
      for i in range(5):
        self.var_chargeable.charge(500)
        self.assertEqual(self.var_chargeable.credit,self.befor_chargeable+(i+1)*500)
      #chage test for chargeable time limit
      self.befor_chargeable_time_limit=self.var_chargeable_time_limit.credit
      for i in range(5):
        self.var_chargeable_time_limit.charge(500)
        self.assertEqual(self.var_chargeable_time_limit.credit,self.befor_chargeable_time_limit+(i+1)*500)
    
    def test_extend(self):
      self.befor_time_limit=self.var_chargeable_time_limit.time_limit
      for i in range(a):
        self.var_chargeable_time_limit.extend(1):
        self.assertEqual(self.var_chargeable_time_limit.time_limit,self.befor_time_limit+(i+1)*timedelta(days=30))
    




a=ChargeAbleTimeLimit(1000,"2020 11 11")
a.extend(4)
a.charge(500)
print(a.time_limit)

# sudo rm -rf venv/
# python3 -m venv testenv
# source testenv /bin/activate
