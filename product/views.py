from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


# Create your views here.

def details(request, id):
    book = Product.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))
