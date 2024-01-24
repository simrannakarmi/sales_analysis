from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default="default@example.com")
    location = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='images/CustomerProfilePic/', null=True, blank=True)
    password = models.CharField(max_length=255)
     # Add a OneToOneField to associate a Client with a User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img = models.ImageField(upload_to='images/ProductPic/', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)

class Client_Product_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    totalprice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_indivisual = models.BooleanField(default=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Client_Sales_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    s_id = models.ForeignKey(Sales, on_delete=models.CASCADE)

class TotalSales(models.Model):
    id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

class Client_TotalSales_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    ts_id = models.ForeignKey(TotalSales, on_delete=models.CASCADE)

class DateTotalSales(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Client_DateTotalSales_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    dts_id = models.ForeignKey(DateTotalSales, on_delete=models.CASCADE)

class ProductTotalSales(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Client_ProductTotalSales_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    dts_id = models.ForeignKey(ProductTotalSales, on_delete=models.CASCADE)

class DateProductTotalSales(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Client_DateProductTotalSales_Bridge(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    dts_id = models.ForeignKey(DateProductTotalSales, on_delete=models.CASCADE)


    def __str__(self):
        return self.name