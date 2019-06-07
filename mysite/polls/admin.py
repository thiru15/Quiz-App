from django.contrib import admin
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



admin.site.register(Question)

admin.site.register(Choice)