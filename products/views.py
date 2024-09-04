from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer 
from rest_framework import status


# Create your views here.
@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
