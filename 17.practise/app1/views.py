
from django.shortcuts import render, redirect
from .forms import DetailForm, DetailForm2, DetailForm3

def home(requests):
	return render(requests,'app1/home.html')

def homeform(requests):
	f1 = DetailForm()
	return render(requests,'app1/homeform.html',{ 'form':f1 })

def homeform2(requests):
	f1 = DetailForm()
	return render(requests,'app1/homeform2.html',{ 'form':f1 })

def homeform3(requests):
	f1 = DetailForm()
	return render(requests,'app1/homeform3.html',{ 'form':f1 })

def homeform4(requests):
	f1 = DetailForm()
	return render(requests,'app1/homeform4.html',{ 'form':f1 })

def homeform5(requests):
	f1 = DetailForm2()
	return render(requests,'app1/homeform5.html',{ 'form':f1 })

def homeform6(requests):
	if requests.method == 'POST':
		f1 = DetailForm2(requests.POST)

		if f1.is_valid():
			f1.save()
			return redirect('homeform6')
		else:
			print(f1.errors)
	else:
		f1 = DetailForm2()
	return render(requests,'app1/homeform6.html',{ 'form':f1 })


def homeform7(requests):
	if requests.method == 'POST':
		f1 = DetailForm3(requests.POST)

		if f1.is_valid():
			f1.save()
			return redirect('homeform7')
		else:
			print(f1.errors)
	else:
		f1 = DetailForm3()
	return render(requests,'app1/homeform7.html',{ 'form':f1 })

# Create your views here.