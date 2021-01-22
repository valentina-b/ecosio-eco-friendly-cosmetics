from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)


@login_required
def order_history(request):
    """ Display the user's order history. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """ Display the user's edit profile details form. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile_details.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def loyalty_status(request):
    """ Display the user's edit profile details form. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    unlock_loyalty_level_2 = 61 - profile.total_loyalty_points
    unlock_loyalty_level_3 = 101 - profile.total_loyalty_points

    template = 'profiles/loyalty_status.html'
    context = {
        'orders': orders,
        'profile': profile,
        'unlock_loyalty_level_2': unlock_loyalty_level_2,
        'unlock_loyalty_level_3': unlock_loyalty_level_3,
    }

    return render(request, template, context)


@login_required
def register_for_event(request):
    """ User registers for the loyalty level 3 event """
    profile = get_object_or_404(UserProfile, user=request.user)

    profile.going_to_event = True
    profile.save()

    messages.success(request, 'Event attendance registered!')

    return redirect(reverse('loyalty_status'))
