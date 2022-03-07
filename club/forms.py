from django import forms
from .models import TechType, product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'