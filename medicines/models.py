from django.db import models

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

class User(models.Model):
    gender=(
        ('Female','Female'),
        ('Male','Male')
    )
    uName=models.CharField(max_length=50)
    uAddress=models.CharField(max_length=200)
    uMobile=models.IntegerField()
    uImage=models.ImageField(upload_to='uploads/%y/%m/%d')
    uGender=models.CharField(max_length=20,choices=gender)
    def __str__(self):
        return self.uName

class OrderDetails(models.Model):
    categories=(
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('Out for Delivered','Out for Delivered')
    )
    oProductID=models.ForeignKey(Products,on_delete=models.CASCADE)
    oCustomerID=models.ForeignKey(User,on_delete=models.CASCADE)
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