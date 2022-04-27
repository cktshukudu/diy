from django import forms
from .models import webSite
from django.forms import ModelForm


class webForm(forms.ModelForm):
    class Meta:
        model = webSite
        fields = ['htmlString', 'companyName', 'images']