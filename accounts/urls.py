from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/',views.profile,name='profile'),
    path('',views.home,name='home')
]