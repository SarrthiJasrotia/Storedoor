from django.shortcuts import render

# Create your views here.

#Store 
def store(request):
    context = {}
    return render(request, 'store/store.html')
#cart
def cart(request):
    context = {}
    return render(request, 'store/cart.html')

