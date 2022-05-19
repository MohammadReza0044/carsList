from pyexpat import model
from unicodedata import name
from django.db import models

class personalInfo(models.Model):
    name = models.TextField(max_length=50)
    family = models.TextField(max_length=50)
    phone_number = models.IntegerField(max_length=11)
    city = models.TextField(max_length=50, blank=True)
    email = models.EmailField(max_length=300,blank=True)

    def __str__(self):
        return self.name , self.family



class user(models.Model):
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    
    def __str__(self):
        return self.username , self.password