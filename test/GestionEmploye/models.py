from django.db import models
from GestionDepartement.models import Departement
# Create your models here.

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=200, blank=True, default='')
    adresse = models.CharField(max_length=200,blank=True, default='')
    attachedTo = models.ForeignKey(Departement , on_delete=models.CASCADE)