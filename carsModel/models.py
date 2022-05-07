from pyexpat import model
from django.db import models

class cars(models.Model):
    brand = models.CharField(max_length= 50)
    model = models.CharField(max_length= 50)
    color = models.CharField(max_length= 50)
    seat =  models.CharField(max_length= 50)
    yearOfModel = models.DateField()

    def __str__(self):
        return self.brand 
