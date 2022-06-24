from dataclasses import field
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employe, Employe
from .forms import EmpForm


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'


class EmpView(ListView):
    model = Employe
    context_object_name = 'employe'
    template_name = "GestionEmploye/EmpView.html"


class EmpCreate(CreateView):
    model = Employe
    template_name = "GestionEmploye/EmpCreate.html"
    success_url = reverse_lazy('GestionEmploye:listhtml')
    form_class = EmpForm


class EmpUpdateView(UpdateView):
    model = Employe
    fields = '__all__'
    pk_url_kwarg = 'pk'
    template_name = "GestionEmploye/EmpUpdate.html"
    success_url = reverse_lazy('GestionEmploye:listhtml')
    context_object_name = 'employe'


class EmpDeleteView(DeleteView):
    model = Employe
    pk_url_kwarg = 'pk'
    template_name = "GestionEmploye/EmpDelete.html"
    success_url = reverse_lazy('GestionEmploye:listhtml')
    context_object_name = 'employe'
