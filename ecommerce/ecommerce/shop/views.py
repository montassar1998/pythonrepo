from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    res = Product.objects.all()
    item_name = request.GET.get('item-name')
    if(item_name != '' and item_name is not None):
        res = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(res,4)
    page = request.GET.get('page')
    res = paginator.get_page(page)
    return render(request, 'shop/index.html', {'products': res})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    