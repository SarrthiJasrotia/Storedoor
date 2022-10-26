from django.urls import path
from . import views

urlpatterns =[
    path('',views.store, name = "store"),
    path('cart/',views.cart, name = "cart"),
    path('update_item/',views.updateItem, name = "update_item"),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('createProduct/', views.createProduct, name='createProduct')
    
   
]