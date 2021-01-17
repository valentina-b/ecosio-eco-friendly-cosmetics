from django import forms
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_category_names = [(c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all()
        friendly_brand_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_category_names
        self.fields['brand'].choices = friendly_brand_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-product-form-field'
