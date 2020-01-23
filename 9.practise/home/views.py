
from django.shortcuts import render, redirect

def index(request,page):
	context = { 'page':page, 'location':'Lavatech Technology', 'city':'Pune' }
	return render(request,'home/index.html', context)

def info(request):
	return redirect('home',page=640)

