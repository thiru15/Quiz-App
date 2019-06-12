from django.contrib import admin
from .models import Users,Question,Choice

# Register your models here.
admin.site.register(Users)
admin.site.register(Question)
admin.site.register(Choice)
