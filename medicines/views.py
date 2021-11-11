from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    products_tablets_0=Products.objects.filter(pCategories='tablets')[0]
    products_tablets_1 = Products.objects.filter(pCategories='tablets')[1]
    products_tablets_2 = Products.objects.filter(pCategories='tablets')[2]
    products_tablets_3 = Products.objects.filter(pCategories='tablets')[3]

    products_injection_0=Products.objects.filter(pCategories='injection')[0]
    products_injection_1= Products.objects.filter(pCategories='injection')[1]
    products_injection_2 = Products.objects.filter(pCategories='injection')[2]
    products_injection_3= Products.objects.filter(pCategories='injection')[3]

    products_drink_0=Products.objects.filter(pCategories='drink')[0]
    products_drink_1 = Products.objects.filter(pCategories='drink')[1]
    products_drink_2 = Products.objects.filter(pCategories='drink')[2]
    products_drink_3= Products.objects.filter(pCategories='drink')[3]

    context={
    'products_tablets_0':products_tablets_0,
        'products_tablets_1':products_tablets_1,
        'products_tablets_2':products_tablets_2,
        'products_tablets_3':products_tablets_3,
        'products_injection_0':products_injection_0,
        'products_injection_1':products_injection_1,
        'products_injection_2':products_injection_2,
        'products_injection_3':products_injection_3,
        'products_drink_0':products_drink_0,
        'products_drink_1':products_drink_1,
        'products_drink_2':products_drink_2,
        'products_drink_3':products_drink_3
    }
    return render(request,'medicines/home.html',context)

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
