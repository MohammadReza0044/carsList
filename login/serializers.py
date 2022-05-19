from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import personalInfo , user


class personSerialiser(serializers.ModelSerializer):
    class Meta:
        model = personalInfo
        fields = ['id', 'name', 'family', 'phone_number', 'city', 'email']


class userSerialiser(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username', 'password']