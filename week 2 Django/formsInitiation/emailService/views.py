# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Djangoforms.settings import EMAIL_HOST_USER
from .forms import ContactForm
def contactView(request):
    print(EMAIL_HOST_USER)
    if request.method == 'GET':
        print("we get")
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = '<h1>'+message+'</h1>'
            try:
                send_mail(subject, message, from_email, ["montassar.riahi@etudiant-isi.utm.tn"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Done')
    return render(request, "emailService/email.html", {'form': form})

def successView(request):
    return HttpResponse( 'Success! Thank you for your message.')