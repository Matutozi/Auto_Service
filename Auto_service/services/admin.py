from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('driver', 'mechanic', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'mechanic')
    search_fields = ('description', 'driver__user__username')

