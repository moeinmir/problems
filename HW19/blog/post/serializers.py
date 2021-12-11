from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['post_title']


class CategorySerializar(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
