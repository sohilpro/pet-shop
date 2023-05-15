from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import viewsets
from .models import CategoryModel
from .serializers import CategorySerializer


class ProductsView(APIView) : 
    serializer_class = serializers.ProcudtsSerializers
    def get(self , request): 
        products = models.ProductsModel.objects.all()
        ser_data = serializers.ProcudtsSerializers(instance=products , many = True)
        return Response(ser_data.data)


class ProductView(APIView) :
    def get(self, request  , slug ) : 
        print(slug)
        product = models.ProductsModel.objects.filter(slug = slug).first()
        if product : 
            ser_data = serializers.ProcudtsSerializers(instance=product ,many = False)
            return Response(ser_data.data)
        return Response({'status' : 'not found'})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
