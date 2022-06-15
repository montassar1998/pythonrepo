from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    # return HttpResponse("<h1>it works</h1>")
    date = datetime.today()
    context = {"TheDate": date, "Devops": "Docker"}
    return render(request, "TP1Django/index.html", context)
