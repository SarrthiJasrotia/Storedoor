
from django.shortcuts import render
from .models import *
# Create your views here.

#Store 
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)
#cart
def cart(request):
    context = {}
    return render(request, 'store/cart.html')

