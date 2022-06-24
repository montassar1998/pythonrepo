from .models import Departement
from django import forms


class DepForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ('nom','etage')
