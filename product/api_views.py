from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer, ProductSerializer, ProductTypeSerializer, ItemLogSerializer
from .models import Category, ItemLog, Product, ProductType

class CategoryAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"Category"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



class ProductTypeAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = ProductTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"ProductType"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            product_type = ProductType.objects.get(gtin_number=id)
            serializer = ProductTypeSerializer(product_type)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        product_type = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_type, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"Product"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        product = Product.objects.all()
        if(not product):
            return Response({"status": "success"}, status=status.HTTP_200_OK)

        serializer = ProductSerializer(product, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class ItemLogAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = ItemLogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"ItemLog"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item_log = ItemLog.objects.get(id=id)
            serializer = ItemLogSerializer(item_log)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        item_log = ItemLog.objects.all()
        serializer = ItemLogSerializer(item_log, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

