from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers


class CategoryView(APIView)  : 
    def get(self ,request)  : 
        category = models.CategoryModel.objects.all()
        ser_data = serializers.CategorySerializers(instance=category , many =True)
        return Response(ser_data.data)
# Create your views here.
