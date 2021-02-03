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
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    cart_products_quantity = sum(cart.values())
    cart_products_quantity_limit = 150

    if cart_products_quantity >= cart_products_quantity_limit:
        messages.error(request, f'Oh no, that would be over our {cart_products_quantity_limit} products per order limit. Please adjust your order.')
        return redirect(redirect_url)
    else:
        # don't run code if QueryDict has no value ('') for submitted product quantity
        try:
            quantity = int(request.POST.get('quantity'))

            if item_id in list(cart.keys()):
                current_cart = cart_contents(request)
                current_cart_items = current_cart['cart_items']
                current_cart_item_quantity = 0

                # can't add more if there already are 99 products in the cart
                if cart[item_id] >= 99:
                    messages.info(request, f'You can order up to 99 same products per order')

                # PDPs need a different solution
                # their input is not updating quantity like cart- it's adding on top
                # don't add on top if sum of what's in the cart and what you're adding is higher than 99
                elif '/shop/' in redirect_url:
                    request_dict = request.POST
                    item_id_str = str(item_id)
                    request_dict_quantity = int(request_dict['quantity'])
                    for current_cart_item in current_cart_items:
                        if item_id_str == current_cart_item['item_id']:
                            current_cart_item_quantity = current_cart_item['quantity']
                            quantity_sum = current_cart_item_quantity + request_dict_quantity

                            # first check if with this new amount cart would have more than the alowed limit
                            cart_products_quantity_sum = cart_products_quantity + request_dict_quantity
                            if cart_products_quantity_sum > cart_products_quantity_limit:
                                messages.error(request, f'Oh no, that would be over our {cart_products_quantity_limit} products per order limit. Please adjust your order.')
                                return redirect(redirect_url)

                            # if amount within the limit, check if there's more than 99 products
                            # adjust the product quantity to max 99
                            else:
                                if quantity_sum > 99:
                                    cart[item_id] = 99
                                    messages.info(request, f'You can order up to 99 items of the same product per order. We have updated {product.name.title()} quantity to {cart[item_id]}.')
                                else:
                                    cart[item_id] += quantity
                                    messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
                else:
                    cart[item_id] += quantity
                    messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
            else:
                cart_products_quantity_sum = cart_products_quantity + quantity
                if cart_products_quantity_sum > cart_products_quantity_limit:
                    messages.error(request, f'Oh no, that would be over our {cart_products_quantity_limit} products per order limit. Please adjust your order.')
                    return redirect(redirect_url)
                else:
                    cart[item_id] = quantity
                    messages.success(request, f'Added {product.name.title()} to your cart')

        except ValueError:
            messages.error(request, f'You left the product quantity blank. Try again!')
            return redirect(redirect_url)

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    cart_products_quantity = sum(cart.values())
    cart_products_quantity_limit = 150

    # don't run code if QueryDict has no value ('') for submitted product quantity
    try:
        quantity = int(request.POST.get('quantity'))

        if quantity > 0:
            cart_products_quantity_sum = cart_products_quantity + (quantity - cart[item_id])
            if cart_products_quantity_sum > cart_products_quantity_limit:
                messages.error(request, f'Oh no, that would be over our {cart_products_quantity_limit} products per order limit. Please adjust your order.')
                return redirect(reverse('view_cart'))
            else:
                # inform the user that product quantity was left to be the same if quantity hasn't changed
                if cart[item_id] == quantity:
                    messages.info(request, f'You left the product quantity for {product.name.title()} the same. Did you forget to adjust it?')
                else:
                    cart[item_id] = quantity
                    messages.success(request, f'Updated {product.name.title()} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name.title()} from your cart')

    except ValueError:
        messages.error(request, f'You left the product quantity blank. Try again!')
        return redirect(reverse('view_cart'))

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
