
from django.shortcuts import render

def page1(request):
	return render(request,'app1/page1.html')

def pass_to_page2(request):
	if request.method == 'GET':
	  name=request.GET['name']
	  email=request.GET['email']
	  password=request.GET['password']
	  context = {'name':name , 'email':email, 'password':password}
	return render(request,'app1/page2.html',context)

def page3(request):
	return render(request,'app1/page3.html')

def pass_to_page3(request):
	if request.method == 'POST':
	  name=request.POST['name']
	  email=request.POST['email']
	  password=request.POST['password']
	  context= {'name':name , 'email':email , 'password':password}
	return render(request,'app1/page4.html',context)

# Create your views here.