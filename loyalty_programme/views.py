from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the loyalty programme page """

    return render(request, 'loyalty_programme/loyalty_programme.html')