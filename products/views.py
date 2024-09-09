from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes #해당 뷰에 대한 권한 검사를 수행. 인증된 사용자만 접근.
from .models import Product, Comment
from django.core import serializers
from rest_framework.response import Response
from .serializers import ProductSerializer, CommentSerializer 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# 함수형
# @api_view(["GET"])
# def product_list(request):
#     if request.method == "GET":
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

# @api_view(["POST"])
# @permission_classes([IsAuthenticated]) #권한 데코레이터
# def product_create(request):
#     if request.method == "POST":
#         serializer= ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
#         print(serializer.errors)
#         return Response(serializer.errors, status=400)

#클래스형 조회화 생성
class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    permission_classes([IsAuthenticated])
    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)    


#함수형 상세조회, 수정, 삭제
# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticated]) #권한 데코레이터
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer= ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
#     elif request.method == "DELETE":
#         product.delete()
#         data={"delete":f"Product({pk}) is deleted."}
#         return Response(data, status=status.HTTP_200_OK)

#클래스형 상세조회, 수정, 삭제
class ProductDetailAPIView(APIView):
    permission_classes([IsAuthenticated])

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer=ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        data={"delete":f"Product({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)

#함수형 댓글 조회 생성
#@api_view(["GET","POST"])
#def comment_list(request, pk):
#    if request.method == "GET":
#        product = get_object_or_404(Product, pk=pk)
#        comments = product.comments.all()
#        serializer = CommentSerializer(comments, many=True)
#        return Response(serializer.data)
#    
#    elif request.method =="POST":
#        serializer = CommentSerializer(data=request.data)
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            return Response(serializer.data)
#        print(serializer.errors)
#        return Response(serializer.errors)


#클래스형  코멘트 조회, 생성  
class CommentListAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    permission_classes([IsAuthenticated])
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


#함수형 코멘트 삭제, 수정
#@api_view(["DELETE","PUT"])
#@permission_classes([IsAuthenticated])
#def comment_detail(request, pk):
#    
#    comment = get_object_or_404(Comment, pk=pk)
#    
#    if request.method=="DELETE":
#        comment.delete()
#        data={"delete":f"Comment({pk}) is deleted."}
#        return Response(data, status=status.HTTP_200_OK)   
#
#    elif request.method=="PUT":
#        serializer=CommentSerializer(comment, data=request.data, partial=True)
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            return Response(serializer.data)


#클래스형 삭제 수정
class CommentDetailAPIView(APIView):
    permission_classes([IsAuthenticated])

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        data={"delete":f"Comment({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
