from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    catories=(
        ('tablets','tablets'),
        ('injection','injection'),
        ('drink','drink')
    )
    pName=models.CharField(max_length=50)
    pDescription=models.CharField(max_length=200,null=True,blank=True)
    pProduceDate=models.DateTimeField()
    pExpireDate=models.DateTimeField()
    pImage=models.ImageField(upload_to='uploads/%y/%m/%d')
    pBuyPrice=models.FloatField()
    pSellPrice=models.FloatField()
    pConcentration=models.FloatField(default=100)
    pCategories=models.CharField(max_length=20,choices=catories)
    def __str__(self):
        return  self.pName

class Customer(models.Model):
    Cuser=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    gender=(
        ('Female','Female'),
        ('Male','Male')
    )
    CFullName=models.CharField(max_length=100)
    CAddress=models.CharField(max_length=200)
    CMobile=models.IntegerField()
    CImage=models.ImageField(upload_to='uploads/%y/%m/%d')
    CGender=models.CharField(max_length=20,choices=gender)
    CEmail=models.CharField(max_length=30,null=True)
    CUserName=models.CharField(max_length=50,unique=True)
    CPassword=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.CFullName

class OrderDetails(models.Model):
    categories=(
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('Out for Delivered','Out for Delivered')
    )
    oProductID=models.ForeignKey(Products,on_delete=models.CASCADE)
    oCustomerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    oDate=models.DateTimeField(auto_now_add=True)
    oQuantity=models.IntegerField()
    oTatalPrice=models.FloatField()
    oCategories=models.CharField(max_length=20,choices=categories)

    def __str__(self):
        return str(self.id)


class Suppliers(models.Model):
    sCompanyName=models.CharField(max_length=50)
    sAddress=models.CharField(max_length=100)
    sMobile=models.IntegerField()
    sCity=models.CharField(max_length=50)
    sSalesName=models.CharField(max_length=50)

    def __str__(self):
        return self.sCompanyName


class RequestDetails(models.Model):
    rSupplierID=models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    rProductID=models.ForeignKey(Products,on_delete=models.CASCADE)
    rDate=models.DateTimeField(auto_now_add=True)
    rQuantity=models.IntegerField()
    rTotalPrice=models.FloatField()

    def __str__(self):
        return str(self.id)
