from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Products)
admin.site.register(Suppliers)
admin.site.register(User)
admin.site.register(RequestDetails)
admin.site.register(OrderDetails)
