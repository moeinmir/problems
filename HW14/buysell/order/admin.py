from django.contrib import admin
from .models import ListOfCom
from .models import Sellers
from .models import Category
from .models import Order
from .models import Buyers
from .models import ListOfInt

# Register your models here.

admin.site.register(ListOfCom)
admin.site.register(Sellers)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Buyers)
admin.site.register(ListOfInt)
