import imp
from django import http
from django import forms
from django.db.models import Q

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

    def clean_firstname(self):
        submittedFName = self.cleaned_data['firstname']
        if(submittedFName == ""):
            raise forms.ValidationError('This field cannot be left empty')
        for i in Contact.objects.all():
            if (i.firstname == submittedFName):
                raise forms.ValidationError(
                    "Firstname already exists in the database")
        return submittedFName

    def clean_lastname(self):
        submittedLName = self.cleaned_data['lastname']
        if(submittedLName == ""):
            raise forms.ValidationError('This field cannot be left empty')
        for i in Contact.objects.all():
            if (i.lastname == submittedLName):
                raise forms.ValidationError(
                    "Lastname already exists in the database")
        return submittedLName


def method3(request):
    if request.method == 'POST':
        form = contactform3(request.POST)
        if form.is_valid():
            submittedFName = form.cleaned_data['firstname']
            submittedLName = form.cleaned_data['lastname']
            submittedEmail = form.cleaned_data['Email']
            submittedMsg = form.cleaned_data['msg']
            # get must return only one
            userInput = Contact(submittedFName,
                                submittedLName,
                                submittedEmail,
                                submittedMsg)
            ''' Contact.objects.create(
                firstname=submittedFName, lastname=submittedLName, Email=submittedEmail,
                msg=submittedMsg) '''
            verif = Contact.objects.filter(firstname=submittedFName)

            form.save()
            # return HttpResponse("<h1>Data already exists !</h1")
            return HttpResponse("<h1> Data has been submitted using method 3, this method is about a built-in django class that writes and/or loads the form of the corresponding schema </h1>")
    else:
        form = contactform3()
    return render(request, "m1/myform3.html", {"mycontactform3": form})


def listAllContacts(request):
    print("list all contact")
    res = Contact.objects.all()
    return render(request, "m1/listAll.html", {"result": res})


def SearchByName(request):
    print("search by name")
    criteria = request.POST["searchFor"]
    print(criteria)
    # works on only one field , alternative is Q
    # result = Contact.objects.filter(
    #     firstname__contains=criteria,
    #     lastname__contains=criteria,
    #     Email__contains=criteria,
    #     msg__contains=criteria)
    lookups = Q(firstname__icontains=criteria) | Q(
        lastname__icontains=criteria) | Q(msg__icontains=criteria) | Q(Email__icontains=criteria)

    results = Contact.objects.filter(lookups)
    # .distinct()
    context = {'specificFields': results}
    print(context['specificFields'])
    return render(request, "m1/selectedFields.html", context)


def updateCandByName(request, oldName):
    if(request.method == "POST"):
        oldName = request.POST["toBeUpdatedCandidateName"]
        fn = request.POST["newFirstName"] if request.POST["newFirstName"] is not "" else "invalide"
        ln = request.POST["newLastName"] if request.POST["newLastName"] is not "" else "invalide"
        msg = request.POST["NewMsg"] if request.POST["NewMsg"] is not "" else "invalide"
        email = request.POST["newEmail"] if request.POST["newEmail"] is not "" else "invalide"
        print("fn=", type(fn))
        Contact.objects.filter(firstname=oldName).update(
            firstname=fn, lastname=ln, Email=email, msg=msg)
    else:
        oldName = "POST only, please consult the form"
    return HttpResponse("Updated")


def deleteCand(request):
    name = request.POST["toBeDeletedCandidateName"]
    #lookups = Q(firstname__icontains=name)
    results = Contact.objects.filter(firstname=name).delete()
    return HttpResponse("hello, contact deleted ")
