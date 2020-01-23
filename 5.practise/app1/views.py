from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	return redirect('https://www.google.com')

def signup(request):
	return redirect('https://www.lavatech.net')

