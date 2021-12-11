from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def seller_list(request):

    sellers = Sellers.objects.all()
    serializer = SellerSerializer(sellers, many=True)

    return Response(data=serializer.data, status=200)
