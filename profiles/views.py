from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)


def order_history(request):
    """ Display the user's order history. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def edit_profile(request):
    """ Display the user's edit profile details form. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile_details.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


def loyalty_status(request):
    """ Display the user's edit profile details form. """

    template = 'profiles/loyalty_status.html'
    context = {}

    return render(request, template, context)