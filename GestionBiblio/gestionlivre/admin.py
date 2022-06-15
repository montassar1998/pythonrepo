from django.contrib import admin

# Register your models here.
from .models import  Author, Book


myModels = [Author,Book]
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstname',)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in myModels[1]._meta.get_fields()]
