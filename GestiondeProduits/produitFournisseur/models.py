from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=36)
    design = models.CharField(max_length=36)
    state = models.CharField(max_length=36)

    def __str__(self):
        return "Supplier "+self.name


class Product(models.Model):
    name = models.CharField(max_length=36)
    design = models.CharField(max_length=36)
    state = models.CharField(max_length=36)
    image = models.ImageField(upload_to="")
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "Produit "+self.name + " "+ str(self.price)
