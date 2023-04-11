from django import forms
from .models import Token

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['name', 'description', 'price', 'brand', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'This art is...', 'rows': '4', 'cols': '50'}),
            'price': forms.TextInput(attrs={'placeholder': '$0.00'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Brand name'}),
        }
