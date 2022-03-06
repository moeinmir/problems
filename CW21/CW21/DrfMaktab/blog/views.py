import random

import redis
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from blog.filter import PostListFilter
from blog.models import Post

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import generics, mixins

from blog.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer, \
    OtpRequestSerializer


# @api_view(['GET', 'POST'])
# def post_list_create(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(published=True).all()
#         serializer = PostSerializer(posts, many=True)
#
#         return Response(data=serializer.data, status=200)
#
#     elif request.method == 'POST':
#         serializer = PostCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         post = serializer.save()
#
#         post.creator = request.user
#         post.save()
#
#         resp_serializer = PostSerializer(post)
#         return Response(data=resp_serializer.data, status=201)


# class PostList(APIView):
#
#     def get(self, request):
#         posts = Post.objects.filter(published=True).all()
#         serializer = PostSerializer(posts, many=True)
#
#         return Response(data=serializer.data, status=200)
#
#     def post(self, request):
#         serializer = PostCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         post = serializer.save()
#
#         post.creator = request.user
#         post.save()
#
#         resp_serializer = PostSerializer(post)
#         return Response(data=resp_serializer.data, status=201)


class PostListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.filter(published=True).all()
    permission_classes = (IsAuthenticated,)
    filterset_class = PostListFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        resp_serializer = PostSerializer(post)
        headers = self.get_success_headers(serializer.data)
        return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'user': self.request.user
        }


# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail_update_delete(request, id):
#     # try:
#     #     post = Post.objects.get(id=id)
#     # except Post.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#
#     post = get_object_or_404(Post, id=id)
#
#     if request.method == "GET":
#         serializer = PostDetailSerializer(post)
#         return Response(data=serializer.data, status=200)
#
#     elif request.method == 'PUT':
#         if post.creator != request.user:
#             return Response(data={'msg': 'this post owned by another user'}, status=400)
#
#         serializer = PostUpdateSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_post = serializer.save()
#         resp_serializer = PostDetailSerializer(updated_post)
#         return Response(resp_serializer.data, status=200)
#
#     elif request.method == 'DELETE':
#         if post.creator != request.user:
#             return Response(data={'msg': 'this post owned by another user'}, status=400)
#         post.delete()
#
#         return Response(status=204)

class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        if self.request.method == 'GET':
            Post.objects.all()
        else:
            return Post.objects.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        else:
            return PostUpdateSerializer


class OtpView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = OtpRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']

        otp = random.randint(1000, 9999)

        # send sms to phone

        r = redis.Redis(host='redis_db', port=6379, db=0)
        r.set(f'otp:{phone}', otp)

        return Response({'phone': phone}, status=200)



