from turtle import title
from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
# Create your models here.


class Userdashboard(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title