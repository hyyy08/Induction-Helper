from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProcessRequest(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "This is not a POST request"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return Response({"message": "This is a POST request"}, status=status.HTTP_200_OK)