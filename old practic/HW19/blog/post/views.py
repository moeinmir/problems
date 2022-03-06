from django.db.models.fields import SlugField
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import get_object_or_404
# Create your views here.
from django.http.response import Http404
from rest_framework import generics, mixins


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


class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


@api_view(['GET', 'PUT', 'DELETE'])
def category_details_rest(request, id):
    category = Category.objects.get(id=id)
    print(category)
    if request.method == "GET":
        serializer = CategorySerializar(category)
        return Response(data=serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = CategorySerializar(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_category = serializer.save()
        resp_serializer = CategorySerializar(updated_category)
        return Response(resp_serializer.data, status=200)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)


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
