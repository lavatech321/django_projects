
from django.shortcuts import render

class Emp:
	eid=1001
	ename='Raman'

def page1(request):
	obj = Emp()
	name = 'ram'
	products = {'id':101,'name':'pepsi'}
	l1 = ['jack','jill','jimmy']
	context = {'obj':obj, 'name':name, 'products': products, 'l1': l1}
	return render(request,'app1/page1.html', context)

# Create your views here.