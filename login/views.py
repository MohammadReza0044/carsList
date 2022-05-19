import imp
from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import personSerialiser
from .models import personalInfo

class personView(APIView):
    def post(self,request):
        serialiser = personSerialiser (data= request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response (serialiser.data)
        return Response (serialiser.errors, status= status.HTTP_400_BAD_REQUEST)

    
    def get (self,request):
        persons = personalInfo.objects.all()
        serialiser = personSerialiser(persons, many=True)
        return Response (serialiser.data)


class person_detailView (APIView):
    def get_object (self ,pk):
        try:
            persons = personalInfo.objects.get(pk = pk)
        except:
                personalInfo.DoesNotExist
                raise Http404
        return persons
   

    def get (self, request, pk):
        persons = self.get_object(pk)
        serialiser = personSerialiser(persons)
        return Response (serialiser.data)

    
    def put (self, request , pk):
        persons = self.get_object(pk)
        serialiser = personSerialiser(persons, data= request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response (serialiser.data, status= status.HTTP_202_ACCEPTED)
        return Response (serialiser.errors, status= status.HTTP_406_NOT_ACCEPTABLE)