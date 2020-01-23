
from django.http import HttpResponse

def f2(request,stage):
  return HttpResponse('Welcome to Django Class, we are at stage - '+stage)

def f3(request,name,age,city):
  return HttpResponse('<h1>Your name: {0} , age: {1} and city: {2} </h1>'.format(name,age,city))

def f4(request,no,author):
  return HttpResponse('<p>This is Page {0}. The Author is: {1}</p>'.format(no,author))
