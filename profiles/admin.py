from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_loyalty_points', 'earned_loyalty_points',
                    'donated_loyalty_points', 'going_to_event',)


admin.site.register(UserProfile, UserProfileAdmin)
