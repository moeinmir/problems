from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
import ast

from django.db.models.fields.related import ManyToManyField
from django.utils.translation import to_language

# Create your models here.


class Sellers(models.Model):
    name = models.CharField(max_length=72)
    national_code = models.CharField(max_length=72)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Buyers(models.Model):
    name = models.CharField(max_length=72)
    national_code = models.CharField(max_length=72)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=72)
    discription = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=72)





class Exist(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='existing')


class NotExist(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='notexisting')


class ListOfCom(models.Model):
    stock_status = (('existing', "existing"), ('notexisting', "notexisting"))
    name = models.CharField(max_length=72)
    price = models.PositiveIntegerField()
    remaining = models.PositiveIntegerField()
    Seller = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.TextField()
    puttosell_date = models.DateTimeField(auto_now_add=True)
    Tag = models.ManyToManyField(Tag)
    status = models.CharField(max_length=20,
                              choices=stock_status,
                              default='existing')
    ex_and_no = models.Manager()
    existing_com = Exist()
    notexisting_com = NotExist()

    def __str__(self):
        return self.name


existing_com = Exist()

status_choices = (('PAY', "payed"), ('NOT', "notpayed"))


class BuyyerFactor(models.Model):
    factor_number = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    factor_pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.factor_number)+" "+str(self.cost))


class SellerFactor(models.Model):
    factor_number = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    factor_pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.factor_number)+" "+str(self.cost))


class BuyyerEmail(models.Model):
    email_text = models.TextField()
    Buyers = models.ForeignKey(Buyers, on_delete=models.PROTECT)
    BuyyerFactor = models.ForeignKey(BuyyerFactor, on_delete=models.PROTECT)


class SellerEmail(models.Model):
    email_text = models.TextField()
    Sellers = models.ForeignKey(Sellers, on_delete=models.PROTECT)
    SellerFactor = models.ForeignKey(SellerFactor, on_delete=models.PROTECT)


class Order(models.Model):
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    comodity = models.ForeignKey(ListOfCom, on_delete=models.PROTECT)
    BuyyerFactor = models.ForeignKey(
        BuyyerFactor, null=True, blank=True, on_delete=models.PROTECT)
    SellerFactor = models.ForeignKey(
        SellerFactor, null=True, blank=True, on_delete=models.PROTECT)
    number = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9,
                              choices=status_choices,
                              default='NOT')

    def __str__(self):
        return str(self.cost)


class ListOfInt(models.Model):
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    comodity = models.ForeignKey(ListOfCom, on_delete=models.CASCADE)
    puttointrest_date = models.DateTimeField(auto_now_add=True)
