from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    msg = models.CharField(max_length=1000)
    Email = models.EmailField(max_length=100)