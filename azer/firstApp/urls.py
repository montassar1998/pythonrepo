from django.contrib import admin
from django.urls import URLPattern, path
from .views import index
urlpatterns=[
    path('',index)
]