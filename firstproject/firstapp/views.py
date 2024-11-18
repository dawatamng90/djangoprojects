from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    return HttpResponse('<h2>Hello, Students. Welcome to Django tutorials.</h2>')