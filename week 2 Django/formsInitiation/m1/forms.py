from django import forms


class contactform2(forms.Form):
    firstname  = forms.CharField(max_length=100)
    lastname= forms.CharField(max_length=100)
    Email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


