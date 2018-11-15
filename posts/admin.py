from django.contrib import admin

# Register your models here.
from .models import Person


class ClientAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("client", "date")



admin.site.register(Person, ClientAdmin)