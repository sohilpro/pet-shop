from django.db import models

class CategoryModel(models.Model) : 
    name  = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name