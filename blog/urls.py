from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('doctor/', views.doctor, name="doctor")
]