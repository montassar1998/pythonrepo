from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    result = Book.objects.all()
    context = {"listeLivres":result}
    return render(request,"gestionlivre/index.html",context)