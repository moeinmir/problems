from django.urls import path
from .views import *
urlpatterns = [
    path('seller_list/', seller_list, name='seller_list')

]
