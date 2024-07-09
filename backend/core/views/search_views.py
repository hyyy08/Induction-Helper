#created by Tony
#for performing search for student users and equipments
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from core.models import DatabaseUser, Equipment
from core.serializers import DatabaseUserSerializer, InductionSerializer, EquipmentSerializer

class UserSearchView(APIView):
    def get(self, request):
        query_params = request.query_params
        q_userID = query_params.get('userID')
        q_firstName = query_params.get('firstName')
        q_lastName = query_params.get('lastName')
        
        if q_userID:
            users = DatabaseUser.objects.filter(userID=q_userID)
        elif q_firstName:
            users = DatabaseUser.objects.filter(firstName__icontains=q_firstName)
        elif q_lastName:
            users = DatabaseUser.objects.filter(lastName__icontains=q_lastName)
        else:
            return Response({"error": "No search data provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not users.exists():
            return Response({"message": "No users found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Serializer
        user_data = DatabaseUserSerializer(users, many=True).data
        for user in user_data:
            user_obj = DatabaseUser.objects.get(userID=user['userID'])
            inductions = user_obj.induction_set.all()
            user['inductions'] = InductionSerializer(inductions, many=True).data
            
        return Response(user_data, status=status.HTTP_200_OK)

class EquipmentSearchView(APIView):
    def get(self, request):
        query_params = request.query_params
        q_barcode = query_params.get('barcode')
        q_equipmentName = query_params.get('equipmentName')
        
        query = Q()
        if q_barcode:
            query &= Q(barcode=q_barcode)
        if q_equipmentName:
            query &= Q(equipmentName__icontains=q_equipmentName)
        
        if not query:
            return Response({"error": "No search data provided"}, status=status.HTTP_400_BAD_REQUEST)

        equipments = Equipment.objects.filter(query)
        if not equipments.exists():
            return Response({"message": "No equipment found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
