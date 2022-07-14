from django.urls import path
from .views import  add_to_cart,cart,checkout,hx_menu_cart,update_cart,hx_cart_total,success

urlpatterns = [
    path('add_to_cart/<int:product_id>', add_to_cart, name= 'add_to_cart'),
    path('cart/',cart,name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('update-cart/<int:product_id><str:action>/',update_cart,name='update_cart'),
    path('hx_menu_cart/',hx_menu_cart,name='hx_menu_cart'),
    path('hx_cart_total/',hx_cart_total,name='hx_cart_total'),
    path('success/', success, name='success'),

]