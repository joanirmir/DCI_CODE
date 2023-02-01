from django.shortcuts import render

from .models import Product
# Create your views here.
# detail view using FBV

def detail(request, pk):
    product = Product.objects.get(pk = pk)
    # breakpoint()
    # TODO: visitor count exercise
    product_visits = request.session.get('product_visits', {})
    breakpoint()
    product_key = 'pk_' + str(pk)
    if product_key in product_visits:
        product_visits[product_key] += 1
    else:
        product_visits[product_key] = 1

    request.session['product_visits'] = product_visits
    # retrieve information from the session
    product_visits = request.session.get('products_visits')
    context = {'product': product, 'product_visits': product_visits}
    return render(request, 'products/detail.html', context)