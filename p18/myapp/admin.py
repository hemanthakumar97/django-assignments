from django.contrib import admin
from .models import *
# Register your models here.

class ProfessorAdminView(admin.ModelAdmin):
    list_display = ("first_name", "last_name","email")
    list_editable = ("email",)
    list_filter = ("first_name", "last_name","email")
    search_fields = ("first_name", "last_name")


admin.site.register(Professor, ProfessorAdminView)
admin.site.register(Subject)