from django.db import models

# Create your models here.
class Farmer (models.Model) :
    name = models.CharField(max_length=50)
    siret = models.CharField(max_length=14)
    address = models.CharField(max_length=100)


