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

from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination




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


# 한 페이지션 설정
class ProductPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 30


#클래스형 조회화 생성
class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        paginator = ProductPagination()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
        

    permission_classes([IsAuthenticated])
    def post(self, request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)    



##믹스인
#class ProductCUAPIView(ListCreateAPIView):
#    queryset =Product.objects.all()
#    serializer_class=ProductSerializer 
#    permission_classes=[IsAuthenticated]
# 
#수정만 권한주기 >> 오버라이딩 >> ing


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

# #클래스형 상세조회, 수정, 삭제
# class ProductDetailAPIView(APIView):
#     permission_classes([IsAuthenticated])
    
#     def get_object(self, pk):
#         return get_object_or_404(Product, pk=pk)

#     def get(self, request, pk):
#         product = self.get_object(pk)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = self.get_object(pk)
#         serializer=ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         data={"delete":f"Product({pk}) is deleted."}
#         return Response(data, status=status.HTTP_200_OK)


#믹스인 상품 상세조회 수정 삭제
class ProductRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset =Product.objects.all()
    serializer_class=ProductSerializer 
    permission_classes=[IsAuthenticated]

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
    
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        data={"delete":f"Comment({pk}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer=CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
