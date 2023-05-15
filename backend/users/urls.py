from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

app_name = 'user'
urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user-registration'),
    path('logout/', TokenBlacklistView.as_view(), name='user_logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('information/' , views.UserInfoView.as_view() , name='user_info_view') ,
]