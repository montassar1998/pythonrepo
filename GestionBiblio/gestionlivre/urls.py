from django.contrib import admin
from django.urls import path
from .views import getBookDetails, index, insertBook , proceedToInsertion

urlpatterns = [
    path("",index,name="index"), 
    path("<int:book_id>/details",getBookDetails, name="detailsOfBook"),
    path('insertBook/', insertBook,name='newBookForm'),
    path("insertBook/proceedToInsertBook/" ,proceedToInsertion ,  name='proceed')
]