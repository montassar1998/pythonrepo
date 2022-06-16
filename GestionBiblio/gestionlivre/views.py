from django.shortcuts import render
from .models import Book , Author
# Create your views here.

from django.forms.models import model_to_dict

def index(request):
    result = Book.objects.all()
    context = {"listeLivres": result}
    return render(request, "gestionlivre/index.html", context)


def getBookDetails(request, book_id):
    result = Book.objects.get(pk=book_id)
    
    context = {}
    #return render(request, "gestionlivre/details.html", context)
    object = model_to_dict(result, fields=[field.name for field in Book._meta.fields])
    result1 = Author.objects.filter(id=object["id"]).first()
    return render(request,'gestionlivre/details.html', {"result":object,"Author": result1})
