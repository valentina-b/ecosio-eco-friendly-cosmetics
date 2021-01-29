from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

from cart.contexts import cart_contents

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        current_cart = cart_contents(request)
        current_cart_items = current_cart['cart_items']
        current_cart_item_quantity = 0

        # can't add more if there already are 99 products in the cart
        if cart[item_id] >= 99:
            messages.info(request, f'You can order up to 99 same products per order')

        # PDPs need a different solution
        # their input is not updating quantity like cart- it's adding on top
        # can't add on top if sum of what's in the cart and what you're adding is higher than 99
        elif '/shop/' in redirect_url:
            request_dict = request.POST
            request_dict_quantity = request_dict['quantity']
            try:
                request_dict_product_id = redirect_url.split('/')[2]
                request_dict_quantity = int(request_dict_quantity)
                request_dict_product_id = int(request_dict_product_id)
            except ValueError:
                # because redirect url at shop (/shop/) doesn't provide product ID info
                # case for adding a product directly from the feed
                request_dict_product_id = int(item_id)
                request_dict_quantity = int(request_dict_quantity)
            for current_cart_item in current_cart_items:
                for cart_item_id in current_cart_item['item_id']:
                    cart_item_id = int(cart_item_id)
                    if cart_item_id == request_dict_product_id:
                        current_cart_item_quantity = int(current_cart_item['quantity'])
                        quantity_sum = current_cart_item_quantity + request_dict_quantity
                        if quantity_sum > 99:
                            cart[item_id] = 99
                            messages.info(request, f'You can order up to 99 items of the same product per order. We have updated {product.name.title()} quantity to {cart[item_id]}.')
                        else:
                            request_dict_product_id = item_id
                            cart[item_id] += quantity
                            messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
                        return redirect(redirect_url)
        else:
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name.title()} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name.title()} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name.title()} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
