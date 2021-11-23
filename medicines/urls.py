from django.urls import path
from . import views
urlpatterns=[
    path('products/',views.home,name='products'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name="contact"),
    path('customer/',views.customer,name="customer")
]