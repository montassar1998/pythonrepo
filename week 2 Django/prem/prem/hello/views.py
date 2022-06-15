from django.shortcuts import render

# Create your views here.
#views are what is a controller in the MVC design pattern
def index(request):
    return render(request,"hello/index.html")