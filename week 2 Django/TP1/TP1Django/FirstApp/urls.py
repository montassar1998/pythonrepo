from django.contrib import admin
from .views import allArticles, article1, article2, article3, fctArticle, index
from django.urls import path

urlpatterns = [
    path("", index, name='index'),
    path("<int:article_id>/", fctArticle, name="htmlArticle"),
    path("A1", article1, name='article1'),
    path("A2", article2, name='article2'),
    path("A1", article3, name='article3'),
    path("all", allArticles,name="allArticles")



]
