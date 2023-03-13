from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class EmployeeView(APIView):
    def get(self, request):
        data = [12, 2, 3]
        content = {'data': data, 'message': "Data get successfully"}
        return Response(data=content, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.query_params)
        content = {'data': [], 'message': "Data get successfully"}
        return Response(data=content, status=status.HTTP_200_OK)