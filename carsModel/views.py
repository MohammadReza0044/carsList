from ast import Try
from dataclasses import dataclass
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .serializers import carSerializer
from .models import car

class carList (APIView):
    def get (self,request):
        cars = car.objects.all()
        serializer = carSerializer (cars, many = True)
        return Response (serializer.data) 


class car_details (APIView):
    def get (self,request,pk):
        try:
            cars = car.objects.get(pk=pk)
        except:
            car.DoesNotExist
            return Response (status=status.HTTP_404_NOT_FOUND)
        serializer = carSerializer(cars)
        return Response (serializer.data)

