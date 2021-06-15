from django.db import models


# here we create all the django classes
# Create your models here.
class Farmer(models.Model):
    name_farmer = models.CharField(max_length=50)
    siret = models.CharField(max_length=14)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name_farmer


class Product(models.Model):
    name_product = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)
    international_codification = models.CharField(max_length=50)
    farmers = models.ManyToManyField(Farmer)

    def __str__(self):
        return self.name_product


class Certificate(models.Model):
    name_certificate = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_certificate
