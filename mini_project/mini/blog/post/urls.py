from django.urls import path
from .views import *
from django.views.generic import TemplateView
from .views import CategoryListView

app_name = 'post'

urlpatterns = [

    path('post_list/', post_list),
    path('post_details/<slug>', post_details),
    path('category/', CategoryListView.as_view(template_name='category_list_view.html')),
    path('category_details_view/<int:category_id>', category_details_view),
]
