from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html' {"products": products})