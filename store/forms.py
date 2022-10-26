from dataclasses import field
from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'