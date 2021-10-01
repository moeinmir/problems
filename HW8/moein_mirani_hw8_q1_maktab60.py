import datetime
class Acount:


  list_of_client={}
  min_acn_bln=10
  
  def __init__(self,acn_num,acn_bln):
    self.acn_num=acn_num
    self.acn_bln=acn_bln
    Acount.list_of_client.update({self.acn_num:self})
    self.list_of_trans=[]
  @classmethod
  def diposit(cls,acn_num1,dip_amn):
    cls.acn_num1=acn_num1
    self=Acount.list_of_client[cls.acn_num1]
    self.dip_amn=dip_amn
    Acount.list_of_client[cls.acn_num1].acn_bln=Acount.list_of_client[cls.acn_num1].acn_bln+self.dip_amn
    self.list_of_trans.append({datetime.datetime.now().isoformat():f"type of trans: deposit, amount of trans: {self.dip_amn}"})
  @classmethod
  def limit(cls,acn_num1,wit_amn):
    cls.acn_num1=acn_num1
    self=Acount.list_of_client[cls.acn_num1]
    self.wit_amn=wit_amn
    if Acount.list_of_client[cls.acn_num1].acn_bln-self.wit_amn>Acount.min_acn_bln:
      print("permitted")
      return True
    else:
      print("not permitted") 
      return False

  @classmethod
  def withdrawal(cls,acn_num1,wit_amn):
    cls.acn_num1=acn_num1
    self=Acount.list_of_client[cls.acn_num1]
    self.wit_amn=wit_amn
    if cls.limit(cls.acn_num1,self.wit_amn):
      Acount.list_of_client[cls.acn_num1].acn_bln=Acount.list_of_client[cls.acn_num1].acn_bln-self.wit_amn
      self.list_of_trans.append({datetime.datetime.now().isoformat():f"type of trans: withdrawal, amount of trans: {self.wit_amn}"})
    else:
      print("your account supply is not enought") 

  @classmethod
  def transfer(cls,acn_num1,acn_num2,tra_amn):
    cls.acn_num1=acn_num1
    self1=Acount.list_of_client[cls.acn_num1]
    cls.acn_num2=acn_num2
    self2=Acount.list_of_client[cls.acn_num2]
    self1.tra_amn=tra_amn
    if cls.limit(acn_num1,tra_amn):
      Acount.list_of_client[cls.acn_num1].acn_bln=Acount.list_of_client[cls.acn_num1].acn_bln-self1.tra_amn
      Acount.list_of_client[cls.acn_num2].acn_bln=Acount.list_of_client[cls.acn_num2].acn_bln+tra_amn
      self1.list_of_trans.append({datetime.datetime.now().isoformat():f"type of trans: transfer, amount of trans:{self1.tra_amn},destination:{cls.acn_num2}"})
      self2.list_of_trans.append({datetime.datetime.now().isoformat():f"type of trans: deposit, amount of trans:{self1.tra_amn},source:{cls.acn_num1}"})
    else:
      print("your account supply is not enought")

  @classmethod
  def trans_report(cls,acn_num1,date_time):
    cls.date_time=date_time
    y = list(map(int, (cls.date_time).split()))
    cls.date_time = datetime.datetime.combine(datetime.date(y[0], y[1], y[2]),datetime.time(y[2], y[4], y[5]))
    period=datetime.timedelta(minutes=2)
    cls.list_of_trans_period=[]
    for i in Acount.list_of_client[cls.acn_num1].list_of_trans:
        for (key,value) in i.items():
            if  cls.date_time-period < datetime.datetime.fromisoformat(key) < cls.date_time+period+period:
                cls.list_of_trans_period.append(i)
    return cls.list_of_trans_period


#example
Acount(1,1000)
Acount(2,2000)
Acount.transfer(1,2,500)
Acount.withdrawal(2,150)
Acount.diposit(1,5000)
Acount.diposit(1,2000)
print(Acount.list_of_client[1].list_of_trans)
print(Acount.list_of_client[2].list_of_trans)
print(Acount.list_of_client[1].trans_report(1,"2020 11 11 11 11 11"))




