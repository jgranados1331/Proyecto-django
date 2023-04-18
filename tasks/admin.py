from django.contrib import admin
from .models import Taks

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
# Register your models here.
admin.site.register(Taks, TaskAdmin)