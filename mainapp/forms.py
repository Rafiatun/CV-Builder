from django import forms
from .models import *


class IntroductionForm(forms.ModelForm):
    class Meta:
        model= Introduction
        fields= '__all__'
