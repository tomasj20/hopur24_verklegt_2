from django.forms import ModelForm, widgets
from django import forms
from home.models import Cereal, cerealCategory,cerealImage
from django.shortcuts import get_object_or_404
from django.db import models


class imageForm(ModelForm):
    path = forms.URLField(label='Put IMG URL HERE')
    class Meta:
        model = cerealImage
        fields = ['image', 'path']

        widgets = {
            'image': widgets.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Cereal Name'}),
        }