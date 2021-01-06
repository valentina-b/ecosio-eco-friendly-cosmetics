from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

import random

# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'organic_products' in request.GET:
            products = products.filter(is_organic=True)

        if 'vegan_products' in request.GET:
            products = products.filter(is_vegan=True)

        if 'crueltyfree_products' in request.GET:
            products = products.filter(is_crueltyfree=True)

        if 'natural_products' in request.GET:
            products = products.filter(is_natural=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Looks like you didn't enter any keywords. Please try again!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_page(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # get the product's category
    product_category = product.category
    # select all products in the system
    all_products = Product.objects.all()
    # filter out from all products those that match the product's category
    category_filtered_products = all_products.filter(category=product_category)
    # get 3 random projects from that category
    three_random_products = random.sample(list(category_filtered_products), 3)
    # create more intuitive variables to be used in jinja templates
    random_product_1 = three_random_products[0]
    random_product_2 = three_random_products[1]
    random_product_3 = three_random_products[2]

    context = {
        'product': product,
        'product_category': product_category,
        'random_product_1': random_product_1,
        'random_product_2': random_product_2,
        'random_product_3': random_product_3,
    }

    return render(request, 'products/product_page.html', context)
