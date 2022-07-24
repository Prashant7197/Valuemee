from distutils.command.upload import upload
from email.policy import default
from unicodedata import name
from django.db import models
from matplotlib.pyplot import title
# from django.core.validators import FileExtensionValidator

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=70)
    profiles = models.CharField(max_length=120, default="Physiotherapist MBBS")
    experience = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="doctors/", default="default.png")
    gender = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    ]
    gender = models.CharField(max_length=25, choices=gender, default="male")
    remarks = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
