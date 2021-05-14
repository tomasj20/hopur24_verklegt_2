from django.forms import ModelForm, widgets
from django import forms
from home.models import Cereal, cerealCategory, cerealImage, paymentInfo
from django.forms import TextInput
from django.shortcuts import get_object_or_404

class PaymentForm(ModelForm):
    class Meta:
        model = paymentInfo
        exclude = ['user']
        fields = ['creditCardNumber','expiryDate','cvv']
        widgets = {
                'creditCardNumber': TextInput(attrs={'placeholder': 'Card Number'}),
                'expiryDate': TextInput(attrs={'placeholder': 'Ex: 123'}),
                'cvv': TextInput(attrs={'placeholder': 'Email'}),
            }