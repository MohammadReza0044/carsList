from curses import meta
from dataclasses import field
from rest_framework import serializers
from .models import cars

class carSerializer (serializers.ModelSerializer):
    class meta:
        model = cars
        field = ['brand','model','color','yearOfModel']