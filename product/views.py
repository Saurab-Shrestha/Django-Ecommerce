from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from order.models import Order
from django.http import JsonResponse
import requests
# Create your views here.
def product(request,slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product,slug=slug)
    return render(request, "product/product.html",{'product':product,'categories':categories})
