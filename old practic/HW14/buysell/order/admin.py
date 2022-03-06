from django.contrib import admin
from .models import ListOfCom
from .models import Sellers
from .models import Category
from .models import Order
from .models import Buyers
from .models import ListOfInt
from .models import BuyyerFactor
from .models import SellerFactor
from .models import BuyyerEmail
from .models import SellerEmail
from .models import Tag

# Register your models here.

admin.site.register(ListOfCom)
admin.site.register(Sellers)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Buyers)
admin.site.register(ListOfInt)
admin.site.register(BuyyerFactor)
admin.site.register(SellerFactor)
admin.site.register(BuyyerEmail)
admin.site.register(SellerEmail)
admin.site.register(Tag)

