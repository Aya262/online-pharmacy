from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm , CustomerForm ,LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
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
        print(request.FILES)
        form=CustomerForm(request.POST,request.FILES)
        for field in form:
            print("field Error {} : {}".format(field.name,field.errors))
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerForm()
    context={'form':form}
    return render(request,'register3.html',context)

def login(request):
    '''
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('CFullName')
            password=form.cleaned_data.get('CPassword')
            try:
                customer=Customer.objects.get(CFullName=username,CPassword=password)
                print("yes")
                return redirect('index')
            except:
                messages.error(request,'The username or the password is incorrect')
    else :
        form=LoginForm()
    context={'form':form}
    return render(request,'login2.html',context)
    '''
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        try:
            customer=Customer.objects.filter(CFullName=username,CPassword=password)
            print(customer)
            print("yes")
            return redirect('index')
        except:
            messages.error(request,'The username or the password is incorrect')
    return render(request,'login2.html')

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

def customer(request):
    form=CustomerForm()
    context={'form':form}
    return render(request,'register3.html',context)