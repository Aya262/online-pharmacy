from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    products_tablets=Products.objects.filter(pCategories='tablets')[:4].values()
    products_injection=Products.objects.filter(pCategories='injection')[:4].values()
    products_drink=Products.objects.filter(pCategories='drink')[:4].values()
    context={
    'products_tablets':products_tablets,
        'products_injection':products_injection,
        'products_drink':products_drink
    }
    return render(request,'medicines/home.html',context)