from django.shortcuts import render
from .models import *
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    products_drink=Products.objects.filter(pCategories='drink')
    products_drink=dict(enumerate(products_drink))
    products_tablets = Products.objects.filter(pCategories='tablets')
    products_tablets = dict(enumerate(products_tablets))
    products_injection = Products.objects.filter(pCategories='injection')
    products_injection = dict(enumerate(products_injection))

    context={'products_drink':products_drink,
             'products_tablets':products_tablets,
             'products_injection':products_injection}
    return render(request,'medicines/home.html',context)

def register(request):
    if request.method=="POST":
        print(request.POST)

    context={}
    return render(request,'register.html',context)

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    submitted=False
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            #assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else :
        form=ContactForm()
        if 'submitted' in request.GET:
            submitted=True

    context={'form':form,'submitted':submitted}
    return render(request,'contact.html',context)