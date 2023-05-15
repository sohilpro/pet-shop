from rest_framework import serializers
from . import models
from rest_framework import serializers
from .models import CategoryModel, ProductsModel





class ProcudtsSerializers(serializers.ModelSerializer) : 
    category = serializers.SlugRelatedField( slug_field='name' , read_only=True)
    class Meta : 
        model = models.ProductsModel
        fields = '__all__'





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductsModel
        fields = '__all__'





class CategorySerializer(serializers.ModelSerializer):
    latest_products = serializers.SerializerMethodField()
    def get_latest_products(self, obj):
        last_three_products = ProductsModel.objects.filter(category=obj).order_by('-id')[:3]
        serializer = ProductSerializer(instance=last_three_products, many=True)
        return serializer.data
    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'latest_products',)