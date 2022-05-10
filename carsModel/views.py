from django.http import Http404
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
    def get_object(self,pk):
            try:
                cars = car.objects.get(pk=pk)
            except:
                car.DoesNotExist
                raise Http404
            return cars
    
    def get (self,request,pk):
        cars = self.get_object(pk)
        serializer = carSerializer(cars)
        return Response (serializer.data)

    def put (self, request,pk):
        cars = self.get_object(pk)
        serializer = carSerializer(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request,pk):
        cars = self.get_object(pk)
        serializer = carSerializer(cars,data=request.data)
        cars.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)


