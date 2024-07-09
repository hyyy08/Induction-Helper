from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.serializers import InstructorUserSerializer
from core.is_super import IsSuperUser 

class CreateInstructorUserView(APIView):
    permission_classes = [IsAuthenticated, IsSuperUser] #Check if logged in and have super admin permission
    def post(self, request, format=None):
        serializer = InstructorUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Instructor user created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
