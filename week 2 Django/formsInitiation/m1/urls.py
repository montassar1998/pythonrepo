"""Djangoforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import deleteCand, method1, method2, method3, listAllContacts, SearchByName, updateCandByName

urlpatterns = [
    path("m1/", method1),
    path("m2/", method2),
    path("m3/", method3, name = "home"), 
    path("listAlle/", listAllContacts, name="listAll"),
    path("listByCondition",SearchByName, name="searchByName"),
    path('m3/delete/', deleteCand, name="deleteCand"),
    path('m3/<str:oldName>', updateCandByName, name="update"),

]
