from pyexpat import model
from attr import field, fields
from django import forms

from authentication.models import Customer
from .models import PostModel, Doctor


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('author','title', 'content')
    
class DoctorForm(forms.ModelForm):
    remarks = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Doctor
        fields = ('name', 'profiles', 'image', 'gender','experience', 'remarks')