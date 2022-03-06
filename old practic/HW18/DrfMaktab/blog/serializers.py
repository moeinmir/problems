from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import *

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    creator = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'tag', 'creator']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'tag']


class PostDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    tags = TagSerializer(many=True)
    tag = TagSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'creator', 'tags', 'tag']


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'tag']




class CategorySerializar(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostDetailsSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    tags = TagSerializer(many=True)
    tag = TagSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'creator', 'tags', 'tag']

    # class Meta:
    #     model = Post
    #     fields = '__all__'


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
