from pydoc import Doc
from unicodedata import name
from django.shortcuts import redirect, render
from .models import PostModel, Doctor
from .forms import PostModelForm, DoctorForm

# from django.http import HttpResponse
# Create your views here.


def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blog_detail.html', context)

def doctor(request):
    posts = Doctor.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('doctor')
    else:
        form = DoctorForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'doctor.html', context)