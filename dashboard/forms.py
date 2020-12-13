from django import forms
from django.forms import ModelForm
from .models import *


class ItemsForm(forms.ModelForm):

    label = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write task...'}))
    
    class Meta:
        model = Item
        fields = '__all__'