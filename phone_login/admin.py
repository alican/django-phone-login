from django.contrib import admin

from .models import PhoneToken




@admin.register(PhoneToken)
class PhoneTokenAdmin(admin.ModelAdmin):
    """
    Admin View
    """
    list_display = ('phone_number', 'otp', 'timestamp', 'attempts', 'used')
    search_fields = ('phone_number', )
    list_filter = ('timestamp', 'attempts', 'used')
    readonly_fields = ('phone_number', 'otp', 'timestamp', 'attempts')
