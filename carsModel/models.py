from pyexpat import model
from django.db import models


class car (models.Model):
    brand = models.CharField(max_length= 50)
    model = models.CharField(max_length= 50)
    color = models.CharField(max_length= 50)

    def __str__(self):
        return self.brand , self.model
