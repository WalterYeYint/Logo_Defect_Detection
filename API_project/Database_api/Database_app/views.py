from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Detections
from . serializers import DetectionsSerializer
# Create your views here.

class ViolationsList(APIView):
    def get(self,request, pk=None):
        detections1 = Detections.objects.all()
        serializer = DetectionsSerializer(detections1, many = True)
        return Response(serializer.data)

    def post (self,request):
        serializer = DetectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetClass(APIView):
    def get (self, request, pk):
        detections1 = Detections.objects.get(serial_no=pk)#, many=False)
        serializer = DetectionsSerializer(detections1, many = False)
        return Response(serializer.data)