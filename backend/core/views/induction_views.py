# ./core/views/Induction_views.py
# This file interacts with the Induction model using the rest framework

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Induction, DatabaseUser, Equipment, Category
from core.serializers import InductionSerializer
from rest_framework.exceptions import NotFound

# List all Inductions
class InductionListView(APIView):
    def get(self, request, format=None):
        inductions = Induction.objects.all()  # Use a different variable name here
        serializer = InductionSerializer(inductions, many=True)
        return Response(serializer.data)

# Create a new Induction
class InductionCreateView(generics.CreateAPIView):
    queryset = Induction.objects.all()
    serializer_class = InductionSerializer

# Delete a Induction
class InductionDeleteView(generics.DestroyAPIView):
    queryset = Induction.objects.all()
    serializer_class = InductionSerializer
    
    def get_object(self):
        userID = self.kwargs.get('userID')
        category_name = self.kwargs.get('category')
        equipmentName = self.kwargs.get('equipmentName')
        try:
            userID = DatabaseUser.objects.get(userID=userID)
            category = Category.objects.get(category=category_name)
            obj = Induction.objects.get(userID=userID, category=category, equipmentName=equipmentName)
            return obj
        except (Category.DoesNotExist, DatabaseUser.DoesNotExist):
            raise NotFound('An induction with the given userID, category, and equipmentName does not exist.')

# Retrieve, update, or destroy a Induction
class InductionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Induction.objects.all()
    serializer_class = InductionSerializer

    def get_object(self):
        userID = self.kwargs.get('userID')
        category_name = self.kwargs.get('category')
        equipmentName = self.kwargs.get('equipmentName')
        try:
            userID = DatabaseUser.objects.get(userID=userID)
            category = Category.objects.get(category=category_name)
            obj = Induction.objects.get(userID=userID, category=category, equipmentName=equipmentName)
            return obj
        except (Category.DoesNotExist, DatabaseUser.DoesNotExist):
            raise NotFound('An induction with the given userID, category, and equipmentName does not exist.')