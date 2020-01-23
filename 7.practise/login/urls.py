
from django.urls import path
from . import views
urlpatterns = [
    path('signup/<username>', views.signup , name='signup'),
]

