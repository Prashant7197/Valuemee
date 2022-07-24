from pyexpat import model
from attr import field
from django import forms
from .models import Doctor, Customer
from django.db import transaction


class CusomerSignForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return customer

class DoctorSignForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        

