
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):
    book_status=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=50,null=True,blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    photo_book=models.ImageField(upload_to="photos",null=True,blank=True)
    photo_author=models.ImageField(upload_to="photos",null=True,blank=True)
    rental_price_day=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    rental_period=models.IntegerField(null=True,blank=True)
    rental_total_price=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=book_status,null=True,blank=True)
    catagery=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title


