from audioop import reverse
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        
        if len(password)<6:
            messages.add_message(request,messages.ERROR,'Password should be at least more than 6 characters')
            context['has_error'] = True
        
        if password!=password2:
            messages.add_message(request,messages.ERROR,'Password mismatch')
            context['has_error'] = True
        
        if not validate_email(email):
            messages.add_message(request,messages.ERROR,'Enter a valid email address')
            context['has_error'] = True
        
        if not username:
            messages.add_message(request,messages.ERROR,'Username is required')
            context['has_error'] = True
            
        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.ERROR,'Username is taken, please choose another one')
            context['has_error'] = True
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR,'Email is already exists, please choose another one')
            context['has_error'] = True
        
        if context['has_error']:
            return render(request, 'register.html', context)
        
        user=User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        
        messages.add_message(request,messages.SUCCESS,'Account created, you can now login')
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')  
        return redirect('/')  
    
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username, password=password)
        
        if not user:
            messages.add_message(request, messages.ERROR, 'Invalid credentials')
            
            return render(request, 'login.html', context)
        
        login(request, user)
        
        messages.add_message(request, messages.SUCCESS, f'Welcome {user.username}')
        
        return redirect(reverse('home'))
        
        
        
    
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    
    messages.add_message(request, messages.SUCCESS, 'Successfully logged out')
    return redirect(reverse('login_user'))