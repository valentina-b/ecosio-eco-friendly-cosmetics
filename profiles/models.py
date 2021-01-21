from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from django.db.models import Sum


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information, order history and
    loyalty programme status
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='country', null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    earned_loyalty_points = models.DecimalField(max_digits=10, decimal_places=0, null=False, default=0)
    donated_loyalty_points = models.DecimalField(max_digits=10, decimal_places=0, null=False, default=0)
    total_loyalty_points = models.DecimalField(max_digits=10, decimal_places=0, null=False, default=0)
    going_to_event = models.BooleanField(default=False)

    def update_earned_loyalty_points(self, *args, **kwargs):
        """
        Get the points based on previous orders
        """
        self.earned_loyalty_points = self.orders.aggregate(Sum('loyalty_points'))['loyalty_points__sum'] or 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
