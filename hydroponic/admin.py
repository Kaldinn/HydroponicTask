from django.contrib import admin
from .models import HydroponicSystem, Measurement

@admin.register(HydroponicSystem)
class HydroponicSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner')
    search_fields = ('name', 'owner__username')
    list_filter = ('owner',)
    ordering = ('name',)
    list_display_links = ('id', 'name')
    list_per_page = 25

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds')
    search_fields = ('hydroponic_system__name', 'timestamp')
    list_filter = ('hydroponic_system', 'timestamp', 'ph', 'temperature', 'tds')
    ordering = ('-timestamp',)
    list_display_links = ('id', 'hydroponic_system')
    list_per_page = 25
