from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    short_name = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_short_name(self):
        return self.short_name


class Product(models.Model):

    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=375)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_eco = models.BooleanField(default=True, null=True, blank=True)
    is_crueltyfree = models.BooleanField(default=True, null=True, blank=True)
    is_vegan = models.BooleanField(default=True, null=True, blank=True)
    is_organic = models.BooleanField(default=True, null=True, blank=True)
    is_natural = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name
