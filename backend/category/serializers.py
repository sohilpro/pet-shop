from rest_framework import serializers
from . import models
from products.models import ProductsModel



class CategorySerializers(serializers.ModelSerializer) : 
    products = serializers.SerializerMethodField()
    class Meta  : 
        model = models.CategoryModel
        fields = '__all__'

    def get_products(self , obj) : 
        result = obj.products.all()
        return ProductsSerializers(instance=result , many = True).data


class ProductsSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model  = ProductsModel
        fields = '__all__'