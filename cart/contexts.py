from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import UserProfile


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    user_is_loyal = False

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COSTS
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    original_total = total

    # loyalty programme benefits
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        # 10% discount for first purchase per account
        if user.total_loyalty_points == 0:
            total = round(total - (total * Decimal(0.10)), 2)

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        # free delivery for loyalty level 2 and 3 customers
        if user.total_loyalty_points > 60:
            delivery = 0
            free_delivery_delta = 0
            user_is_loyal = True

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'original_total': original_total,
        'user_is_loyal': user_is_loyal,
    }

    return context
