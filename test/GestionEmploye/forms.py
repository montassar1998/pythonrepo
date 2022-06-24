from .models import Departement, Employe
from django import forms


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"
