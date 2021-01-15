from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)


def order_history(request):
    """ Display the user's order history. """

    template = 'profiles/order_history.html'
    context = {}

    return render(request, template, context)


def edit_profile(request):
    """ Display the user's edit profile details form. """

    template = 'profiles/edit_profile_details.html'
    context = {}

    return render(request, template, context)


def loyalty_status(request):
    """ Display the user's edit profile details form. """

    template = 'profiles/loyalty_status.html'
    context = {}

    return render(request, template, context)
