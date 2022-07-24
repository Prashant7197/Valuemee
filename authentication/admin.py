from django.contrib import admin
from . models import Customer, Doctor, User
# from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Doctor)