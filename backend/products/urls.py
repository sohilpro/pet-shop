from django.urls import path , re_path
from . import views
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet



router = DefaultRouter()
router.register(r'last-three-products', CategoryViewSet)



app_name = 'products'
urlpatterns = [
    path('' , views.ProductsView.as_view() , name='products') , 
    path('', include(router.urls)),
    re_path( r'(?P<slug>[-\w]+)/' , views.ProductView.as_view() , name='product') , 
]