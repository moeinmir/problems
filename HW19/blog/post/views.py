from django.db.models.fields import SlugField
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.


@api_view(['GET'])
def post_list_rest(request):

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_list_rest(request):

    category = Category.objects.all()
    serializer = CategorySerializar(category, many=True)

    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def post_details_rest(request, id):

    post = Post.objects.get(id=id)
    serializer = PostDetailsSerializer(post)

    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_details_rest(request, id):

    category = Category.objects.get(id=id)
    serializer = CategoryDetailsSerializer(category)
    return Response(data=serializer.data, status=200)


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
