from django.http import request
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

# def doctor(request):
#     return render(request, 'doctor.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

