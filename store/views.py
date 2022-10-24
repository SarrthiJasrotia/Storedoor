from itertools import product
from django.shortcuts import render
from .models import *
# Create your views here.

#Store 
def store(request):
    product = Product.objects.all()
    context = {}
    return render(request, 'store/store.html')
#cart
def cart(request):
    context = {}
    return render(request, 'store/cart.html')

