from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request,'home.html')

def auth(request):
    return render (request,'auth.html')

def login(request):
    return render (request,'login.html')

