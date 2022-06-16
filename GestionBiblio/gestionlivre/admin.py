from django.contrib import admin

# Register your models here.
from .models import  Author, Book

myModels = [Author,Book]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('firstname',)
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in myModels[1]._meta.get_fields()]
    list_display = ("title","price")
    list_editable = ("title",)
    list_display_links= ('price',)
    search_fields = ("title",)
    list_filter = ("category",)
    list_per_page = 10 #diplay only 10 instances per page


# admin.site.register(Author)
# admin.site.register(Book)

