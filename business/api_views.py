from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import *

class ActionLogAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = ActionLogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"ActionLog"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            action_log = ActionLog.objects.get(id=id)
            serializer = ActionLogSerializer(action_log)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        action_log = ActionLog.objects.all()
        serializer = ActionLogSerializer(action_log, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    
class CompanyAPIView(APIView):
    #permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data, "message":"Company"}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)