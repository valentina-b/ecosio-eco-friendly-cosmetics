from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('loyalty_status/', views.loyalty_status, name='loyalty_status'),
    path('register_for_event/', views.register_for_event, name='register_for_event'),
]
