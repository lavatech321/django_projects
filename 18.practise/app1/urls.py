
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('signup1/', views.signup1 , name='signup1'),
    path('signup2/', views.signup2 , name='signup2'),
]
