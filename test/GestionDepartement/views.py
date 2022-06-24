from dataclasses import field
from itertools import count
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from GestionEmploye.models import Employe
from .models import Departement
from .forms import DepForm




class DepView(ListView):
    model = Departement
    context_object_name = 'departments'
    template_name = "GestionDepartement/DepView.html"


class DepCreate(CreateView):
    model = Departement
    template_name = "GestionDepartement/Depcreate.html"
    success_url = reverse_lazy('GestionDepartement:listhtml')
    form_class = DepForm


class DepUpdateView(UpdateView):
    model = Departement
    fields = ['nom', 'etage']
    pk_url_kwarg = 'pk'
    template_name = "GestionDepartement/DepUpdate.html"
    success_url = reverse_lazy('GestionDepartement:listhtml')
    context_object_name = 'departments'


class DepDeleteView(DeleteView):
    model = Departement
    pk_url_kwarg = 'pk'
    template_name = "GestionDepartement/Depdelete.html"
    success_url = reverse_lazy('GestionDepartement:listhtml')
    context_object_name = 'departments'
