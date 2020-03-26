
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(requests):
	count = User.objects.count()
	return render(requests,'app1/home.html', {'count':count})

def signup1(requests):
	form = UserCreationForm()
	return render(requests,'app1/signup.html', { 'form':form })


def signup2(requests):
	if requests.method == 'POST':
		form = UserCreationForm(requests.POST)
		if form.is_valid():
			user = form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(requests,'app1/signup.html', { 'form':form })

# Create your views here.