from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Product, Comment
from django.core import serializers
from rest_framework.response import Response
from .serializers import ProductSerializer, CommentSerializer 
from rest_framework import status


# Create your views here.
@api_view(["GET","POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
@api_view(["GET","PUT","DELETE"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer= ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        product.delete()
        data={"delete":f"Product({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    

@api_view(["GET","POST"])
def comment_list(request, pk):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        comments = product.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method =="POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)
    
@api_view(["DELETE","PUT"])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method=="DELETE":
        comment.delete()
        data={"delete":f"Comment({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)   

    elif request.method=="PUT":
        serializer=CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)