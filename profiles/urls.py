from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('loyalty_status/', views.loyalty_status, name='loyalty_status'),
    path('register_for_event/', views.register_for_event, name='register_for_event'),
    path('donate_plant_tree/', views.donate_plant_tree, name='donate_plant_tree'),
    path('donate_recycle_plastic/', views.donate_recycle_plastic, name='donate_recycle_plastic'),
    path('donate_clean_forest/', views.donate_clean_forest, name='donate_clean_forest'),
]
