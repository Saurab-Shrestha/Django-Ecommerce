from tkinter import N
from django.urls import path
from .views import homepage,shop,contact

urlpatterns = [
    path('',homepage,name ='homepage'),
    path('shop/',shop, name= "shop"),
    path('contact/',contact, name= "contact"),
]