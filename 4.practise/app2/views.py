from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1(request):
	return HttpResponse('<h1>Welcome to Our First Page!</h1>')

def page2(request):
	return HttpResponse('<h1>Thank You for visiting us again!</h1>')

