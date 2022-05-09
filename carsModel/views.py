from ast import Try
from dataclasses import dataclass
import stat
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions



from .serializers import carSerializer
from .models import car

class carList (APIView):
    def get (self,request):
        cars = car.objects.all()
        serializer = carSerializer (cars, many = True)
        return Response (serializer.data) 
    
    def post(self, request, format=None):
        serializer = carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class car_details (APIView):
    def get (self,request,pk):
        try:
            cars = car.objects.get(pk=pk)
        except:
            car.DoesNotExist
            return Response (status=status.HTTP_404_NOT_FOUND)
        serializer = carSerializer(cars)
        return Response (serializer.data)

