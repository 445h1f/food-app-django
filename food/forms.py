from django import forms
from .models import Item

"""Form to add item"""
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'image']

