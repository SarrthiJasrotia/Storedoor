from django.http import JsonResponse
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
        order ={'get_cart_total':0,'get_cart_items':0}
    data = {'items':items, 'order':order}
    return render(request, 'store/cart.html', data)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)
