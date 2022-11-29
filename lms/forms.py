from django import forms
from .models import *

class Book_form(forms.ModelForm):

    class  Meta:
        model=Book
        fields=[
            'title',
            'author',
            'price',
            'photo_book',
            'photo_author',
            'rental_price_day',
            'rental_period',
             'rental_total_price',
            'pages',
            'status',
            'catagery',
           
        ]

        widgets={
              'title':forms.TextInput(attrs={'class':"form-control"}),
            'author':forms.TextInput(attrs={'class':"form-control"}),
            'price':forms.NumberInput(attrs={'class':"form-control"}),
            'photo_book':forms.FileInput(attrs={'class':"form-control"}),
            'photo_author':forms.FileInput(attrs={'class':"form-control"}) ,
            'rental_price_day':forms.NumberInput(attrs={'class':"form-control",'id':"priceday"}),
            'rental_period':forms.NumberInput(attrs={'class':"form-control",'id':'no-days'}),
            'rental_total_price':forms.NumberInput(attrs={'class':"form-control",'id':'rental_total_price'}),
            'pages':forms.NumberInput(attrs={'class':"form-control"}),
            'catagery':forms.Select(attrs={'class':"form-control"}),
            'status':forms.Select(attrs={'class':"form-control"}),
        }

class Catagery_form(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control"}),
        }
