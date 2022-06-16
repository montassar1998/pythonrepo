from django.contrib import admin
from django.urls import path
from .views import getBookDetails, index

urlpatterns = [
    path("",index,name="index"), 
    path("<int:book_id>",getBookDetails, name="detailsOfBook")
    
]