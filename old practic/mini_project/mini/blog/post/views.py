from django.db.models.fields import SlugField
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import *

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def post_details(request, slug):

    post = Post.objects.get(slug=slug)
    # comment = Comment.objects.filter(related_post=post_id)
    return render(request, 'post_details.html', {'post': post})
    # return render(request, 'post_details.html', {'post': post, 'comment': comment})


def category_details_view(request, category_id):
    post = Post.objects.filter(post_category=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'category_details_view.html', {'post': post, 'category': category})


class CategoryListView(ListView):
    model = Category
