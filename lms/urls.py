from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('book',views.books,name='book'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
   
   path('test',views.test,name='test'),
   path('username_valdiate/',views.check,name='check')
   
]
