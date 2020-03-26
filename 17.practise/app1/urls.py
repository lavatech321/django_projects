
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('homeform/', views.homeform , name='homeform'),
    path('homeform2/', views.homeform2 , name='homeform2'),
    path('homeform3/', views.homeform3 , name='homeform3'),
    path('homeform4/', views.homeform4 , name='homeform4'),
    path('homeform5/', views.homeform5 , name='homeform5'),
    path('homeform6/', views.homeform6 , name='homeform6'),
    path('homeform6_6/', views.homeform6_6 , name='homeform6_6'),
    path('homeform7/', views.homeform7 , name='homeform7'),
    path('homeform8/', views.homeform8 , name='homeform8'),
]

