from django.forms import ModelForm, widgets
from django.shortcuts import get_object_or_404
from django import forms
from home.models import Cereal, cerealCategory


class CerealCreateForm(ModelForm):
    image = forms.CharField(required='True', widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    class Meta:
        model = Cereal
        exclude = ['id', 'image', 'total']

        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Cereal Name'}),
            'manufacturer': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Producer'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'How many units'}),
            'description': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Some description'}),
            'category': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'price'}),
            'discount': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product discount'}),
            'status': widgets.CheckboxInput(attrs={'class': 'checkbox'}),

        }