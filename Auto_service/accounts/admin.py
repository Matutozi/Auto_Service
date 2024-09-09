from django.contrib import admin
from .models import CustomUser, Address

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'other_name', 'date_joined', 'date_of_birth')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('custom_user', 'street_address', 'city', 'state', 'country')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address, AddressAdmin)
