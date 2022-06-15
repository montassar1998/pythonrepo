from django.shortcuts import render
from .models import Article
# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Application Home Page!')
    result = Article.objects.all()
    context = {"listearticle": result}
    return render(request, 'FirstApp/index.html', context)


def allArticles(request):
    result = Article.objects.all()
    context = {"listearticle": result}
    return render(request, "FirstApp/listing.html", context)


def fctArticle(request, article_id):
    result = Article.objects.get(pk=article_id)
    context = {"listearticle": result}
    return render(request, 'FirstApp/Article.html', context)


def article1(request):
    return render(request, 'FirstApp/article1.html')


def article2(request):
    return render(request, 'FirstApp/article2.html')


def article3(request):
    return render(request, 'FirstApp/article3.html')
