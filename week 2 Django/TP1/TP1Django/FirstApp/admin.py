from django.contrib import admin

# Register your models here.
from .models import Article
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    #list_display = ("id","nom","qte","ref")
    list_display = [field.name for field in Article._meta.get_fields()]
    list_editable=("nom",)

