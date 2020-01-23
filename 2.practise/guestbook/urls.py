
from django.contrib import admin
from django.urls import path

 urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('home/<stage>' , views.f2 ),
    path('index/<name>' , views.f3 ),
    path('info/<name>/<no>' , views.f4 ),
    path('page/<name>/<int:no>' , views.f5 ),
    path('next/<str:name>/<int:no>', views.f6  ),
    path('new/<slug:idno>', views.f7)    
]

