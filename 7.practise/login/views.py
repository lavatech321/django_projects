
from django.shortcuts import render

def signup(request, username):
	context = { 'username': username , 'mail': 'abc@gmail.com'} 
	return render(request, 'signup.html', context)

