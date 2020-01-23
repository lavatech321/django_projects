
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('home/' , views.f1 ),                           
    path('home/page1' , views.f2 ),               
    path('apple/mango/chikoo' , views.f3 )  
]
