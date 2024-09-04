from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def product_list(request):
    pass