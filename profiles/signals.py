from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from checkout.models import Order


@receiver(post_save, sender=Order)
def get_earned_loyalty_points(sender, instance, created, **kwargs):
    """
    Update earned loyalty points on order update/create
    """
    instance.userprofile.update_earned_loyalty_points()


@receiver(post_delete, sender=Order)
def get_earned_loyalty_points(sender, instance, **kwargs):
    """
    Update earned loyalty points on order delete
    """
    instance.userprofile.update_earned_loyalty_points()
