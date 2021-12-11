from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sellers
        fields = '__all__'


class BuyyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyers
        fields = '__all__'


class CategoryDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TagDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ListOfComDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListOfCom
        fields = '__all__'


class BuyyerFactorDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuyyerFactor
        fields = '__all__'


class SellerFactorDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerFactor
        fields = '__all__'


class BuyyerEmailDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuyyerEmail
        fields = '__all__'


class SellerEmailDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerEmail
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ListOfIntDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListOfInt
        fields = '__all__'
