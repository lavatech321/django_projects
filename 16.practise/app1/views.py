
from django.shortcuts import render
from .forms import Details

def home(requests):
	return render(requests,'app1/home.html')

def home2(requests):
	form = Details()
	return render(requests,'app1/home2.html', { 'form':form })

def home3(requests):
	if requests.method == 'POST':
		form = Details(requests.POST)
		if form.is_valid():
			pass
	else:
		form = Details()
	return render(requests,'app1/home3.html', { 'form':form })


# Create your views here.