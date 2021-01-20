from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'earned_loyalty_points')


admin.site.register(UserProfile, UserProfileAdmin)
