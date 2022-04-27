from django import forms
from .models import webSite
from django.forms import ModelForm
from .models import Image


class webForm(forms.ModelForm):
    class Meta:
        model = webSite
        fields = ['htmlString', 'companyName', 'images']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')