# ./core/views/Catalog_views.py
# This file interacts with the Catalog model using the rest framework

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from core.serializers import CatalogSerializer
from core.models import Catalog, Category, Equipment
from rest_framework.exceptions import NotFound

## List all users in database
class CatalogListView(APIView):
    def get(self, request, format=None):
        catalog = Catalog.objects.all()
        serializer = CatalogSerializer(catalog, many=True) 
        return Response(serializer.data)

#create a new non-admin user in database    
class CatalogCreateView(generics.CreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
class CatalogDeleteView(generics.DestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
    def get_object(self):
        category_name = self.kwargs.get('category')
        equipmentName = self.kwargs.get('equipmentName')
        try:
            category = Category.objects.get(category=category_name)
            obj = Catalog.objects.get(category=category, equipmentName=equipmentName)
            return obj
        except (Category.DoesNotExist, Catalog.DoesNotExist):
            raise NotFound('A catalog item with the given category and equipmentName does not exist.')
    
class CatalogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
    def get_object(self):
        category_name = self.kwargs.get('category')
        equipmentName = self.kwargs.get('equipmentName')
        try:
            category = Category.objects.get(category=category_name)
            obj = Catalog.objects.get(category=category, equipmentName=equipmentName)
            return obj
        except (Category.DoesNotExist, Catalog.DoesNotExist):
            raise NotFound('A catalog item with the given category and equipmentName does not exist.')
    
