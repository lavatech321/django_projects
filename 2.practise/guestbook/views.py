
from django.http import HttpResponse

def f2(request,stage):
  return HttpResponse('Welcome to Django Class, we are at stage - '+stage)

def f3(request,name):
  return HttpResponse('<h1>Welcome to Django Class - My name is: {0} </h1>'.format(name))

def f4(request,name,no):
  return HttpResponse('<p>Welcome to Django Class - My name is: {0} and ID is: {1}</p>'.format(name,no))

def f5(request,name,no):
  return HttpResponse('<p>Welcome to Django Class - My name is: {0} and ID is: {1}</p>'.format(name,no))

def f6(request,name,no):
  return HttpResponse('<p>Welcome to Django Class - My name is: {0} and ID is: {1}</p>'.format(name,no))

def f7(request,idno):
  return HttpResponse('<p>Welcome to Django Class - Slug is : {0}</p>'.format(idno))
