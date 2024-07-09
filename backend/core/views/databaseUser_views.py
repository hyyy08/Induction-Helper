# ./core/views/databaseUser_views.py
# This file interacts with the DatabaseUser model using the rest framework

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from core.serializers import DatabaseUserSerializer
from core.models import DatabaseUser

## List all users in database
class UserListView(APIView):
    def get(self, request, format=None):
        users = DatabaseUser.objects.all()
        serializer = DatabaseUserSerializer(users, many=True)
        return Response(serializer.data)

## Create new user
class UserCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DatabaseUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(DatabaseUserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = DatabaseUser.objects.all()
    serializer_class = DatabaseUserSerializer
    lookup_field = 'userID' 
    
class UserRetrieveUpdateDestroy(APIView):
    def put(self, request, userID, *args, **kwargs):
        try:
            user = DatabaseUser.objects.get(userID=userID)
        except DatabaseUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DatabaseUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Log the errors to understand why the request is failing
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)