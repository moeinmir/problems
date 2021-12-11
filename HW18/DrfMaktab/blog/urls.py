

from django.urls import path
from blog.views import *

urlpatterns = [
    path('post/', post_list_create, name='post_list'),
    path('post/<int:id>/', post_detail_update_delete, name='post_detail'),
    path('post_list_rest/', post_list_rest, name='post_list_rest'),
    path('category_list_rest/', category_list_rest, name='category'),
    path('post_details_rest/<int:id>', post_details_rest),
    path('category_details_rest/<int:id>', category_details_rest)




]
