from dataclasses import dataclass
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status



from .serializers import carSerializer
from .models import car

class carList (APIView):
    def get (self,request):
        cars = car.objects.all()
        serializer = carSerializer (cars, many = True)
        token = 'abcd'
        return JsonResponse (serializer.data, safe=False) 

