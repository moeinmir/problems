from django.db import models


# Create your models here.

class Sellers(models.Model):
    name = models.CharField(max_length=72)
    national_code = models.CharField(max_length=72)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Buyers(models.Model):
    name = models.CharField(max_length=72)
    national_code = models.CharField(max_length=72)
    email=models.EmailField()
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=72)
    discription = models.TextField()
    def __str__(self):
        return self.name


class ListOfCom(models.Model):
    name = models.CharField(max_length=72)
    price = models.PositiveIntegerField()
    remaining = models.PositiveIntegerField()
    Seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    Category= models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.TextField()
    puttosell_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

status_choices = (('PAY', "payed"),('NOT', "notpayed"))






class Order(models.Model):
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    comodity = models.ForeignKey(ListOfCom, on_delete=models.PROTECT)
    number = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=9,
                  choices=status_choices,
                  default='NOT')

    def __str__(self):
        return str(self.cost)



class ListOfInt(models.Model):
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    comodity = models.ForeignKey(ListOfCom, on_delete=models.CASCADE)
    puttointrest_date = models.DateTimeField(auto_now_add=True)


