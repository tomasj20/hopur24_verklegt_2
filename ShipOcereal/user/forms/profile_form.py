from django.forms import ModelForm, widgets
from user.models import user_info
class ProfileForm(ModelForm):
    class Meta:
        model = user_info
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Götunafn og Nr'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Póstnúmer'}),
            'town': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bæjarfélag'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image Url'}),
            'country': widgets.Select(attrs={'class': 'form-control', 'placeholder': 'country'})
        }
