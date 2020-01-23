
from django.shortcuts import render,redirect

def signup(request,name,mail):
	context = { 'name':name , 'mail':mail }
	return render(request, 'login/signup.html', context)

def login(request):
	return redirect('signup', name='abc' , mail='abc@gmail.com')

