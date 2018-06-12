from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    content = {}
    content['hello'] = 'Hello World'
    return render(request,'hello.html',content)