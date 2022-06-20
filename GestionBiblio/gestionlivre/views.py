from unittest import loader
from django.shortcuts import render
from .models import Book, Author
# Create your views here.

from django.forms.models import model_to_dict


def index(request):
    result = Book.objects.all()
    context = {"listeLivres": result}
    return render(request, "gestionlivre/index.html", context)


def getBookDetails(request, book_id):
    result = Book.objects.get(pk=book_id)

    # return render(request, "gestionlivre/details.html", context)
    object = model_to_dict(
        result, fields=[field.name for field in Book._meta.fields])
    result1 = Author.objects.filter(id=object["id"]).first()
    return render(request, 'gestionlivre/details.html', {"result": object, "Author": result1})


def insertBook(request):
    AuthorsList = Author.objects.all()
    context = {'AuthorsList':AuthorsList}
    return render(request, 'gestionlivre/newBook.html',context)


def proceedToInsertion(request):
    #modelForm is easier !!! 
    result = dict()
    result['title'] = request.GET["title"]
    result['price'] = request.GET["price"]
    result['summary'] = request.GET["summary"]
    result['category'] = request.GET["category"]
    result['stock'] = request.GET["stock"]
    result['author'] = request.GET["author"]
    toBeInserted = Book()
    toBeInserted.title = result['title']
    toBeInserted.price = result['price']
    toBeInserted.summary = result['summary']
    toBeInserted.category = result['category']
    toBeInserted.stock = result['stock']
    #we have the ID of the author, we will now fetch it and copy it 
    fetchedAuthor = Author.objects.get(pk=(result['author']))
    toBeInserted.author = fetchedAuthor
    toBeInserted.save()

    
    #return HttpResponse(template.render(context, request))
    return render(request, 'gestionlivre/result.html', {'result': result})
