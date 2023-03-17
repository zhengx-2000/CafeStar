from django.db import models


# Create your models here.

class User(models.Model):
    UserID = models.IntegerField(primary_key=True, max_length=10, verbose_name='UserID')
    Manager = models.BooleanField(default=False, verbose_name='Manager')
    Fullname = models.CharField(max_length=30, verbose_name='Fullname')
    Username = models.CharField(max_length=30, verbose_name='Username')
    Email = models.EmailField(max_length=30, verbose_name='Email')
    Password = models.CharField(max_length=30, verbose_name='Password')
    PhoneNumber = models.IntegerField(max_length=11, verbose_name='PhoneNumber')
    Point = models.IntegerField(max_length=4, verbose_name='Point', null=True, blank=True)


class Order(models.Model):
    OrderID = models.IntegerField(primary_key=True, max_length=10, verbose_name='OrderID')
    UserID = models.IntegerField(max_length=10, verbose_name='UserID')
    DrinkID = models.IntegerField(max_length=10, verbose_name='DrinkID', null=True, blank=True)
    Status = models.BooleanField(default=False, verbose_name='Status')
    Drink = models.CharField(max_length=30, verbose_name='Drink')
    Sweetness = models.CharField(max_length=10, verbose_name='Sweetness', null=True, blank=True)
    Milk = models.CharField(max_length=10, verbose_name='Milk', null=True, blank=True)
    PickupTime = models.TimeField(verbose_name='PickupTime')
    Price = models.IntegerField(max_length=4, verbose_name='Price')
    Point = models.IntegerField(max_length=4, verbose_name='Point')


class Drink(models.Model):
    DrinkID = models.IntegerField(primary_key=True, max_length=10, verbose_name='DrinkID')
    Name = models.CharField(max_length=30, verbose_name='Name')
    Picture = models.ImageField(upload_to='drink_images/',
                                verbose_name='Picture')  # Here is a directory to store drinks pictures
    Description = models.CharField(max_length=100, verbose_name='Description')
    Nutrition = models.CharField(max_length=100, verbose_name='Nutrition', null=True, blank=True)
    Ingredients = models.CharField(max_length=100, verbose_name='Ingredients', null=True, blank=True)
    Price = models.IntegerField(max_length=4, verbose_name='Price')
    Point = models.IntegerField(max_length=4, verbose_name='Point')
    Rating = models.FloatField(verbose_name='Rating', null=True, blank=True)


class ShopStatus(models.Model):
    OpenTime = models.DateTimeField(verbose_name='OpenTime')
    CloseTime = models.DateTimeField(verbose_name='CloseTime')
    OrderCount = models.IntegerField(max_length=3, verbose_name='OrderCount')
    NextOrderID = models.IntegerField(max_length=10, verbose_name='NextOrderID')
