from django.shortcuts import render, get_object_or_404

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    featured_product_1 = get_object_or_404(Product, pk=2)
    featured_product_2 = get_object_or_404(Product, pk=43)
    featured_product_3 = get_object_or_404(Product, pk=56)

    template = 'homepage/index.html'
    context = {
        'featured_product_1': featured_product_1,
        'featured_product_2': featured_product_2,
        'featured_product_3': featured_product_3,
    }

    return render(request, template, context)
