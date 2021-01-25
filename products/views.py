from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

import random

# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    product_tag = None
    product_tag_friendly_names = {
        'is_crueltyfree': 'cruelty-free',
        'is_vegan': 'vegan',
        'is_organic': 'organic',
        'is_natural': 'natural',
    }

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

        if 'product_tag' in request.GET:
            # get the django querydict from the url, where product_tag is key
            product_tag = request.GET['product_tag']
            # create a python dictionary with matching boolean to use as a filter
            product_tag_dictionary = {product_tag: True}
            # use dictionary as a filter through the products
            products = products.filter(**product_tag_dictionary)
            # store friendly name under product_tag to display it on the page
            if product_tag in product_tag_friendly_names:
                product_tag = product_tag_friendly_names[product_tag]

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
        'product_tag': product_tag,
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

    product_loyalty_points = int(product.price / 10)

    context = {
        'product': product,
        'product_category': product_category,
        'random_product_1': random_product_1,
        'random_product_2': random_product_2,
        'random_product_3': random_product_3,
        'product_loyalty_points': product_loyalty_points,
    }

    return render(request, 'products/product_page.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Only our ECOSiO team has access to this.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Only our ECOSiO team has access to this.')
        return redirect(reverse('homepage'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Only our ECOSiO team has access to this.')
        return redirect(reverse('homepage'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
