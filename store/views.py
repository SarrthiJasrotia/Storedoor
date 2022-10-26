
from multiprocessing import context
from operator import imod
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


import json

from .forms import ProductForm
from .models import *
# Create your views here.

def createProduct(request):
    form = ProductForm()

    if request.method =="POST":
        # print('Prinitng post', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context ={'form':form}
    return render(request, 'store/product_form.html', context)
#login

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            
        else:
            
            return redirect('/login_user')

    else:
        return render(request,'store/login.html',{})

def logout_user(request):
    logout(request)
    return redirect('/')
#Store 
def store(request):
    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'store/store.html', data)

#signup
def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'store/signup.html', context)





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
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action', action)
    print('productId', productId)


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
