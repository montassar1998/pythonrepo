import imp
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
# used in method 2
from .forms import contactform2
# used in method 3
from django.forms import ModelForm
# Create your views here.


def method1(request):
    if request.method == "POST":
        f = request.POST["firstname"]
        l = request.POST["lastname"]
        e = request.POST["email"]
        m = request.POST["email"]
        contact = Contact.objects.create(
            firstname=f, lastname=l, Email=e, msg=m)
        # line 13 replaces both line 15,16
        #contact = Contact(firstname= f, lastname= l, Email= e, msg= m)
        # contact.save()
        return HttpResponse("<h1>Data has been inserted successfully </h1>")
    return render(request, "m1/myform1.html")


def method2(request):

    if request.method == 'POST':
        form = contactform2(request.POST)

        if form.is_valid():
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['Email']
            m = form.cleaned_data['msg']

            contact = Contact.objects.create(
                firstname=f, lastname=l, Email=e, msg=m)

            return HttpResponse("<h1>Data has been inserted successfully using method 2, classform </h1>")
    else:
        form = contactform2()
    return render(request, "m1/myform2.html", {'mycontactform2': form})


# method 3 : the best
class contactform3(ModelForm):
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'Email', 'msg')


def method3(request):
    if request.method == 'POST':
        form = contactform3(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Data has been submitted using method 3, this method is about a built-in django class that writes and/or loads the form of the corresponding schema </h1>")
    else:
        form = contactform3()
    return render(request, "m1/myform3.html", {"mycontactform3": form})
