from django.shortcuts import render

def index(request):
	return render(request,'app1/index.html')

def page1(request):
	return render(request,'app1/page1.html')

def page2(request):
	context = { 'username': 'Ram Verma' , 'email': 'ram@gmail.com' }
	return render(request,'app1/page2.html', context)

def page3(request):
	context = { 'target_drink_list': ['cola','pepsi','sprit'] , 'user_drink': 'pepsi' }
	return render(request,'app1/page3.html', context)

def page4(request):
	context = { 'target_drink_list': [] , 'drinks': ['cola','pepsi','sprit'],
	 'store': {'1':'Fabrics' , '2':'Steel' , '3':'Cosmatics'} }
	return render(request,'app1/page4.html', context)

def page5(request):
	return render(request,'app1/page5.html')


# Create your views here.
