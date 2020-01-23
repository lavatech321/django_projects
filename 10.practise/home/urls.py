
from django.urls import path
from . import views
urlpatterns = [
    path('index/<page>', views.index , name='home'),
    path('info/', views.info , name='info'),
]
