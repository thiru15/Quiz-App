from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Question,Choice
from import_export.admin import ImportExportModelAdmin

class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Question, ViewAdmin)

# Register your models here
admin.site.register(Profile,ViewAdmin)

admin.site.register(Choice,ViewAdmin)