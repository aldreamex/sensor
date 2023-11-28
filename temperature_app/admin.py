from django.contrib import admin
from .models import TemperatureReading

@admin.register(TemperatureReading)
class TempAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'timestamp', 'mac_address']
