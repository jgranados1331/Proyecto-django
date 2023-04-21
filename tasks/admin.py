from django.contrib import admin
from .models import Taks, Categoria, Vehiculo, Marca,subcategoria


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(subcategoria)