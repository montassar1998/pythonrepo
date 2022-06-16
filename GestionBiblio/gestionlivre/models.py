from django.db import models

# Create your models here.
# •title : Le titre du livre. Champ obligatoire.
# •price : Le prix du livre (nombre décimal). Champ facultatif.
# •summary : Le résumé du livre. Champ facultatif.
# •author : L'auteur du livre (relation plusieurs-à-un et suppression en cascade). Champ facultatif.
# •category : La catégorie (avec les choix suivants : , , , , , ). Champ facultatif.
# •stock : La quantité en stock (avec une valeur par défaut de 0). Champ facultatif.


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    wikipedia = models.URLField(max_length=2049)
    def __str__(self) :
        return self.firstname + " " + self.lastname+ " "+self.wikipedia



class Book(models.Model):

    title = models.CharField(max_length=100)
    price = models.IntegerField(default=10, blank=True)
    summary = models.CharField(max_length=10000, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null= True)


    #enum choices or tuple
    class GenreChoice(models.TextChoices):
        Aventure = 'Aventure',
        Thriller = 'Thriller',
        Fantastique = 'Fantastique',
        Romance = 'Romance', 
        Sciencefiction = 'Science-fiction',
    category = models.CharField(
        max_length=17,
        choices=GenreChoice.choices,
        blank=True
    )
    stock = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return "abc"
