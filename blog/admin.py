from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pk',
        'published_date',
        'slug'
    )


admin.site.register(Blog, BlogAdmin)
