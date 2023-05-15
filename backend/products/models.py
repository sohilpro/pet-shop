from django.db import models
from category.models import CategoryModel
# Create your models here.

class ProductsModel(models.Model) : 
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE , related_name='products' , null=True , blank=True)
    name = models.CharField(max_length=150)
    slug =models.SlugField(null=False, blank=True, max_length=200, unique=True, allow_unicode=True, verbose_name='slug-field')
    desc = models.TextField()
    src = models.ImageField(upload_to='product_images/' , null=True ,blank=True)
    alt = models.CharField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField()
    favorite_id = models.IntegerField(unique=True)


    def __str__(self) -> str:
        return f'{str(self.id)} - {self.name} - {self.desc[:30]}'
    
    class Meta  : 
        ordering = ('id' ,)

