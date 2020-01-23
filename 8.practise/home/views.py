
from django.shortcuts import render, redirect

def index(request):
	context = { 'name':'Lavatech Technology', 'city':'Pune' }
	return render(request,'home/index.html', context)

def info(request):
	context = { 'name':'Google', 'city':'SanFrancsisco' }
	return redirect('home')

