from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

class UserLogoutView(APIView):
    
    def post(self, request, format=None):
        # Perform user logout
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)