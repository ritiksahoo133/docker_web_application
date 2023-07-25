from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloDocker(request):
      return HttpResponse("<h1>Hello, Docker</h1>")