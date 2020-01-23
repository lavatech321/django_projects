from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('<h1>This is Our Home Page!</h1>')

def signup(request):
	return HttpResponse('<h1>Please SignUp!</h1>')
