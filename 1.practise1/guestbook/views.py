
from django.http import HttpResponse

def f1(request):
  return HttpResponse('Welcome to Django Class - I')

def f2(request):
  return HttpResponse('<h1>Welcome to Django Class - II</h1>')

def f3(request):
  return HttpResponse('<p>Welcome to Django Class - III</p>')
