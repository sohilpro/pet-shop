from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer , UserInformationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken






class UserRegistrationAPIView(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

class UserInfoView(APIView) : 
    permission_classes = [IsAuthenticated ,]
    def get(self , request) : 
        ser_data = UserInformationSerializer(instance=request.user)
        return Response(ser_data.data ,status=status.HTTP_200_OK)



