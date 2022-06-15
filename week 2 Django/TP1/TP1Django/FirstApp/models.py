from django.db import models

# Create your models here.
#manytoone author and book 
#manytomany book and category
#onetoone 


class Article(models.Model):
    nom = models.CharField(max_length=100)
    ref   = models.CharField(max_length=100)
    qte = models.IntegerField(default=0)
    abc = models.CharField(max_length=3,default=0)

