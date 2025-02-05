from django.db import models

# Create your models here.
class Logintable(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type=models.CharField(max_length=100)


class Usertable(models.Model):
    Loginid=models.ForeignKey(Logintable,on_delete=models.CASCADE,default=1)
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    def __str__(self):
        return self.Firstname


class Producttable(models.Model):
    Productname=models.CharField(max_length=100)
    Image = models.FileField()
    Quantity=models.IntegerField()
    Unitprice=models.IntegerField()
    Brand = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000)
    def __str__(self):
        return self.Productname

class Carttable(models.Model):
    Productid = models.IntegerField()
    Productname = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    price = models.IntegerField()
    Userid = models.CharField(max_length=100)

    def __str__(self):
        return self.Productname

class Billtable(models.Model):
    Productid = models.IntegerField()
    Productname = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    price = models.IntegerField()
    Userid = models.CharField(max_length=100)
    Date = models.DateField()
    Firstname = models.CharField(max_length=100)

    def __str__(self):
        return self.Productname
