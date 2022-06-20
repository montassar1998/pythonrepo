from django.shortcuts import render
from .models import Product, Supplier
# Create your views here.


def get_model_fields(model):
    return model._meta.fields


def index(request):
    result = Product.objects.all()     # converts ValuesQuerySet into Python list
    # this function returns all fields of a Model
    allFields = get_model_fields(Product)
    # converts ValuesQuerySet into Python list
    list_result = {entry for entry in result}
    result = Product.objects.all()     # converts ValuesQuerySet into Python list

    # The `iterator()` method ensures only a few rows are fetched from
    # the database at a time, saving memory.
    for star in result.iterator():
        # show __str__(self) in console
        print(star)
    context = {"res": result, "test": list_result}
    return render(request, "produitFournisseur/index.html", context)
