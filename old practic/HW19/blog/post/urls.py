from django.urls import path
from .views import *
from django.views.generic import TemplateView


app_name = 'post'

urlpatterns = [

    path('post_list/', post_list),
    path('post_details/<slug>', post_details),
    path('category/', CategoryListView.as_view(template_name='category_list_view.html')),
    path('category_details_view/<int:category_id>', category_details_view),



    path('post_list_rest/', post_list_rest, name='post_list_rest'),
    path('category_list_rest/', category_list_rest, name='category'),
    path('post_details_rest/<int:id>', post_details_rest),
    path('category_details_rest/<int:id>', category_details_rest),
    path('post_details_rest_class/<int:pk>',
         PostDetail.as_view(), name='post_details_rest_class'),


]
