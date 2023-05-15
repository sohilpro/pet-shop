from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomeView(APIView):
	def get(self, request):
		return Response({'message' : 'Home Page'}, status=status.HTTP_200_OK)

