from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Question,Choice

# Register your models here
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Choice)
