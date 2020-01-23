
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('home/<stage>' , views.f2 ),
    path('index/' , views.f3 , { 'name':'Ram' , 'age': 45 , 'city': 'Pune' }),
    path('page/<no>' , views.f4 , { 'author': 'Shakespear' }),
]

