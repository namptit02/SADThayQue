from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from product.models import Product


# Create your views here.
def index(request):
    books = Product.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))
