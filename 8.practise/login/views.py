
from django.shortcuts import render,redirect

def signup(request):
	context = { 'name':'ABC Farms' }
	return render(request, 'signup.html', context)

def login(request):
	context = { 'name':'Techno' }
	return redirect('signup')
