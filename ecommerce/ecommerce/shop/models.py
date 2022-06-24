from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_added']

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category , related_name = 'categorie',on_delete = models.CASCADE )
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
