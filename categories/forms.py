from django import forms
from categories.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
