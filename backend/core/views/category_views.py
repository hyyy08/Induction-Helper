# ./core/views/Category_views.py
# This file interacts with the Category model using the rest framework

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from core.serializers import CategorySerializer
from core.models import Category

## List all users in database
class CategoryListView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True) 
        return Response(serializer.data)

#create a new non-admin user in database    
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category' 
    
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category'
