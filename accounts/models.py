from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    governorate=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='uploads/%Y/%m/%d',null=True)