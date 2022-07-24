from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    cust_image = models.ImageField(upload_to="customer")
    email = models.EmailField(max_length=50, blank=True)
    age = models.IntegerField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True)
    profiles = models.CharField(max_length=120, default="Physiotherapist MBBS")
    doc_image = models.ImageField(upload_to="doctors")
    experience = models.IntegerField()
    profiles = models.CharField(max_length=120, default="Physiotherapist MBBS")
    gender = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    ]
    gender = models.CharField(max_length=25, choices=gender, default="male")
    remarks = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
