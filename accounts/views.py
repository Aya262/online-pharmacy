from django.shortcuts import render
from .models import user
# Create your views here.

def profile(request,pk):
    user_pk=user.objects.get(id=pk)
    context={'user':user_pk}
    return render(request,'accounts/profile.html',context)

def home(request):
    return render(request,'accounts/home.html')