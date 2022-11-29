from pytube import Youtube
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# from django.http import HttpResponseRedirect
# from django.urls import reverse
def index(request):


    context={
        "books":Book.objects.all(),
        "cat":Category.objects.all(),
        'form':Book_form(),
        'catagery':Catagery_form(),
        "allbooks":Book.objects.filter(active=True).count(),
        "rentalBooks":Book.objects.filter(status='rental').count(),
        "soldBooks":Book.objects.filter(status='sold').count(),
        "availableBooks":Book.objects.filter(status='available').count(),

     
        
    }
   
    if request.method=='POST':
        add_book=Book_form(request.POST,request.FILES)
        add_catagery=Catagery_form(request.POST)
        if add_book.is_valid():
            # if not add_book.title in context['s'][0].title:
              add_book.save()
        if add_catagery.is_valid():
            add_catagery.save()
    return render(request,"pages/index.html",context)



def books(request):
    search_name=request.GET.get("search_name")
    context={
        "books":Book.objects.all(),
        "cat":Category.objects.all(),
        'catagery':Catagery_form(),
        'form':Book_form(),

        
           
    }
    if(search_name):
        search=context['books'].filter(title__icontains=search_name)
        context.update({'books':search})
        
    return render(request,'pages/books.html',context)









def update(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        update_book=Book_form(request.POST,request.FILES,instance=book)
        if update_book.is_valid():
            update_book.save()
            return redirect('/')
    else:
        context={
        'form':Book_form(instance=book),
           }
        return render(request,'pages/update.html',context)


def delete(request,id):
    delete_book=Book.objects.get(id=id)
    if request.method=='POST':
        delete_book.delete()
        return redirect('index')

    return render(request,'pages/delete.html')
  



















#   test deal with ajax
def test(request):
    
    return render(request,"test.html")

def check(request):
    username=request.GET.get('username')
    # username=request.POST.get('username')
    # print(username)
    is_token=Book.objects.filter(author__iexact=username).exists()
    if(is_token):
          print(is_token)
          return JsonResponse({"error":'username already is token '})
    else:
        return JsonResponse({})
    # return JsonResponse({"error":'username already is token2 '})