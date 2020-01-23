from django.shortcuts import render, redirect

# Create your views here.

def page1(request):
	return redirect('home')

def page2(request):
	return redirect('signup')

