from django.db import models

# Create your models here.


class InStockManager(models.Manager):
    def get_queryset(self):
        return super(InStockManager, self).get_queryset().filter(status='+')


class OutofStockManager(models.Manager):
    def get_queryset(self):
        return super(OutofStockManager, self).get_queryset().filter(status='-')


class Product(models.Model):
    STATUS_CHOICES = [
        ('+', 'in stock'),
        ('-', 'out of stock'),
        ('o', 'unknown')
    ]
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='o'
    )
    objects = models.Manager()  # Default django manager
    in_stock = InStockManager()  # Manager to return in stock products
    # Manager to return out of stock products
    out_of_stock = OutofStockManager()
