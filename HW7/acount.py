class Acount:

  
  list_of_client={}
  min_acn_bln=10
  
  def __init__(self,acn_num,acn_bln):
    self.acn_num=acn_num
    self.acn_bln=acn_bln
    Acount.list_of_client.update({self.acn_num:self})

  @classmethod
  def diposit(cls,acn_num1,dip_amn):
    cls.acn_num1=acn_num1
    self=Acount.list_of_client[cls.acn_num1]
    self.dip_amn=dip_amn
    Acount.list_of_client[cls.acn_num1].acn_bln=Acount.list_of_client[cls.acn_num1].acn_bln+self.dip_amn

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

    



