from django.contrib import admin
from django.contrib.auth.models import User
from testapp.models import Quiz1,Profile,Choice,Quiz2,Choice2,Profile1,Profile2,Document
from import_export.admin import ImportExportModelAdmin

class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Quiz1, ViewAdmin)
admin.site.register(Quiz2, ViewAdmin)

# Register your models here
admin.site.register(Profile,ViewAdmin)

admin.site.register(Choice,ViewAdmin)
admin.site.register(Choice2,ViewAdmin)
admin.site.register(Profile1,ViewAdmin)
admin.site.register(Profile2,ViewAdmin)
admin.site.register(Document,ViewAdmin)
# Register your models here.
 