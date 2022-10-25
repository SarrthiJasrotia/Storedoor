
from django.shortcuts import render
from .models import *
# Create your views here.

#Store 
def store(request):
    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'store/store.html', data)
#cart
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
    data = {'items':items}
    return render(request, 'store/cart.html',data)

